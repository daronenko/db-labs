DROP SCHEMA IF EXISTS "public" CASCADE;

CREATE SCHEMA IF NOT EXISTS "public";

CREATE TABLE "products" (
  "id" serial PRIMARY KEY,
  "name" varchar UNIQUE NOT NULL,
  "organization" varchar NOT NULL,
  "release_date" date NOT NULL,
  "category" integer NOT NULL,
  "migration_price" integer,
  "license_price" integer NOT NULL
);

CREATE TABLE "users" (
  "id" serial PRIMARY KEY,
  "username" varchar UNIQUE NOT NULL,
  "email" varchar UNIQUE NOT NULL,
  "password" varchar NOT NULL,
  "first_name" varchar,
  "last_name" varchar,
  "country" integer
);

CREATE TABLE "installations" (
  "id" serial PRIMARY KEY,
  "installation_date" date NOT NULL,
  "uninstallation_date" date,
  "user_id" integer NOT NULL,
  "software_id" integer NOT NULL
);

CREATE TABLE "product_categories" (
  "id" serial PRIMARY KEY,
  "name" varchar NOT NULL
);

CREATE TABLE "countries" (
  "id" serial PRIMARY KEY,
  "name" varchar NOT NULL
);

ALTER TABLE "products" ADD FOREIGN KEY ("category") REFERENCES "product_categories" ("id") ON DELETE CASCADE ON UPDATE CASCADE;

ALTER TABLE "users" ADD FOREIGN KEY ("country") REFERENCES "countries" ("id") ON DELETE CASCADE ON UPDATE CASCADE;

ALTER TABLE "installations" ADD FOREIGN KEY ("user_id") REFERENCES "users" ("id") ON DELETE CASCADE ON UPDATE CASCADE;

ALTER TABLE "installations" ADD FOREIGN KEY ("software_id") REFERENCES "products" ("id") ON DELETE CASCADE ON UPDATE CASCADE;
