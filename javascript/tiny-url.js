// Node.js Buffer will be used to handle character encoding
var encode = function(longUrl) {
  return new Buffer(longUrl).toString('base64');
};

var decode = function(shortUrl) {
  return new Buffer(shortUrl, 'base64').toString('ascii');
};
