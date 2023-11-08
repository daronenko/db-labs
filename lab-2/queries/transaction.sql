BEGIN TRANSACTION ISOLATION LEVEL READ UNCOMMITTED;

UPDATE installations SET uninstallation_date = CURRENT_DATE
WHERE user_id IN (
    SELECT users.id FROM users
        WHERE users.country = (
            SELECT countries.id FROM countries
                WHERE countries.name = 'Wales'
        )
);

DELETE FROM users
WHERE users.id IN (
    SELECT users.id FROM users
        WHERE users.country = (
            SELECT countries.id FROM countries
                WHERE countries.name = 'Wales'
        )
);

END;
