import sqlite3
import os
from flet import Page, UserControl, Column, TextField, ElevatedButton, DataTable, DataColumn, DataRow, DataCell, Text, ListView, Row

# CONEXION A LA BASE DE DATOS
BASE_DIR = os.getcwd()
DB_PATH = os.path.join(BASE_DIR, "resoluciones.db")
conn = sqlite3.connect(DB_PATH, check_same_thread=False)
cur = conn.cursor()



class Instrumentos(UserControl):
    def __init__(self):
        super().__init__()
        # VARIABLES DE DATOS
        self.id_instrumento = None
        self.tabla = DataTable(
            columns=[
                DataColumn(Text("ID")),
                DataColumn(Text("INSTRUMENTO")),              
            ],
            rows=[
                
            ],
            

        )
        self.todos_los_instrumentos = ListView(
            controls=[
                self.tabla
                ],
            auto_scroll=True
            ) 
        
        self.agregar_instrumento = TextField(label="Agregar Instrumento")
            
        self.agregarBoton = ElevatedButton("Agregar Instrumento",on_click=self.agregarInstrumento, bgcolor="blue", color="white" )
        self.editarBoton = ElevatedButton("Editar Instrumento",on_click=self.editarInstrumento, bgcolor="orange", color="white" )
        self.eliminarBoton = ElevatedButton("Eliminar Instrumento",on_click=self.eliminarInstrumento, bgcolor="red", color="white" )
        
        self.agregarBoton.visible = True
        self.editarBoton.visible = False
        self.eliminarBoton.visible = False
    
    def editarInstrumento(self,e):
        cur.execute("UPDATE instrumentos SET (nombre)=(?) WHERE (instrumento_id)=(?)", [self.agregar_instrumento.value, self.id_instrumento])
        conn.commit()
        #borrar datos antiguaos y volver a leer
        self.agregar_instrumento.value = None
        self.tabla.rows.clear()
        self.mostrarInstrumentos()
        self.ocultarBotones()
        self.page.update()
    
    def eliminarInstrumento(self, e):
        cur.execute("DELETE FROM instrumentos WHERE instrumento_id=?", [self.id_instrumento])
        conn.commit()
        #borrar datos antiguaos y volver a leer
        self.agregar_instrumento.value = None
        self.tabla.rows.clear()
        self.mostrarInstrumentos()
        self.ocultarBotones()
        self.page.update()
    
    def mostrarBotones(self, e1, e2):
        self.agregar_instrumentos.value = e2

        self.agregarBoton.visible = False
        self.editarBoton.visible = True
        self.eliminarBoton.visible = True
        self.id_instrumento = int(e1)
        self.instrumento_a_editar = e2
        self.update()
        
    def ocultarBotones(self):
        self.agregarBoton.visible = True
        self.editarBoton.visible = False
        self.eliminarBoton.visible = False
        self.update()
        
    def mostrarInstrumentos(self):
        cur.execute("SELECT * from instrumentos")
        conn.commit()

        instrumentos_guardados = cur.fetchall()
        for instrumento in instrumentos_guardados:
            self.tabla.rows.append(
                    DataRow(
                          cells=[
                              DataCell(Text(instrumento[0])),
                              DataCell(Text(instrumento[1])),
                          ], 
                        on_select_changed=lambda e:self.mostrarBotones(e.control.cells[0].content.value, e.control.cells[1].content.value)
                       ) )
        self.update()
    
    # MANTIENE LA INFORMACIÓN CONTENIDA EN PANTALLA SIEMPRE DEBE SER did_mount
    def did_mount(self):
        self.mostrarInstrumentos()
    
    def agregarInstrumento(self, e):
        cur.execute("INSERT INTO instrumentos (nombre) VALUES (?)", [self.agregar_instrumento.value])
        conn.commit()
        #borrar datos antiguaos y volver a leer
        self.agregar_instrumento.value = None
        self.tabla.rows.clear()
        self.mostrarInstrumentos()
        self.page.update()

    
    #ARMA TODO LO DE LA CLASE SIEMPRE DEBE SER build
    def build(self):
        return Column([
            Text("INSTRUMENTOS ADMINISTRATIVOS", size=30),
            self.agregar_instrumento,            
            Row([self.agregarBoton, self.editarBoton, self.eliminarBoton]),
            self.todos_los_instrumentos

            
        ])