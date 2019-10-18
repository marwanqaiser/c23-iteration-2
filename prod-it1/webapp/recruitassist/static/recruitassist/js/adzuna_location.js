// This function is doing the visualization for the skill shortage part.
$('#location_submit').click(function() {
    $.ajax({
        url: "/location_choose/",
        method: 'POST',
        data: {
            suburb: $("#location_input").val(),
            click: true
        },
        // this is the function run after successfully get data from backend.
        success: function (data) {
            var provider = document.getElementById("location_choose");
            provider.action = ""
            provider.target = "the_iframe"
            console.log(provider.action)

            var button = document.getElementById("provider_submit_btn");
                button.style.display = "block";

            console.log(button.display)
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
            console.log(dic_count[0])
            console.log(dic_name[0])

            var x = document.getElementById("full_result");
            console.log(x.style.display)
        if ((x.style.display == "") || (x.style.display == "none")){
            console.log("get in if")
            x.style.display = "block";
        }
        console.log("start piechart")
        if (len.length == 0) {
                x.style.display = "none";
                alert("Oops！" + $("#location_input").val() + " doesn't seem to have skill shortages! Please try another.")
        }
        else {

        var dps1 = [];
        for(var i = 0; i < dic_count.length; i++) {
        dps1.push({y: dic_count[i], label: dic_name[i]});

        }
        // this is the chart creating part.
        var chart = new CanvasJS.Chart("chartContainer", {

//            animationEnabled: true,
            title: {
                text: "Number of Available Jobs!",
                fontSize : 20
            },
         	axisX:{
	    interval: 1,
	    labelAngle: -90

	},
            data: [{
                 type: "column",
                indexLabel: "{y}",
                indexLabelPlacement: "outside",
                indexLabelOrientation: "horizontal",
                dataPoints: dps1
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

