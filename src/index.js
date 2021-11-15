require('dotenv').config()

const express = require('express');
const cors = require('cors');
const handleMessage = require('./handle-message');
const verifyToken = require('./verify-token');

const app = express();
app.use(cors());

app.get('/', (req, res) => {
  return res.status(httpStatus.OK).json({message: 'App is working'});
});

app.use(express.urlencoded({extended: true}));
app.use(express.json());


app.get('/webhook', verifyToken);
app.post('/webhook', handleMessage);


const PORT = process.env.PORT ?? 3000;
app.listen(PORT, () => console.log(`Webhook is listening on port ${PORT}`));
