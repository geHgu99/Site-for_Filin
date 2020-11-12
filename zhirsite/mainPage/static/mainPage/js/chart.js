function drawChart() {
    // Define the chart to be drawn.
    var data = new google.visualization.DataTable();
    data.addColumn('date', 'Data');
    data.addColumn('number', 'measure');
    var base = JSON.parse(document.getElementById('county-data').textContent);
    for (i in base) {
        data.addRow(
           [new Date(Date.UTC(i.data)), i.weight],
        );
    }



     // Set chart options
    var options = {'title':'График твоей жиробазности', 'width':550, 'height':400};

    // Instantiate and draw the chart.
    var chart = new google.visualization.LineChart(document.getElementById ('container'));
    chart.draw(data, options);
}
google.charts.setOnLoadCallback(drawChart);