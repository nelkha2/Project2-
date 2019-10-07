  var url = `/topartists-data/${timeFrame}`;
  var xdata = [];
  var ydata = [];
  var listofTimeFrames = ["All Time", "1960`s", "1970`s", "1980`s", "1990`s", "2000`s", "2010`s"]
  

  d3.json(url).then(function(response) {
  
    var allTimeTopArtists = response;
    // console.log(allTimeTopArtists)

    function getArtistData(chosenTimeFrame) {
        for (var i = 0, l = allTimeTopArtists.length; i < l; i++) {
            xdata.push(Object.keys(allTimeTopArtists[i])[0])
            ydata.push(Object.values(allTimeTopArtists[i])[0]);
        }
    };

    // Default Data
    setBarChart('All Time');

    function setBarChart(chosenTimeFrame) {
        getArtistData(chosenTimeFrame);

        var layout = {
            title: 'Top 25 Artists',
            xaxis: {
                // rangeselector: selectorOptions
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
    };

    var innerContainer = document.querySelector('[data-num="0"'),
        plotEl = innerContainer.querySelector('.plot'),
        timeFrameSelector = innerContainer.querySelector('.timeframedata');

    function assignOptions(textArray, selector) {
        for (var i = 0; i < textArray.length;  i++) {
            var currentOption = document.createElement('option');
            currentOption.text = textArray[i];
            selector.appendChild(currentOption);
        }
    }

    assignOptions(listofTimeFrames, timeFrameSelector);

    function updateTimeFrame(){
        setBarChart(timeFrameSelector.value);
    }

    timeFrameSelector.addEventListener('change', updateTimeFrame, false);
});