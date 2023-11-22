-- Обновить тело отзыва с указанным id
UPDATE store.reviews
SET review_content = jsonb_set(review_content, '{body}', '"This is a new body for my review!"')
WHERE id = 'a5621056-ed3e-4bd2-aefe-6f4324aa9b0f';
