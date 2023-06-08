from pyodbc import *


class Database:
    connection_string = ("Driver=SQL Server;"
                        "Server=TEW-DEV03\\SQLEXPRESS;"
                        "Database=Chatbot;"
                        "Trusted_Connection=True;"
                        )

    def __init__(self):
        self.connection = connect(self.connection_string)

    def read(self, id):
        cursor = self.connection.cursor()

        cursor.execute("SELECT * FROM [dbo].[Chat] WHERE [Id] = ?", id)
        for x in cursor.fetchall():
            print(x)
            chat_history = x.ChatHistory
            split_chat_history = chat_history.split(';')

            for message in split_chat_history:
                print(message)

    def write(self, ticket):
        print(ticket.CustomerId, ticket.ChatHistory)
        cursor = self.connection.cursor()
        cursor.execute("INSERT INTO [dbo].[Chat] ([CustomerId], [ChatHistory]) VALUES (?, ?)", ticket.CustomerId, ticket.ChatHistory)
        cursor.commit()


class Ticket:
    def __init__(self, customer_id, chat_history):
        self.CustomerId = customer_id
        self.ChatHistory = chat_history
