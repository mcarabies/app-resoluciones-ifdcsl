from sqlalchemy import MetaData, Table, Column, Integer, String, DateTime, ForeignKey, create_engine, insert

metadata = MetaData()

profesorados = Table("profesorados",metadata,
                    Column("profesorado_id", Integer(), primary_key=True, autoincrement=True),
                    Column("nombre", String(40))
                    )

organismos = Table("organismos",metadata,
                    Column("organismo_id", Integer(), primary_key=True, autoincrement=True),
                    Column("nombre", String(40))
                    )

instrumentos = Table("instrumentos",metadata,
                    Column("instrumento_id", Integer(), primary_key=True, autoincrement=True),
                    Column("nombre", String(40), unique=True, nullable=True)
                    )

materias = Table("materias",metadata,
                    Column("materia_id", Integer(), primary_key=True, autoincrement=True),
                    Column("nombre", String(120))
                    )

#Relaciones
planes = Table("planes",metadata,
                    Column("plan_id", Integer(), primary_key=True, autoincrement=True),
                    Column("instrumento_id", ForeignKey("instrumentos.instrumento_id")),
                    Column("numero", Integer()),
                    Column("organismo_id", ForeignKey("organismos.organismo_id")),
                    Column("año", Integer()),
                    Column("profesorado_id", ForeignKey("profesorados.profesorado_id")),
                    Column("link", String(150))
                    )

materias_planes = Table("materias_planes", metadata,
                    Column("materia_plan_id", Integer(), primary_key=True, autoincrement=True),
                    Column("materia_id", ForeignKey("materias.materia_id")),
                    Column("plan_id", ForeignKey("planes.plan_id")),
                    )

#creacion del motor
engine = create_engine("sqlite:///C:\\Users\\mcara\\Desktop\\resoluciones_app\\resoluciones.db")
connection = engine.connect()
metadata.drop_all(engine)
metadata.create_all(engine)
connection.close()