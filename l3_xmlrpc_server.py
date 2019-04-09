from xmlrpc.server import SimpleXMLRPCServer
from xmlrpc.server import SimpleXMLRPCRequestHandler

# Restrict to a particular path.
class RequestHandler(SimpleXMLRPCRequestHandler):
    rpc_paths = ('/RPC2',)

# Create server
with SimpleXMLRPCServer(('0.0.0.0', 8001), requestHandler=RequestHandler, allow_none=True, use_builtin_types=True) as server:
    server.register_introspection_functions()
    from l2_subprocess import run_pandoc
    server.register_function(run_pandoc)
    print('Function registered: run_pandoc()')
    # Run the server's main loop
    server.serve_forever()
#USAGE: sudo python l3_xmlrpc_server.py
#OR:    nohup sudo python l3_xmlrpc_server.py &
