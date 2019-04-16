function base64ToArrayBuffer(base64) {
    var binaryString = window.atob(base64);
    var binaryLen = binaryString.length;
    var bytes = new Uint8Array(binaryLen);
    for (var i = 0; i < binaryLen; i++) {
       var ascii = binaryString.charCodeAt(i);
       bytes[i] = ascii;
    }
    return bytes;
 }

function saveByteArray(fileName, byte) {
    var blob = new Blob([byte], {type: "application/octet-stream"});
    var link = document.createElement('a');
    link.href = window.URL.createObjectURL(blob);
    link.download = fileName;
    link.click();
}

function json_to_file(json, fileName) {
  data = JSON.parse(json).data
  byte_array = base64ToArrayBuffer(data)
  saveByteArray(fileName, byte_array)
}

//USAGE
function test_json_to_file() {
  obj = {data: btoa('hello')}
  json_to_file(JSON.stringify(obj), 'download.txt')
}
