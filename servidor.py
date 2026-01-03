from http.server import BaseHTTPRequestHandler, HTTPServer
import json
from datetime import datetime
import sys
import platform

class Servidor(BaseHTTPRequestHandler):
    """Servidor HTTP básico con múltiples endpoints"""
    
    def _enviar_respuesta(self, codigo, contenido, tipo="text/html"):
        """Método auxiliar para enviar respuestas HTTP"""
        self.send_response(codigo)
        self.send_header("Content-type", tipo)
        self.send_header("Access-Control-Allow-Origin", "*")
        self.end_headers()
        if isinstance(contenido, str):
            contenido = contenido.encode('utf-8')
        self.wfile.write(contenido)
    
    def _enviar_json(self, datos, codigo=200):
        """Método auxiliar para enviar respuestas JSON"""
        self._enviar_respuesta(codigo, json.dumps(datos, indent=2, ensure_ascii=False), "application/json")
    
    def log_message(self, format, *args):
        """Personalizar el formato del log"""
        print(f"[{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}] {args[0]}")
    
    def do_GET(self):
        """Manejar peticiones GET"""
        
        # Página de inicio
        if self.path == "/":
            html = """
            <!DOCTYPE html>
            <html lang="es">
            <head>
                <meta charset="UTF-8">
                <meta name="viewport" content="width=device-width, initial-scale=1.0">
                <title>Eva - Servidor Python</title>
                <style>
                    * { margin: 0; padding: 0; box-sizing: border-box; }
                    body {
                        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
                        background: linear-gradient(135deg, #3776AB 0%, #FFD43B 100%);
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
                        color: #FFD43B;
                        text-decoration: none;
                        display: block;
                        padding: 8px 0;
                        transition: transform 0.2s;
                    }
                    .endpoints a:hover { transform: translateX(10px); }
                    .badge {
                        background: #3776AB;
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
                    <h1>🐍 Eva Server</h1>
                    <p>Servidor web en Python</p>
                    <span class="badge">Python {}</span>
                    <div class="endpoints">
                        <h3>📡 Endpoints Disponibles:</h3>
                        <a href="/api/info">📊 /api/info - Información del servidor</a>
                        <a href="/api/health">💚 /api/health - Estado de salud</a>
                        <a href="/api/tiempo">🕐 /api/tiempo - Fecha y hora actual</a>
                    </div>
                </div>
            </body>
            </html>
            """.format(platform.python_version())
            self._enviar_respuesta(200, html)
        
        # API: Información del servidor
        elif self.path == "/api/info":
            info = {
                "nombre": "Eva Server",
                "version": "1.0.0",
                "descripcion": "Servidor web educativo con Python",
                "tecnologias": ["Python", "http.server"],
                "python_version": platform.python_version(),
                "autor": "Javier Quiñan",
                "repositorio": "https://github.com/JavierQuinan/Eva"
            }
            self._enviar_json(info)
        
        # API: Health check
        elif self.path == "/api/health":
            health = {
                "status": "OK",
                "timestamp": datetime.now().isoformat(),
                "plataforma": platform.system(),
                "arquitectura": platform.architecture()[0],
                "python_version": platform.python_version()
            }
            self._enviar_json(health)
        
        # API: Tiempo actual
        elif self.path == "/api/tiempo":
            ahora = datetime.now()
            tiempo = {
                "fecha": ahora.strftime("%d/%m/%Y"),
                "hora": ahora.strftime("%H:%M:%S"),
                "timestamp": int(ahora.timestamp()),
                "dia_semana": ahora.strftime("%A"),
                "iso": ahora.isoformat()
            }
            self._enviar_json(tiempo)
        
        # Ruta no encontrada
        else:
            error = {
                "error": "Ruta no encontrada",
                "mensaje": f"La ruta {self.path} no existe",
                "rutas_disponibles": ["/", "/api/info", "/api/health", "/api/tiempo"]
            }
            self._enviar_json(error, 404)


def main():
    """Función principal para iniciar el servidor"""
    host = 'localhost'
    puerto = 8000
    
    servidor = HTTPServer((host, puerto), Servidor)
    
    print("""
    ╔═══════════════════════════════════════════╗
    ║       🐍 Eva Server - Python              ║
    ╠═══════════════════════════════════════════╣
    ║  Servidor iniciado correctamente          ║
    ║  URL: http://{}:{}              ║
    ║                                           ║
    ║  Endpoints disponibles:                   ║
    ║  • GET /                                  ║
    ║  • GET /api/info                          ║
    ║  • GET /api/health                        ║
    ║  • GET /api/tiempo                        ║
    ╚═══════════════════════════════════════════╝
    """.format(host, puerto))
    
    try:
        servidor.serve_forever()
    except KeyboardInterrupt:
        print("\n🛑 Servidor detenido")
        servidor.server_close()
        sys.exit(0)


if __name__ == "__main__":
    main()
    