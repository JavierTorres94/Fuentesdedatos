Python 3.12.0a6 (tags/v3.12.0a6:f9774e5, Mar  7 2023, 23:52:43) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import sqlite3
>>> coneccion = sqlite3.connect('Ejemplo.db')
>>> c=conexion.cursor()
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    c=conexion.cursor()
NameError: name 'conexion' is not defined. Did you mean: 'coneccion'?
>>> c.execute("SELECT * FROM acciones")
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    c.execute("SELECT * FROM acciones")
NameError: name 'c' is not defined
>>> print c.fetchone()
SyntaxError: Missing parentheses in call to 'print'. Did you mean print(...)?
>>> conexion.close()
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    conexion.close()
NameError: name 'conexion' is not defined. Did you mean: 'coneccion'?
