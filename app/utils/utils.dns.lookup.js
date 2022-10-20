var dotenv = require('dotenv')
dotenv.config()
var {Resolver} = require('dns')
const resolver = new Resolver()

resolver.setServers(['172.20.0.10'])

function lookup(name) {
    resolver.resolveCname(name, function (err, addresses, family) {
        var answer = `${addresses[0]}` + "."
        return answer
    });
}


module.exports = lookup
