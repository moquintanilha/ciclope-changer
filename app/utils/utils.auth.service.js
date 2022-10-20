const axios = require('axios')
const dotenv = require('dotenv')
dotenv.config()

function getToken(clientId, secret){
  const data = JSON.stringify({
    "client_id": `${clientId}`,
    "secret": `${secret}`
  });

  const config = {
    method: 'post',
    url: `${process.env.TIGER_URL}`,
    headers: {
      'Content-Type': 'application/json'
    },
    data: data

  };

  axios(config)
.then(function (response) {
  console.log(JSON.stringify(response.data))
})
.catch(function (error) {
  console.log(error)
});

}



module.exports = getToken