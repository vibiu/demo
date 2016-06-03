function route(handler, pathname, response, request) {
    console.log('About to route a request for ' + pathname);
    if (typeof handler[pathname] === 'function') {
        // return handler[pathname]();
        handler[pathname](response, request);
    } else {
        console.log('No request handler found for ' + pathname);
        // return "404 Not Found."
        response.writeHead(404, {"Content-Type": "text-plain"});
        response.write("404 Not found");
        response.end()
    }
}

exports.route = route;
