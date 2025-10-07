from flask import Flask, request, jsonify
from calculations import calculate_roi

app = Flask(__name__)

@app.route('/simulate', methods=['POST'])
def simulate():
    data = request.get_json()
    try:
        results = calculate_roi(data)
        return jsonify(results), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True)
