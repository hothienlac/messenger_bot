const axios = require('axios');


module.exports = (message, recipient) => {
  const body = {
    "messaging_type": "RESPONSE",
    "recipient": {
      "id": recipient,
    },
    "message": {
      "text": message,
    },
  };

  axios.post(`https://graph.facebook.com/v12.0/me/messages?access_token=${process.env.PAGE_ACCESS_TOKEN}}`, body)
  .then(function (response) {
    console.log(response);
  })
  .catch(function (error) {
    console.log(error);
  });
}