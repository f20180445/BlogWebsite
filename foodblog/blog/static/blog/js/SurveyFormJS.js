function submitBtn() {

//Logic to check if Name is Valid
    var nameField = document.forms[0].name.value;
    var name=true;
    if (nameField==""){
        window.alert("had to come here");
        name=false;
    }

//Logic to check if Email is Valid
    var emailField = document.forms[0].email.value;
    var at = emailField.indexOf("@");
    var dot = emailField.lastIndexOf(".");
    var email=true;
    if (at < 1 || dot < at+2 || dot==emailField.length){
        email=false;
    }



//Logic to check if Name and Email are Fine
    if (name==true){
        if (email==true){
            window.alert("Form Submitted Successfully!");
            return true;
        }
        else{
            window.alert("Email Incorrect");
            return false;
        }
    }
    else{
        window.alert("Name Incorrect");
        return false;
    }

}
