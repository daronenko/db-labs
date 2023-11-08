-- Получить общее количество установок каждого продукта
SELECT products.name, COUNT(installations.id) AS installation_count
FROM products
LEFT JOIN installations ON products.id = installations.software_id
GROUP BY products.name;
