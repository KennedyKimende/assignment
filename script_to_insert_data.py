from faker import Faker
import psycopg2
import random

# Initialize Faker
fake = Faker()

# Connect to PostgreSQL
conn = psycopg2.connect(
    dbname="simpledb",
    user="postgres",
    password="postgres",
    host="localhost",
    port="5433"
)
cur = conn.cursor()

# Insert 1,000 authors
author_ids = []
for _ in range(1000):
    name = fake.name()
    birthdate = fake.date_of_birth(minimum_age=25, maximum_age=90)
    cur.execute(
        "INSERT INTO authors (name, birthdate) VALUES (%s, %s) RETURNING author_id",
        (name, birthdate)
    )
    author_id = cur.fetchone()[0]
    author_ids.append(author_id)

conn.commit()
print("Inserted 1000 authors.")

# Insert 10,000 books
for _ in range(10000):
    title = fake.sentence(nb_words=5)
    published_date = fake.date_between(start_date='-30y', end_date='today')
    author_id = random.choice(author_ids)
    cur.execute(
        "INSERT INTO books (title, published_date, author_id) VALUES (%s, %s, %s)",
        (title, published_date, author_id)
    )

conn.commit()
print("Inserted 10,000 books.")

# Clean up
cur.close()
conn.close()
