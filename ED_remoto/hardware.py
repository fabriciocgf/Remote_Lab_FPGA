from flask import Blueprint, Response, request, jsonify
from flask import current_app as app
import subprocess

b = ["1", "1", "1", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0"]

hardware_bp = Blueprint('hardware_bp', __name__,
                     template_folder='templates',
                     static_folder='static')

@hardware_bp.route('/chaves', methods=['POST'])
def chaves():
    Key = request.form['chave']
    Botao(int(Key)+3, b)
    Escrever(b)
    return Response(Key)

@hardware_bp.route('/resetar')
def resetar():
    global b
    b = ["1", "1", "1", "0", "0", "0", "0", "0", "0", "0", "0", "0", "0"]
    Escrever(b)
    return jsonify('ok')

@hardware_bp.route('/Gravar', methods=['POST'])
def Gravar():
    file = request.form['file']
    GravarFPGA(file)
    return jsonify(file)

def Botao(n, b):
    if b[n] == "0":
        b[n] = "1"
    else:
        b[n] = "0"

def Escrever(b):
    c = 'quartus_stp -t ChangeMemory.tcl '+ "".join(b)
    p = subprocess.Popen(c,  shell=True)

def GravarFPGA(a):
    c = 'quartus_pgm -c "USB-Blaster [3-2]" -m JTAG -o "p;'+ app.config['UPLOAD_FOLDER'] + '/' + a + '"'
    p = subprocess.Popen(c,  shell=True)
