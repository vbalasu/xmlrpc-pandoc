var xmlrpc = require('xmlrpc')
var client = xmlrpc.createClient({ host: '54.209.175.70', port: 8001, path: '/RPC2'})
  client.methodCall('run_pandoc', ['markdown', 'docx', new Buffer([65, 66, 67, 68])], function (error, value) {
    console.log(value)
  })
