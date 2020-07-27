function unpack(rows, index) {
    return rows.map(function(rows) {
      return rows[index];
    });
  }

  function buildPlot() {
  d3.json(`http://127.0.0.1:5000/sunburst`).then(function(data){
    console.log(data)

    var parents = data.map(d=>d[0])
    var labels = data.map(d=>d[1])
    // labels = [];
    // parents = [];
    // for (var i = 0; i < 2; i++) {
    //     d = data[i]
    //     labels.push(d[0])
    //     parents.push(d[1])
    //     labels.push(d[1])
    //     parents.push(d[3])
    //     labels.push(d[3])
    //     parents.push(d[""])
        // labels.push(data[3])
        // parents.push('')
    // }
    // console.log(labels)
    // console.log(parents)
    // var genre = unpack(data, 3);
    // var author = unpack(data, 1);
    // var series = unpack(data, 2);
    // var title = unpack(data, 0);

    var data = [
        {
        type: "sunburst",
        maxdepth: 4,
        labels: labels,
        parents: parents,
        //   value: [genre,author,series,title]
        }
    ];

    var layout = {
    margin: {l: 0, r: 0, b: 0, t:0},
    sunburstcolorway:[
        "#636efa","#EF553B","#00cc96","#ab63fa","#19d3f3",
        "#e763fa", "#FECB52","#FFA15A","#FF6692","#B6E880"
    ],
    extendsunburstcolorway: true
    };


    Plotly.newPlot('sunburst', data, layout);
    })

    };

  buildPlot();