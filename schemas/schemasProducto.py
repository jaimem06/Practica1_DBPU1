
schemaProducto = {
    "type": "object",
    'properties': {
        "nombre": {"type": "string"},
        "fecha_caducidad": {"type": "string"},
        "cantidad": {"type": "integer"},
        "precio_unitario": {"type": "number"},
        "nombre_lote": {"type": "string"}
    },
    'required': ["nombre", "fecha_caducidad", "cantidad", "precio_unitario", "nombre_lote"],
}