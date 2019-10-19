$('#find_submit').click(function() {
    var suburb_input = document.getElementById("result").rows[1].cells[5].innerHTML;
    suburb_input = suburb_input[0].toUpperCase() + suburb_input.slice(1,suburb_input.length).toLowerCase();
    console.log(suburb_input)
    $.ajax({
        url: "/location_choose/",
        method: 'POST',
        data: {
            suburb: suburb_input,
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
            console.log(dic_count[0])
            console.log(dic_name[0])

console.log("start piechart")
        if (len.length == 0) {

                alert("Oops！" + $("#location_input").val() + " does not seem to have skill shortage! Please try another.")
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
