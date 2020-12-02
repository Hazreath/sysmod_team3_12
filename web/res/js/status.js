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
})
