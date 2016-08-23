from flask import Flask, jsonify, request

app = Flask(__name__)
tasks = [
    {
        'id': 1,
        'title': u'OSPA',
        'description': u'This is ospaf-api test',
        'done': False
    },
    {
        'id': 2,
        'title': u'Garvin',
        'description': u'I am garvin',
        'done': False
    }
]

@app.route('/')
def hello_world():
    return 'Hello World!'
@app.route('/json', methods=['GET'])
def json():
    return jsonify({'tasks': tasks})

@app.route('/process_json', methods=['POST'])
def process_json():
    print(request.json)
    return jsonify(request.json)

if __name__ == '__main__':
    app.run()
