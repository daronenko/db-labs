-- Получить список покупок пользователя, включая дату покупки
SELECT
    store.softwares.name AS software,
    store.purchase_history.purchase_date
FROM store.purchase_history
INNER JOIN store.softwares
    ON store.softwares.id = store.purchase_history.software_id
WHERE store.purchase_history.user_id = 'f535b73f-2d48-4c9a-9260-a0aac5f9bc67';
