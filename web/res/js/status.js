$(document).ready(function() {
    console.log("ready")
    
    // Fetch username from local storage
    var uname = document.getElementById("name")
    
    uname.innerHTML = localStorage.getItem("email")
    
    // Fetch balance
    var balance_div = document.getElementById("balance")
    getUserBalance(balance_div)
    
    // Fetch transactions
    var transferts_div = document.getElementById("transferts")
    getUserTransactions(transferts_div)
    
    // bind modify and delete onclick events
    
    
    // Onclick btn_transfer : go to transfer page
    document.getElementById("btn_transfer").addEventListener('click',function() {
        window.location.replace("transfer.html");
    })
})

function displayModifyPopup(id,dest_account,amount) {
    //$("modify-popup").show()
    var dest = document.getElementById("dest_account")
    var am = document.getElementById("amount")
    dest.value = dest_account
    am.value = amount
    $("amount").value = amount
    
   //input checking
document.getElementById("btn_submit_transfer").addEventListener('click',function(e) {
        if (!dest.value || !am.value) {
            errorToast("One of the required value is empty !")
        } else if (!isValidEmail(dest.value)) {
            errorToast("Destination account has wrong email format !")
        } else if (parseInt(am.value) <= 0) {
            errorToast("Amount must be above 0 !")
        } else {
            modifyTransaction(id,dest,amount)
        }
    })
}