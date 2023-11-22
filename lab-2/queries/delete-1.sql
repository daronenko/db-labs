-- Удалить все отзывы указанного пользователя на определенную программу
DELETE FROM store.reviews
WHERE
    user_id = 'ab7ff2a2-16ad-43b2-b95b-907f57ed19c5'
    AND software_id = 'f9ba21e4-e856-487f-a142-1792d74d45e5';
