from HandleDB import HandleDB
SERVER = 'NB-CACICID\\SQL22'
DATABASE = 'AdventureWorks2022'
connection_string = f"DRIVER=ODBC Driver 17 for SQL Server;SERVER={SERVER};DATABASE={DATABASE};Trusted_Connection=yes;" 

person = HandleDB(connection_string, 'Person.Person')

# print(person.read(['FirstName', 'LastName']))
# person.create({
#     "BusinessEntityID": "20778",
#     "FirstName": "'Pino'",
#     "LastName": "'Daniele'",
#     "PersonType": "'EM'",
#     "NameStyle": "0",
#     "EmailPromotion": "0",
#     "ModifiedDate": "2020-3-16"
# })
# person.update({
#     "FirstName": "'Pino'",
#     "LastName": "'Daniele'",
# }, "BusinessEntityID = 20777")
person.delete("BusinessEntityID = 20777")