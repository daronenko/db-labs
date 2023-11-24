-- Search by name
ALTER TABLE store.softwares
ADD COLUMN _name_tsvector tsvector;

UPDATE store.softwares
SET _name_tsvector = to_tsvector('english', name);

-- CREATE INDEX idx_name_search
-- ON store.softwares
-- USING gin(_name_tsvector);

SELECT * FROM store.softwares
WHERE _name_tsvector @@ to_tsquery('english', 'car');

-- Search by description
ALTER TABLE store.softwares
ADD COLUMN _description_tsvector tsvector;

UPDATE store.softwares
SET _description_tsvector = to_tsvector('english', description);

-- CREATE INDEX idx_description_search
-- ON store.softwares
-- USING gin(_description_tsvector);

SELECT * FROM store.softwares
WHERE _description_tsvector @@ to_tsquery('english', 'pats');
