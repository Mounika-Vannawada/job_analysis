const width_threshold = 480;
//line chart 
function drawLineChart(salary) {
  if ($("#lineChart").length) {
    ctxLine = document.getElementById("lineChart").getContext("2d");
    optionsLine = {
      scales: {
        yAxes: [
          {
            scaleLabel: {
              display: true,
              labelString: 'Salary'
            }
          }
        ]
      }
    };

    // Set aspect ratio based on window width
    optionsLine.maintainAspectRatio =
      $(window).width() < width_threshold ? false : true;
    configLine = {
      type: "line",
      data: {
        labels: salary.labels,
        datasets: [
          {
            label: "Hour minimum",
            data: salary.hourmin,
            fill: false,
            borderColor: "rgb(75, 192, 192)",
            lineTension: 0.1
          },
          {
            label: 'Hour maximum',
            data: salary.hourmax,
            fill: false,
            borderColor: "rgba(255,99,132,1)",
            lineTension: 0.1
          }
        ]
      },
      options: optionsLine
    };

    lineChart = new Chart(ctxLine, configLine);
  }
}

//line chart 
function drawLineChart2(salary) {
  if ($("#lineChart").length) {
    ctxLine = document.getElementById("lineChart2").getContext("2d");
    optionsLine = {
      scales: {
        yAxes: [
          {
            scaleLabel: {
              display: true,
              labelString: 'Salary'
            }
          }
        ]
      }
    };

    // Set aspect ratio based on window width
    optionsLine.maintainAspectRatio =
      $(window).width() < width_threshold ? false : true;
    configLine = {
      type: "line",
      data: {
        labels: salary.labels,
        datasets: [
          {
            label: "year minimum",
            data: salary.yearmin,
            fill: false,
            borderColor: "rgb(75, 192, 192)",
            lineTension: 0.1
          },
          {
            label: 'year maximum',
            data: salary.yearmax,
            fill: false,
            borderColor: "rgba(255,99,132,1)",
            lineTension: 0.1
          }
        ]
      },
      options: optionsLine
    };

    lineChart = new Chart(ctxLine, configLine);
  }
}



//bar graph
function drawBarChart(dict) {
  if ($("#barChart").length) {
    ctxBar = document.getElementById("barChart").getContext("2d");

    optionsBar = {
      responsive: true,
      scales: {
        yAxes: [
          {
            ticks: {
              beginAtZero: true
            },
            scaleLabel: {
              display: true,
              labelString: ""
            }
          }
        ]
      }
    };

    optionsBar.maintainAspectRatio =
      $(window).width() < width_threshold ? false : true;

    configBar = {
      type: "bar",
      data: {
        labels: dict.labels,
        datasets: [
          {
            label: "Jobs",
            data: dict.graphdata,
            backgroundColor: dict.backgroundColor,
            borderColor: dict.borderColor,
            borderWidth: 1
          }
        ]
      },
      options: optionsBar
    };

    barChart = new Chart(ctxBar, configBar);
  }
}


//bar graph 2nd 
function drawBarChart2(dict) {
  if ($("#barChart").length) {
    ctxBar = document.getElementById("barChart2").getContext("2d");

    optionsBar = {
      responsive: true,
      scales: {
        yAxes: [
          {
            ticks: {
              beginAtZero: true
            },
            scaleLabel: {
              display: true,
              labelString: ""
            }
          }
        ],
        xAxes: [
          {
            
              stacked: true
          }
        ]
      }
    };

    optionsBar.maintainAspectRatio =
      $(window).width() < width_threshold ? false : true;

    configBar = {
      type: "bar",
      data: {
        labels: dict.labels,
        datasets: [
          {
            label: "Jobs",
            data: dict.graphdata,
            backgroundColor: dict.backgroundColor,
            borderColor: dict.borderColor,
            borderWidth: 1
          }
        ]
      },
      options: optionsBar
    };

    barChart = new Chart(ctxBar, configBar);
  }
}


//bar graph 3nd 
function drawBarChart3(dict) {
  if ($("#barChart").length) {
    ctxBar = document.getElementById("barChart3").getContext("2d");

    optionsBar = {
      responsive: true,
      scales: {
        yAxes: [
          {
            ticks: {
              beginAtZero: true
            },
            scaleLabel: {
              display: true,
              labelString: ""
            }
          }
        ]
      }
    };

    optionsBar.maintainAspectRatio =
      $(window).width() < width_threshold ? false : true;

    configBar = {
      type: "bar",
      data: {
        labels: dict.labels,
        datasets: [
          {
            label: "Jobs",
            data: dict.graphdata,
            backgroundColor: dict.backgroundColor,
            borderColor: dict.borderColor,
            borderWidth: 1
          }
        ]
      },
      options: optionsBar
    };

    barChart = new Chart(ctxBar, configBar);
  }
}


//bar graph 3nd 
function drawBarChart4(dict) {
  if ($("#barChart").length) {
    ctxBar = document.getElementById("barChart4").getContext("2d");

    optionsBar = {
      responsive: true,
      scales: {
        yAxes: [
          {
            ticks: {
              beginAtZero: true
            },
            scaleLabel: {
              display: true,
              labelString: ""
            }
          }
        ]
      }
    };

    optionsBar.maintainAspectRatio =
      $(window).width() < width_threshold ? false : true;

    configBar = {
      type: "bar",
      data: {
        labels: dict.labels,
        datasets: [
          {
            label: "Jobs",
            data: dict.graphdata,
            backgroundColor: dict.backgroundColor,
            borderColor: dict.borderColor,
            borderWidth: 1
          }
        ]
      },
      options: optionsBar
    };

    barChart = new Chart(ctxBar, configBar);
  }
}



