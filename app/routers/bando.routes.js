module.exports = app => {
  const bando = require("../controllers/bando.controllers.js");
  let router = require("express").Router();

  router.patch("/", bando.registerUpdate);
  
  app.use('/api/action', router);
};