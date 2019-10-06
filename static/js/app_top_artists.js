// // @TODO: Use `d3.json` to fetch the sample data for the plots
var url = `/topartists-data`;
let xdata = []
let ydata = []

var selectorOptions = {
    buttons: [{
        step: 'month',
        stepmode: 'backward',
        count: 1,
        label: '1m'
    }, {
        step: 'month',
        stepmode: 'backward',
        count: 6,
        label: '6m'
    }, {
        step: 'year',
        stepmode: 'todate',
        count: 1,
        label: 'YTD'
    }, {
        step: 'year',
        stepmode: 'backward',
        count: 1,
        label: '1y'
    }, {
        step: 'all',
    }],
};

d3.json(url).then(function(response) {

var topartists = response;
console.log(topartists)

for (var i = 0, l = topartists.length; i < l; i++) {
    xdata.push(Object.keys(topartists[i])[0])
    ydata.push(Object.values(topartists[i])[0]);
}

// for (var i = 0, l = topartists.length; i < l; i++) {
//     console.log(Object.keys(topartists[i])[0])
//     console.log(Object.values(topartists[i])[0]);
// }

var layout = {
    title: 'Top 25 Artists',
    xaxis: {
        rangeselector: selectorOptions
    },
    yaxis: {
        fixedrange: true
    }
};

var data = [
    {
      x: xdata,
      y: ydata,
      type: 'bar'
    }
  ];
  
  Plotly.newPlot('top-artists-chart', data, layout);

});