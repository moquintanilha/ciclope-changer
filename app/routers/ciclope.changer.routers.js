module.exports = app => {
  const changer = require("../controllers/ciclope.changer.controllers.js");
  let router = require("express").Router();

  router.patch("/", changer.registerUpdate);
  
  app.use('/api/action', router);
};