from pyodbc import *


class Database:
    connection_string = ("Driver=SQL Server;"
                        "Server=TEW-DEV03\\SQLEXPRESS;"
                        "Database=Chatbot;"
                        "Trusted_Connection=True;"
                        )

    def __init__(self):
        self.connection = connect(self.connection_string)


class Ticket:
    def __init__(self, customer_id, chat_history):
        self.CustomerId = customer_id
        self.ChatHistory = chat_history