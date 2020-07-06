from flask import Blueprint, Response
from importlib import import_module

video_bp = Blueprint('video_bp', __name__,
                     template_folder='templates',
                     static_folder='static')

Camera = import_module('camera_opencv').Camera

@video_bp.route('/video_feed')
def video_feed():
    return Response(gen(Camera()),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

def gen(camera):
    while True:
        frame = camera.get_frame()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')