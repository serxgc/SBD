#!/bin/bash
ES="http://localhost:9200"

until curl -s "$ES" > /dev/null; do
  echo "Esperando a Elasticsearch..."
  sleep 3
done

curl -s -X PUT "$ES/articulos/_doc/1?refresh=true" -H 'Content-Type: application/json' \
  -d '{"titulo":"Guia de MongoDB","contenido":"Introduccion publica a NoSQL","visibilidad":"publico"}'

curl -s -X PUT "$ES/articulos/_doc/2?refresh=true" -H 'Content-Type: application/json' \
  -d '{"titulo":"Informe interno Q3","contenido":"Datos de clientes de prueba","visibilidad":"interno"}'

curl -s -X PUT "$ES/articulos/_doc/3?refresh=true" -H 'Content-Type: application/json' \
  -d '{"titulo":"Politica de accesos","contenido":"Documento de ejemplo","visibilidad":"interno"}'
