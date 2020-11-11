function drawChart() {
    // Define the chart to be drawn.
    var data = new google.visualization.DataTable();
    data.addColumn('string', 'Data');
    data.addColumn('number', 'measure');
    alert("ZHOPA");
    {% for i in base %}
        data.addRows([
           [{{ i.data }}, {{ i.weight }}],
           [{{ i.data }}, {{ i.weight }}],
        ]);
    {% endfor %}




     // Set chart options
    var options = {'title':'График твоей жиробазности', 'width':550, 'height':400};

    // Instantiate and draw the chart.
    var chart = new google.visualization.PieChart(document.getElementById ('container'));
    chart.draw(data, options);
}
google.charts.setOnLoadCallback(drawChart);