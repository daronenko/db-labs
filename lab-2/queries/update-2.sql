-- Обновление имени, фамилии и страны пользователя с определенным идентификатором
UPDATE users SET
    first_name = 'Ivan',
    last_name = 'Ivanov',
    country = (SELECT countries.id FROM countries WHERE name = 'Russia')
WHERE id = 98;
