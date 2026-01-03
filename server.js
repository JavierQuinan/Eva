const express = require("express");
const app = express();
const port = 8000;

// Middleware para parsear JSON
app.use(express.json());

// Middleware para logging de requests
app.use((req, res, next) => {
  console.log(`[${new Date().toISOString()}] ${req.method} ${req.path}`);
  next();
});

// =====================
// RUTAS PRINCIPALES
// =====================

// Página de inicio
app.get("/", (req, res) => {
  res.send(`
    <!DOCTYPE html>
    <html lang="es">
    <head>
      <meta charset="UTF-8">
      <meta name="viewport" content="width=device-width, initial-scale=1.0">
      <title>Eva - Servidor Node.js</title>
      <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body {
          font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
          background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
          min-height: 100vh;
          display: flex;
          justify-content: center;
          align-items: center;
          color: white;
        }
        .container {
          text-align: center;
          padding: 40px;
          background: rgba(255,255,255,0.1);
          border-radius: 20px;
          backdrop-filter: blur(10px);
          box-shadow: 0 8px 32px rgba(0,0,0,0.3);
        }
        h1 { font-size: 2.5rem; margin-bottom: 20px; }
        p { font-size: 1.2rem; margin-bottom: 30px; opacity: 0.9; }
        .endpoints {
          text-align: left;
          background: rgba(0,0,0,0.2);
          padding: 20px;
          border-radius: 10px;
          margin-top: 20px;
        }
        .endpoints h3 { margin-bottom: 15px; }
        .endpoints a {
          color: #7df9ff;
          text-decoration: none;
          display: block;
          padding: 8px 0;
          transition: transform 0.2s;
        }
        .endpoints a:hover { transform: translateX(10px); }
        .badge {
          background: #339933;
          padding: 5px 15px;
          border-radius: 20px;
          font-size: 0.9rem;
          display: inline-block;
          margin-top: 20px;
        }
      </style>
    </head>
    <body>
      <div class="container">
        <h1>🖥️ Eva Server</h1>
        <p>Servidor web en Node.js con Express</p>
        <span class="badge">Express v5.1.0</span>
        <div class="endpoints">
          <h3>📡 Endpoints Disponibles:</h3>
          <a href="/api/info">📊 /api/info - Información del servidor</a>
          <a href="/api/health">💚 /api/health - Estado de salud</a>
          <a href="/api/tiempo">🕐 /api/tiempo - Fecha y hora actual</a>
        </div>
      </div>
    </body>
    </html>
  `);
});

// =====================
// API ENDPOINTS
// =====================

// Información del servidor
app.get("/api/info", (req, res) => {
  res.json({
    nombre: "Eva Server",
    version: "1.0.0",
    descripcion: "Servidor web educativo con Node.js y Express",
    tecnologias: ["Node.js", "Express.js", "JavaScript"],
    autor: "Javier Quiñan",
    repositorio: "https://github.com/JavierQuinan/Eva"
  });
});

// Health check
app.get("/api/health", (req, res) => {
  res.json({
    status: "OK",
    uptime: process.uptime(),
    timestamp: new Date().toISOString(),
    memoria: {
      usada: `${Math.round(process.memoryUsage().heapUsed / 1024 / 1024)} MB`,
      total: `${Math.round(process.memoryUsage().heapTotal / 1024 / 1024)} MB`
    }
  });
});

// Endpoint de tiempo
app.get("/api/tiempo", (req, res) => {
  const ahora = new Date();
  res.json({
    fecha: ahora.toLocaleDateString("es-ES"),
    hora: ahora.toLocaleTimeString("es-ES"),
    timestamp: ahora.getTime(),
    zona_horaria: Intl.DateTimeFormat().resolvedOptions().timeZone
  });
});

// =====================
// MANEJO DE ERRORES
// =====================

// Ruta 404
app.use((req, res) => {
  res.status(404).json({
    error: "Ruta no encontrada",
    mensaje: `La ruta ${req.path} no existe`,
    rutas_disponibles: ["/", "/api/info", "/api/health", "/api/tiempo"]
  });
});

// Manejador de errores global
app.use((err, req, res, next) => {
  console.error("Error:", err.message);
  res.status(500).json({
    error: "Error interno del servidor",
    mensaje: err.message
  });
});

// =====================
// INICIAR SERVIDOR
// =====================
app.listen(port, () => {
  console.log(`
  ╔═══════════════════════════════════════════╗
  ║     🖥️  Eva Server - Node.js + Express     ║
  ╠═══════════════════════════════════════════╣
  ║  Servidor iniciado correctamente          ║
  ║  URL: http://localhost:${port}              ║
  ║                                           ║
  ║  Endpoints disponibles:                   ║
  ║  • GET /                                  ║
  ║  • GET /api/info                          ║
  ║  • GET /api/health                        ║
  ║  • GET /api/tiempo                        ║
  ╚═══════════════════════════════════════════╝
  `);
});
