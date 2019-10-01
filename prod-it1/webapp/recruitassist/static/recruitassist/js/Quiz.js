
function myFunction() {
    var x = document.getElementById("team");
    if (x.style.display === "block") {
        x.style.display = "none";
    } else {
        x.style.display = "block";
    }
    var recommendation1 = document.getElementById("recommendation1");
    var recommendation2 = document.getElementById("recommendation2");
    var q1 =document.getElementsByName("question1_choice");
    console.log(q1)
    var communication = document.getElementById("Communication");
    var communication_result = document.getElementById("Communication_result");
    if (q1[0].checked) {
        communication.style.display = 'block';
        communication_result.style.display = 'block';
    }

    var q2 =document.getElementsByName("question2_choice");
    var english = document.getElementById("English");
    var english_result = document.getElementById("English_result");
    if (q2[0].checked) {
        english.style.display = 'block';
        english_result.style.display = 'block';
    }
    else {
        english.style.display = 'none';
        english_result.style.display = 'none';
    }
    var q3 =document.getElementsByName("question3_choice");
    var interview = document.getElementById("Interview");
    var interview_result = document.getElementById("Interview_result");
    if (q3[0].checked) {
        interview.style.display = 'block';
        interview_result.style.display = 'block'
    }
    else {
        interview.style.display = 'none';
        interview_result.style.display = 'none'
    }
    var q4 =document.getElementsByName("question4_choice");
    if (q4[0].checked) {
        communication.style.display = 'block';
        communication_result.style.display = 'block';
    }
    if (q1[1].checked && q4[1].checked) {
        communication.style.display = 'none';
        communication_result.style.display = 'none';
    }
    if (q1[1].checked && q2[1].checked && q3[1].checked && q4[1].checked ) {
        recommendation1.style.display = 'none';
        recommendation2.style.display = 'block';
    }

}
