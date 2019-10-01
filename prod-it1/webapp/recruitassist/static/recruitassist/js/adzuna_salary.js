$('#salary_submit').click(function() {
    $.ajax({
        url: "/salary_information/",
        method: 'POST',
        data: {
            suburb: $("#suburb_input").val(),
            category: $("#job_title_input").val(),
            click: true
        },
        success: function (data) {
            var salary_list = []
            var len = new Array()

            $.each(JSON.parse(data),function(key,value) {
//           This line is for add the data information in the result, but if the data return from backend is not ordered, the graph
//           seems like a mess. So i comment it because idk how to sort it.
//              salary_list.push({x: new Date(key.slice(0,4),key.slice(5,7)), y:value})
                salary_list.push({y:value})
                if (value > 0) {
                    len.push(1)
                }
            });

            console.log(salary_list[0])

            var x = document.getElementById("full_result_2");
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
       var chart = new CanvasJS.Chart("chartContainer_salary", {
	animationEnabled: true,

	theme: "light2",

	title:{
		text: "salary information for " + $("#job_title_input").val() + " in " + $("#suburb_input").val()
	},

	axisY:{
		includeZero: false
	},

	data: [{
		type: "line",
		dataPoints: salary_list
	}]

    });
    }
    chart.render();
        }

    });
});
