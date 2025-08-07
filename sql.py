import mysql.connector
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()
#  Connect to your local MySQL server
def get_connection():
    connection=mysql.connector.connect(
        host= os.getenv("MYSQL_HOST"),
        user=os.getenv("MYSQL_USER"),       #  Replace with your MySQL username
        password=os.getenv("MYSQL_PASSWORD"),   #  Replace with your MySQL password
        database=os.getenv("MYSQL_DATABASE")    # Replace with your database name (must already exist)
    )
    return connection

connection = get_connection()
cursor = connection.cursor()

# Create table if not exists
table_info = """
CREATE TABLE IF NOT EXISTS STUDENT (
    name VARCHAR(50),
    course VARCHAR(50),
    grade CHAR(1),
    marks INT
)
"""
cursor.execute(table_info)

# Insert some records
cursor.execute("INSERT INTO STUDENT VALUES ('Krish', 'Data Science', 'A', 90)")
cursor.execute("INSERT INTO STUDENT VALUES ('Sudhanshu', 'Data Science', 'B', 100)")
cursor.execute("INSERT INTO STUDENT VALUES ('Darius', 'Data Science', 'A', 86)")
cursor.execute("INSERT INTO STUDENT VALUES ('Vikash', 'DEVOPS', 'A', 50)")
cursor.execute("INSERT INTO STUDENT VALUES ('Dipesh', 'DEVOPS', 'A', 35)")

# Commit the transaction so inserts are saved
connection.commit()

# Display all records
print("The inserted records are:")
cursor.execute('''SELECT * FROM STUDENT''')
data = cursor.fetchall()

for row in data:
    print(row)

# Close the connection
cursor.close()
connection.close()
