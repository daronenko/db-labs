CREATE OR REPLACE FUNCTION calc_migration_price()
RETURNS TRIGGER AS
$$
BEGIN
    UPDATE store.softwares SET migration_price = license_price * 0.3
    WHERE id = NEW.id;
    RETURN NEW;
END;
$$
LANGUAGE 'plpgsql';

CREATE TRIGGER calc_migration_price_trigger
AFTER INSERT ON store.softwares
FOR EACH ROW
EXECUTE FUNCTION calc_migration_price();
