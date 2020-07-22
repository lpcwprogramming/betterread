-- Exported from QuickDBD: https://www.quickdatabasediagrams.com/
-- Link to schema: https://app.quickdatabasediagrams.com/#/d/ijGHGj
-- NOTE! If you have used non-SQL datatypes in your design, you will have to change these here.


CREATE TABLE "Books" (
    "book_id" serial   NOT NULL,
    "book_title" varchar(100)   NOT NULL,
    "series_name" varchar(100)   NOT NULL,
    "language" varchar(100)   NOT NULL,
    "author_id" int   NOT NULL,
    "fiction_non" varchar(100)   NOT NULL,
    "genre" varchar(100)   NOT NULL,
    "number_of_pages" varchar(100)   NOT NULL,
    "year_read" varchar(100)   NOT NULL,
    CONSTRAINT "pk_Books" PRIMARY KEY (
        "book_id","author_id"
     )
);

CREATE TABLE "Hometowns" (
    "author_id" int   NOT NULL,
    "hometown" varchar(100)   NOT NULL,
    "books_written" varchar(100)   NOT NULL,
    CONSTRAINT "pk_Hometowns" PRIMARY KEY (
        "author_id"
     )
);

CREATE TABLE "Authors" (
    "author_id" serial   NOT NULL,
    "author_name" varchar(100)   NOT NULL,
    CONSTRAINT "pk_Authors" PRIMARY KEY (
        "author_id"
     )
);

ALTER TABLE "Books" ADD CONSTRAINT "fk_Books_author_id" FOREIGN KEY("author_id")
REFERENCES "Authors" ("author_id");

ALTER TABLE "Hometowns" ADD CONSTRAINT "fk_Hometowns_author_id" FOREIGN KEY("author_id")
REFERENCES "Authors" ("author_id");

