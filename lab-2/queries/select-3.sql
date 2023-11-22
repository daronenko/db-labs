-- Получить ТОП-10 программ по рейтингу из категории "education" 
SELECT
    store.softwares.name AS software,
    store.softwares.description,
    ROUND(AVG(store.reviews.rating), 1) AS avg_rating
FROM store.softwares
JOIN store.reviews
    ON store.softwares.id = store.reviews.software_id
WHERE store.softwares.category = 'education'
GROUP BY store.softwares.name, store.softwares.description
ORDER BY avg_rating DESC
LIMIT 10;
