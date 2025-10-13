from typing import List
from pyodbc import Connection, connect, Cursor, Row

class HandleDB():
    connection: Connection
    cursor: Cursor
    tableName: str 
    def __init__(self):
        pass
    
    def read()-> List[Row]:
        pass
    
    def create() -> None:
        pass
    
    def update() -> None:
        pass
    
    def delete() -> None:
        pass