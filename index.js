const Logger = require("./app/utils/utils.logger.js");

if (process.env.NODE_ENV === 'production') {
  /* istanbul ignore next */
  require('newrelic');
}

const express = require("express");
const cors = require("cors");
const app = express();
var corsOptions = {
  "Origin": "http://localhost:7072",
};

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


require('./app/routers/ciclople.changer.routers.js')(app)
/* istanbul ignore if */
if (!module.parent) {
  const server = app.listen(8080, function () {
    const port = server.address().port;
    console.log('App listening at http://localhost:%s', port);
  });
}

module.exports = app;
