const express = require("express");
const app = express();
const port = 8000;

app.get("/", (req, res) => {
  res.send("<h1>Hola, este es mi servidor web en Node.js con express!</h1>!");
});

app.listen( port, () => {
  console.log(`Servidor iniciado en http://localhost:${port}`);
});
