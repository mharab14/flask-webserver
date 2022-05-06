var options = {
    series: [{
        name: 'temp',
        data: []
    }, {
        name: 'humidity',
        data: []
    }],
    chart: {
        height: 350,
        type: 'area'
    },
    dataLabels: {
        enabled: false
    },
    stroke: {
        curve: 'smooth'
    },
    tooltip: {
        x: {
            format: 'dd/MM/yy HH:mm'
        },
    },
};

charts = {}
charts["2"] = new ApexCharts(document.querySelector("#temphum-2"), options);
charts["2"].render();

charts["31"] = new ApexCharts(document.querySelector("#temphum-31"), options);
charts["31"].render();

charts["6"] = new ApexCharts(document.querySelector("#temphum-6"), options);
charts["6"].render();

$(document).ready(function () {

    var socket = io();

    socket.on('response', function (data) {
        // $("#temp-" + data["no"]).html(data["temp"] + "C");
        // $("#hum-" + data["no"]).html(data["hum"] + "%");
        charts[data["no"]].appendData([{
            data: [data["temp"]]
          }, {
            data: [data["hum"]]
          }])
    });


});