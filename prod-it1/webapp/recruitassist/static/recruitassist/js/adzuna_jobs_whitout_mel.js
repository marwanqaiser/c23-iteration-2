$('#job_submit_without_mel').click(function() {

    var box = $(".box:checked").val();
    $.ajax({
        url: "top_jobs_without_mel/",
        method: 'POST',
        data: {
            jobs: $("#job_input").val(),
            area: box
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

            var x = document.getElementById("chartContainer_jobs_without_mel");
            var y = document.getElementById("chartContainer_jobs");
            console.log(x.style.display)
        // hide the previous result
        if (y.style.display == "block"){
            console.log("hide the previous graph")
            y.style.display = "none";
        }

        //show the result if first time run
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
        var dps1 = [];
        for(var i = 0; i < location_count.length; i++) {
        dps1.push({y: location_count[i], label: location_name[i]});

        }
        var chart_jobs_without_mel = new CanvasJS.Chart("chartContainer_jobs_without_mel", {

            animationEnabled: true,
            title: {
                text: "Top suburbs for " + $("#job_input").val()
            },
            data: [{
                type: "pie",
                startAngle: 240,
                yValueFormatString: "##0\"\"",
                indexLabel: "{label} {y}",
                dataPoints: dps1
            }]
        });

        }
        console.log("finished")
        if (len.length > 0) {
        chart_jobs_without_mel.render();
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
