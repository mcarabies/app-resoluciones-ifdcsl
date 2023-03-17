import sqlite3
import os
from flet import Page, UserControl, Column, TextField, ElevatedButton, DataTable, DataColumn, DataRow, DataCell, Text, ListView, Row

# CONEXION A LA BASE DE DATOS
BASE_DIR = os.getcwd()
DB_PATH = os.path.join(BASE_DIR, "resoluciones.db")
conn = sqlite3.connect(DB_PATH, check_same_thread=False)
cur = conn.cursor()



class Profesorados(UserControl):
    def __init__(self):
        super().__init__()
        # VARIABLES DE DATOS
        self.tabla = DataTable(
            columns=[
                DataColumn(Text("ID")),
                DataColumn(Text("PROFESORADO"))
            ],
            rows=[
                
            ]
        )
        self.todos_los_profesorados = ListView(
            controls=[
                self.tabla
                ],
            auto_scroll=True
            ) 
        
        self.agregar_profesorado = TextField(label="Agregar Profesorado")
            
        self.agregarBoton = ElevatedButton("Agregar Profesorado",on_click=self.agregarProfesorado, bgcolor="blue", color="white" )
        self.editarBoton = ElevatedButton("Editar Profesorado",on_click=self.editarProfesorado, bgcolor="orange", color="white" )
        self.eliminarBoton = ElevatedButton("Eliminar Profesorado",on_click=self.eliminarProfesorado, bgcolor="red", color="white" )
    
    def editarProfesorado(self, e):
        pass
    
    def eliminarProfesorado(e):
        pass
    
    
    def mostrarProfesorados(self):
        cur.execute("SELECT * from profesorados")
        conn.commit()
        profesorados_guardados = cur.fetchall()
        for profesorado in profesorados_guardados:
            self.tabla.rows.append(
                    DataRow(
                          cells=[
                              DataCell(Text(profesorado[0])),
                              DataCell(Text(profesorado[1])),
                          ] 
                       ) )
        self.update()
    
    # MANTIENE LA INFORMACIÓN CONTENIDA EN PANTALLA SIEMPRE DEBE SER did_mount
    def did_mount(self):
        self.mostrarProfesorados()
    
    def agregarProfesorado(self, e):
        cur.execute("INSERT INTO profesorados (nombre) VALUES (?)", [self.agregar_profesorado.value])
        conn.commit()
        #borrar datos antiguaos y volver a leer
        self.agregar_profesorado.value = None
        self.tabla.rows.clear()
        self.mostrarProfesorados()
        self.page.update()

    
    #ARMA TODO LO DE LA CLASE SIEMPRE DEBE SER build
    def build(self):
        return Column([
            Text("PROFESORADOS ACTIVOS", size=30),
            self.agregar_profesorado,            
            Row([self.agregarBoton, self.editarBoton, self.eliminarBoton]),
            self.todos_los_profesorados

            
        ])