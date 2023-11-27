-- EXPLAIN ANALYZE
SELECT
    name,
    description,
    tags,
    license_price
FROM store.softwares
WHERE
    category = 'education'
    AND 'creation' = ANY(tags);

-- CREATE INDEX idx_category ON "store"."softwares" ("category");
-- CREATE INDEX idx_tags ON "store"."softwares" USING GIN("tags");


-- EXPLAIN ANALYZE
SELECT
    softwares.name,
    reviews.rating,
    reviews.review_content
FROM store.reviews
JOIN store.softwares ON reviews.software_id = softwares.id
WHERE
    softwares.category = 'education'
    AND reviews.rating >= 4;

-- CREATE INDEX idx_category ON "store"."softwares" ("category");
-- CREATE INDEX idx_rating ON "store"."reviews" ("rating");
