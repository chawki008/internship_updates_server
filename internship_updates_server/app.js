var express = require('express');
var path = require('path');
var favicon = require('serve-favicon');
var logger = require('morgan');
var cookieParser = require('cookie-parser');
var bodyParser = require('body-parser');
const { exec } = require('child_process');
var index = require('./routes/index');
var users = require('./routes/users');

var app = express();

// view engine setup
app.set('views', path.join(__dirname, 'views'));
app.set('view engine', 'ejs');

// uncomment after placing your favicon in /public
//app.use(favicon(path.join(__dirname, 'public', 'favicon.ico')));
app.use(logger('dev'));
app.use(bodyParser.json());
app.use(bodyParser.urlencoded({ extended: false }));
app.use(cookieParser());
app.use(express.static(path.join(__dirname, 'public')));
app.use(
    (req, res, next) => {
        console.log(req.headers);
        res.header('Access-Control-Allow-Origin', '*');
        res.header('Access-Control-Allow-Headers', ['Content-Type', 'Authorization']);
        res.header('Access-Control-Allow-Methods', ['PUT']);
        next();
    });
// app.use('/', index);
app.use('/users', users);
app.use("/offers", (req, res) => {
    exec('python ../weather.py > ../resultFile.json', (err, stdout, stderr) => {
        if (err) {
            // node couldn't execute the command
            return;
        } else {
            res.json(require("../resultFile.json"));
            // console.log(stdout);
        }
    });
})

// catch 404 and forward to error handler
app.use(function(req, res, next) {
    var err = new Error('Not Found');
    err.status = 404;
    next(err);
});

// error handler
app.use(function(err, req, res, next) {
    // set locals, only providing error in development
    res.locals.message = err.message;
    res.locals.error = req.app.get('env') === 'development' ? err : {};

    // render the error page
    res.status(err.status || 500);
    res.render('error');
});

module.exports = app;