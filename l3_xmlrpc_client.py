def convert(convert_from, convert_to, source_filename):
    import xmlrpc.client
    import sys, base64
    s = xmlrpc.client.ServerProxy('http://54.209.175.70:8001', allow_none=True, use_builtin_types=True)
    #s = xmlrpc.client.ServerProxy('http://127.0.0.1:8001', allow_none=True, use_builtin_types=True)
    with open(source_filename, "rb") as f:
        source_data = f.read()
    (out, err) = s.run_pandoc(convert_from, convert_to, base64.encodebytes(source_data))
    sys.stdout.buffer.write(out)
import sys
if __name__ == '__main__':
    if len(sys.argv) != 4:
        print('Syntax:  python l3_xmlrpc_client.py <<convert_from>> <<convert_to>> <<source_filename>>')
        print('Example: python l3_xmlrprc_client.py markdown docx README.md')
    else:
        convert(sys.argv[1], sys.argv[2], sys.argv[3])
