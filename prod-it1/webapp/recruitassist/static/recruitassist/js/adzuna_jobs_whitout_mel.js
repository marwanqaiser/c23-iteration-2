$('#job_submit_without_mel').click(function() {

    var box = $(".box:checked").val();
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

            var x = document.getElementById("new_result_iteration3");
            var y = document.getElementById("chartContainer_jobs");
            console.log(x.style.display)
        // hide the previous result
        if (y.style.display == "block"){
            console.log("hide the previous graph")
            y.style.display = "none";
        }


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
        function onClick(e){

        //show the result if first time run
        if ((x.style.display == "") || (x.style.display == "none")){
            console.log("get in if")
            x.style.display = "block";
        }
//		alert(  e.dataSeries.type+ ", dataPoint { position:" + e.dataPoint.label + ", y: "+ e.dataPoint.y + " }" );
//        var table = document.getElementById("shortage_table");
//        $("#shortage_table  tr:not(:first)").html("");
//        var per = [
//  			{id:001,name:'a',job:'ad'},
//			{id:002,name:'b',job:'ap'},
//			{id:003,name:'c',job:'bot'}
//			];
//        for(var i = 0;i < per.length; i++){
//         oneRow = table.insertRow();
//         cell1= oneRow.insertCell();
//         cell2= oneRow.insertCell();
//         cell3= oneRow.insertCell();
//         cell4= oneRow.insertCell();
//         cell1.innerHTML = per[i]["id"];
//         cell2.innerHTML= per[i]["name"];
//         cell3.innerHTML = per[i]["job"];
//         cell4.innerHTML= i;
//         }
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
                    $("#shortage_table  tr:not(:first)").html("");
                    var table = document.getElementById("shortage_table");
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
