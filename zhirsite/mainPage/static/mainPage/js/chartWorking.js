function drawChart() {
    // Define the chart to be drawn.
    var data = new google.visualization.DataTable();
    data.addColumn('string', 'Browser');
    data.addColumn('number', 'Percentage');
    data.addRows([
       ['Firefox', 45.0],
       ['IE', 26.8],
       ['Chrome', 12.8],
       ['Safari', 8.5],
       ['Opera', 6.2],
       ['Others', 0.7]
    ]);

    // Set chart options
    var options = {'title':'Browser market shares at a specific website, 2014', 'width':550, 'height':400};

    // Instantiate and draw the chart.
    var chart = new google.visualization.PieChart(document.getElementById ('container'));
    chart.draw(data, options);
}
google.charts.setOnLoadCallback(drawChart);