from flask import Flask, request, Response

app = Flask(__name__)


message = {
    'role': 'user',
    'content': ''
}
messages = []


@app.route('/messages', methods=['GET'])
def messages_get():
    messages.append(message)
    return messages, 200


@app.route('/messages', methods=['POST'])
def ask():
    messages.append(request.get_json())
    return Response("{'a':'b'}", status=201, mimetype='application/json')

if __name__ == '__main__':
    app.run()
