db = db.getSiblingDB("tienda");

db.usuarios.insertMany([
  { username: "alice", password: "alice123" },
  { username: "bob",   password: "bob123" }
]);

db.pedidos.insertMany([
  { producto: "Teclado", cantidad: 2 },
  { producto: "Raton",   cantidad: 1 },
  { producto: "Monitor", cantidad: 3 }
]);

db.createUser({
  user: "appuser",
  pwd: "apppass",
  roles: [{ role: "readWrite", db: "tienda" }]
});
