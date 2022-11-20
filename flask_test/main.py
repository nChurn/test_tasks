from flask import Flask, request
from werkzeug.exceptions import BadRequest

app = Flask(__name__)

@app.route("/url_name/", methods=['GET'])
def hello_view():
    name = request.args.get('name', None)
    message = request.args.get("message", None)
    if not name:
        return BadRequest("Name must be set")
    if not message:
        return BadRequest("Message must be set")
    return f"Hello {name}! {message}"

app.run(debug=True)