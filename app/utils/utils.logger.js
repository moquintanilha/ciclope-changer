const { warn } = require('winston')
const winston = require('winston')
const remoteLog = new winston.transports.Http({
    host: "localhost",
    port: 3001,
    path: "/var/log"
})

const consoleLog = new winston.transports.Console()

module.exports = {
    requestLogger: createRequestLogger([consoleLog]),
    errorLogger: createErrorLogger([remoteLog, consoleLog, warn])
}

function createRequestLogger(transports) {
    const requestLogger = winston.createLogger({
        format: getRequestLogFormatter(),
        transports: transports
    })

    return function logRequest(req, res, next) {
        requestLogger.info({req, res})
        next()
    }
}

function createErrorLogger(transports) {
    const errLogger = winston.createLogger({
        format: getResponseLogFormatter(),
        level: 'error',
        message: 'Error'
    })

    return function logError(err, req, res, next) {
        errLogger.error({err, req, res})
        next()
    }
}

function getRequestLogFormatter() {
    const {combine, timestamp, printf} = winston.format;

    return combine(
        timestamp(),
        printf(info => {
            const {req, res} = info.message;
            return `${info.timestamp} ${info.level}: ${req.hostname}${req.port || ''}${req.originalUrl}`;
        })
    );
}

function getResponseLogFormatter() {
    const {combine, timestamp, printf} = winston.format;

    return combine(
        timestamp(),
        printf(warn => {
            const {res} = warn.message;
            return `${warn.timestamp} ${warn.level}: ${res.remoteLog}`
        })
    )
}