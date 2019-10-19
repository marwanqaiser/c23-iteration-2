function setMail(){
    var ddl = document.getElementById("job_title_input");
    var selectedOption = ddl.options[ddl.selectedIndex];
    var mailValue = selectedOption.getAttribute("value");
    var textBox = document.getElementById("suburb_input");
    var textBox2= document.getElementById("suburb_input2")
    if(mailValue=="it-jobs"){
        textBox.options.length=0
        textBox2.options.length=0
       var option = document.createElement('option');
       option.text = option.value = "Melbourne Region";
       console.log("cnm")
//       textBox.appendChild(option);
       textBox.options.add(option);

       var option = document.createElement('option');
       option.text = option.value = "Geelong Region";
//       textBox2.appendChild(option);
       textBox2.options.add(option);
    }
    else if(mailValue=="admin-jobs"){
       textBox.options.length=0
       textBox2.options.length=0
       var option = document.createElement('option');
       option.text = option.value = "Melbourne Region";
//       textBox.appendChild(option);
       textBox.options.add(option);
       var option = document.createElement('option');
       option.text = option.value = "Geelong Region";
//       textBox.appendChild(option);
       textBox.options.add(option);

       var option = document.createElement('option');
       option.text = option.value = "Bendigo Region";
//       textBox.appendChild(option);
       textBox.options.add(option);

       var option = document.createElement('option');
       option.text = option.value = "La Trobe Region";
//       textBox.appendChild(option);
       textBox.options.add(option);

       var option = document.createElement('option');
       option.text = option.value = "Ballarat Region";
//       textBox.appendChild(option);
       textBox.options.add(option);

       var option = document.createElement('option');
       option.text = option.value = "Geelong Region";
//       textBox2.appendChild(option);
       textBox2.options.add(option);

       var option = document.createElement('option');
       option.text = option.value = "Bendigo Region";
//       textBox2.appendChild(option);
       textBox2.options.add(option);

       var option = document.createElement('option');
       option.text = option.value = "La Trobe Region";
//       textBox2.appendChild(option);
       textBox2.options.add(option);

       var option = document.createElement('option');
       option.text = option.value = "Ballarat Region";
//       textBox2.appendChild(option);
       textBox2.options.add(option);


    }
        else if(mailValue=="healthcare-nursing-jobs"){
       textBox.options.length=0
       textBox2.options.length=0
       var option = document.createElement('option');
       option.text = option.value = "Melbourne Region";
//       textBox.appendChild(option);
       textBox.options.add(option);
       var option = document.createElement('option');
       option.text = option.value = "Geelong Region";
//       textBox.appendChild(option);
       textBox.options.add(option);

       var option = document.createElement('option');
       option.text = option.value = "Bendigo Region";
//       textBox.appendChild(option);
       textBox.options.add(option);

       var option = document.createElement('option');
       option.text = option.value = "La Trobe Region";
//       textBox.appendChild(option);
       textBox.options.add(option);

       var option = document.createElement('option');
       option.text = option.value = "Ballarat Region";
//       textBox.appendChild(option);
       textBox.options.add(option);

       var option = document.createElement('option');
       option.text = option.value = "Shepparton Region";
       textBox.options.add(option);
//        textBox.appendChild(option);

       var option = document.createElement('option');
       option.text = option.value = "Mildura Region";
//       textBox.appendChild(option);
       textBox.options.add(option);

       var option = document.createElement('option');
       option.text = option.value = "Geelong Region";
//       textBox2.appendChild(option);
       textBox2.options.add(option);

       var option = document.createElement('option');
       option.text = option.value = "Bendigo Region";
//       textBox2.appendChild(option);
       textBox2.options.add(option);

       var option = document.createElement('option');
       option.text = option.value = "La Trobe Region";
//       textBox2.appendChild(option);
       textBox2.options.add(option);

       var option = document.createElement('option');
       option.text = option.value = "Ballarat Region";
//       textBox2.appendChild(option);
       textBox2.options.add(option);

       var option = document.createElement('option');
       option.text = option.value = "Shepparton Region";
//       textBox2.appendChild(option);
       textBox2.options.add(option);

        var option = document.createElement('option');
       option.text = option.value = "Mildura Region";
       textBox2.options.add(option);


    }
            else if(mailValue=="accounting-finance-jobs"){
       textBox.options.length=0
       textBox2.options.length=0
       var option = document.createElement('option');
       option.text = option.value = "Melbourne Region";
       textBox.options.add(option);
       var option = document.createElement('option');
       option.text = option.value = "Geelong Region";
       textBox.options.add(option);


       var option = document.createElement('option');
       option.text = option.value = "Geelong Region";
       textBox2.options.add(option);
    }
       else if(mailValue=="teaching-jobs"){
       textBox.options.length=0
       textBox2.options.length=0
       var option = document.createElement('option');
       option.text = option.value = "Melbourne Region";
       textBox.options.add(option);
       var option = document.createElement('option');
       option.text = option.value = "Geelong Region";
       textBox.options.add(option);

       var option = document.createElement('option');
       option.text = option.value = "Bendigo Region";
       textBox.options.add(option);

       var option = document.createElement('option');
       option.text = option.value = "La Trobe Region";
       textBox.options.add(option);

       var option = document.createElement('option');
       option.text = option.value = "Ballarat Region";
       textBox.options.add(option);

       var option = document.createElement('option');
       option.text = option.value = "Shepparton Region";
       textBox.options.add(option);

       var option = document.createElement('option');
       option.text = option.value = "Geelong Region";
       textBox2.options.add(option);

       var option = document.createElement('option');
       option.text = option.value = "Bendigo Region";
       textBox2.options.add(option);

       var option = document.createElement('option');
       option.text = option.value = "La Trobe Region";
       textBox2.options.add(option);

       var option = document.createElement('option');
       option.text = option.value = "Ballarat Region";
       textBox2.options.add(option);

       var option = document.createElement('option');
       option.text = option.value = "Shepparton Region";
       textBox2.options.add(option);

    }
       else if(mailValue=="sales-jobs"){
       textBox.options.length=0
       textBox2.options.length=0
       var option = document.createElement('option');
       option.text = option.value = "Melbourne Region";
       textBox.options.add(option);
       var option = document.createElement('option');
       option.text = option.value = "Geelong Region";
       textBox.options.add(option);

       var option = document.createElement('option');
       option.text = option.value = "Bendigo Region";
       textBox.options.add(option);

       var option = document.createElement('option');
       option.text = option.value = "La Trobe Region";
       textBox.options.add(option);

       var option = document.createElement('option');
       option.text = option.value = "Geelong Region";
       textBox2.options.add(option);

       var option = document.createElement('option');
       option.text = option.value = "Bendigo Region";
       textBox2.options.add(option);

       var option = document.createElement('option');
       option.text = option.value = "La Trobe Region";
       textBox2.options.add(option);
       }

               else if(mailValue=="engineering-jobs"){
       textBox.options.length=0
       textBox2.options.length=0
       var option = document.createElement('option');
       option.text = option.value = "Melbourne Region";
       textBox.options.add(option);
       var option = document.createElement('option');
       option.text = option.value = "Geelong Region";
       textBox.options.add(option);

       var option = document.createElement('option');
       option.text = option.value = "La Trobe Region";
       textBox.options.add(option);


       var option = document.createElement('option');
       option.text = option.value = "Geelong Region";
       textBox2.options.add(option);


       var option = document.createElement('option');
       option.text = option.value = "La Trobe Region";
       textBox2.options.add(option);





    }
}
