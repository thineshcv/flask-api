import os
import json
import psycopg2

# PostgreSQL connection details
host = "localhost"
database = "postgres"
user = "user"
password = "user"

# Directory path containing JSON files
directory = "./data"

# Table name
table_name = "patient_data"

# SQL statement to create the table
create_table_query = f"""
    CREATE TABLE IF NOT EXISTS {table_name} (
        filename TEXT PRIMARY KEY,
        content JSONB    
    );
"""

# Establishing a connection to PostgreSQL
conn = psycopg2.connect(
    host=host,
    database=database,
    user=user,
    password=password
)

# Creating a cursor object
cursor = conn.cursor()
print("connected successfully")

# Creating the table if it does not exist
cursor.execute(create_table_query)
print("created table")
conn.commit()

# Fetching all JSON files in the directory
json_files = [file for file in os.listdir(directory) if file.endswith(".json")]

# Iterating over each JSON file
for file in json_files:
    with open(os.path.join(directory, file)) as json_file:
        data = json.load(json_file)
        json_content = json.dumps(data)

    # Inserting the JSON content and filename into the PostgreSQL table
    cursor.execute(f"INSERT INTO {table_name} (content, filename) VALUES (%s, %s)", (json_content, file))
    print(cursor.execute(f"select * FROM {table_name}"))
    conn.commit()

# Closing the cursor and the connection
cursor.close()
conn.close()
