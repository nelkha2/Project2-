var chosenwthTimeFrame = 'All-Time'
var listofwthTimeFrames = ["All-Time", "1960`s", "1970`s", "1980`s", "1990`s", "2000`s", "2010`s"]
setwthBarChart('All-Time');


  
function setwthBarChart(chosenwthTimeFrame) {
      var wthUrl = `/words-to-hits-data/${chosenwthTimeFrame}`;
      var xwthData = [];
      var ywthData = [];
      var zwthData = [];

      d3.json(wthUrl).then(function(wthResponse) {
          var mostwthArtists = wthResponse;
          console.log(mostwthArtists)
          
          for (var i = 0, l = mostwthArtists.length; i < l; i++) {
            xwthData.push(Object.keys(mostwthArtists[i])[0])
            ywthData.push(Object.values(mostwthArtists[i])[0]);
          }
      
      var wthLayout = {
          title: 'Average Words Compared to Hits',
      };

      var wthData = [
          {
          x: xwthData,
          y: ywthData,
          mode: 'markers',
          marker: {
            color: ['rgb(93, 164, 214)', 'rgb(255, 144, 14)',  'rgb(44, 160, 101)', 'rgb(255, 65, 54)']
          }
          }
      ];
      
      Plotly.newPlot('most-wth-chart', wthData, wthLayout);
});
  }

var innerContainer = document.getElementById('wthBar'),
      plotEl = innerContainer.querySelector('.wthPlot'),
      wthTimeFrameSelector = innerContainer.querySelector('.wthtimeframedata');
      // console.log(innerContainer);
      // console.log(plotEl);
      // console.log(wthTimeFrameSelector);

  function assignOptions(textArray, selector) {
      for (var i = 0; i < textArray.length;  i++) {
          var currentOption = document.createElement('option');
          currentOption.text = textArray[i];
          selector.appendChild(currentOption);
      }
  }

  assignOptions(listofwthTimeFrames, wthTimeFrameSelector);

  function updatewthTimeFrame(){
    setwthBarChart(wthTimeFrameSelector.value);
  }

  wthTimeFrameSelector.addEventListener('change', updatewthTimeFrame, false);