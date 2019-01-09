# Logo-Classifier
Logo Classifier is using Pytorch model to classify logos
The supported logos are
**Adidas**, **Aldi**, **Apple**, **Becks**, **BMW**, **Carlsberg**, **Chimay**, **Coca-Cola**, **Corona**, **DHL**, **Erdinger**, **Esso**, **Fedex**, **Ferrari**, **Ford**, **Foster's**, **Google**, **Guiness**, **Heineken**, **HP**, **Milka**, **Nvidia**, **Paulaner**, **Pepsi**, **Ritter Sport**, **Shell**, **Singha**, **Starbucks**, **Stella Artois**, **Texaco**, **Tsingtao** and **UPS** or No Logo if there is no logo exists.

# Data
[FlickrLogos32](http://www.multimedia-computing.de/flickrlogos/) Collected logos of 32 different logo brands from Flickr. All logos have an approximately planar surface.

![Screenshot](http://www.multimedia-computing.de/flickrlogos/images/visualsummary3-test-800.jpg)

# Training
Pretrained resnet152 was used as a starting point.
0.8 of the data is used in training, 0.1 for validation and 0.1 for testing
*Logo_Classifier.ipynb* shows the progress of the training and how we did it.

# Usage

## Cloud app
To use our application you just need to enter to the [web app](https://logo-classifier.herokuapp.com/) and upload your image file and it will tell you the prediction and confidence.
The web app is deployed on Heroku.

## Run locally
Because of memory imitations Heroku app can be down, in this case you can run the app locally.

- Clone the repo
`git clone https://github.com/DavidAshraf/Logo-Classifier`

- install dependencies, go to "web app" directory and run this command from
`pip3 install -r requirements.txt`

- download the [model](https://drive.google.com/open?id=1cUKtzKvXP8HamvrF2KeZFvlLQ1qCKw7c) in the same directory "web app"

- run the app
`python3 logo-classifier.py`

# Credits
We would like to thank  Christian Eggert for providing us with the [dataset](http://www.multimedia-computing.de/flickrlogos/)
# License
[MIT](https://choosealicense.com/licenses/mit/)
