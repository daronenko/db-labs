-- Представление из самых популярных программ
CREATE OR REPLACE VIEW popular_software AS
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

-- Представление из ТОП-10 программ по рейтингу из категории "education" 
CREATE OR REPLACE VIEW education_top AS
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
