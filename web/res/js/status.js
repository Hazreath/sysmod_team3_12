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
    
    // Onclick btn_transfer : go to transfer page
    document.getElementById("btn_transfer").addEventListener('click',function() {
        window.location.replace("transfer.html");
    })
    document.getElementById("btn_disconnect").addEventListener('click',function() {
        window.location.replace("login.html");
    })
    document.getElementById("btn_cancel_transfer").addEventListener('click',function() {
        var popup = document.getElementById("modify-popup")
        popup.style.visibility = "hidden"
    })
})

function displayModifyPopup(id,dest_account,amount) {
    var popup = document.getElementById("modify-popup")
    popup.style.visibility = "visible"
    var dest = document.getElementById("dest_account")
    var am = document.getElementById("amount")
    dest.value = dest_account
    am.value = amount
    
    console.log(id,dest,amount)
    
   //input checking
document.getElementById("btn_submit_transfer").addEventListener('click',function(e) {
        if (!dest.value || !am.value) {
            errorToast("One of the required value is empty !")
        } else if (!isValidEmail(dest.value)) {
            errorToast("Destination account has wrong email format !")
        } else if (parseInt(am.value) <= 0) {
            errorToast("Amount must be above 0 !")
        } else {
            modifyTransaction(id,dest.value,am.value)
            popup.style.visibility = "hidden"
        }
    })
}

function displayModalUndo(id,dest_account,amount) {
    if (confirm("Are you sure you want to undo this transfer ?")) {
        undoTransaction(id,dest_account,amount)
    }
}