SELECT * FROM store.softwares;  -- ok

SELECT
    id,
    software,
    description,
    total_purchases
FROM store.popular_software; -- permission denied

SELECT
    software,
    description,
    total_purchases
FROM store.popular_software;  -- ok

UPDATE store.users
SET user_type = 'group'
WHERE id = 'c6047093-ac9c-424f-a9d0-03cd9b80b3db';  -- permission denied

UPDATE store.users
SET username = 'adamsss'
WHERE id = 'c6047093-ac9c-424f-a9d0-03cd9b80b3db';  -- ok
