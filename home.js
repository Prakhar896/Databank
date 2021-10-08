function checkPassword() {
  var pwd = document.getElementById("authkeyfield").value;

  var checkURL = 'https://databank.drakonzai.repl.co/passwordCheck'

  axios({
    method: 'post',
    url: checkURL,
    data: {
      "data": pwd
    },
    headers: {
      'DataBankAccessCode': 'ert56',
      "Content-Type": 'application/json'
    }
  }).then((response) => {
    if (response.data.startsWith("Authorisation successful!")) {
      document.getElementsByClassName('dataBankFiles')[0].style.visibility = "visible"
      console.log('Auth successful.')
      var tempAuthToken = response.data.substring(43)
      console.log(tempAuthToken)
      setTimeout(() => {
        document.location = 'http://databank.drakonzai.repl.co/data/' + tempAuthToken
      }, 2000)
    } else {
      document.getElementsByClassName('dataBankFiles')[0].style.visibility = "hidden"
      alert("Incorrect password. Please try again!")
      console.log('Auth unsuccessful')
    }
  })
}