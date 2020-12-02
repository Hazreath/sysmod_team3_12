// API endpoint parameters
const ROOT = "http://localhost:8000"
const URL_API_TOKEN = ROOT + "/token"
const URL_API_ME = ROOT + "/users/me/"
const URL_API_MY_ACCOUNT = ROOT + "/account"
const URL_API_USER_TRANSACTIONS = ROOT + "/transaction"
const URL_API_MODIFY_TRANSACTIONS = ROOT + "/transaction/modify"
// Other params
const CURRENCY = " €"

function login(username, password) {
    $.ajax({
        url : URL_API_TOKEN,
        type:"POST",
        crossDomain: true,
        headers: {  
            'Access-Control-Allow-Origin': 'x-requested-with',
            'Content-Type': 'application/x-www-form-urlencoded'
        },
        data: {
            'username':username,
            'password':password
        },
        success: function(json) {
            // Keep token in memory
            localStorage.setItem("token", json.access_token);
            getUserInfo(json.access_token)
        },
        error: function(data) {
            errorToast("Wrong username or password.")
        }
        
    })
}
function getUserInfo(token) {
    $.ajax({
        url : URL_API_ME,
        type:"GET",
        crossDomain: true,
        headers: {  
            'Access-Control-Allow-Origin': 'x-requested-with',
            'Authorization': 'Bearer ' + token,
            'Accept': 'application/json'
        },
        success: function(json) {
            console.log(json)
            // Keep profile infos in memory
            localStorage.setItem("id", json.id);
            localStorage.setItem("email", json.email );
            
            // Go to status page
            window.location.replace("status.html");
        },
        error: function(data) {
            errorToast("Error when reaching server.")
        }
        
    })
}
function getUserBalance(div) {
    var token = localStorage.getItem("token")
    $.ajax({
        url : URL_API_MY_ACCOUNT,
        type:"GET",
        crossDomain: true,
        headers: {  
            'Access-Control-Allow-Origin': 'x-requested-with',
            'Authorization': 'Bearer ' + token,
            'Accept': 'application/json'
        },
        success: function(json) {
            
            displayBalance(div,json.balance)
            
        },
        error: function(data) {
            // TODO ERROR CASES (token expired etc)
            errorToast(data.responseJSON.detail)
            // Token may have expired
            window.location.replace("login.html");
        }
        
    })
}
function getUserTransactions(table) {
    var token = localStorage.getItem("token")
    var my_id = localStorage.getItem("id")
    $.ajax({
        url : URL_API_USER_TRANSACTIONS,
        type:"GET",
        crossDomain: true,
        headers: {  
            'Access-Control-Allow-Origin': 'x-requested-with',
            'Authorization': 'Bearer ' + token,
            'Accept': 'application/json'
        },
        success: function(json) {
            console.log(json)
            displayTransactions(table,json)
            
        },
        error: function(data) {
            errorToast(data.responseJSON.detail)
            // Token may have expired
            window.location.replace("login.html");
        }
        
    })
}
function addNewTransaction(dest, amount) {
    var token = localStorage.getItem("token")
    console.log("token:" + token)
    console.log("dest:" + dest)
    console.log("amounr:" + amount)
    $.ajax({
        url : URL_API_USER_TRANSACTIONS,
        type:"POST",
        crossDomain: true,
        headers: {  
            'Access-Control-Allow-Origin': 'x-requested-with',
            'Content-Type': 'application/json',
            'Authorization': 'Bearer ' + token,
            'Accept': 'application/json'
            
        },
        data: JSON.stringify({
            'amount':amount.toString(),
            'dest_account_email':dest
        }),
        success: function(json) {
            toast("Transaction successful !")
            
        },
        error: function(data) {
            errorToast(data.responseJSON.detail)
            
            if (data.responseJSON == "Invalid credentials") {
                // Token has expired
                window.location.replace("login.html");
            }
        }
        
    })
}
function modifyTransaction(id, dest, amount) {
    var token = localStorage.getItem("token")
    console.log(id + " " + dest + " " + amount)
    $.ajax({
        url : URL_API_MODIFY_TRANSACTIONS,
        type:"POST",
        crossDomain: true,
        headers: {  
            'Access-Control-Allow-Origin': 'x-requested-with',
            'Content-Type': 'application/json',
            'Authorization': 'Bearer ' + token,
            'Accept': 'application/json'
            
        },
        data: JSON.stringify({
            'amount':amount.toString(),
            
            'id':id
        }),
        success: function(json) {
            toast("Transaction successful !")
            
        },
        error: function(data) {
            errorToast(data.responseJSON.detail)
            console.log(data)
            if (data.responseJSON == "Invalid credentials") {
                // Token has expired
                window.location.replace("login.html");
            }
        }
        
    })
}
// displays
function displayTransactions(tr_list,list) {
    var my_id = localStorage.getItem("id")
    var html = ""
    let index = 1
    list.forEach(function(t) {
        
        let row = tr_list.insertRow(index)
        let cell = row.insertCell(0)
        html = "Transfer"
        if (t.source_account.id == my_id) {
            html += " to " + t.dest_account.user.email
            // Add modify and delete to MY transaction
            let cellSettings = row.insertCell(1)
            cellSettings.innerHTML = 
                "<a class='modify' id='"+ t.id + "'>" +
                "<img src='res/images/settings.png'></img></a>"
            +   "<a class='delete' id='"+ t.id + "'>" +
                "<img src='res/images/delete.png'></img></a>"
        
        cellSettings.getElementsByClassName("modify")[0].addEventListener('click',function(it) {
            console.log(t.id)
            displayModifyPopup(t.id, t.dest_account.user.email, t.amount)
        })
        } else {
            html += " from " + t.source_account.user.email
        }
        html += ": " + t.amount + CURRENCY
        cell.innerHTML = html
        index++
        
        
    })
    //tr_list.innerHtml = html
}
function displayBalance(div_balance, balance) {
    div_balance.innerHTML = "Your balance: " + balance + CURRENCY
}



// Verifications
function isValidEmail(email) {
    format = /.+@.+\.\D{1,3}/
    return format.test(email)
}
// Toasts display
function errorToast(text) {
  // Get the snackbar DIV
  var toast = document.getElementById("error-toast");

  toast.innerHTML = text
  // Add the "show" class to DIV
  toast.className = "show";
    
  // After 3 seconds, remove the show class from DIV
  setTimeout(function(){ 
      toast.className = toast.className.replace("show", "hide");
  }, 3000);
}
function toast(text) {
  // Get the snackbar DIV
  var toast = document.getElementById("toast");

  toast.innerHTML = text
  // Add the "show" class to DIV
  toast.className = "show";
    
  // After 3 seconds, remove the show class from DIV
  setTimeout(function(){ 
      toast.className = toast.className.replace("show", "hide");
  }, 3000);
}