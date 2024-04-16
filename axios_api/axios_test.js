const axios = require('axios');

const url = "http://127.0.0.1:8000/api/todo";


async function addTask(title, description) {
  try {
    const response = await axios.post(url, {
      title: title,
      description: description
    });

    if (response.status === 200) {
      console.log(`Task added successfully: ${JSON.stringify(response.data)}`);
    } else {
      console.error(`Failed to add task. Status code: ${response.status}, Error: ${response.data}`);
    }
  } catch (error) {
    console.error(`Error: ${error.message}`);
  }
}

// Usage
const title = "love52035566ed";
const description = "Love dubu dahyun666dd";

addTask(title, description);
