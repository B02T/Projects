const http = require('http');
const data = require('./products/products.json');

const port = process.env.PORT || 5000;
const server = http.createServer((req, res) => {
    res.writeHead(200, {'Content-Type': 'application/json'});
    res.write(JSON.stringify(products));
});
server.listen(port, () => {`Server running on port ${port}`});