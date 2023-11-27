-- READ UNCOMMITTED, READ COMMITTED, REPEATABLE READ, SERIALIZABLE
BEGIN TRANSACTION ISOLATION LEVEL SERIALIZABLE;

UPDATE store.softwares
SET license_price = ROUND(license_price * 0.9)
WHERE id = '5a50ed1a-9f98-4a69-a93d-dd196af1fcb2';

COMMIT;

INSERT INTO store.softwares VALUES (
    'e914d404-a938-4108-a517-b3c953bbb565',
    'Elegant 2',
    'This is an awesome software!',
    'education',
    '{}'::varchar[],
    '1.0.0',
    '2023-11-26',
    '10',
    '10'
);
