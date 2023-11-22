-- Получить ТОП-10 программ по покупкам
SELECT
    store.softwares.name AS software,
    store.softwares.description,
    COUNT(*) AS total_purchases
FROM store.softwares
JOIN store.purchase_history
    ON store.softwares.id = store.purchase_history.software_id
GROUP BY store.softwares.name, store.softwares.description
ORDER BY total_purchases DESC
LIMIT 10;
