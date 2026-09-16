from flask import Flask, jsonify
from datetime import datetime
import socket

app = Flask(__name__)

@app.route('/api/v1/details')
def details():
    return jsonify({
        'time': datetime.now().strftime("%I:%M:%S%p on %B %d, %Y"),
        'hostname': socket.gethostname(),
        'message': 'My spoon is too big!!!!'
    })

@app.route('/api/v1/healthz')
def health():
    return jsonify({
        'status': 'Up'
    }), 200

if __name__ == '__main__':
    app.run(host="0.0.0.0")
