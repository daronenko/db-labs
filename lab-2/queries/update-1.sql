-- Добавить тэг "map" для всех программ, которые имеют категорию "navigation"
UPDATE store.softwares
SET tags = array_append(tags, 'map')
WHERE category = 'navigation';
