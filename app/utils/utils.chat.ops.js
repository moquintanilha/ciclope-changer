const axios = require('axios');
const dotenv = require('dotenv');
dotenv.config();

function sendMsg(host, vpnAlternate){
  var data = JSON.stringify({
    "host": `${host}`,
    "vpnAlternate": `${vpnAlternate}`
  });

  var config = {
    method: 'post',
    url: `${process.env.CHATOPS_HOST}`,
    headers: { 
      'Content-Type': 'application/json'
  },
  data : data

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