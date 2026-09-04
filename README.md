# DualServer / Eva — Node.js + Python HTTP foundations

> **CONSOLIDATED / HISTORICAL SOURCE**

## ES

Este repositorio se conserva temporalmente como fuente histórica del ejercicio DualServer. La parte útil ya fue curada y refactorizada dentro de:

`JavierQuinan/Proyectos` → `foundations/http/`

La versión consolidada conserva la comparación entre un servidor Node.js/Express y uno Python `http.server`, pero elimina HTML de presentación innecesario, acoplamiento con nombres del repo original y CORS wildcard. También mejora testabilidad, timestamps y binding local por defecto.

Este repositorio ya no debe recibir nuevas features ni utilizarse como evidencia principal del portfolio. Su siguiente estado recomendado es **archivado** y, después de conservar el snapshot necesario, puede evaluarse su eliminación definitiva.

### Qué se preservó

- endpoints HTTP equivalentes;
- health/info JSON;
- logging de requests;
- manejo 404;
- comparación framework vs librería estándar.

### Qué se refactorizó

- Node.js expone `createApp()` para facilitar pruebas;
- Python utiliza `ThreadingHTTPServer`;
- timestamps UTC;
- binding a `127.0.0.1` por defecto;
- eliminación de CORS permisivo no necesario;
- eliminación de UI inline para concentrar el ejemplo en fundamentos HTTP.

Destino consolidado:
https://github.com/JavierQuinan/Proyectos/tree/main/foundations/http

---

## EN

This repository is temporarily preserved as the historical source for the DualServer exercise. The useful material has already been curated and refactored into:

`JavierQuinan/Proyectos` → `foundations/http/`

The consolidated version preserves the comparison between a Node.js/Express server and Python `http.server`, while removing unnecessary presentation HTML, coupling to original repository names and wildcard CORS. It also improves testability, timestamps and local-only binding defaults.

This repository should no longer receive new features or be used as primary portfolio evidence. Its recommended next state is **archived**, and after the required snapshot is preserved it can be evaluated for final deletion.

### Preserved

- equivalent HTTP endpoints;
- JSON health/info responses;
- request logging;
- 404 handling;
- framework vs standard-library comparison.

### Refactored

- Node.js exports `createApp()` for testability;
- Python uses `ThreadingHTTPServer`;
- UTC timestamps;
- loopback binding by default;
- unnecessary permissive CORS removed;
- inline UI removed to keep the example focused on HTTP fundamentals.

Consolidated destination:
https://github.com/JavierQuinan/Proyectos/tree/main/foundations/http

## License

ISC — see `LICENSE`.
