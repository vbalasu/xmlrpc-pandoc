import xmlrpc.client
import sys, base64
#s = xmlrpc.client.ServerProxy('http://54.209.175.70:8001', allow_none=True, use_builtin_types=True)
s = xmlrpc.client.ServerProxy('http://127.0.0.1:8001', allow_none=True, use_builtin_types=True)
(out, err) = s.run_pandoc('markdown', 'docx', base64.encodebytes(b'# This is some markdown in bytes'))
sys.stdout.buffer.write(out)
#USAGE: python l3_xmlrpc_client.py
