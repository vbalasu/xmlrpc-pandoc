import os, sys, base64, uuid
def run_pandoc(format_from, format_to, b64data):
  data = base64.decodebytes(b64data)
  from docker_run import docker_run
  filename = 'temp/'+str(uuid.uuid4()).replace('-', '')
  with open(filename, 'wb') as f:
    f.write(data)
  (out, err) = docker_run(["-v", os.getcwd()+":/source", "jagregory/pandoc", "-f", format_from, "-t", format_to, "-o", "/dev/stdout", filename])
  os.remove(filename)
  sys.stderr.buffer.write(err)
  return (out, err)

def main():
  (out, err) = run_pandoc("markdown", "docx", base64.encodebytes(b"# some new string"))
  sys.stdout.buffer.write(out)
# USAGE sudo python -c "import l2_subprocess as l2; l2.main()"
