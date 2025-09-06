from flask import Flask, request, send_file, render_template
from PIL import Image
import io
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/crop', methods=['POST'])
def crop():
    # Recebe dados da área de corte e imagem
    x = int(request.form['x'])
    y = int(request.form['y'])
    width = int(request.form['width'])
    height = int(request.form['height'])
    file = request.files['image']
    
    # Abre a imagem e faz o crop
    img = Image.open(file.stream)
    cropped_img = img.crop((x, y, x + width, y + height))
    
    # Salva em memória e retorna a imagem
    img_io = io.BytesIO()
    cropped_img.save(img_io, 'PNG')
    img_io.seek(0)
    
    return send_file(img_io, mimetype='image/png')

if __name__ == '__main__':
    app.run(debug=True)