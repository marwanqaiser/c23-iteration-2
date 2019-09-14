$('#job_submit').click(function() {
    $.ajax({
        url: "top_jobs/",
        method: 'POST',
        data: {
            jobs: $("#job_input").val(),
            click: true
        },
        success: function (data) {
            var location_count = new Array()
            var location_name = new Array()
            var len = new Array()
            $.each(JSON.parse(data),function(key,value) {

                location_name.push(key)
                location_count.push(value)
                if (value > 0) {
                    len.push(1)
                }
            });
            console.log(location_count)
            console.log(location_name)

            var x = document.getElementById("chartContainer_jobs");
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
        var chart_job = new CanvasJS.Chart("chartContainer_jobs", {

            animationEnabled: true,
            title: {
                text: "Top 10 best suburb for " + $("#job_input").val()
            },
            data: [{
                type: "pie",
                startAngle: 240,
                yValueFormatString: "##0.0\"\"",
                indexLabel: "{label} {y}",
                dataPoints: [
                    {y: location_count[0], label: location_name[0]},
                    {y: location_count[1] , label: location_name[1]},
                    {y: location_count[2] , label: location_name[2]},
                    {y: location_count[3] , label: location_name[3]},
                    {y: location_count[4] , label: location_name[4]},
                    {y: location_count[5] , label: location_name[5]},
                    {y: location_count[6] , label: location_name[6]}
                ]
            }]
        });

        }
        console.log("finished")
        if (len.length > 0) {
        chart_job.render();
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