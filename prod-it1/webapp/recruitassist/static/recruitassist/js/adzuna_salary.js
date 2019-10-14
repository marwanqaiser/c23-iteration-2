// This js function is for the salary function visualization.
$('#salary_submit').click(function() {
    $.ajax({
        url: "/salary_information/",
        method: 'POST',
        data: {
            suburb: $("#suburb_input").val(),
            suburb2: $("#suburb_input2").val(),
            category: $("#job_title_input").val(),
            click: true
        },
        success: function (data) {
            if ($("#suburb_input").val() == $("#suburb_input2").val()) {
                alert("Please choose 2 different locations！")
                return;
            }

            var salary_list1 = new Array() // to store the salary data for 1st location
            var salary_list2 = new Array() // to store salary data for 2nd location
            var salary_date = new Array()
            var len = new Array()
            var location_list = []
            var salary_list_2 = []
            $.each(JSON.parse(data),function(key,value) {
//           This line is for add the data information in the result, but if the data return from backend is not ordered, the graph
//           seems like a mess. So i comment it because idk how to sort it.
//              salary_list.push({x: new Date(key.slice(0,4),key.slice(5,7)), y:value})
                location_list.push(key)
                salary_list_2.push(value)
                if (value !== 0) {
                    len.push(1)
                }
            });

            console.log(salary_list_2)
            $.each(salary_list_2[0],function(key,value) {
                salary_date.push(key)
                salary_list1.push(value)
            });
            console.log(salary_list1)

            $.each(salary_list_2[1],function(key,value) {
                salary_date.push(key)
                salary_list2.push(value)
            });
            console.log(salary_list2)
//            console.log(salary_date[0])

            var x = document.getElementById("full_result_2");
            var y = document.getElementById("chartContainer_salary");
            console.log(x.style.display)
        // hide the previous result
        if (y.style.display == "block"){
            console.log("hide the previous graph")
            y.style.display = "none";
        }
            console.log(x.style.display)

        if ((x.style.display == "") || (x.style.display == "none")){
            console.log("get in if")
            x.style.display = "block";
        }

        console.log("start piechart")

        if (len.length == 0) {
                x.style.display = "none";
                alert("Oops！" + "No enough data for "+ $("#job_title_input").val() + " in " + $("#suburb_input").val())
        }

        else {
        var dps1 = [];
        var dps2 = [];
        for(var i = 0; i < salary_date.length; i++)
        {
        dps1.push({y: salary_list1[i],x: new Date(salary_date[i])}); // list for draw graph for location1
        dps2.push({y: salary_list2[i],x: new Date(salary_date[i])}); // list for draw graph for location1
            }
       var chart = new CanvasJS.Chart("chartContainer_salary", {
	animationEnabled: true,

	theme: "light2",

	title:{
		text: "Average salary information for " + $("#job_title_input").val() + " in " + $("#suburb_input").val() + " and " + $("#suburb_input2").val()
	},

	axisX:{
	    valueFormatString: "MMM-YYYY",
	    crosshair: {
			enabled: true,
			snapToDataPoint: true
		},
	    interval: 1,
        intervalType: "month",
	    title: "Date",
	    labelAngle: 90

	},


	axisY:{
	    title: "Salary (AUD)",
	    crosshair: {
			enabled: true
		},
		includeZero: false
	},

    // This is used to make the legend click function.
    legend: {
            cursor: "pointer",
            itemclick: function (e) {
                //console.log("legend click: " + e.dataPointIndex);
                //console.log(e);
                if (typeof (e.dataSeries.visible) === "undefined" || e.dataSeries.visible) {
                    e.dataSeries.visible = false;
                } else {
                    e.dataSeries.visible = true;
                }

                e.chart.render();
            }
        },

	data: [
	{
		type: "line",
		showInLegend: true,
		name: $("#suburb_input").val(),
		dataPoints: dps1
	},
	{
		type: "line",
		showInLegend: true,
		name: $("#suburb_input2").val(),
		dataPoints: dps2
	}
	]

    });
    }
    chart.render();



        }

    });
});
