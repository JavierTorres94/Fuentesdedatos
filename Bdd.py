Python 3.12.0a6 (tags/v3.12.0a6:f9774e5, Mar  7 2023, 23:52:43) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import sqlite3
>>> sqlite3.version

Warning (from warnings module):
  File "<pyshell#1>", line 1
DeprecationWarning: version is deprecated and will be removed in Python 3.14
'2.6.0'
>>> sqlite3.sqlite_version
'3.40.1'
>>> import sqlite3
>>> conexion = sqlite3.connect('Ejemplo.db')
>>> c=conexion.cursor()
>>> c.execute('''CREATE TABLE acciones (fecha text, operacion text, simbolo text,cantidad real, precio real)''')
<sqlite3.Cursor object at 0x000001A506ACD840>
>>> select * from acciones;
SyntaxError: invalid syntax
>>> DROP TABLE acciones;
SyntaxError: invalid syntax
>>> c.execute("INSERT INTO acciones VALUES
...           
SyntaxError: incomplete input
>>> c.execute("INSERT INTO acciones VALUES ('24/nov/2016', 'compra', 'INV', 100, 15.43)")
...           
<sqlite3.Cursor object at 0x000001A506ACD840>
>>> conexion.commit()
...           
>>> conexion.close()
...           
