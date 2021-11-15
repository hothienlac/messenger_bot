const messengerAPI = require('./messenger-api');

const handleMessage = (req, res) => {
  const body = req.body;

  if (body.object === 'page') {

    body.entry.forEach((entry) => {
      const webhook_event = entry.messaging[0];
      messengerAPI(webhook_event.message.text, webhook_event.sender.id)
    });

    res.status(200).send('EVENT_RECEIVED');
  } else {
    res.sendStatus(404);
  }

};

module.exports = handleMessage