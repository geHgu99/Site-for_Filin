function drawChart() {
    // Define the chart to be drawn.
    var data = new google.visualization.DataTable();
    data.addColumn('string', 'Data');{% for i in base %}
        data.addRows([
           [{{ i.data }}, {{ i.weight }}],
        ]);
    {% endfor %}
    data.addColumn('number', 'Measure');

     // Set chart options
    var options = {'title':'График твоей жиробазности', 'width':550, 'height':400};
    // Instantiate and draw the chart.
    var chart = new google.visualization.LineChart(document.getElementById ('container'));
    chart.draw(data, options);
}
google.charts.setOnLoadCallback(drawChart);