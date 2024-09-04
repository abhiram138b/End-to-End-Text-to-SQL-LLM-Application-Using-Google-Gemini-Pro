import sqlite3

# Connect to SQLite
connection = sqlite3.connect("student.db")

# Create a cursor object
cursor = connection.cursor()

# Create the table
table_info = """
CREATE TABLE IF NOT EXISTS STUDENT (
    NAME VARCHAR(25),
    CLASS VARCHAR(25),
    SECTION VARCHAR(25),
    MARKS INT
);
"""
cursor.execute(table_info)

# Insert some records
cursor.execute('''INSERT INTO STUDENT (NAME, CLASS, SECTION, MARKS) VALUES ('Abhiram', 'Data Science', 'A', 90)''')
cursor.execute('''INSERT INTO STUDENT (NAME, CLASS, SECTION, MARKS) VALUES ('Rajesh', 'Data Science', 'B', 100)''')
cursor.execute('''INSERT INTO STUDENT (NAME, CLASS, SECTION, MARKS) VALUES ('Abhiram', 'Data Science', 'A', 86)''')
cursor.execute('''INSERT INTO STUDENT (NAME, CLASS, SECTION, MARKS) VALUES ('Abhiram', 'Data Science', 'A', 50)''')
cursor.execute('''INSERT INTO STUDENT (NAME, CLASS, SECTION, MARKS) VALUES ('Abhiram', 'Data Science', 'A', 35)''')

# Display all records
print("The inserted records are:")
data = cursor.execute('''SELECT * FROM STUDENT''')
for row in data:
    print(row)

# Close the connection
connection.commit()
connection.close()
