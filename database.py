# database.py
import sqlite3

def connect_database():
    conexion = sqlite3.connect('DataBaseMercado.db')
    cursorDB = conexion.cursor()
    return conexion, cursorDB

def close_database(conexion):
    conexion.close()