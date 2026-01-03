# DualServer - Servidor Web Educativo

<div align="center">

![Node.js](https://img.shields.io/badge/Node.js-339933?style=for-the-badge&logo=nodedotjs&logoColor=white)
![Express.js](https://img.shields.io/badge/Express.js-000000?style=for-the-badge&logo=express&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black)

[![GitHub](https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white)](https://github.com/JavierQuinan/Eva)

**Un proyecto educativo que demuestra cómo crear servidores web tanto en Node.js como en Python**

</div>

---

## Tabla de Contenidos

- [Descripcion](#descripcion)
- [Caracteristicas](#caracteristicas)
- [Tecnologias Usadas](#tecnologias-usadas)
- [Requisitos Previos](#requisitos-previos)
- [Instalacion](#instalacion)
- [Uso](#uso)
- [Endpoints API](#endpoints-api)
- [Estructura del Proyecto](#estructura-del-proyecto)
- [Contribuir](#contribuir)
- [Licencia](#licencia)

---

## Descripcion

**DualServer** es un proyecto educativo que implementa servidores web basicos en dos lenguajes de programacion diferentes:
- **Node.js** con Express.js
- **Python** con el modulo `http.server`

Este proyecto es ideal para aprender los fundamentos de desarrollo backend y comparar las implementaciones entre ambos lenguajes.

---

## Caracteristicas

- Servidor HTTP funcional en Node.js y Python
- Multiples rutas y endpoints
- API REST con respuestas JSON
- Respuestas rapidas y eficientes
- Facil de configurar y extender
- Codigo comentado y educativo

---

## Tecnologias Usadas

| Tecnologia | Version | Descripcion |
|------------|---------|-------------|
| Node.js | 18+ | Entorno de ejecucion JavaScript |
| Express | 5.1.0 | Framework web para Node.js |
| Python | 3.8+ | Lenguaje de programacion |
| npm | 9+ | Gestor de paquetes |

---

## Requisitos Previos

Antes de comenzar, asegurate de tener instalado:

### Para Node.js:
- **Node.js** (v18 o superior) - [Descargar](https://nodejs.org/)
- **npm** (incluido con Node.js)

```bash
# Verificar instalacion
node --version
npm --version
```

### Para Python:
- **Python 3** (v3.8 o superior) - [Descargar](https://python.org/)

```bash
# Verificar instalacion
python --version
```

---

## Instalacion

1. **Clonar el repositorio**
```bash
git clone https://github.com/JavierQuinan/Eva.git
cd Eva
```

2. **Instalar dependencias de Node.js**
```bash
npm install
```

---

## Uso

### Servidor Node.js (Express)

```bash
# Metodo 1: Usando npm
npm start

# Metodo 2: Directamente con node
node server.js
```

El servidor estara disponible en: `http://localhost:8000`

### Servidor Python

```bash
python servidor.py
```

El servidor estara disponible en: `http://localhost:8000`

> **Nota:** Ambos servidores usan el puerto 8000, por lo que solo puedes ejecutar uno a la vez.

---

## Endpoints API

### Servidor Node.js (Express)

| Metodo | Endpoint | Descripcion |
|--------|----------|-------------|
| `GET` | `/` | Pagina de inicio |
| `GET` | `/api/info` | Informacion del servidor |
| `GET` | `/api/health` | Estado de salud del servidor |
| `GET` | `/api/tiempo` | Fecha y hora actual |

### Servidor Python

| Metodo | Endpoint | Descripcion |
|--------|----------|-------------|
| `GET` | `/` | Pagina de inicio |
| `GET` | `/api/info` | Informacion del servidor |
| `GET` | `/api/health` | Estado de salud del servidor |

---

## Estructura del Proyecto

```
DualServer/
├── server.js        # Servidor Node.js con Express
├── servidor.py      # Servidor Python
├── package.json     # Configuracion y dependencias npm
├── README.md        # Documentacion del proyecto
└── .gitignore       # Archivos ignorados por Git
```

---

## Contribuir

Las contribuciones son bienvenidas. Para contribuir:

1. Haz un Fork del proyecto
2. Crea una rama para tu feature (`git checkout -b feature/NuevaCaracteristica`)
3. Haz commit de tus cambios (`git commit -m 'Agregar nueva caracteristica'`)
4. Haz Push a la rama (`git push origin feature/NuevaCaracteristica`)
5. Abre un Pull Request

---

## Licencia

Este proyecto esta bajo la Licencia ISC. Ver el archivo `LICENSE` para mas detalles.

---

<div align="center">

**Si este proyecto te fue util, considera darle una estrella en GitHub**

Hecho por [Javier Quinan](https://github.com/JavierQuinan)

</div>
