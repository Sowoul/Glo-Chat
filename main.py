from flask import Flask, render_template, request
from flask_socketio import SocketIO, emit

# Create the Flask app
app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret_key'
socketio = SocketIO(app, async_mode='threading')

# Store connected clients
clients = []

# Route for the chatroom page


@app.route('/')
def index():
    return render_template('index.html')

# Event handler for new connections


@socketio.on('connect')
def connect():
    clients.append(request.sid)
    print('Client connected:', request.sid)

# Event handler for disconnections


@socketio.on('disconnect')
def disconnect():
    clients.remove(request.sid)
    print('Client disconnected:', request.sid)

# Event handler for chat messages


@socketio.on('message')
def message(data):
    print('Message from', request.sid, ':', data)
    emit('message', data, broadcast=True, include_self=False)


if __name__ == '__main__':
    # Run the app with SocketIO
    socketio.run(app, host='0.0.0.0', port=5000, debug=True)

