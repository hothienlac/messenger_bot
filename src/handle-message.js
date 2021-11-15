

const handleMessage = (req, res ) => {
  const body = req.body;

  console.log({body});

  res.status(200).send('EVENT_RECEIVED');
};

module.exports = handleMessage