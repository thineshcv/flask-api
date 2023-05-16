from flask import Flask, jsonify, abort
import os
import json

app = Flask(__name__)

@app.route('/data/<filename>', methods=['GET'])
def get_json(filename):
    data_path = os.path.join('data', filename)

    if not os.path.exists(data_path):
        abort(404)

    with open(data_path) as file:
        try:
            json_data = json.load(file)
            return jsonify(json_data)
        except json.JSONDecodeError:
            abort(500)

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0', port=5000)
