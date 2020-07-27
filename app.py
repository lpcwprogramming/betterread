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
Years = Base.classes.years
# Bardata = Base.classes.bardata

#Create  session from Python to the DB
session = Session(engine)

#Flask Routes
#######################################################################

#Template routes
@app.route("/")
def home():
    #Template for home page
    return render_template("index.html")

@app.route("/plots")
def plots():
    #Template for home page
    return render_template("Plots.html")

@app.route("/booklist")
def booklist():
    #Template for home page
    return render_template("books.html")

#Bar chart year routes
@app.route("/bar/2011")
def bar_2011():

    #Select data to be used
    data = [Books.book_title, Books.genre, Books.year_read]
    
    #SQL query
    year_2011 = session.query(*data)\
                .filter(Books.year_read == "2011")\
                .order_by(Books.year_read)\
                .distinct().all()

    #Return JSON format
    return jsonify(list(year_2011))

@app.route("/bar/2012")
def bar_2012():

    #Select data to be used
    data = [Books.book_title, Books.genre, Books.year_read]
    
    #SQL query
    year_2012 = session.query(*data)\
                .filter(Books.year_read == "2012")\
                .order_by(Books.year_read)\
                .distinct().all()

    #Return JSON format
    return jsonify(list(year_2012))

@app.route("/bar/2013")
def bar_2013():

    #Select data to be used
    data = [Books.book_title, Books.genre, Books.year_read]
    
    #SQL query
    year_2013 = session.query(*data)\
                .filter(Books.year_read == "2013")\
                .order_by(Books.year_read)\
                .distinct().all()

    #Return JSON format
    return jsonify(list(year_2013))

@app.route("/bar/2014")
def bar_2014():

    #Select data to be used
    data = [Books.book_title, Books.genre, Books.year_read]
    
    #SQL query
    year_2014 = session.query(*data)\
                .filter(Books.year_read == "2014")\
                .order_by(Books.year_read)\
                .distinct().all()

    #Return JSON format
    return jsonify(list(year_2014))

@app.route("/bar/2015")
def bar_2015():

    #Select data to be used
    data = [Books.book_title, Books.genre, Books.year_read]
    
    #SQL query
    year_2015 = session.query(*data)\
                .filter(Books.year_read == "2015")\
                .order_by(Books.year_read)\
                .distinct().all()

    #Return JSON format
    return jsonify(list(year_2015))

@app.route("/bar/2016")
def bar_2016():

    #Select data to be used
    data = [Books.book_title, Books.genre, Books.year_read]
    
    #SQL query
    year_2016 = session.query(*data)\
                .filter(Books.year_read == "2016")\
                .order_by(Books.year_read)\
                .distinct().all()

    #Return JSON format
    return jsonify(list(year_2016))

@app.route("/bar/2017")
def bar_2017():

    #Select data to be used
    data = [Books.book_title, Books.genre, Books.year_read]
    
    #SQL query
    year_2017 = session.query(*data)\
                .filter(Books.year_read == "2017")\
                .order_by(Books.year_read)\
                .distinct().all()

    #Return JSON format
    return jsonify(list(year_2017))

@app.route("/bar/2018")
def bar_2018():

    #Select data to be used
    data = [Books.book_title, Books.genre, Books.year_read]
    
    #SQL query
    year_2018 = session.query(*data)\
                .filter(Books.year_read == "2018")\
                .order_by(Books.year_read)\
                .distinct().all()

    #Return JSON format
    return jsonify(list(year_2018))

@app.route("/bar/2019")
def bar_2019():

    #Select data to be used
    data = [Books.book_title, Books.genre, Books.year_read]
    
    #SQL query
    year_2019 = session.query(*data)\
                .filter(Books.year_read == "2019")\
                .order_by(Books.year_read)\
                .distinct().all()

    #Return JSON format
    return jsonify(list(year_2019))

#Sunburst chart route
@app.route("/sunburst")
def sunburst():

    #Tuples data
    return render_template("final.json")

#Sub plots route
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

#Year list route
@app.route("/years")
def years():
    
    #Select data to be used
    data = [Years.years]

    #SQL query
    year_list = session.query(*data).all()

    #Return JSON format
    return jsonify(year_list)

#Year list route
@app.route("/genres")
def genres():
    
    #Select data to be used
    data = [Books.genre]

    #SQL query
    genre_list = session.query(*data).distinct().all()

    #Return JSON format
    return jsonify(genre_list)


if __name__ == '__main__':
    app.run(debug=True)