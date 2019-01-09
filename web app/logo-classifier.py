#!flask/bin/python
from flask import Flask,request,jsonify,render_template
from torch import load
from torch.nn import Linear, LogSoftmax, Dropout, ReLU, Sequential
from torchvision import models
from image_utils import predict
from PIL import Image
import io


image_extensions=['ras', 'xwd', 'bmp', 'jpe', 'jpg', 'jpeg', 'xpm', 'ief', 'pbm', 'tif', 'gif', 'ppm', 'xbm', 'tiff', 'rgb', 'pgm', 'png', 'pnm']
cp_location = 'aug_cutout.pt'

def upload_file():
    global model, idx_to_class
    # checking if the file is present or not.
    if request.method == 'GET':
        return render_template('logo-classifier.html')
    if 'file' not in request.files:
        return "No file found"

    # checking if the file is of accepted extension
    file = request.files['file']
    if file.filename.split('.')[1] not in image_extensions:
        return jsonify({'error':'invalid image file'})

    image_bytes = file.read()
    pil_image = Image.open(io.BytesIO(image_bytes))

    pred,class_pred=predict(pil_image, model, 1)
    return render_template('prediction.html', prediction=idx_to_class[class_pred.item()], confidence=round(pred.item()*100,2))

if __name__ == '__main__':

    # loading model
    model = models.resnet152(pretrained=False)
    classifier = Sequential(Linear(2048, 1024),
                                 ReLU(),
                                 Dropout(p=0.3),
                                 Linear(1024, 512),
                                 ReLU(),
                                 Dropout(p=0.3),
                                 Linear(512, 33),
                                 LogSoftmax(dim=1))
    model.fc=classifier
    checkpoint = load(cp_location, map_location='cpu')
    model.load_state_dict(checkpoint['state_dict'])

    idx_to_class ={}
    for key,value in checkpoint['class_to_idx'].items():
        idx_to_class[value]=key


    app = Flask(__name__)
    app.add_url_rule("/", "upload_file", upload_file, methods=["GET", "POST"])
    app.run(debug=False)