const DnsUpdate = require("../utils/dns.update.js");
const SendMsg = require("../utils/utils.chat.ops.js")

exports.registerUpdate = (req, res, err) => {
  let vpnName = req.body.vpnName
  let recordId = req.body.recordId
  let vpnAlternate = req.body.vpnAlternate
  let subDomain = req.body.subDomain
  let requester = req.body.requester
  let description = req.body.description

  if (recordId == null || vpnAlternate == null){
    const statusCode = res.status(400); 
    statusCode.send({
      message:
        err.message || "The fields cannot be empty.",
      statusCode:
        err.message || 400
    });
  }
  if (recordId && vpnAlternate) {
    DnsUpdate(recordId, vpnAlternate, requester, subDomain, description);
    SendMsg(vpnName, vpnAlternate);
  }

  res.status(204).send();
}