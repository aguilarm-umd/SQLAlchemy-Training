#! /usr/bin/env python

import sys, pdb
from sqlalchemy import Table, Column, Integer, String, MetaData, ForeignKey
from sqlalchemy import create_engine, select

# Description:
# This is a toy application for learning SQLAlchemy.
# This application does five things:
# - Connect to either a Postgres or SQLite Database
# - Sets up the database
# - Queries the database
# - Populates the database
# - Queries again

# Gather User Input
inp = input("Postgress (1) or SQLite (2)?\n")
engine = None
if inp == '1':
    conn_url = 'postgresql+psycopg2://postgres:password@localhost:5432/testdb'
    engine = create_engine(conn_url)

elif inp == '2':
    engine = create_engine('sqlite:///:memory:')
else:
    sys.exit("Bad Input: Either \'1\' or \'2\'")

# Setup Database
meta = MetaData()
users = Table('users', meta,
            Column('user_id', Integer, primary_key=True),
            Column('name', String, nullable=False)
        )

books = Table('books', meta,
            Column('user_id', Integer, ForeignKey('users.user_id')),
            Column('title', String, nullable=False)
        )

meta.create_all(engine)
conn = engine.connect()

# First Query
users_set = conn.execute(select([users])).fetchall()
books_set = conn.execute(select([books])).fetchall()
print(users_set)
print(books_set)

# Populate Database
if not users_set:
    conn.execute(users.insert(),
                [
                    {'user_id': 1, 'name': 'marc'},
                    {'user_id': 2, 'name': 'andreu'},
                    {'user_id': 3, 'name': 'grillo'},
                    {'user_id': 4, 'name': 'aguilar'},
                ]
    )

if not books_set:
    conn.execute(books.insert(),
                [
                    {'user_id': 1, 'title': 'one piece'},
                    {'user_id': 2, 'title': 'magi'},
                    {'user_id': 3, 'title': 'the book of numbers'},
                    {'user_id': 4, 'title': 'fermat\'s enigma'},
                ]
    )

# Second Query
users_set = conn.execute(select([users])).fetchall()
books_set = conn.execute(select([books])).fetchall()
print(users_set)
print(books_set)