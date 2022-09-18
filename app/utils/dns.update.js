const axios = require('axios');
const dotenv = require('dotenv');
dotenv.config();



function dnsUpdate(rrset, content) {
    let data = JSON.stringify({
      "ttl": null,
      "record_type": "CNAME",
      "description": "VPN switching",
      "requester": "ciclope-changer",
      "destination": {
        "value": `${content}`,
        "type": "DEVICE"
      },
      "status": "TO_UPDATE",
      "provider_name": "Amazon-Fury_Core"
    });
      
      let config = {
        method: 'patch',
        url: `https://pdc.furycloud.io/domains/mercadolibre.io/records/${rrset}`,
        headers: { 
          'x-auth-token': `${process.env.CDC_API_KEY}`, 
          'Content-Type': 'application/json',
          'cache-control': 'no-cache'
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

module.exports = dnsUpdate;