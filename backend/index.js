const express = require('express');
const cors = require('cors');
const multer = require('multer');
const { spawn } = require('child_process');

const app = express();
app.use(cors());

const upload = multer({ dest: 'uploads/' });

app.post('/upload', upload.single('file'), (req, res) => {
  const python = spawn('/Users/devendersingh/miniforge3/envs/test_env/bin/python', ['chi_squared_test.py', req.file.path]);

  let dataToSend = '';

  python.stdout.on('data', (data) => {
    dataToSend += data.toString();
  });

  python.stderr.on('data', (data) => {
    console.error(`stderr: ${data}`);
  });

  python.on('close', (code) => {
    console.log(`child process exited with code ${code}`);
    if (!dataToSend) {
      return res.status(500).send({ error: 'No data returned from Python script' });
    }

    try {
      const parsedData = JSON.parse(dataToSend);
      res.send(parsedData);
    } catch (error) {
      console.error('Error parsing JSON:', error);
      res.status(500).send({ error: 'Failed to parse JSON' });
    }
  });
});

app.listen(5001, () => {
  console.log('Server is running on port 5001');
}); 
