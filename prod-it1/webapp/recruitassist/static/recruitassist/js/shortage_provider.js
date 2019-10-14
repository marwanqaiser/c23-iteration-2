$('#provider_submit_btn').click(function() {
     var provider = document.getElementById("location_choose");
            provider.action = "/listprovider/"
            provider.target = ""
            console.log(provider.action)

//    $.ajax({
//        url: "/listprovider/",
//        method: 'POST',
//        data: {
//            suburb: $("#location_input").val(),
//        },
//        success: function (result) {
//                alert('Go to training institution page.')
////                window.location = '/listprovider/'
//            },
//        })
        })