const http = require('http');
const port = process.env.port || 5000;
const products = require('./products/products.json');
const server = http.createServer((req, res) => {
    const method = req.method;
    const url = req.url;
    if (method === 'GET' && url === '/api/products') {
        res.writeHead(200, {'Content-Type' :'application/json'});
        res.end(JSON.stringify(products));
    }
    res.writeHead(404, {'Content-Type' :'application/json'});
    res.end(JSON.stringify({message: 'Route not found'}));
});
server.listen(port, () => {console.log(`Server running on ${port}.`);});