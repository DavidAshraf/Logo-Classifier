import torch
import numpy as np
resize_size=255
image_size=224
mean= np.array([0.485, 0.456, 0.406])
std = np.array([0.229, 0.224, 0.225])
from flask import jsonify
def process_image(image):
    ''' Scales, crops, and normalizes a PIL image for a PyTorch model,
        returns an Numpy array
    '''
    # image=Image.open(image_path)
    # TODO: Process a PIL image for use in a PyTorch model
    if image.size[0] > image.size[1]:
       image.thumbnail((10000000,resize_size))
    else:
       image.thumbnail((resize_size,10000000))
    width=image.size[0]
    height=image.size[1]
    left = (width-image_size)/2
    top = (height-image_size)/2
    right = (width+image_size)/2
    bottom = (height+image_size)/2
    image = image.crop((left,top,right,bottom))
    image_np = np.array(image)/255
    mean_array=np.array(mean)
    std_array=np.array(std)
    image_np = (image_np-mean_array)/std_array
    image_np = image_np.transpose((2,0,1))
    return torch.from_numpy(image_np)

def predict(image, model, topk=5):
    ''' Predict the class (or classes) of an image using a trained deep learning model.
    '''
    
    # TODO: Implement the code to predict the class from an image file
    img = process_image(image)
    img.unsqueeze_(0)
    img=img.float()
    with torch.no_grad():
      model.eval()
      log_ps=model(img)
      ps = torch.exp(log_ps)
      preds,classes = ps.topk(topk,dim=1)
      return preds,classes