$(document).ready(function() {
    console.log("ready")
    
    // TODO REMOVE ONLY FOR TEST
//    document.getElementById("username").value = "a@b.fr"
//    document.getElementById("password").value = "zzz"
    
    $("#login-button").click(function (e) {
          e.preventDefault();
         // Get username & password
         let u = document.getElementById("username").value
         let p = document.getElementById("password").value
         
         if (!u || !p) {
            errorToast("One of the required field is empty !")
         } else if (!isValidEmail(u)) {
             errorToast("Invalid email format !")
         } else {
            login(u,p)
         }

    })
})