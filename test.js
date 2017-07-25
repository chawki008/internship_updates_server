const { exec } = require('child_process');
exec('python weather.py > resultFile.json', (err, stdout, stderr) => {
    if (err) {
        // node couldn't execute the command
        return;
    } else {
        console.log(stdout);
    }
});