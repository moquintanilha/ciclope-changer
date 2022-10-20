const axios = require('axios')
const dotenv = require('dotenv')
const lookup = require('../utils/utils.dns.lookup.js')
const chatOps = require('../utils/utils.chat.ops.js')
const authService = require('../utils/utils.auth.service.js')
dotenv.config();



function dnsUpdate(vpnName, requester, description) {

    if (vpnName === 'conductor') {
      var subDomain = `${process.env.CONDUCTOR_SUBDOMAIN}`
      var recordId = `${process.env.CODUCTOR_RECORD_ID}`
      let host = `${process.env.VPN_CONDUCTOR_HOST}`
      let string = JSON.stringify(`${process.env.VPN_CONDUCTOR_ALTERNATE}`)
      const alternateHosts = JSON.parse("[" + string + "]")
      const alternateHostsParser = alternateHosts[0].split(',')
      const vpnLocation = lookup(host)
      let randomIndex = vpnLocation
      while(randomIndex === vpnLocation){
        randomIndex = alternateHostsParser[Math.floor(Math.random() * alternateHostsParser.length)];
      }
      var vpnAlternate = randomIndex;
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
    })
    let clientId = `${process.env.CLIENT_ID}`
    let secret = `${process.env.SECRET}`
    let token = authService(clientId, secret)
    let config = {
      method: 'patch',
      url: `https://${process.env.CDC_HOST}/domains/${process.env.DOMAIN}/subdomains/${subDomain}/records/${recordId}`,
      headers: {
        'x-auth-token': token,
        'Content-Type': 'application/json',
        'cache-control': 'no-cache'
      },
      data : data
    };
      
    axios(config)
      .then(function (response) {
      console.log(JSON.stringify(response.data))
    })
      .catch(function (error) {
      console.log(error);
    });
    chatOps(vpnName, vpnAlternate)
}

module.exports = dnsUpdate