var chosenVerboseTimeFrame = 'All-Time'
var listofVerboseTimeFrames = ["All-Time", "1960`s", "1970`s", "1980`s", "1990`s", "2000`s", "2010`s"]
setVerboseBarChart('All-Time');


function setVerboseBarChart(chosenVerboseTimeFrame) {
      var verboseUrl = `/lyrics-data/${chosenVerboseTimeFrame}`;
      var xVerboseData = [];
      var yVerboseData = [];
      d3.json(verboseUrl).then(function(verboseResponse) {
          var mostVerboseArtists = verboseResponse;
          //console.log(mostVerboseArtists)
          
          for (var i = 0, l = mostVerboseArtists.length; i < l; i++) {
            xVerboseData.push(Object.keys(mostVerboseArtists[i])[0])
            yVerboseData.push(Object.values(mostVerboseArtists[i])[0]);
          }
      
      var verboseLayout = {
          title: 'Most Verbose Artists',
      };

      var verboseData = [
          {
          x: xVerboseData,
          y: yVerboseData,
          type: 'bar',
          marker: {
            color: 'rgb(142,124,195)'
          }
          }
      ];
      
      Plotly.newPlot('most-verbose-chart', verboseData, verboseLayout);
});
  }

var innerContainer = document.getElementById('verboseBar'),
      plotEl = innerContainer.querySelector('.verbosePlot'),
      verboseTimeFrameSelector = innerContainer.querySelector('.verbosetimeframedata');
      // console.log(innerContainer);
      // console.log(plotEl);
      // console.log(verboseTimeFrameSelector);

  function assignOptions(textArray, selector) {
      for (var i = 0; i < textArray.length;  i++) {
          var currentOption = document.createElement('option');
          currentOption.text = textArray[i];
          selector.appendChild(currentOption);
      }
  }

  assignOptions(listofVerboseTimeFrames, verboseTimeFrameSelector);

  function updateVerboseTimeFrame(){
    setVerboseBarChart(verboseTimeFrameSelector.value);
  }

  verboseTimeFrameSelector.addEventListener('change', updateVerboseTimeFrame, false);