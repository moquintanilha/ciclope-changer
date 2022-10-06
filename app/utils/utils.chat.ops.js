const axios = require('axios');
const dotenv = require('dotenv');
dotenv.config();

function sendMsg(vpnName, vpnAlternate){
  const data = JSON.stringify({
    "host": `${vpnName}`,
    "vpnAlternate": `${vpnAlternate}`
  });

  const config = {
    method: 'post',
    url: `${process.env.CHATOPS_HOST}`,
    headers: {
      'Content-Type': 'application/json'
    },
    data: data

  };

  axios(config)
.then(function (response) {
  console.log(JSON.stringify(response.data));
})
.catch(function (error) {
  console.log(error);
});

}



module.exports = sendMsg;