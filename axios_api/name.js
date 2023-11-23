const axios = require('axios');

// Define the URL of your FastAPI application
const url = 'http://127.0.0.1:8000/name';

// Define the data you want to post
const data = { name: 'lovely Dahyun' };

// Send a POST request
axios.post(url, data)
  .then(response => {
    // Print the response
    console.log(response.data);
  })
  .catch(error => {
    // Handle errors
    console.error("Error:", error);
  });
