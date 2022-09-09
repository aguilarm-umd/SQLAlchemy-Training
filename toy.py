#! /usr/bin/env python

import sys, pdb
from sqlalchemy import Table, Column, Integer, String, MetaData, ForeignKey
from sqlalchemy import create_engine, select

inp = input("Postgress (1) or SQLite (2)?\n")
engine = None
if inp == '1':
    # Currently set up to use my ip address. The postgres server is ported to 5432
    conn_url = 'postgresql+psycopg2://postgres:password@localhost:5432/testdb'
    engine = create_engine(conn_url)

elif inp == '2':
    engine = create_engine('sqlite:///:memory:')
else:
    sys.exit("Bad Input: Either \'1\' or \'2\'")

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

# Right now I will try to fetch:
# The sqlite version is created from memory so it wont have anything
# The first time the postgres version won't have anything, but if this
# file is ran more than once, the query will not be empty
users_set = conn.execute(select([users])).fetchall()
books_set = conn.execute(select([books])).fetchall()
print(users_set)
print(books_set)

# I will now populate the databases
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

# Now if I retrieve the tables there will definitely be entries
users_set = conn.execute(select([users])).fetchall()
books_set = conn.execute(select([books])).fetchall()
print(users_set)
print(books_set)