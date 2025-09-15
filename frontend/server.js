const express = require('express');
const bodyParser = require('body-parser');
const axios = require('axios');
const app = express();
const PORT = 3000;

// Set EJS as template engine
app.set('view engine', 'ejs');
app.set('views', __dirname + '/views');

// Middleware
app.use(bodyParser.urlencoded({ extended: true }));

// Render the form
app.get('/', (req, res) => {
  res.render('index');
});

// Handle form submission
app.post('/submit', async (req, res) => {
  const { itemName, itemDescription } = req.body;
  try {
    // Flask backend is reachable by its service name in Docker Compose
    const resp = await axios.post('http://backend:5000/submittodoitem', {
      itemName,
      itemDescription
    });
    res.send(`<h2>${resp.data.message}</h2><a href="/">Go Back</a>`);
  } catch (err) {
    res.send(`<h2>Error: ${err.message}</h2>`);
  }
});

app.listen(PORT, () => {
  console.log(`Frontend running at http://localhost:${PORT}`);
});

