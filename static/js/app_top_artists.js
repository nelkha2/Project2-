  var chosenTimeFrame = 'All-Time'
  var listofTimeFrames = ["All-Time", "1960`s", "1970`s", "1980`s", "1990`s", "2000`s", "2010`s"]
  setBarChart('All-Time');


    function setBarChart(chosenTimeFrame) {
        var url = `/topartists-data/${chosenTimeFrame}`;
        var xdata = [];
        var ydata = [];
        d3.json(url).then(function(response) {
            var allTimeTopArtists = response;
            console.log(allTimeTopArtists)
            
            for (var i = 0, l = allTimeTopArtists.length; i < l; i++) {
                xdata.push(Object.keys(allTimeTopArtists[i])[0])
                ydata.push(Object.values(allTimeTopArtists[i])[0]);
            }
        
        var layout = {
            title: 'Top 25 Artists',
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
    }

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