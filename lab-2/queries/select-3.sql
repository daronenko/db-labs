-- Получить список всех установок продуктов, которые были установлены после определенной даты, включая информацию о пользователе и продукте
SELECT users.username, products.name, installations.installation_date
FROM installations
INNER JOIN users ON installations.user_id = users.id
INNER JOIN products ON installations.software_id = products.id
WHERE installations.installation_date > '2023-11-1';
