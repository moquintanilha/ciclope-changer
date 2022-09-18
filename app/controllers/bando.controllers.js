const DnsUpdate = require("../utils/dns.update.js");
const SendMsg = require("../utils/utils.chat.ops.js")

exports.registerUpdate = (req, res, err) => {
  const host = req.body.host;
  const vpnAlternate = req.body.vpnAlternate;

  if (host == null || vpnAlternate == null){
    const statusCode = res.status(400); 
    statusCode.send({
      message:
        err.message || "The fields cannot be empty.",
      statusCode:
        err.message || 400
    });
  }
  else 
    DnsUpdate(host, vpnAlternate);
    SendMsg(host, vpnAlternate);

  res.status(204).send();
}