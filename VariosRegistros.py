Python 3.12.0a6 (tags/v3.12.0a6:f9774e5, Mar  7 2023, 23:52:43) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import sqlite3
>>> conexion = sqlite3.connect('Ejemplo.db')
>>> c= conexion.cursor()
>>> 
>>> movimientos = [('24/nov/2016', 'venta', 'HPC', 50,20.01), ('25/nov/2016', 'compra', 'SNY', 100, 7.18), ('26/nov/2016', 'compra', 'XBX' 75, 5.33)]
SyntaxError: invalid syntax. Perhaps you forgot a comma?
>>> c.executemany('insert into acciones values(?,?,?,?,?)', movimientos)
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    c.executemany('insert into acciones values(?,?,?,?,?)', movimientos)
NameError: name 'movimientos' is not defined
>>> coneccion.commit()
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    coneccion.commit()
NameError: name 'coneccion' is not defined. Did you mean: 'conexion'?
>>> for row in c.execute("SELECT * from acciones"):
...     print (row)
... conexion.close()
SyntaxError: invalid syntax
>>> for row in c.execute("SELECT * FROM acciones where operacion = 'compra'"):
...     operacion [ 'compra'"):
...                 
SyntaxError: incomplete input
>>> print (row)
...                 
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    print (row)
NameError: name 'row' is not defined. Did you mean: 'pow'?
>>> import sqlite3
>>> import time
>>> conexion = sqlite3.connect('Ejemplo.db')
>>> c=conexion.cursor()
>>> fecha=time.ctime()
>>> operacion = 'compra'
>>> simbolo='IBM'
>>> cantidad = 50
precio=13.23

movimientos = [(fecha, operaciones, simbolo, cantidad, precio)]
Traceback (most recent call last):
  File "<pyshell#24>", line 1, in <module>
    movimientos = [(fecha, operaciones, simbolo, cantidad, precio)]
NameError: name 'operaciones' is not defined. Did you mean: 'operacion'?
c.executemany(INSERT INTO acciones VALUES(?,?,?,?,?)', movimientos)
              
SyntaxError: unterminated string literal (detected at line 1)
conexion.close()
              
import sqlite3
conexion = sqlite3.connect('Ejemplo.db')
c=conexion.cursor()

op = ('venta',)
for row in c.execute('SELECT * FROM acciones where operacion =?',op):
    print (row)
    conexion.close()

    
import sqlite3
conexion = sqlite3.connect('Ejemplo.db')
c = conexion.cursor()

fecha= ""
cantidad =""
c.execute('''SELECT fecha, cantidad from acciones''')
<sqlite3.Cursor object at 0x000001B160A4FCC0>
regisgtros=c.fetchall()
for registro in registros
SyntaxError: incomplete input
for registro in registros:
    fecha=regisgro[0]
    cantidad = registro[1]
    conexion.close()
