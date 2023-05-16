from flask import Flask, jsonify
import psycopg2

app = Flask(__name__)

# PostgreSQL connection details
db_host = 'postgres'
db_port = '5432'
db_name = 'postgres'
db_user = 'user'
db_password = 'user'
# Table name
table_name = "patient_data"


@app.route("/data/<filename>", methods=["GET"])
def get_file_content(filename):
    # Establishing a connection to PostgreSQL
    conn = psycopg2.connect(
        host=db_host,
        database=db_name ,
        user=db_user,
        password=db_password
    )

    # Creating a cursor object
    cursor = conn.cursor()

    # Querying the table for the given filename
    cursor.execute(f"SELECT content FROM {table_name} WHERE filename = %s", (filename,))
    result = cursor.fetchone()

    # Closing the cursor and the connection
    cursor.close()
    conn.close()

    if result:
        # Returning the content if the file is found
        return jsonify({"filename": filename, "content": result[0]})
    else:
        # Returning an error message if the file is not found
        return jsonify({"error": "File not found"}), 404

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0', port=5000)
