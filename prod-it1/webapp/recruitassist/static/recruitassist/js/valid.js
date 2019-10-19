function doSomething(){
var val = $("#provider_list").val();

var obj = $("#provider").find("option[value='" + val + "']");

if (obj != null && obj.length > 0)
    return true  // allow form submission
else
    alert("Please select the suburb from the list!");
    return false
}
