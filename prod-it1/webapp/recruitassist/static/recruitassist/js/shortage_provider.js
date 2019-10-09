$('#provider_submit_btn').click(function() {
    $.ajax({
        url: "/listprovider/",
        method: 'POST',
        data: {
            suburb: $("#location_input").val(),
        },
        success: function (result) {
                alert('Go to training institution page.')
            },
        })
        })