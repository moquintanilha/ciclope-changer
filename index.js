const Logger = require("./app/utils/utils.logger.js");

if (process.env.NODE_ENV === 'production') {
  /* istanbul ignore next */
  require('newrelic');
}

const express = require("express");
const http = require('http')
const cors = require("cors");
const app = express();
var corsOptions = {
  "Origin": "http://localhost:7072",
};
const swaggerUi = require('swagger-ui-express');
const swaggerFile = require('./swagger_output.json');

app.use(cors(corsOptions));
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


require('./app/routers/ciclope.changer.routers.js')(app)
/* istanbul ignore if */
if (!module.parent) {
  http.createServer(app).listen(3000)
  console.log("Listening at http://localhost:%s (HTTP)", 3000)
  app.use('/doc', swaggerUi.serve, swaggerUi.setup(swaggerFile))

  const server = app.listen(8080, function () {
    const port = server.address().port;
    console.log('App listening at http://localhost:%s', port);
  });
}

module.exports = app;
