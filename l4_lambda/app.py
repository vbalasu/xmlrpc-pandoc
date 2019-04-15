from chalice import Chalice, Response
from chalicelib import l3_xmlrpc_client as c
import sys, base64, json
app = Chalice(app_name='l4_lambda')

@app.route('/', methods=['POST'], content_types=['text/plain'], cors=True)
def index():
    return app.current_request.raw_body

@app.route('/convert/{convert_from}/to/{convert_to}', methods=['POST'],
           content_types=['application/octet-stream'], cors=True)
def pandoc_convert(convert_from, convert_to):
    out = c.convert(convert_from, convert_to, app.current_request.raw_body)
    obj = {'data': base64.b64encode(out).decode()} 
    return obj
#    return Response(
#        base64.b64encode(out),
#        headers={
#            'Content-Type': 'application/octet-stream',
#        },
#        status_code=200)
# USAGE: $ curl -s -H 'Accept: application/octet-stream' -H 'Content-Type: application/octet-stream' -X POST http://127.0.0.1:8000/convert/markdown/to/html --data-binary @../README.md |jq -r '.data' |base64 -D
# USAGE: $ curl -s -H 'Accept: application/octet-stream' -H 'Content-Type: application/octet-stream' -X POST https://tmo99v9gxj.execute-api.us-east-1.amazonaws.com/api/convert/markdown/to/docx --data-binary @../README.md |jq -r '.data' |base64 -D >output.docx 


# The view function above will return {"hello": "world"}
# whenever you make an HTTP GET request to '/'.
#
# Here are a few more examples:
#
# @app.route('/hello/{name}')
# def hello_name(name):
#    # '/hello/james' -> {"hello": "james"}
#    return {'hello': name}
#
# @app.route('/users', methods=['POST'])
# def create_user():
#     # This is the JSON body the user sent in their POST request.
#     user_as_json = app.current_request.json_body
#     # We'll echo the json body back to the user in a 'user' key.
#     return {'user': user_as_json}
#
# See the README documentation for more examples.
#
