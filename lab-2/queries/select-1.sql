-- Получить список установленных продуктов для конкретного пользователя, включая информацию о дате установки и удаления
SELECT products.name, installations.installation_date, installations.uninstallation_date
FROM installations
INNER JOIN products ON installations.software_id = products.id
WHERE installations.user_id = 34;
