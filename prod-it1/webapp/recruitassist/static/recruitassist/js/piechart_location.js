function piechart_locations() {

        var x = document.getElementById("chartContainer");
        if (x.style.display === "none") {
            x.style.display = "block";
        } else {
            x.style.display = "none";
        }
       var dic = []
       for(var key in m)
        {
            dic.push(key)
           console.log(key)
        }
        var chart = new CanvasJS.Chart("chartContainer", {

            animationEnabled: true,
            title: {
                text: "Desktop Search Engine Market Share - 2016"
            },
            data: [{
                type: "pie",
                startAngle: 240,
                yValueFormatString: "##0.00\"\"",
                indexLabel: "{label} {y}",
                dataPoints: [
                    {y: 5040, label: "Google"},
                    {y: 7543, label: "Bing"},
                    {y: 754, label: "Baidu"},
                    {y: 4341, label: "Yahoo"},
                    {y: 1446, label: "Others"}
                ]
            }]
        });
        chart.render();
    }