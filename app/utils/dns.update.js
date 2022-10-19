const axios = require('axios');
const dotenv = require('dotenv');
const chatOps = require('../utils/utils.chat.ops.js')
dotenv.config();



function dnsUpdate(vpnName, requester, description) {
    if (vpnName === 'conductor'){
      var subDomain = `${process.env.CONDUCTOR_SUBDOMAIN}`
      var recordId = `${process.env.CODUCTOR_RECORD_ID}`
      let string = JSON.stringify(`${process.env.VPN_CONDUCTOR_ALTERNATE}`)
      let alternateHosts = JSON.parse("[" + string + "]")
      let alternateHostsParser = alternateHosts[0].split(',')
      var vpnAlternate = alternateHostsParser[Math.floor(Math.random() * alternateHostsParser.length)]
    }
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
      chatOps(vpnName, vpnAlternate)
}

module.exports = dnsUpdate;