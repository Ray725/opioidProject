var fs = require('fs')
var request = require('request');
var sleep = require('sleep');
var county_key = {};
var counties = [];


fs.readFile('Opiod Deaths by County 1999-2015.csv', function(err, data) {
  if (err) {
    throw err;
  }
  // format the data as best as we can
  data_array = data.toString().split("\n");
  for (var i = 0; i < data_array.length; i++) {
    data_array[i] = data_array[i].split("\t");
  }

  // first get a list of all unique counties
  for (var j = 1; j < data_array.length; j++) {
    // if the county isn't in the list of counties
    if (counties.indexOf(data_array[j][3]) === -1) {
      counties.push(data_array[j][3]);
    }
  }

  geocoderequest(counties);
});

function geocoderequest(countieslist) {
  // for each county make geocoding request and add to dictionary/object
  for (var k = 0; k < countieslist.length; k++) {
    if(k === 3133) {
      continue;
    }
    console.log(`On number ${k} out of ${countieslist.length}`);
    try {
      var county_name = countieslist[k].slice(0, -1).substr(1);
    } catch(error) {
      continue;
    }
    var website_string = `https://maps.googleapis.com/maps/api/geocode/json?address=${county_name}&key=AIzaSyCYDdjxFPVgyCik1xIv4ZK-Z8OU-nSkbTo`;
    getlocation(county_name, website_string, printfunction, function(htmlJSON, county, printfunc) {
      try {
        county_key[county] = htmlJSON.results[0].geometry.location;
      } catch (error) {
        console.log(`${k} position undefined in counties list`);
      }
      printfunc();
    });

    // make sure we don't pass API allowed calls
    if(k % 50 === 0 && k > 0) {
      sleep.sleep(1);
    }

  }
}

function getlocation(county, url, printfunc, callback) {
  request(url, function(err, res, body) {
    if (err) {
      console.log(err);
    }
    var htmlJSON = JSON.parse(body);
    callback(htmlJSON, county, printfunc);
  });
}

function printfunction() {
  console.log(county_key);
}
