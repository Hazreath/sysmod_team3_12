function validate() {
  var username = document.getElementById('username').value
  var password = document.getElementById('password').value
  if (username == 'Alex' && password == '1234') {
    alert('Login succesfully')
    return false
  } else {
    alert('Wrong data.')
    return false
  }
}
