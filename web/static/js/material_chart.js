$(function () {
$.getJSON('/static/data/material_count.json' , function (data) {
    var series = [];
    var series2 = [{data:[],name:'使用次数'}];
    var cat = [];
    for(var i in data){
        cat.push(data[i].name)
        var d = {name:data[i].name,data:[data[i].count]};
        series.push(d);
        series2[0].data.push(data[i].count);
    }

    $('#material_count').highcharts({
        chart: {
            type: 'bar'
        },
        title: {
            text: ''//'食材使用次数'
        },
        //subtitle: {
        //    text: 'Source: Wikipedia.org'
        //},
        xAxis: {
            categories: cat,
            title: {
                text: null
            }
        },
        yAxis: {
            min: 0,
            title: {
                text: '食材使用次数',
                align: 'high'
            },
            labels: {
                overflow: 'justify'
            }
        },
        //tooltip: {
        //    valueSuffix: ' 次'
        //},
        plotOptions: {
            bar: {
                dataLabels: {
                    enabled: false//true
                }
            }
        },
        legend: {
            layout: 'vertical',
            align: 'right',
            verticalAlign: 'top',
            x: -40,
            y: 100,
            floating: true,
            borderWidth: 1,
            backgroundColor: ((Highcharts.theme && Highcharts.theme.legendBackgroundColor) || '#FFFFFF'),
            shadow: true
        },
        credits: {
            enabled: false
        },
        series: series2
        //data: data
    });
});
$.getJSON('/static/data/material_amount.json' , function (data) {
    var series = [];
    var series2 = [{data:[],name:'用量(g/个)'}];
    var cat = [];
    for(var i in data){
        if(data[i].amount<=50){continue;}
        cat.push(data[i].name)
        //var d = {name:data[i].name,data:[data[i].count]};
        //series.push(d);
        series2[0].data.push(data[i].amount);
    }

    $('#material_amount').highcharts({
        chart: {
            type: 'bar'
        },
        title: {
            text: ''//'食材用量'
        },
        //subtitle: {
        //    text: 'Source: Wikipedia.org'
        //},
        xAxis: {
            categories: cat,
            title: {
                text: null
            }
        },
        yAxis: {
            min: 0,
            title: {
                text: '食材用量',
                align: 'high'
            },
            labels: {
                overflow: 'justify'
            }
        },
        //tooltip: {
        //    valueSuffix: ' 次'
        //},
        plotOptions: {
            bar: {
                dataLabels: {
                    enabled: false//true
                }
            }
        },
        legend: {
            layout: 'vertical',
            align: 'right',
            verticalAlign: 'top',
            x: -40,
            y: 100,
            floating: true,
            borderWidth: 1,
            backgroundColor: ((Highcharts.theme && Highcharts.theme.legendBackgroundColor) || '#FFFFFF'),
            shadow: true
        },
        credits: {
            enabled: false
        },
        series: series2
        //data: data
    });
});
});        
