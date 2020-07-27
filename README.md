# **The Better Read Than Dead Book Project**


## **Background**

When I was in 5th grade, I decided that if I wanted to be smart I had to read books. I marched myself to a book store and asked a staffer whatI should read. This was the beginning of a beautfiul obsession that went from lists in notebooks, to an Excel sheet, and finally to this project. It's truly been a natural progression of all of my interests - books, computers, and making my life difficult. 


## **Data**

This is a personal log of the books I have read spanning roughly 18 years (2001-2019). My original dataset included the title, name of the series, volume, and the author's name. Eventually, I began adding number of pages, the year the book was published, and the year I read the book. Unfortunately, this was never meant to be a formal dataset, so there were inconsistencies in the data that was available and how the data was recorded. 


## **ETL Process**

The first stage of the data cleaning involved joining the two data sets I had for the books, one of them in a Word Document and the second one in Excel. To achieve this, I manually joined the two files in Excel. The data in the Word document had both the title and the author’s name on the same line, separated by a dash. I used the tools in Excel to separate these into two columns. 

Once I had both data sets on the same file. I loaded the csv into Jupyter Notebook to continue working with the data and filling out the gaps. My next step was to pull additional data from the Goodreads API and load everything into a SQL database. Because many of the inconsistencies only came up throgh errors as I was loading the data, the data cleaning process was very iterative. 

In preparing the data for the Goodreads API, I had to go back and modify some of the author entries, which contained author name and series name or genre in the same column. The API also missed authors whose names were misspelled or contained foreign characters. In the process of loading the data into the database, there were also errors that came up - such as books with the same title, added spaces in the author's name, etc. These issues kept SQL from assigning primary keys, foreign keys, and table connections. 

### _Goodreads API_

I had originally intended to pull page numbers, genres, and additional author information from the Goodreads API. Although their API has all these functionalities, they are difficult to access due to the way the API is structured. Paired with incomplete and sparse documentation, it seemed like the API would be impossible to use. 

However, I found a [user created library] (https://github.com/sefakilic/goodreads) meant to serve as a more intuitive interface to Goodread's API. Through it, I was able to pull author information, such as hometowns, which will be used in later versions of this project. These new data points were also loaded into the SQL database. 

## **Flask API**

I built a Flask API to serve my HTML pages and pull data from the SQL database. This happened parallel to the ETL process. I first created the routes for my front facing pages, namely my home page, visualization page, and data page. I then created routes to pull data from SQL as was necessary for my visualizations. Below are all the existing API routes. 

*/*
*/plots*
*/booklist*
*/bar/2011*
*/bar/2012*
*/bar/2013*
*/bar/2014*
*/bar/2015*
*/bar/2016*
*/bar/2017*
*/bar/2018*
*/bar/2019*
*/sunburst*
*/scatter*
*/years*
*/genres*


## **Dashboard**

I built the dashboard using a combination of JavaScript, HTML, and CSS. At the moment, there is a static home page, a page to display the visualizations and a data page. 

### _Visualizations_

There are currently two visualizations available on the plots page. The first is a line and scatter plot displaying the amount of books read between 2011 and 2019. The second plot presents the pages for each book read in that time period.

### _Data Page_

I built the data page to hold a full list of the books I've read, with the idea of sharing it with people who might be looking for book recommendations. 


## **Next steps**

This is definitely a passion project for me. My plan is to keep adding books to the dataset as I read them, and updating the plots to reflect the new data. I would also like to add a search option to the data page, where people can filter by author or genre as they desire. Eventually, I would like to automate the process of adding information and updating the plots. I would also like to add more content to the page, such as recommendations and book reviews. 
