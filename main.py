from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/receivedata', methods=['POST'])
def receive_data():
    data = request.json
    tag = data.get('tag')
    confidence = data.get('confidence')
    print(f'Received data: Tag: {tag}, Confidence: {confidence}')
    # Lakukan sesuatu dengan data yang diterima di sini
    return jsonify({'message': 'Data received successfully'}), 200

if __name__ == '__main__':
    app.run(host='192.168.11.221', port=5000, debug=True)
