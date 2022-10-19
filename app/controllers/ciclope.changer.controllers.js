const DnsUpdate = require("../utils/dns.update.js");

exports.registerUpdate = (req, res, err) => {
  let vpnName = req.body.vpnName
  let requester = req.body.requester
  let description = req.body.description

  if (vpnName == null || requester == null){
    const statusCode = res.status(400); 
    statusCode.send({
      message:
        err.message || "The fields cannot be empty.",
      statusCode:
        err.message || 400
    });
  }
  if (vpnName && requester) {
    DnsUpdate(vpnName, requester, description);
  }

  res.status(204).send();
}