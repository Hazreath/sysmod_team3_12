$(document).ready(function() {
    console.log("ready")
    
    // Fetch username from local storage
    var uname = document.getElementById("name")
    
    uname.innerHTML = localStorage.getItem("email")
    // TODO REMOVE TEST
//    let d = document.getElementById("dest_account")
//    let a = document.getElementById("amount")
//    d.value = 'gimme@money.fr'
//    a.value = '1'
    
    $('#btn_account').click(function(e){
        window.location.replace("status.html");
    })
    $("#btn_disconnect").click(function(e) {
        window.location.replace("login.html");
    })
    // Submit new transfer
    $("#btn_submit_transfer").click(function (e) {
         e.preventDefault();
          
         // Check input are correct
         let dest = document.getElementById("dest_account").value
         let amount = document.getElementById("amount").value
         // TODO CHECK EMAIL FORMAT
         if (!dest || !amount) {
            errorToast("One of the required field is empty !")
         } else if (!isValidEmail(dest)) {
            errorToast("Destination account email has invalid email format !")
         } else if (parseInt(amount) <= 0) {
             errorToast("Amount must be more than 0 !")
         } else {
            addNewTransaction(dest, amount)
         }
    })
})
