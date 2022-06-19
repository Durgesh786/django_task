$(document).ready(function () {

    /*
        Flot: User-Registration Daily
    */
    $('#userSelector').themePluginMultiSelect().on('change', function () {
        var rel = $(this).val();
        $('#userSelectorItems .chart').removeClass('chart-active').addClass('chart-hidden');

        $('#userSelectorItems .chart[data-users-rel="' + rel + '"]').addClass('chart-active').removeClass('chart-hidden');
    });

    $('#userSelector').trigger('change');

    $('#userSelectorWrapper').addClass('ready');
    var flotDashSales1 = $.plot('#flotDashSales1', flotDashSales1Data, {
        colors: ['#2baab1'],
        series: {
            lines: {
                show: true,
                lineWidth: 2
            },
            points: {
                show: true
            },
            shadowSize: 0
        },
        grid: {
            hoverable: true,
            clickable: true,
            borderColor: 'rgba(0,0,0,0.1)',
            borderWidth: 1,
            labelMargin: 15,
            backgroundColor: 'transparent'
        },
        yaxis: {
            min: 0,
            color: 'rgba(0,0,0,0.1)'
        },
        xaxis: {
            mode: 'categories',
            color: 'rgba(0,0,0,0)'
        },
        legend: {
            show: false
        },
        tooltip: true,
        tooltipOpts: {
            content: '%y',
            shifts: {
                x: -30,
                y: 25
            },
            defaultTheme: false
        }
    });

    /*
        Flot: User-Registration Monthly
    */
    var flotDashSales2 = $.plot('#flotDashSales2', flotDashSales2Data, {
        colors: ['#2baab1'],
        series: {
            lines: {
                show: true,
                lineWidth: 2
            },
            points: {
                show: true
            },
            shadowSize: 0
        },
        grid: {
            hoverable: true,
            clickable: true,
            borderColor: 'rgba(0,0,0,0.1)',
            borderWidth: 1,
            labelMargin: 15,
            backgroundColor: 'transparent'
        },
        yaxis: {
            min: 0,
            color: 'rgba(0,0,0,0.1)'
        },
        xaxis: {
            mode: 'categories',
            color: 'rgba(0,0,0,0)'
        },
        legend: {
            show: false
        },
        tooltip: true,
        tooltipOpts: {
            content: '%y',
            shifts: {
                x: -30,
                y: 25
            },
            defaultTheme: false
        }
    });

    /*
        Flot: User-Registration Yearly
    */
    var flotDashSales3 = $.plot('#flotDashSales3', flotDashSales3Data, {
        colors: ['#2baab1'],
        series: {
            lines: {
                show: true,
                lineWidth: 2
            },
            points: {
                show: true
            },
            shadowSize: 0
        },
        grid: {
            hoverable: true,
            clickable: true,
            borderColor: 'rgba(0,0,0,0.1)',
            borderWidth: 1,
            labelMargin: 15,
            backgroundColor: 'transparent'
        },
        yaxis: {
            min: 0,
            color: 'rgba(0,0,0,0.1)'
        },
        xaxis: {
            mode: 'categories',
            color: 'rgba(0,0,0,0)'
        },
        legend: {
            show: false
        },
        tooltip: true,
        tooltipOpts: {
            content: '%y',
            shifts: {
                x: -30,
                y: 25
            },
            defaultTheme: false
        }
    });


    $('#questionSelector').themePluginMultiSelect().on('change', function () {
        var rel = $(this).val();
        $('#questionSelectorItems .chart').removeClass('chart-active').addClass('chart-hidden');

        $('#questionSelectorItems .chart[data-question-rel="' + rel + '"]').addClass('chart-active').removeClass('chart-hidden');
    });
    $('#questionSelector').trigger('change');
    $('#questionSelectorWrapper').addClass('ready');


    /*
        Flot: Questions-Daily
    */
    var flotQuestion1 = $.plot('#flotQuestion1', flotQuestion1Data, {
        colors: ['#2baab1'],
        series: {
            lines: {
                show: true,
                lineWidth: 2
            },
            points: {
                show: true
            },
            shadowSize: 0
        },
        grid: {
            hoverable: true,
            clickable: true,
            borderColor: 'rgba(0,0,0,0.1)',
            borderWidth: 1,
            labelMargin: 15,
            backgroundColor: 'transparent'
        },
        yaxis: {
            min: 0,
            color: 'rgba(0,0,0,0.1)'
        },
        xaxis: {
            mode: 'categories',
            color: 'rgba(0,0,0,0)'
        },
        legend: {
            show: false
        },
        tooltip: true,
        tooltipOpts: {
            content: '%y',
            shifts: {
                x: -30,
                y: 25
            },
            defaultTheme: false
        }
    });

    /*
        Flot: Questions-Monthly
    */
    var flotQuestion2 = $.plot('#flotQuestion2', flotQuestion2Data, {
        colors: ['#2baab1'],
        series: {
            lines: {
                show: true,
                lineWidth: 2
            },
            points: {
                show: true
            },
            shadowSize: 0
        },
        grid: {
            hoverable: true,
            clickable: true,
            borderColor: 'rgba(0,0,0,0.1)',
            borderWidth: 1,
            labelMargin: 15,
            backgroundColor: 'transparent'
        },
        yaxis: {
            min: 0,
            color: 'rgba(0,0,0,0.1)'
        },
        xaxis: {
            mode: 'categories',
            color: 'rgba(0,0,0,0)'
        },
        legend: {
            show: false
        },
        tooltip: true,
        tooltipOpts: {
            content: '%y',
            shifts: {
                x: -30,
                y: 25
            },
            defaultTheme: false
        }
    });

    /*
        Flot: Questions-Yearly
    */
    var flotQuestion3 = $.plot('#flotQuestion3', flotQuestion3Data, {
        colors: ['#2baab1'],
        series: {
            lines: {
                show: true,
                lineWidth: 2
            },
            points: {
                show: true
            },
            shadowSize: 0
        },
        grid: {
            hoverable: true,
            clickable: true,
            borderColor: 'rgba(0,0,0,0.1)',
            borderWidth: 1,
            labelMargin: 15,
            backgroundColor: 'transparent'
        },
        yaxis: {
            min: 0,
            color: 'rgba(0,0,0,0.1)'
        },
        xaxis: {
            mode: 'categories',
            color: 'rgba(0,0,0,0)'
        },
        legend: {
            show: false
        },
        tooltip: true,
        tooltipOpts: {
            content: '%y',
            shifts: {
                x: -30,
                y: 25
            },
            defaultTheme: false
        }
    });



});