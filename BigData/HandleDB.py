from typing import List, Dict
from pyodbc import Connection, connect, Cursor, Row

class HandleDB():
    connection: Connection
    cursor: Cursor
    tableName: str 
    def __init__(self, connString: str, tblName: str):
        self.connection = connect(connString)
        self.cursor = self.connection.cursor()
        self.tableName = tblName
        
    def read(self, colonne: List[str], condition: str)-> List[Row]:
        str_colonne = ", ".join(colonne)
        if(type(condition) is not None):
            self.cursor.execute(f"SELECT {str_colonne} FROM {self.tableName} WHERE {condition}")
        else:
            self.cursor.execute(f"SELECT {str_colonne} FROM {self.tableName}")
        return self.cursor.fetchall()
        
    def create(self, values: Dict) -> None:
        colonne = ", ".join(values.keys())
        valori = ", ".join(values.values())
        query = f"insert into {self.tableName} ({colonne}) values ({valori})"
        print(query)
        self.cursor.execute(query)
        self.connection.commit()

    def update(self, values: Dict, condition: str) -> None:
        key_value = []
        for k, v in values.items():
            key_value.append(f"{k}={v}")
        
        sets = ", ".join(key_value)
        query = f"update {self.tableName} set {sets} where {condition}"
        print(query)
        self.cursor.execute(query)
        self.connection.commit()
    
    def delete(self, condition: str) -> None:
        self.cursor.execute(f"delete from {self.tableName} where {condition}")
        self.connection.commit()