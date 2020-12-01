$(document).ready(function() {
    console.log("ready")
    
    // TODO REMOVE ONLY FOR TEST
    document.getElementById("username").value = "benji@aled.fr"
    document.getElementById("password").value = "aled"
    
    $("#login-button").click(function (e) {
          e.preventDefault();
         // Get username & password
         let u = document.getElementById("username").value
         let p = document.getElementById("password").value
         if (u && p) {
            login(u,p)
         } else {
            // TODO Display error message
            alert("One of the field was left empty !")
         }

    })
})
var URL_WS_TOKEN = "http://localhost:8000/token"
function login(username, password) {
    var url_auth = URL_WS_TOKEN + "?username=" + username + "&password="
        + password
    $.ajax({
        url : URL_WS_TOKEN,
        type:"POST",
//      dataType:'jsonp',
//        crossDomain: true,
//        type:'json',
        headers: {  
            'Access-Control-Allow-Origin': 'x-requested-with',
            'Content-Type':'application/json'
        },

        data: {
            username:username,
            password:password
        },
        success: function(json) {
            console.log(json)
            // Keep token in memory
        }
    })
}