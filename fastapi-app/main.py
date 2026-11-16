from fastapi import FastAPI, Request, HTTPException
from pydantic import BaseModel
from pymongo import MongoClient
import os, requests

app = FastAPI(title="API NoSQL (vulnerable)")
mongo = MongoClient(os.getenv("MONGO_HOST", "mongo"), 27017)
db = mongo[os.getenv("MONGO_DATABASE", "tienda")]

class Login(BaseModel):
    username: str
    password: str

class Pedido(BaseModel):
    producto: str
    cantidad: int

# ----- Login VULNERABLE (NoSQLi) -----
@app.post("/login_mongo")
async def login(req: Request):
    data = await req.json()
    # ❌ acepta operadores $ en credenciales
    user = db.usuarios.find_one({"username": data.get("username"),
                                 "password": data.get("password")}, {"_id": 0})
    if user:
        return {"msg": "ok"}
    raise HTTPException(status_code=401, detail="Bad creds")

# ----- Búsqueda ES VULNERABLE -----
@app.get("/articulos")
def art_search(q: str = "*"):
    return requests.get("http://elasticsearch:9200/articulos/_search",
                        params={"q": q}).json()

# ----- CRUD pedidos -----
@app.get("/pedidos")
def listar_pedidos():
    return list(db.pedidos.find({}, {"_id": 0}))

@app.post("/pedidos")
def crear_pedido(p: Pedido):
    db.pedidos.insert_one(p.model_dump())
    return {"msg": "creado"}

@app.put("/pedidos/{producto}")
def actualizar_pedido(producto: str, p: Pedido):
    r = db.pedidos.update_one({"producto": producto},
                              {"$set": {"cantidad": p.cantidad}})
    if r.matched_count == 0:
        raise HTTPException(status_code=404, detail="No existe")
    return {"msg": "actualizado"}

@app.delete("/pedidos/{producto}")
def borrar_pedido(producto: str):
    r = db.pedidos.delete_one({"producto": producto})
    if r.deleted_count == 0:
        raise HTTPException(status_code=404, detail="No existe")
    return {"msg": "borrado"}
