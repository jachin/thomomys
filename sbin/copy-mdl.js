var copy = require('copy-files');

copy({
  files: {
    'material.min.css': __dirname + '/node_modules/material-design-lite/dist/material.min.css'
  },
  dest: '/static/css/',
}, function (err) {

});
