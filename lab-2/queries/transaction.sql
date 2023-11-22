BEGIN TRANSACTION ISOLATION LEVEL SERIALIZABLE;

DELETE FROM store.purchase_history
WHERE user_id = 'e1d4abfd-4e20-4cb3-8f03-5371fbe39e65'
    AND software_id = '88d5b381-d9ba-4d6d-b741-d24ee0684b7c'
RETURNING *;

WITH new_software AS (
  SELECT software_id AS id
  FROM store.reviews
  WHERE rating >=
)

INSERT INTO store.purchase_history (id, user_id, software_id, price, purchase_date)
VALUES uuid_generate_v4(), 'e1d4abfd-4e20-4cb3-8f03-5371fbe39e65', new_software.id, 0, CURRENT_DATE
FROM (
    SELECT software_id AS id
    FROM store.reviews
    WHERE rating >= 3
    ORDER BY random()
    LIMIT 1
) AS new_software;

COMMIT;
