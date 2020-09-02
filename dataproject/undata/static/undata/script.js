"use strict";

function problem1Chart() {
  var year = document.getElementById("year");
  var range = document.getElementById("range");
  var country = document.getElementById("country");

  var yearValue = year.options[year.selectedIndex].value;
  var rangeValue = range.options[range.selectedIndex].value;
  var countryValue = country.options[country.selectedIndex].value;

  var endYear;

  if (rangeValue != "1") {
    endYear = parseInt(yearValue) + parseInt(rangeValue) - 1;
  } else {
    endYear = yearValue;
  }

  var url =
    "prob1response?year=" +
    yearValue +
    "&&range=" +
    rangeValue +
    "&&country=" +
    countryValue;

  console.log(countryValue);

  fetch(url)
    .then(res => {
      return res.json();
    })

    .then(indiaData => {
      console.log(indiaData);
      indiaData = Object.entries(indiaData);
      console.log(indiaData);

      var titleText = countryValue + "'s Population Over the Years";

      var seriesArray = [
        {
          name: "Year (" + yearValue + "-" + endYear + ")",
          data: indiaData
        }
      ];

      prepCharts(titleText, seriesArray);
    })
    .catch(error => console.log(error));
}

function problem2Chart() {
  var year = document.getElementById("year");
  var group = document.getElementById("group");

  var yearValue = year.options[year.selectedIndex].value;
  var groupValue = group.options[group.selectedIndex].value;

  var url = "prob2response?year=" + yearValue + "&&group=" + groupValue;

  console.log(url);

  fetch(url)
    .then(response => {
      return response.json();
    })
    .then(aseanData => {
      aseanData = Object.entries(aseanData);

      for (let i = 0; i < aseanData.length; i++) {
        let country = aseanData[i][0];

        if (country == "Viet Nam") aseanData[i][0] = "VietNam";
        if (country == "Brunei Darussalam") aseanData[i][0] = "Brunei";
        if (country == "Russian Federation") aseanData[i][0] = "Russia";
        if (country == "United States of America") aseanData[i][0] = "USA";
        if (country == "Lao People's Democratic Republic")
          aseanData[i][0] = "Laos";
      }

      var titleText =
        groupValue + " Countries Population in the Year " + yearValue;

      var seriesArray = [
        {
          name: "Countries",
          data: aseanData
        }
      ];

      prepCharts(titleText, seriesArray);
    })
    .catch(error => console.log(error));
}

function problem3Chart() {
  var year = document.getElementById("year");
  var group = document.getElementById("group");
  var range = document.getElementById("range");

  var yearValue = year.options[year.selectedIndex].value;
  var groupValue = group.options[group.selectedIndex].value;
  var rangeValue = range.options[range.selectedIndex].value;

  var endYear;

  if (rangeValue != "1") {
    endYear = parseInt(yearValue) + parseInt(rangeValue) - 1;
  } else {
    endYear = yearValue;
  }

  var url =
    "prob3response?year=" +
    yearValue +
    "&&range=" +
    rangeValue +
    "&&group=" +
    groupValue;

  fetch(url)
    .then(response => {
      return response.json();
    })
    .then(saarcData => {
      saarcData = Object.entries(saarcData);

      var titleText =
        groupValue + " Countries Population in the Year " + yearValue;

      var seriesArray = [
        {
          name: "Year (" + yearValue + "-" + endYear + ")",
          data: saarcData
        }
      ];

      prepCharts(titleText, seriesArray);
    })
    .catch(error => console.log(error));
}

function prepCharts(titleText, seriesArray) {
  Highcharts.chart("container", {
    chart: {
      type: "column"
    },
    title: {
      text: titleText
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
    series: seriesArray
  });
}

function problem4Chart() {
  var year = document.getElementById("year");
  var group = document.getElementById("group");

  var yearValue = year.options[year.selectedIndex].value;
  var groupValue = group.options[group.selectedIndex].value;

  var url = "prob4response?year=" + yearValue + "&&group=" + groupValue;

  fetch(url)
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
        if (country == "Russian Federation") country = "Russia";
        if (country == "United States of America") country = "USA";
        if (country == "Lao People's Democratic Republic") country = "Laos";

        // each element of seriesArray is of the below format object

        let countryObj = {
          name: country,
          data: populationData
        };

        seriesArray.push(countryObj);
      }

      var titleText =
        groupValue + " Countries Population in the Year " + yearValue;

      Highcharts.chart("container", {
        chart: {
          type: "column"
        },
        title: {
          text: titleText
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
