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
                alert("Oops！" + $("#location_input").val() + " seems doesn't have job shortage!")
        }
        else {
        var chart = new CanvasJS.Chart("chartContainer", {

//            animationEnabled: true,
            title: {
                text: "Number of Available Jobs!",
                fontSize : 20
            },
            data: [{
                 type: "column",
                indexLabel: "{y}",
                indexLabelPlacement: "outside",
                indexLabelOrientation: "horizontal",
                dataPoints: [
                    {y: dic_count[0], label: dic_name[0]},
                    {y: dic_count[1] , label: dic_name[1]},
                    {y: dic_count[2] , label: dic_name[2]},
                    {y: dic_count[3] , label: dic_name[3]},
                    {y: dic_count[4] , label: dic_name[4]},
                    {y: dic_count[5] , label: dic_name[5]},
                    {y: dic_count[6] , label: dic_name[6]},
                    {y: dic_count[7] , label: dic_name[7]},
                    {y: dic_count[8] , label: dic_name[8]},
                    {y: dic_count[9] , label: dic_name[9]}
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
