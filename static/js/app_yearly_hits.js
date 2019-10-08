var chosenYearlyHitsTimeFrame = '2018'
var listofYearlyHitsTimeFrames = ["2018","2017","2016","2015","2014","2013","2012","2011","2010","2009","2008","2007","2006","2005","2004","2003","2002","2001","2000","1999","1998","1997","1996","1995","1994","1993","1992","1991","1990","1989","1988","1987","1986","1985","1984","1983","1982","1981","1980","1979","1978","1977","1976","1975","1974","1973","1972","1971","1970","1969","1968","1967","1966","1965","1964","1963","1962","1961","1960"]
setYearlyHitsBarChart('2018');


function setYearlyHitsBarChart(chosenYearlyHitsTimeFrame) {
      var YearlyHitsUrl = `/yearlyhits-data/${chosenYearlyHitsTimeFrame}`;
      var xYearlyHitsData = [];
      var yYearlyHitsData = [];
      d3.json(YearlyHitsUrl).then(function(YearlyHitsResponse) {
          var mostYearlyHitsArtists = YearlyHitsResponse;
          console.log(mostYearlyHitsArtists)
          
          for (var i = 0, l = mostYearlyHitsArtists.length; i < l; i++) {
            xYearlyHitsData.push(Object.keys(mostYearlyHitsArtists[i])[0])
            yYearlyHitsData.push(Object.values(mostYearlyHitsArtists[i])[0]);
          }
      
          var YearlyHitsLayout = {
            title: 'Top 4 Artists by Number of Hits in a Year',
            height: 600,
            width: 800,
          };

      var YearlyHitsData = [
          {
          labels: xYearlyHitsData,
          values: yYearlyHitsData,
          hole: .4,
          type: 'pie',
          }
      ];
      
      Plotly.newPlot('most-YearlyHits-chart', YearlyHitsData, YearlyHitsLayout);
});
  }

var innerContainer = document.getElementById('YearlyHitsPie'),
      plotEl = innerContainer.querySelector('.YearlyHitsPlot'),
      YearlyHitsTimeFrameSelector = innerContainer.querySelector('.YearlyHitstimeframedata');
      // console.log(innerContainer);
      // console.log(plotEl);
      // console.log(YearlyHitsTimeFrameSelector);

  function assignOptions(textArray, selector) {
      for (var i = 0; i < textArray.length;  i++) {
          var currentOption = document.createElement('option');
          currentOption.text = textArray[i];
          selector.appendChild(currentOption);
      }
  }

  assignOptions(listofYearlyHitsTimeFrames, YearlyHitsTimeFrameSelector);

  function updateYearlyHitsTimeFrame(){
    setYearlyHitsBarChart(YearlyHitsTimeFrameSelector.value);
  }

  YearlyHitsTimeFrameSelector.addEventListener('change', updateYearlyHitsTimeFrame, false);