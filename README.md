# SegBD Lab01 — Seguridad en NoSQL (MongoDB + Elasticsearch + FastAPI)

Laboratorio de la Actividad 1 de Seguridad en Bases de Datos, Blockchain y Big Data (UNIR).
Entorno deliberadamente inseguro, atacado y después defendido de forma controlada.

## Levantar el entorno
\`\`\`bash
docker-compose up -d
\`\`\`
- API: http://localhost:8000
- MongoDB: puerto 27017 (solo accesible desde localhost tras la Defensa 2)
- Elasticsearch: puerto 9200 interno (no publicado al host tras la Defensa 3)

## Estructura
- `docker-compose.yml` — orquestación de los tres servicios
- `init_mongo.js` — carga inicial de usuarios y pedidos en MongoDB
- `init_elastic.sh` — carga inicial del índice `articulos` en Elasticsearch
- `fastapi-app/` — API (Dockerfile, main.py, requirements.txt)

