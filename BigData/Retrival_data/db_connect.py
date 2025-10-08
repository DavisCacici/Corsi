import pyodbc
SERVER = 'NB-CACICID\\SQL22'
DATABASE = 'SiProject_DEMO'
# USERNAME = 'username'
# PASSWORD = 'password'

# connection_string = f"DRIVER=ODBC Driver 17 for SQL Server;SERVER={SERVER};DATABASE={DATABASE};UID={USERNAME};PWD={PASSWORD}"
connection_string = f"DRIVER=ODBC Driver 17 for SQL Server;SERVER={SERVER};DATABASE={DATABASE};Trusted_Connection=yes;" 

try:
    # Establish the connection
    conn = pyodbc.connect(connection_string)
    print("Connection successful!")

    # Create a cursor object to execute queries
    cursor = conn.cursor()

    # Example query
    cursor.execute("SELECT COUNT(*) FROM dbo.AddettoBase")
    print(cursor.fetchall())

    # with open('file.txt', "at") as f:
    #     for row in cursor.fetchall():
    #         print(row)
    #         break
            # f.write(row.acronimo)

except pyodbc.Error as e:
    print("Error:", e)
finally:
    if 'connection' in locals():
        conn.close()