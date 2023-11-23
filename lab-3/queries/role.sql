CREATE USER test_user WITH PASSWORD '123';

GRANT ALL ON SCHEMA store TO test_user;

GRANT SELECT ON store.countries TO test_user;
GRANT SELECT ON store.softwares TO test_user;
GRANT SELECT ON store.purchase_history TO test_user;

GRANT SELECT (id, username, country), UPDATE (username, country)
ON store.users TO test_user;

GRANT SELECT, UPDATE, INSERT ON store.reviews TO test_user;

GRANT SELECT (software, description, total_purchases)
ON store.popular_software TO test_user;

GRANT SELECT (software, description, avg_rating)
ON store.education_top TO test_user;

-- SELECT
--     table_name,
--     privilege_type
-- FROM information_schema.table_privileges
-- WHERE table_schema = 'store' AND table_name = 'countries';
--
-- SELECT
--     table_name,
--     privilege_type
-- FROM information_schema.table_privileges
-- WHERE table_schema = 'store' AND table_name = 'softwares';
--
-- SELECT
--     table_name,
--     privilege_type
-- FROM information_schema.table_privileges
-- WHERE table_schema = 'store' AND table_name = 'purchase_history';
--
-- SELECT
--     table_name,
--     privilege_type,
--     column_name
-- FROM information_schema.column_privileges
-- WHERE table_schema = 'store' AND table_name = 'users';
--
-- SELECT
--     table_name,
--     privilege_type,
--     column_name
-- FROM information_schema.column_privileges
-- WHERE table_schema = 'store' AND table_name = 'reviews';
