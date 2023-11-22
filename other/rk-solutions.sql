-- Вариант 1

-- 1. Начальники отделов, являющиеся главными по работе
SELECT ФИО FROM СОТРУДНИКИ
    WHERE НОМЕР_СТ IN (SELECT ГЛАВНЫЙ FROM РАБОТЫ)
    AND НОМЕР_СТ IN (SELECT НАЧАЛЬНИК FROM ОТДЕЛЫ);

SELECT ФИО, НАЗВ_ОТ FROM СОТРУДНИКИ, ОТДЕЛЫ
    WHERE НОМЕР_СТ IN (SELECT ГЛАВНЫЙ FROM РАБОТЫ)
    AND НОМЕР_СТ IN (SELECT НАЧАЛЬНИК FROM ОТДЕЛЫ)
GROUP BY ФИО;

SELECT ФИО, НАЗВ_ОТ FROM СОТРУДНИКИ, ОТДЕЛЫ WHERE НОМЕР_СТ IN (SELECT ГЛАВНЫЙ FROM РАБОТЫ) AND НОМЕР_СТ IN (SELECT НАЧАЛЬНИК FROM ОТДЕЛЫ) GROUP BY ФИО;

SELECT ФИО FROM СОТРУДНИКИ
    WHERE НОМЕР_СТ IN (SELECT ГЛАВНЫЙ FROM РАБОТЫ
        INNER JOIN ОТДЕЛЫ
        ON РАБОТЫ.ГЛАВНЫЙ = ОТДЕЛЫ.НАЧАЛЬНИК);

-- 2. Работы, у которых нет сотрудников
SELECT НАЗВАНИЕ FROM РАБОТЫ
    WHERE НОМЕР_РБ NOT IN (SELECT РАБОТА FROM СПИСКИ_СТ);

-- 3. Сотрудники, получающие заработную плату максимальную в отделе
SELECT ФИО FROM СОТРУДНИКИ employees_1
    WHERE ЗАРПЛАТА = (SELECT MAX(ЗАРПЛАТА) FROM СОТРУДНИКИ employees_2
        WHERE employees_1.ОТДЕЛ = employees_2.ОТДЕЛ);

SELECT ФИО FROM СОТРУДНИКИ employees
    INNER JOIN
        (SELECT MAX(ЗАРПЛАТА) AS max_salary, ОТДЕЛ FROM СОТРУДНИКИ
            GROUP BY ОТДЕЛ) max_salaries
    ON max_salaries.max_salary = employees.ЗАРПЛАТА
    AND max_salaries.ОТДЕЛ = employees.ОТДЕЛ;


-- Вариант 2

-- 1. Сотрудники, у которых руководители являются начальниками отделов
SELECT ФИО FROM СОТРУДНИКИ
    WHERE РУКОВОД IN (SELECT НАЧАЛЬНИК FROM ОТДЕЛЫ);

-- 2. Сколько работ выполняет каждый отдел
SELECT "ОТДЕЛЫ"."НАЗВ_ОТ", (
    SELECT COUNT(*) FROM "СПИСКИ_СТ"
        WHERE "СПИСКИ_СТ"."СОТР" IN (SELECT "СОТРУДНИКИ"."НОМЕР_СТ" FROM "СОТРУДНИКИ"
            WHERE "СОТРУДНИКИ"."ОТДЕЛ" = "ОТДЕЛЫ"."НОМЕР_ОТ")
) AS "КОЛИЧЕСТВО_РАБОТ" FROM "ОТДЕЛЫ";

-- 3. Главные по работам, получающие заработную плату большую, чем их начальник отдела
SELECT employees_1.ФИО FROM СОТРУДНИКИ employees_1
    WHERE employees_1.ЗАРПЛАТА > (SELECT employees_2.ЗАРПЛАТА FROM СОТРУДНИКИ AS employees_2
        WHERE employees_2.НОМЕР_СТ = (SELECT department.НАЧАЛЬНИК FROM ОТДЕЛЫ AS department
            WHERE department.НОМЕР_ОТ = employees_1.ОТДЕЛ)
    AND employees_2.НОМЕР_СТ IS NOT NULL);


-- Вариант 3

-- 1. Сотрудники, у которых руководитель является главным по работе
SELECT ФИО FROM СОТРУДНИКИ
    WHERE РУКОВОД IN (SELECT ГЛАВНЫЙ FROM РАБОТЫ);

-- 2. Работы, у которых количество задействованных сотрудников меньше 3
SELECT jobs.НАЗВАНИЕ AS РАБОТА FROM РАБОТЫ AS jobs
    WHERE (SELECT COUNT(*) FROM СПИСКИ_СТ AS employees_list
        WHERE employees_list.РАБОТА = jobs.НОМЕР_РБ) < 3;

-- 3. Максимальная зп сотрудника по каждой из работ
SELECT РАБОТЫ.НАЗВАНИЕ AS РАБОТА, MAX(СОТРУДНИКИ.ЗАРПЛАТА) AS "МАКСИМАЛЬНАЯ ЗП" FROM РАБОТЫ, СПИСКИ_СТ, СОТРУДНИКИ
    WHERE РАБОТЫ.НОМЕР_РБ = СПИСКИ_СТ.РАБОТА
    AND СПИСКИ_СТ.СОТР = СОТРУДНИКИ.НОМЕР_СТ
GROUP BY РАБОТЫ.НОМЕР_РБ, РАБОТЫ.НАЗВАНИЕ ORDER BY РАБОТЫ.НОМЕР_РБ;


-- Дополнительные задания

-- 1. Количество сотруднков, принимающих участие в каждой из работ
SELECT НАЗВАНИЕ, COUNT(*) AS employees FROM РАБОТЫ, СОТРУДНИКИ, СПИСКИ_СТ
    WHERE НОМЕР_СТ = СОТР
    AND РАБОТА = НОМЕР_РБ GROUP BY 1;
