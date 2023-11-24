CREATE OR REPLACE FUNCTION total_purchases(target_user uuid)
RETURNS integer AS
$$
DECLARE
    purchases_cursor CURSOR(target_user uuid)
        FOR SELECT software_id, price
        FROM store.purchase_history
        WHERE user_id = target_user;
    total_price integer DEFAULT 0;
    purchase_record record;
BEGIN
    OPEN purchases_cursor(target_user);

    LOOP
        FETCH purchases_cursor INTO purchase_record;
        EXIT WHEN NOT FOUND;

        total_price := total_price + purchase_record.price;
    END LOOP;

    CLOSE purchases_cursor;

    IF total_price = 0 THEN
        RAISE EXCEPTION 'No purchases found for the user %!', target_user;
    END IF;

    RETURN total_price;
END;
$$
LANGUAGE 'plpgsql';


CREATE OR REPLACE FUNCTION is_migration_available(target_user uuid, target_software uuid)
RETURNS boolean AS
$$
DECLARE
    purchases CURSOR(target_user uuid, target_software uuid)
        FOR SELECT id
        FROM store.purchase_history
        WHERE user_id = target_user
            AND software_id = target_software;
    purchase_record record;
BEGIN
    OPEN purchases(target_user, target_software);

    FETCH purchases INTO purchase_record;
    IF NOT FOUND THEN
        CLOSE purchases;
        RETURN false;
    END IF;

    CLOSE purchases;
    RETURN true;
END;
$$
LANGUAGE 'plpgsql';
