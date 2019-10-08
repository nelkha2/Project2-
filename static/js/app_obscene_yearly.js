
      var obscenexUrl = `/obsceneyearly-data`;
      var xobscenexData = [];
      var yobscenexData = [];

      d3.json(obscenexUrl).then(function(obscenexResponse) {
          var mostobscenexArtists = obscenexResponse;
          //console.log(mostobscenexArtists)
          
          for (var i = 0, l = mostobscenexArtists.length; i < l; i++) {
            xobscenexData.push(Object.keys(mostobscenexArtists[i])[0])
            yobscenexData.push(Object.values(mostobscenexArtists[i])[0]);
          }
      
      var obscenexLayout = {
          title: 'Total Obscene Words per Year',
      };

      var obscenexData = [
          {
          x: xobscenexData,
          y: yobscenexData,
          type: 'line',
          marker: {
            color: 'rgb(189, 41, 15)'
          }
          }
      ];
      
      Plotly.newPlot('most-obscenex-chart', obscenexData, obscenexLayout);
});
