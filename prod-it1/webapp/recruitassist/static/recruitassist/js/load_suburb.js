// This function is changing the job shortage drop down list dynamic
window.onload = function(){
　　$.ajax({      // using ajax to send POST request to backend
        url: "/suburbs/",
        method: 'POST',
        data: {
            suburb_1: true
        },
        success: function (data) {
            var select_list = document.getElementById("location_input");
            select_list.options.length=0; //each time when load the Homepage_job page, first remove all options in dropdown list
            suburbs_list = JSON.parse(data)  // get data from backend
             for(var i=0;i<suburbs_list.length;i++){
                    console.log(suburbs_list[i])
                     $("#location_input").append("<option value='" + suburbs_list[i] + "'>" + suburbs_list[i] +"</option>");
            	    }
        }
        })
        }