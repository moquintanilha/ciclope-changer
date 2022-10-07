module.exports = app => {
  const changer = require("../controllers/ciclope.changer.controllers.js");
  let router = require("express").Router();

  router.patch("/", changer.registerUpdate);
  
  app.use('/api/action', router);
  /*
    #swagger.tags = ['Action']
    #swagger.description = 'Endpoint to change an FQDN associated with a VPN.' */
  /*
    #swagger.parameters['action'] = {
               in: 'body',
               description: 'Send a request to DNS service.',
               required: true,
               schema: { $ref: "#/definitions/Action" }
        }
   */
};