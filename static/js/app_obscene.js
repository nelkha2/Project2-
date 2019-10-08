var chosenobsceneTimeFrame = 'All-Time'
var listofobsceneTimeFrames = ["All-Time", "1960`s", "1970`s", "1980`s", "1990`s", "2000`s", "2010`s"]
setobsceneBarChart('All-Time');


function setobsceneBarChart(chosenobsceneTimeFrame) {
      var obsceneUrl = `/obscene-data/${chosenobsceneTimeFrame}`;
      var xobsceneData = [];
      var yobsceneData = [];
      d3.json(obsceneUrl).then(function(obsceneResponse) {
          var mostobsceneArtists = obsceneResponse;
          //console.log(mostobsceneArtists)
          
          for (var i = 0, l = mostobsceneArtists.length; i < l; i++) {
            xobsceneData.push(Object.keys(mostobsceneArtists[i])[0])
            yobsceneData.push(Object.values(mostobsceneArtists[i])[0]);
          }
      
      var obsceneLayout = {
          title: 'Most Obscene Artists',
      };

      var obsceneData = [
          {
          x: xobsceneData,
          y: yobsceneData,
          type: 'bar',
          marker: {
            color: 'rgb(189, 41, 15)'
          }
          }
      ];
      
      Plotly.newPlot('most-obscene-chart', obsceneData, obsceneLayout);
});
  }

  var innerContainer = document.getElementById('obsceneBar'),
  plotEl = innerContainer.querySelector('.obscenePlot'),
  obsceneTimeFrameSelector = innerContainer.querySelector('.obscenetimeframedata');
  // console.log(innerContainer);
  // console.log(plotEl);
  // console.log(obsceneTimeFrameSelector);

function assignOptions(textArray, selector) {
  for (var i = 0; i < textArray.length;  i++) {
      var currentOption = document.createElement('option');
      currentOption.text = textArray[i];
      selector.appendChild(currentOption);
  }
}

assignOptions(listofobsceneTimeFrames, obsceneTimeFrameSelector);

function updateobsceneTimeFrame(){
setobsceneBarChart(obsceneTimeFrameSelector.value);
}

obsceneTimeFrameSelector.addEventListener('change', updateobsceneTimeFrame, false);