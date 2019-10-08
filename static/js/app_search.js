var v = require('voca');
function buildArtistdata(artist) {

    // @TODO: Complete the following function that builds the metadata panel
    $("tbody").children().remove();
    // Use `d3.json` to fetch the metadata for a sample
    d3.json(`/search/${artist}`).then(function(response){
      // Use d3 to select the panel with id of `#sample-metadata`
      console.log(response)
        // Use `.html("") to clear any existing metadata
      
      var tr;
      for (var i = 0; i < response.length; i++) {
            tr = $('<tr/>');
            tr.append("<td>" + response[i].year + "</td>");
            tr.append("<td>" + response[i].rank + "</td>");
            tr.append("<td>" + response[i].song + "</td>");
            $('table').append(tr);
    };
  });
}
var button = d3.select("#artistButton");

button.on("click", function(){
  var inputArtist = d3.select("#autoComplete");
  var inputArtistValue = inputArtist.property("value");
  console.log(inputArtistValue);
  var fixedInput = v.capitalize(inputArtistValue, true);
  console.log(fixedInput);
  console.log("WhattheFUCK?!");
  var myTable = document.getElementById("artist-table");
  var rowCount = myTable.rows.length;
  for (var x=rowCount-1; x>0; x--) {
   myTable.deleteRow(x);
  };
  buildArtistdata(fixedInput)
})