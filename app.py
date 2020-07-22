import numpy as np

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify, render_template
from flask_cors import CORS


#Set up Flask
#######################################################################
app = Flask(__name__)
CORS(app)

#Set up database
#######################################################################

#Create engine
connection = "postgres:postgres@localhost:5432/books"
engine = create_engine(f'postgresql://{connection}')

# reflect an existing database into a new model
Base = automap_base()

# reflect the tables
Base.prepare(engine, reflect=True)

#Save references to each table
Authors = Base.classes.authors
Books = Base.classes.books
Hometowns = Base.classes.hometowns

#Create  session from Python to the DB
session = Session(engine)

#Flask Routes
#######################################################################

@app.route("/")
def home():
    #Template for home page
    return render_template("index.html")
    
    # """List all available api routes."""
    # return (
    #     f"Available Routes:<br/>"
    #     f"/api/v1.0/authors<br/>"
    #     f"/api/v1.0/books<br/>"
    # #     f"/api/v1.0/hometowns<br/>"
    # )


@app.route("/years")
def years():

    #Select data to be used
    data = [Books.year_read]
    
    #SQL query
    years = session.query(*data)\
            .filter(Books.year_read != "0")\
            .order_by(Books.year_read)\
            .distinct().all()

    #Return JSON format
    return jsonify(list(years))


@app.route("/treemap")
def treemap():

    #Select data to be used
    data = [Books.book_title, Books.series_name, Books.author_name, Books.language, Books.fiction_non, Books.genre, Books.year_read]

    #SQL query
    books_treemap = session.query(*data).all()
    
    #Create an book dictionary from the row data and append to a list
    for data in books_treemap:
        book_dict = {}
        book_dict["book_title"] = book_title
        book_dict["series_name"] = series_name
        book_dict["author_name"] = author_name
        book_dict["language"] = language
        book_dict["fiction_non"] = fiction_non
        book_dict["genre"] = genre
        book_dict["year_read"] = year_read
 
    #Return JSON format
    return jsonify(book_dict)

@app.route("/scatter")
def scatter():
    
    #Select data to be used
    data = [Books.book_title, Books.genre, Books.number_of_pages, Books.year_read]

    #SQL query
    books_scatter = session.query(*data)\
                    .filter(Books.year_read != "0")\
                    .order_by(Books.year_read)\
                    .all()

    #Return JSON format
    return jsonify(books_scatter)
    
#     #Author query
#     authors = session.query(Authors.author_id, Authors.author_name).all()

#     session.close()

#     #Create an author dictionary from the row data and append to a list
#     author_data = []
#     for author_id, author_name in authors:
#         author_dict = {}
#         author_dict["author_id"] = author_id
#         author_dict["author_name"] = author_name
#         author_data.append(author_dict)

#     #Return JSON format
#     return jsonify(author_data)


# @app.route("/api/v1.0/books")
# def books(): 

#     # Create  session from Python to the DB
#     session = Session(engine)

#     #Book query
#     books = session.query(Books.book_id,Books.book_title, Books.series_name, Books.author_name, Books.language, Books.fiction_non, Books.genre, Books.number_of_pages, Books.year_read).all()

#     session.close()

#     #Create an book dictionary from the row data and append to a list
#     book_data = []
#     for book_id,book_title,series_name,author_name,language,fiction_non,genre,number_of_pages,year_read in books:
#         book_dict = {}
#         book_dict["book_id"] = book_id
#         book_dict["book_title"] = book_title
#         book_dict["series_name"] = series_name
#         book_dict["author_name"] = author_name
#         book_dict["language"] = language
#         book_dict["fiction_non"] = fiction_non
#         book_dict["genre"] = genre
#         book_dict["number_of_pages"] = number_of_pages
#         book_dict["year_read"] = year_read
#         book_data.append(book_dict)
    
#     #Return JSON format
#     return jsonify(book_data)


# @app.route("/api/v1.0/hometowns")
# def hometowns():
#     # Create  session from Python to the DB
#     session = Session(engine)

#     #Hometown query
#     hometowns = session.query(Hometowns.author_name, Hometowns.hometown, Hometowns.books_written).all()

#     session.close()

#     #Create an author dictionary from the row data and append to a list
#     hometown_data = []
#     for author_name, hometown, books_written in hometowns:
#         hometown_dict = {}
#         hometown_dict["author_name"] = author_name
#         hometown_dict["hometown"] = hometown
#         hometown_dict["books_written"] = books_written
#         hometown_data.append(hometown_dict)

#     #Return JSON format
#     return jsonify(hometown_data)

if __name__ == '__main__':
    app.run(debug=True)