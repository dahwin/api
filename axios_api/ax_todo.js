//create

// const axios = require('axios');

// const url = 'http://127.0.0.1:8000/api/todo';
// const headers = {
//   'accept': 'application/json',
//   'Content-Type': 'application/json'
// };
// const data = {
//   title: 'dubusu',
//   description: 'she is my everything best girl'
// };

// axios.post(url, data, { headers })
//   .then(response => {
//     console.log(response.data);
//   })
//   .catch(error => {
//     console.error('Error:', error.message);
//   });


//read

// const axios = require('axios');

// const url = 'http://127.0.0.1:8000/api/todo';
// const headers = {
//   'accept': 'application/json'
// };

// axios.get(url, { headers })
//   .then(response => {
//     console.log(response.data);
//   })
//   .catch(error => {
//     console.error('Error:', error.message);
//   });


//update

// const axios = require('axios');
// const name = "dubu";

// const url = `http://127.0.0.1:8000/api/todo${name}`;
// console.log(url);
// const headers = { 'accept': 'application/json' };
// const params = { 'desc': 'dublangdungi' };

// // Send a PUT request
// axios.put(url, {}, { headers, params })
//   .then(response => {
//     // Print the response
//     console.log(response.data);
//   })
//   .catch(error => {
//     // Handle errors
//     console.error("Error:", error);
//   });


//Delete
const axios = require('axios');

const todo = 'dubu';
const url = `http://127.0.0.1:8000/api/todo/${todo}`;
console.log(url)
const headers = { 'accept': 'application/json' };

axios.delete(url, { headers })
  .then(response => {
    // Print the response content
    console.log(response.data);
  })
  .catch(error => {
    // Handle error
    console.error(error);
  });
