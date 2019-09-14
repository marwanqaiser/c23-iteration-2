$('#location_submit').click(function() {
    $.ajax({
        url: "location_choose/",
        method: 'POST',
        data: {
            suburb: $("#location_input").val(),
            click: true
        },
        success: function (data) {
            var dic_count = new Array()
            var dic_name = new Array()
            var len = new Array()
            $.each(JSON.parse(data),function(key,value) {

                dic_name.push(key)
                dic_count.push(value)
                if (value > 0) {
                    len.push(1)
                }
            });
            console.log(dic_count)
            console.log(dic_name)

            var x = document.getElementById("chartContainer");
            console.log(x.style.display)
        if ((x.style.display == "") || (x.style.display == "none")){
            console.log("get in if")
            x.style.display = "block";
        }
        console.log("start piechart")
        if (len.length == 0) {
                x.style.display = "none";
                alert("Oops！This place seems doesn't have job shortage! Do you want to try other place?")
        }
        else {
        var chart = new CanvasJS.Chart("chartContainer", {

            animationEnabled: true,
            title: {
                text: "Most job shortages in location you want to know!"
            },
            data: [{
                type: "pie",
                startAngle: 240,
                yValueFormatString: "##0.0\"\"",
                indexLabel: "{label} {y}",
                dataPoints: [
                    {y: dic_count[0], label: dic_name[0]},
                    {y: dic_count[1] , label: dic_name[1]},
                    {y: dic_count[2] , label: dic_name[2]},
                    {y: dic_count[3] , label: dic_name[3]},
                    {y: dic_count[4] , label: dic_name[4]},
                    {y: dic_count[5] , label: dic_name[5]},
                    {y: dic_count[6] , label: dic_name[6]}
                ]
            }]
        });

        }
        console.log("finished")
        if (len.length > 0) {
        chart.render();
        }
        }
    });
});

function hide_location_result() {
    var location_search = document.getElementById("1stfunction");
    var location_result = document.getElementById("location_result");
    var job_search = document.getElementById("2ndfunction");
    if (x.style.display === "none") {
        x.style.display = "block";
    } else {
        x.style.display = "none";
    }
}