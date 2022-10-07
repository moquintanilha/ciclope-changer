const axios = require('axios');
const dotenv = require('dotenv');
dotenv.config();



function dnsUpdate(recordId, vpnAlternate, subDomain, description, requester) {
    let data = JSON.stringify({
      "ttl": `${process.env.TTL}`,
      "record_type": `${process.env.RECORD_TYPE}`,
      "description": `${description}`,
      "requester": `${requester}`,
      "destination": {
        "value": `${vpnAlternate}`,
        "type": `${process.env.TYPE}`
      },
      "status": "TO_UPDATE",
      "provider_name": `${process.env.PROVIDER_NAME}`
    });
      
      let config = {
        method: 'patch',
        url: `https://${process.env.CDC_HOST}/domains/${process.env.DOMAIN}/subdomains/${subDomain}/records/${recordId}`,
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