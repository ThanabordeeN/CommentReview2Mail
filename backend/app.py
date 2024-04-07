from flask import Flask, request, jsonify
from main import run
app = Flask(__name__)

@app.route('/api/post', methods=['POST'])
def post_data():
    data = request.get_json()  # Get the JSON data from the request
    run(data['image'])
    response = {'message': 'Mail Sent Successfully.'}
    return jsonify(response), 200

if __name__ == '__main__':
    app.run(debug=True)