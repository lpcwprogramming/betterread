// Pull data from FLASK API
d3.json(`http://127.0.0.1:5000/scatter`).then(function(data) { 
    
    // Number of pages and years read data for scatter plot
    var books = data.map(d=>d[0])
    var genres = data.map(d=>d[1])
    var pages = data.map(d=>+d[2])
    var years = data.map(d=>+d[3])
    console.log(books)
    console.log(genres)

        // // Trace with line and marker data
        var trace1 = {
            x: ["2011","2012","2013","2014","2015","2016","2017","2018","2019"],
            y: [61,41,22,31,29,27,10,5,9],
            mode: "lines+markers",
            name: "Books per year",
            line: {color: "purple"},
            type: "scatter",
            marker: {
                color: "#CC0066",
                size: 8
            }
        };

var data = [trace1];

var layout = {
  title: "Number of Books Read Between 2011 - 2019",
  xaxis: {
      title: "Year read",
      zeroline: true,
      autotick: false,
    },
  yaxis:{title: "Books read per year"},
  hovermode: "closest",
  
};

Plotly.newPlot('subplots', data, layout, {displayModeBar: false});

})