-- Удаление всех установок, которые были удалены до 2020 года
DELETE FROM installations WHERE uninstallation_date < '2020-01-01';
