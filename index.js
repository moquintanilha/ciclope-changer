const Logger = require("./app/utils/utils.logger.js");
const express = require("express");
const http = require('http');
const path = require('path');
const swaggerUi = require('swagger-ui-express');
const swaggerFile = require('./docs/specs/swagger_output.json');
const app = express();

app.use(express.json());
app.use(express.urlencoded({ extended: true }));
app.use(Logger.requestLogger);
app.use(Logger.errorLogger);

app.get('/health-check', function (req, res) {
  
  res.status(200).send({
    message:
      res.message || "UP"
    });
});

app.get('/guide/',function(req,res){
  res.sendFile(path.join(__dirname+'/docs/guide/index.html'));
  //__dirname : It will resolve to your project folder.
});

require('./app/routers/ciclope.changer.routers.js')(app)
/* istanbul ignore if */
if (!module.parent) {
  http.createServer(app).listen(3001)
  console.log("Listening at http://localhost:%s (HTTP)", 3001)
  app.use('/specs', swaggerUi.serve, swaggerUi.setup(swaggerFile))
  const server = app.listen(8080, function () {
    const port = server.address().port;
    console.log('App listening at http://localhost:%s', port);
  });
}

module.exports = app;
