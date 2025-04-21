create database simpledb;




-- Create the authors table
CREATE TABLE authors (
    author_id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    birthdate DATE
);

-- Create the books table with a foreign key to authors
CREATE TABLE books (
    book_id SERIAL PRIMARY KEY,
    title VARCHAR(200) NOT NULL,
    published_date DATE,
    author_id INT NOT NULL,
    FOREIGN KEY (author_id) REFERENCES authors(author_id)
        ON DELETE CASCADE
        ON UPDATE CASCADE
);