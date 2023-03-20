require('express-async-errors');
const express = require('express');
const cors = require('cors');
const app = express();
const morgan = require('morgan');
const helmet = require("helmet");
const rateLimit = require("express-rate-limit");

app.post('/fail', (req, res) => {
  res.status(200).json({ greeting: `Hello, ${req.body.nome}!` });
});

app.use(morgan('dev'));
app.use(express.json());
app.use(express.static('./images'));
app.use(cors());

app.post('/hello', (req, res) => {
  // req.body agora está disponível
  res.status(200).json({ greeting: `Hello, ${req.body.nome}!` });
});

// se ninguém respondeu, vai cair neste middleware
app.use((req, res) => res.sendStatus(404));
app.use(helmet());

// Configuramos um limitador para uma taxa máxima de 100 requisições em um intervalo de 15 minutos
const limiter = rateLimit({
  max: 100, // número máximo de requisições
  windowMs: 15 * 60 * 1000, // intervalo de tempo, em milissegundos, para atingir o número máximo de requisições
  message: "Muitas requisições originadas desta IP" // mensagem personalizada quando atinge o limit rate

});


app.use(limiter);

app.listen(3001, () => { console.log('Ouvindo na porta 3001'); });