// This js function is for the visualization for top suburb function.
$('#job_submit_without_mel').click(function() {

    var box = $(".box:checked").val(); //get the user input
    $.ajax({
        async : false,
        url: "/top_jobs_without_mel/",
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

            var x = document.getElementById("shortage_result_part");
            console.log(x.style.display)
        // hide the previous result
        x.style.display = "block"


        console.log("start piechart")
        if (len.length == 0) {
                x.style.display = "none";
                alert("Oops！This place seems doesn't have job shortage! Do you want to try other place?")
        }
        else {
        var dps1 = [];
        for(var i = 0; i < location_count.length; i++) {
        dps1.push({y: location_count[i], label: location_name[i], click:onClick});

        }
        // this part is for chart creating.
        var chart_jobs_without_mel = new CanvasJS.Chart("chartContainer_jobs_without_mel", {

            animationEnabled: true,
            title: {
                text: "Top suburbs for " + $("#job_input").val()
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
        chart_jobs_without_mel.render();
        }
        // This is the click function of the chart.
        function onClick(e){

        //show the result if first time run
        y = document.getElementById("new_result_iteration3")
        if ((y.style.display == "") || (y.style.display == "none")){
            console.log("get in if")
            y.style.display = "block";
        }

		$.ajax({
                url: "/details/",
                type: "POST",
                data: {
                    location: e.dataPoint.label,
                    title: $("#job_input").val(),
                },
                success: function (data) {
                  var detail_list = []
                 $.each(JSON.parse(data),function(key,value) {
                       detail_list.push(value)

            });
//                console.log(detail_list[0]['job_title'])
//                console.log(detail_list[1]['job_title'])
//                console.log(detail_list[2]['job_title'])
//                    $("#shortage_table  tr:not(:first)").html("");

                    // this part is geting the table and remove all rows in the table each time click.
                    var table = document.getElementById("tbMain");
                    var rowNum=table.rows.length;
                     for (i=0;i<rowNum;i++)
                     {
                         table.deleteRow(i);
                         rowNum=rowNum-1;
                         i=i-1;
                     }

                    // This part is using a for loop to get data and insert into the table.
                    for(var i = 0; i < detail_list.length; i++) {
                     url = detail_list[i]["url"]
                     oneRow = table.insertRow();
                     cell1= oneRow.insertCell();
                     cell2= oneRow.insertCell();
                     cell3= oneRow.insertCell();
                     cell4= oneRow.insertCell();
                     cell1.innerHTML = detail_list[i]["job_title"];
                     cell2.innerHTML= detail_list[i]["company_name"];
                     cell3.innerHTML = detail_list[i]["location"];
                     cell4.innerHTML= "<a href='" + url + " ' target=" + "_blank" + ">" + "click here" + "</a>";

        }
                }
            });

	    }
        }
    });
});

