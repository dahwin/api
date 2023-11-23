const axios = require('axios');

// Define the URL of your FastAPI application
const url = 'http://127.0.0.1:8000/name';

// Define the data you want to post as an object
const data = [2, 1, 4];

// Send a POST request
axios.post(url, data)
  .then(response => {
    // Format the response content
    const formattedResponse = JSON.stringify(response.data);
    console.log("Raw Response Content:", formattedResponse);
  })
  .catch(error => {
    // Handle errors
    console.error("Error:", error);
  });

