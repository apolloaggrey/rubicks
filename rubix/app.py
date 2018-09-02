import socketio
from flask import Flask, render_template
from flask_socketio import SocketIO
from cube import Cube
import time

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
server = SocketIO(app)
cube1 = Cube()



script= ""
def display_face(cube,face, x=150, y=0):
    script = ""
    print(face)
    for square in face.top_row.squares:  # cube1.shades[square.colour]
        script += f"""
        <script id="W_face_row1({face.top_row})" >
            var canvas = document.getElementById("open_cube");
            var square = canvas.getContext("2d");
            square.fillStyle = "{cube.shades[square.colour]}";
            square.fillRect({x},{y},{48},{48});
        </script>   
        """
        x += 50
    x -= 150
    y += 50
    for square in face.center_row.squares:  # cube1.shades[square.colour]
        script += f"""
        <script id="W_face_row2({face.center_row})" >
            var canvas = document.getElementById("open_cube");
            var square = canvas.getContext("2d");
            square.fillStyle = "{cube.shades[square.colour]}";
            square.fillRect({x},{y},{48},{48});
        </script>   
        """
        x += 50
    x -= 150
    y += 50
    for square in face.bottom_row.squares:  # cube1.shades[square.colour]
        script += f"""
        <script id="W_face_row3({face.bottom_row})" >
            var canvas = document.getElementById("open_cube");
            var square = canvas.getContext("2d");
            square.fillStyle = "{cube.shades[square.colour]}";
            square.fillRect({x},{y},{48},{48});
        </script>   
        """
        x += 50
    y += 50
    return script

def display_cube(cube):
    script = ""
    script += display_face(cube,cube.faces[0])
    script += display_face(cube,cube.faces[1], 0, 150)
    script += display_face(cube,cube.faces[2], 150, 150)
    script += display_face(cube,cube.faces[3], 300, 150)
    script += display_face(cube,cube.faces[4], 150, 300)
    script += display_face(cube,cube.faces[5], 150, 450)
    return script

@app.route('/')
def home(script = script):
    time.sleep(0.05)
    script += """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <title>home</title>
    </head>
    <body>
    
    <canvas id="open_cube" width="450" height="600"
        style=" background:#000000 ;
        border:2px solid #000000;" pa>
    </canvas>"""

    #  ###########################################################################
    script += display_cube(cube1)
    cube1.top_face.rotate()
    # #################################################################################

    script += """
    </body>
    </html>
    """
    return script





def main():
    server.run(app, host='0.0.0.0', debug=True, port=80,use_reloader=True,log_output=True)
    pass


if __name__ == '__main__':
    main()