//bar graph 5nd 
function drawBarChart5(dict) {
  if ($("#barChart").length) {
    ctxBar = document.getElementById("barChart5").getContext("2d");

    optionsBar = {
      responsive: true,
      scales: {
        yAxes: [
          {
            ticks: {
              beginAtZero: true
            },
            scaleLabel: {
              display: true,
              labelString: ""
            }
          }
        ]
      }
    };

    optionsBar.maintainAspectRatio =
      $(window).width() < width_threshold ? false : true;

    configBar = {
      type: "bar",
      data: {
        labels: dict.labels,
        datasets: [
          {
            label: "Jobs",
            data: dict.graphdata,
            backgroundColor: dict.backgroundColor,
            borderColor: dict.borderColor,
            borderWidth: 1
          }
        ]
      },
      options: optionsBar
    };

    barChart = new Chart(ctxBar, configBar);
  }
}


//bar graph 6
function drawBarChart6(dict) {
  if ($("#barChart").length) {
    ctxBar = document.getElementById("barChart6").getContext("2d");

    optionsBar = {
      responsive: true,
      scales: {
        yAxes: [
          {
            ticks: {
              beginAtZero: true
            },
            scaleLabel: {
              display: true,
              labelString: ""
            }
          }
        ]
      }
    };

    optionsBar.maintainAspectRatio =
      $(window).width() < width_threshold ? false : true;

    configBar = {
      type: "bar",
      data: {
        labels: dict.labels,
        datasets: [
          {
            label: "Jobs",
            data: dict.graphdata,
            backgroundColor: dict.backgroundColor,
            borderColor: dict.borderColor,
            borderWidth: 1
          }
        ]
      },
      options: optionsBar
    };

    barChart = new Chart(ctxBar, configBar);
  }
}

//pie chart 
function drawPieChart(piedata) {
  if ($("#pieChart").length) {
    ctxPie = document.getElementById("pieChart").getContext("2d");
    optionsPie = {
      responsive: true,
      maintainAspectRatio: false
    };

    configPie = {
      type: "pie",
      data: {
        datasets: [
          {
            data: [piedata['Contract'], piedata['fulltime']],
            backgroundColor: [
              window.chartColors.purple,
              window.chartColors.green
            ],
            label: "Job Type"
          }
        ],
        labels: ["Contract Jobs: " + piedata['Contract'], "Fulltime Jobs: " + piedata['fulltime']]
      },
      options: optionsPie
    };

    pieChart = new Chart(ctxPie, configPie);
  }
}

//pie chart 
function drawPieChart2(piedata) {
  if ($("#pieChart").length) {
    ctxPie = document.getElementById("pieChart3").getContext("2d");
    optionsPie = {
      responsive: true,
      maintainAspectRatio: false
    };

    configPie = {
      type: "pie",
      data: {
        datasets: [
          {
            data: [piedata['Contract'], piedata['fulltime']],
            backgroundColor: [
              window.chartColors.purple,
              window.chartColors.green
            ],
            label: "Job Type"
          }
        ],
        labels: ["Contract Jobs: " + piedata['Contract'], "Fulltime Jobs: " + piedata['fulltime']]
      },
      options: optionsPie
    };

    pieChart = new Chart(ctxPie, configPie);
  }
}

function updateChartOptions() {
  if ($(window).width() < width_threshold) {
    if (optionsLine) {
      optionsLine.maintainAspectRatio = false;
    }
    if (optionsBar) {
      optionsBar.maintainAspectRatio = false;
    }
  } else {
    if (optionsLine) {
      optionsLine.maintainAspectRatio = true;
    }
    if (optionsBar) {
      optionsBar.maintainAspectRatio = true;
    }
  }
}

function updateLineChart() {
  if (lineChart) {
    lineChart.options = optionsLine;
    lineChart.update();
  }
}

function updateBarChart() {
  if (barChart) {
    barChart.options = optionsBar;
    barChart.update();
  }
}

function reloadPage() {
  setTimeout(function() {
    window.location.reload();
  }); // Reload the page so that charts will display correctly
}

function drawCalendar() {
  if ($("#calendar").length) {
    $("#calendar").fullCalendar({
      height: 400,
      events: [
        {
          title: "Meeting",
          start: "2018-09-1",
          end: "2018-09-2"
        },
        {
          title: "Marketing trip",
          start: "2018-09-6",
          end: "2018-09-8"
        },
        {
          title: "Follow up",
          start: "2018-10-12"
        },
        {
          title: "Team",
          start: "2018-10-17"
        },
        {
          title: "Company Trip",
          start: "2018-10-25",
		  end: "2018-10-27"
        },
        {
          title: "Review",
          start: "2018-11-12"
        },
        {
          title: "Plan",
          start: "2018-11-18"
        }
      ],
      eventColor: "rgba(54, 162, 235, 0.4)"
    });
  }
}
