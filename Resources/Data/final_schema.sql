CREATE TABLE Books (
    book_id serial   NOT NULL UNIQUE,
    book_title varchar(100)   NOT NULL,
    series_name varchar(100),
    language varchar(100)   NOT NULL,
	author_name varchar(100) NOT NULL,
    fiction_non varchar(100)   NOT NULL,
    genre varchar(100)   NOT NULL,
    number_of_pages varchar(100)   NOT NULL,
    year_read varchar(100),
    CONSTRAINT pk_Books PRIMARY KEY (
        book_id
     )
);

CREATE TABLE Hometowns (
    author_name varchar(100)   NOT NULL,
    hometown varchar(100),
    books_written varchar(100)   NOT NULL,
	CONSTRAINT pk_Hometowns PRIMARY KEY (
		author_name
	)
);

CREATE TABLE Authors (
    author_id serial   NOT NULL,
    author_name varchar(100)   NOT NULL,
    CONSTRAINT pk_Authors PRIMARY KEY (
        author_id
     )
);