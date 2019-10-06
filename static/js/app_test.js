<<<<<<< HEAD
// Extract data from json
function buildMetadata(sample) {

=======
function buildMetadata(sample) {

  // @TODO: Complete the following function that builds the metadata panel

>>>>>>> Nader_new
  // Use `d3.json` to fetch the metadata for a sample
  var url_metadata = `/billboard/${rankid}`;
  d3.json(url_metadata).then(function(sample) {
    //display array
    console.log(sample);

    // Use d3 to select the panel with id of `#sample-metadata`
    var metadataSelction = d3.select("#sample-metadata");

    // Use `.html("") to clear any existing metadata
    d3.select("#sample-metadata").html("");

    // Use `Object.entries` to add each key and value pair to the panel
    // Hint: Inside the loop, you will need to use d3 to append new
    // tags for each key-value in the metadata.
    
    Object.entries(sample).forEach(function([key,value]) {
      console.log(key,value);
      var row = metadataSelction.append("div");
      row.text(`${key}: ${value}`);
      
    }
    ); // Object entries ending

  }); // d3.json function ending

} //function buildMetaData ending

//--------------------------------------------------------------------------//

<<<<<<< HEAD
// Build Charts
// function buildCharts(sample) {

  // // @TODO: Use `d3.json` to fetch the sample data for the plots
  // var url_sampleData = `/billboard/${rankid}`;
  // d3.json(url_sampleData).then(function(sample) {
  //   console.log("Sample Data:")
  //   console.log(sample);

    
  //   // @TODO: Build a Bubble Chart using the sample data
  //   var trace = {
  //     x: sample.artist,
  //     y: sample.rank,
  //   //     text:sample.otu_lables,
  //   //   mode:'markers',
  //   //   marker: {
  //   //     color:sample.otu_ids,
  //   //     size:sample.sample_values
  //   //   }
  //   }; // trace ending 

  //   var data = [trace];

  //   // var layout = {
  //   //   title: "Bubble Graph: Sample Population",
  //   //   xaxis: {title: "otu_ids"},
  //   //   yaxis: {title: "sample_values"}
  //   // }; // layout ending

  //   var layout = {
  //   title: "'Bar' Chart",
  //   xaxis: { title: "Drinks"},
  //   yaxis: { title: "% of Drinks Ordered"}
  //   };  

  //   Plotly.newPlot('bubble', data, layout);
=======
function buildCharts(sample) {

  // @TODO: Use `d3.json` to fetch the sample data for the plots
  var url_sampleData = `/billboard/${rankid}`;
  d3.json(url_sampleData).then(function(sample) {
    console.log("Sample Data:")
    console.log(sample);

    
    // @TODO: Build a Bubble Chart using the sample data
    var trace = {
      x: sample.artist,
      y: sample.rank,
    //     text:sample.otu_lables,
    //   mode:'markers',
    //   marker: {
    //     color:sample.otu_ids,
    //     size:sample.sample_values
    //   }
    }; // trace ending 

    var data = [trace];

    // var layout = {
    //   title: "Bubble Graph: Sample Population",
    //   xaxis: {title: "otu_ids"},
    //   yaxis: {title: "sample_values"}
    // }; // layout ending

    var layout = {
    title: "'Bar' Chart",
    xaxis: { title: "Drinks"},
    yaxis: { title: "% of Drinks Ordered"}
    };  

    Plotly.newPlot('bubble', data, layout);
>>>>>>> Nader_new

    // // @TODO: Build a Pie Chart
    // // HINT: You will need to use slice() to grab the top 10 sample_values,
    // // otu_ids, and labels (10 each).
    

    // //Top 10 Sample Values
    // var topSampleValues = sample.sample_values
    // topSampleValues.sort(function(a,b) {
    //   return b -a;
    // }); // sort function ending
    // topSampleValues = topSampleValues.slice(0,10);
    // console.log("Top 10 Sample Values:")
    // console.log(topSampleValues);

    // //Pie Chart 
    // var tracePie = {
    //   labels: sample.otu_ids,
    //   values: topSampleValues,
    //   text: sample.otu_lables,
    //   type: 'pie'
    // };

    // var dataPie = [tracePie];

    // var layoutPie = {
    //   title: "Top 10 Sample Values",
    // }; 
    
    // Plotly.newPlot("pie", dataPie, layoutPie);


<<<<<<< HEAD
  // }); // d3.json function ending 


// } //buildCharts function ending 

//------------------------------------------------------------------------------------------//

//Drop-Down Selection 
function init() {
  // Grab a reference to the dropdown select element
  var selector = d3.select("#selDataset");

  // Use the list of sample names to populate the select options
  d3.json(`/decades`).then((sampleNames) => {
    sampleNames.forEach((sample) => {
      selector
        .append("option")
        .text(sample)
        .property("value", sample);
    });

    // Use the first sample from the list to build the initial plots
    const firstSample = sampleNames[0];
    buildCharts(firstSample);
    buildMetadata(firstSample);
  });
}
=======
  }); // d3.json function ending 


} //buildCharts function ending 

//------------------------------------------------------------------------------------------//

// function init() {
//   // Grab a reference to the dropdown select element
//   var selector = d3.select("#selDataset");

//   // Use the list of sample names to populate the select options
//   d3.json("/names").then((sampleNames) => {
//     sampleNames.forEach((sample) => {
//       selector
//         .append("option")
//         .text(sample)
//         .property("value", sample);
//     });

//     // Use the first sample from the list to build the initial plots
//     const firstSample = sampleNames[0];
//     buildCharts(firstSample);
//     buildMetadata(firstSample);
//   });
// }
>>>>>>> Nader_new

// function optionChanged(newSample) {
//   // Fetch new data each time a new sample is selected
//   buildCharts(newSample);
//   buildMetadata(newSample);
// }

<<<<<<< HEAD
// Initialize the dashboard
init();
=======
// // Initialize the dashboard
// init();
>>>>>>> Nader_new
