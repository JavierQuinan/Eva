# 🖥️ Eva - Servidor Web Dual

<div align="center">

![Node.js](https://img.shields.io/badge/Node.js-339933?style=for-the-badge&logo=nodedotjs&logoColor=white)
![Express.js](https://img.shields.io/badge/Express.js-000000?style=for-the-badge&logo=express&logoColor=white)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black)

[![GitHub](https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white)](https://github.com/JavierQuinan/Eva)

**Un proyecto educativo que demuestra cómo crear servidores web tanto en Node.js como en Python**

</div>

---

## 📋 Tabla de Contenidos

- [📖 Descripción](#-descripción)
- [✨ Características](#-características)
- [🛠️ Tecnologías Usadas](#️-tecnologías-usadas)
- [📦 Requisitos Previos](#-requisitos-previos)
- [🚀 Instalación](#-instalación)
- [💻 Uso](#-uso)
- [🔗 Endpoints API](#-endpoints-api)
- [📁 Estructura del Proyecto](#-estructura-del-proyecto)
- [🤝 Contribuir](#-contribuir)
- [📄 Licencia](#-licencia)

---

## 📖 Descripción

**Eva** es un proyecto educativo que implementa servidores web básicos en dos lenguajes de programación diferentes:
- **Node.js** con Express.js
- **Python** con el módulo `http.server`

Este proyecto es ideal para aprender los fundamentos de desarrollo backend y comparar las implementaciones entre ambos lenguajes.

---

## ✨ Características

- 🌐 Servidor HTTP funcional en Node.js y Python
- 🛣️ Múltiples rutas y endpoints
- 📊 API REST con respuestas JSON
- ⚡ Respuestas rápidas y eficientes
- 🔧 Fácil de configurar y extender
- 📚 Código comentado y educativo

---

## 🛠️ Tecnologías Usadas

| Tecnología | Versión | Descripción |
|------------|---------|-------------|
| ![Node.js](https://img.shields.io/badge/-Node.js-339933?style=flat&logo=nodedotjs&logoColor=white) | 18+ | Entorno de ejecución JavaScript |
| ![Express](https://img.shields.io/badge/-Express-000000?style=flat&logo=express&logoColor=white) | 5.1.0 | Framework web para Node.js |
| ![Python](https://img.shields.io/badge/-Python-3776AB?style=flat&logo=python&logoColor=white) | 3.8+ | Lenguaje de programación |
| ![npm](https://img.shields.io/badge/-npm-CB3837?style=flat&logo=npm&logoColor=white) | 9+ | Gestor de paquetes |

---

## 📦 Requisitos Previos

Antes de comenzar, asegúrate de tener instalado:

### Para Node.js:
- **Node.js** (v18 o superior) - [Descargar](https://nodejs.org/)
- **npm** (incluido con Node.js)

```bash
# Verificar instalación
node --version
npm --version
```

### Para Python:
- **Python 3** (v3.8 o superior) - [Descargar](https://python.org/)

```bash
# Verificar instalación
python --version
```

---

## 🚀 Instalación

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

## 💻 Uso

### 🟢 Servidor Node.js (Express)

```bash
# Método 1: Usando npm
npm start

# Método 2: Directamente con node
node server.js
```

El servidor estará disponible en: `http://localhost:8000`

### 🐍 Servidor Python

```bash
python servidor.py
```

El servidor estará disponible en: `http://localhost:8000`

> ⚠️ **Nota:** Ambos servidores usan el puerto 8000, por lo que solo puedes ejecutar uno a la vez.

---

## 🔗 Endpoints API

### Servidor Node.js (Express)

| Método | Endpoint | Descripción |
|--------|----------|-------------|
| `GET` | `/` | Página de inicio |
| `GET` | `/api/info` | Información del servidor |
| `GET` | `/api/health` | Estado de salud del servidor |
| `GET` | `/api/tiempo` | Fecha y hora actual |

### Servidor Python

| Método | Endpoint | Descripción |
|--------|----------|-------------|
| `GET` | `/` | Página de inicio |
| `GET` | `/api/info` | Información del servidor |
| `GET` | `/api/health` | Estado de salud del servidor |

---

## 📁 Estructura del Proyecto

```
Eva/
├── 📄 server.js        # Servidor Node.js con Express
├── 📄 servidor.py      # Servidor Python
├── 📄 package.json     # Configuración y dependencias npm
├── 📄 README.md        # Documentación del proyecto
└── 📄 .gitignore       # Archivos ignorados por Git
```

---

## 🤝 Contribuir

¡Las contribuciones son bienvenidas! Para contribuir:

1. Haz un Fork del proyecto
2. Crea una rama para tu feature (`git checkout -b feature/NuevaCaracteristica`)
3. Haz commit de tus cambios (`git commit -m 'Agregar nueva característica'`)
4. Haz Push a la rama (`git push origin feature/NuevaCaracteristica`)
5. Abre un Pull Request

---

## 📄 Licencia

Este proyecto está bajo la Licencia ISC. Ver el archivo `LICENSE` para más detalles.

---

<div align="center">

**⭐ Si este proyecto te fue útil, considera darle una estrella en GitHub ⭐**

Hecho con ❤️ por [Javier Quiñan](https://github.com/JavierQuinan)

</div>
