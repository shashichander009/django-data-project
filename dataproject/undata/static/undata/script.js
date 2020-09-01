"use strict";

//  This function prepares a Bar Plot of India's population vs. years.

function prepIndiaChart() {
  // var year = get
  // var range =

  var year = document.getElementById("year");
  var range = document.getElementById("range");

  var yearValue = year.options[year.selectedIndex].value;
  var rangeValue = range.options[range.selectedIndex].value;

  console.log(yearValue);
  console.log(rangeValue);

  var url = "prob1?year=" + yearValue + "&&range=" + rangeValue;

  fetch(url)
    .then(res => {
      return res.json();
    })

    .then(indiaData => {
      console.log(indiaData);
      indiaData = Object.entries(indiaData);
      console.log(indiaData);
      Highcharts.chart("container", {
        chart: {
          type: "column"
        },
        title: {
          text: "India's Population Over the Years"
        },
        subtitle: {
          text: `Source: <a href='https://datahub.io/core/
          population-growth-estimates-and-projections/r/
          population-estimates.csv'>United Nations</a>`
        },
        xAxis: {
          type: "category",
          labels: {
            rotation: -45,
            style: {
              fontSize: "10px",
              fontFamily: "Verdana, sans-serif"
            }
          }
        },
        yAxis: {
          min: 0,
          title: {
            text: "Population (crores)"
          }
        },
        legend: {
          enabled: true
        },
        tooltip: {
          pointFormat: "Population : <b>{point.y:.1f} crores</b>"
        },
        series: [
          {
            name: "Year (1950-2015)",
            data: indiaData
          }
        ]
      });
    })
    .catch(error => console.log(error));
}

//  This function prepares the Bar Chart of population of ASEAN countries in 2014

function prepAseanChart() {
  fetch("/backend/json/data2.json")
    .then(response => {
      return response.json();
    })
    .then(aseanData => {
      aseanData = Object.entries(aseanData);

      for (let i = 0; i < aseanData.length; i++) {
        let country = aseanData[i][0];

        if (country == "Viet Nam") aseanData[i][0] = "VietNam";
        if (country == "Brunei Darussalam") aseanData[i][0] = "Brunei";
        if (country == "Lao People's Democratic Republic")
          aseanData[i][0] = "Laos";
      }

      Highcharts.chart("container", {
        chart: {
          type: "column"
        },
        title: {
          text: "ASEAN Countries Population in 2014"
        },
        subtitle: {
          text: `Source: <a href='https://datahub.io/core/
          population-growth-estimates-and-projections/r/
          population-estimates.csv'>United Nations</a>`
        },
        xAxis: {
          type: "category",
          labels: {
            style: {
              fontSize: "13px",
              fontFamily: "Verdana, sans-serif"
            }
          }
        },
        yAxis: {
          min: 0,
          title: {
            text: "Population (crores)"
          }
        },
        legend: {
          enabled: true
        },
        tooltip: {
          pointFormat: "Population : <b>{point.y:.2f} crores</b>"
        },
        series: [
          {
            name: "Countries",
            data: aseanData
          }
        ]
      });
    })
    .catch(error => console.log(error));
}

//  TOTAL population of SAARC countries over the past years

function prepSaarcChart() {
  fetch("/backend/json/data3.json")
    .then(response => {
      return response.json();
    })
    .then(saarcData => {
      saarcData = Object.entries(saarcData);
      Highcharts.chart("container", {
        chart: {
          type: "column"
        },
        title: {
          text: "SAARC Countries Population Over the Years"
        },
        subtitle: {
          text: `Source: <a href='https://datahub.io/core/
          population-growth-estimates-and-projections/r/
          population-estimates.csv'>United Nations</a>`
        },
        xAxis: {
          type: "category",
          labels: {
            rotation: -45,
            style: {
              fontSize: "10px",
              fontFamily: "Verdana, sans-serif"
            }
          }
        },
        yAxis: {
          min: 0,
          title: {
            text: "Population (crores)"
          }
        },
        legend: {
          enabled: true
        },
        tooltip: {
          pointFormat: "Population : <b>{point.y:.2f} crores</b>"
        },
        series: [
          {
            name: "Year (1950-2015)",
            data: saarcData
          }
        ]
      });
    })
    .catch(error => console.log(error));
}

//  Grouped Bar Chart - ASEAN population vs. years

function prepAseanGroupChart() {
  fetch("/backend/json/data4.json")
    .then(response => {
      return response.json();
    })
    .then(aseanGroupData => {
      // this is to get the array of years
      const firstKey = Object.keys(aseanGroupData)[0];
      const yearsArray = Object.keys(aseanGroupData[firstKey]);

      // it will store the final data for charting
      let seriesArray = [];

      for (let country in aseanGroupData) {
        //Object.values(aseanGroupData[country]) return an array
        //of population values for each country

        const populationData = Object.values(aseanGroupData[country]);

        //changing the name of countries for better display
        if (country == "Viet Nam") country = "VietNam";
        if (country == "Brunei Darussalam") country = "Brunei";
        if (country == "Lao People's Democratic Republic") country = "Laos";

        // each element of seriesArray is of the below format object

        let countryObj = {
          name: country,
          data: populationData
        };

        seriesArray.push(countryObj);
      }

      Highcharts.chart("container", {
        chart: {
          type: "column"
        },
        title: {
          text: "ASEAN Population (2011-2015)"
        },
        subtitle: {
          text: `Source: <a href='https://datahub.io/core/
          population-growth-estimates-and-projections/r/
          population-estimates.csv'>United Nations</a>`
        },
        xAxis: {
          categories: yearsArray,
          crosshair: true
        },
        yAxis: {
          min: 0,
          title: {
            text: "Population (cr)"
          }
        },
        tooltip: {
          headerFormat:
            '<span style="font-size:10px">{point.key}</span><table>',
          pointFormat:
            '<tr><td style="color:{series.color};padding:0">{series.name}: </td>' +
            '<td style="padding:0"><b>{point.y:.2f} cr</b></td></tr>',
          footerFormat: "</table>",
          shared: true,
          useHTML: true
        },
        plotOptions: {
          column: {
            pointPadding: 0.2,
            borderWidth: 0
          }
        },
        series: seriesArray
      });
    })
    .catch(error => console.log(error));
}
