// Pull data from FLASK API
d3.json(`http://127.0.0.1:5000/scatter`).then(function(data) { 
    
    // Number of pages and years read data for scatter plot
    var books = data.map(d=>d[0])
    var genres = data.map(d=>d[1])
    var pages = data.map(d=>+d[2])
    var years = data.map(d=>+d[3])
    console.log(books)
    console.log(genres)

        // Trace with scatter plot data
        var trace1 = {
        x: years,
        y: pages,
        mode: "markers",
        type: "scatter",
        marker: {
            color: "#CC0066",
            size: 7}
        };

        // Scatter plot layout
        var layout = {
            title: "Number of Pages Per Books Read Between 2011 - 2019",
            xaxis: {
                title: "Year read",
                autotick: false,
            },
            yaxis:{title: "Pages per book"},
            hovermode: "closest",

        };
    

    // List for trace
    var data = [trace1];

    // Create scatter plot
    Plotly.newPlot("mydiv", data, layout, {displayModeBar: false});

})