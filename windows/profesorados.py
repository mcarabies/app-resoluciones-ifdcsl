import sqlite3
import os
from flet import Page, UserControl, Column, TextField, ElevatedButton, ListTile, Text

BASE_DIR = os.getcwd()
print(f"Directorio Encontrado: {BASE_DIR}")
DB_PATH = os.path.join(BASE_DIR, "resoluciones.db")
conn = sqlite3.connect(DB_PATH, check_same_thread=False)
cur = conn.cursor()

class Profesorados(UserControl):
    def __init__(self):
        super().__init__()
        self.todos_los_profesorados = Column()
        self.agregar_profesorado = TextField(label="Agregar Profesorado")
        self.editar_profesorado = TextField(label="Editar Profesorado")
    
    def mostrarProfesorados(self):
        cur.execute("SELECT * from profesorados")
        conn.commit()
        profesorados_guardados = cur.fetchall()
        for profesorado in profesorados_guardados:
            self.todos_los_profesorados.controls.append(Text(f"{profesorado}"))
        self.update()
    
    def agregarProfesorado(self, e):
        cur.execute("INSERT INTO profesorados (nombre) VALUES (?)", [self.agregar_profesorado.value])
        conn.commit()
        print("Profesorado agregado ...")
        
    def build(self):
        return Column([
            self.agregar_profesorado,
            ElevatedButton("Agregar Profesorado", on_click=self.agregarProfesorado)
            
        ])