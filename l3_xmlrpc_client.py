import xmlrpc.client
import sys, base64
s = xmlrpc.client.ServerProxy('http://54.209.175.70:8001', allow_none=True, use_builtin_types=True)
#s = xmlrpc.client.ServerProxy('http://127.0.0.1:8001', allow_none=True, use_builtin_types=True)
with open("README.md", "rb") as f:
    markdown = f.read()
(out, err) = s.run_pandoc('markdown', 'docx', base64.encodebytes(markdown))
sys.stdout.buffer.write(out)
#USAGE: python l3_xmlrpc_client.py
