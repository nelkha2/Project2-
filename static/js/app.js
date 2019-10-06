// from data.js
var tableData = data;
var tbody = d3.select("tbody");
// YOUR CODE HERE!
data.forEach((song) => {
    var row = tbody.append("tr");
    Object.entries(song).forEach(([key, value]) => {
      var cell = row.append("td");
      cell.text(value);
    });
  });
var button = d3.select("#filter-btn");
var button2 = d3.select("#reset-btn");
button.on("click", function() {

    // Select the input element and get the raw HTML node
    var inputRankElement = d3.select("#rankbillboard");
    var inputSongElement = d3.select("#songbillboard");
    var inputArtistElement = d3.select("#artistbillboard");
    var inputYearElement = d3.select("#yearbillboard");
    var inputLyricElement = d3.select("#lyricbillboard");
  
    // Get the value property of the input element
    var inputRankValue = inputRankElement.property("value");
    var inputSongValue = inputSongElement.property("value");
    var inputArtistValue = inputArtistElement.property("value");
    var inputYearValue = inputYearElement.property("value");
    var inputLyricValue = inputLyricsElement.property("value");
  
    if (inputRankValue.length == 0) {
      var rankFilteredData = tableData;
    } else {
      var rankFilteredData = tableData.filter(hit => hit.rank === inputRankValue);
    };
    if (inputSongValue.length == 0) {
      var songFilteredData = rankFilteredData;
    } else {
      var songFilteredData = rankFilteredData.filter(hit => inputSongValue.toLowerCase().indexof(hit.title.toLowerCase()) >=0);
    };
    if (inputArtistValue.length == 0) {
      var artistFilteredData = songFilteredData;
    } else {
      var artistFilteredData = songFilteredData.filter(hit => inputArtistValue.toLowerCase().indexof(hit.artist.toLowerCase()) >=0);
    };
    if (inputYearValue.length == 0) {
      var yearFilteredData = artistFilteredData;
    } else {
      var yearFilteredData = artistFilteredData.filter(hit => hit.year === inputYearValue);
    };
    if (inputLyricsValue.length == 0) {
      var finalFilteredData = yearFilteredData;
    } else {
      var finalFilteredData = yearFilteredData.filter(hit => inputLyricsValue.toLowerCase().indexof(hit.lyrics.toLowerCase()) >=0);
    };
    
    var tableHeaderRowCount = 1;
    var table = document.getElementById('hit-table');
    var rowCount = table.rows.length;
    for (var i = tableHeaderRowCount; i < rowCount; i++) {
        table.deleteRow(tableHeaderRowCount);
    };

    console.log(finalFilteredData);
    finalFilteredData.forEach((hit) => {
      var row = tbody.append("tr");
      Object.entries(hit).forEach(([key, value]) => {
        var cell = row.append("td");
        cell.text(value);
      });
    });
});
button2.on("click", function(){
  var tableHeaderRowCount = 1;
  var table = document.getElementById('hit-table');
  var rowCount = table.rows.length;
  for (var i = tableHeaderRowCount; i < rowCount; i++) {
      table.deleteRow(tableHeaderRowCount);
  };
  data.forEach((hit) => {
    var row = tbody.append("tr");
    Object.entries(hit).forEach(([key, value]) => {
      var cell = row.append("td");
      cell.text(value);
    });
  });
})
