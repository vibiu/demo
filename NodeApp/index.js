var server = require('./server');
var router = require('./router');
var requestHanders = require('./requestHandlers');

var handle = {};
handle['/'] = requestHanders.start;
handle['/start'] = requestHanders.start;
handle['/upload'] = requestHanders.upload;
handle['/show'] = requestHanders.show;

server.start(router.route, handle);
