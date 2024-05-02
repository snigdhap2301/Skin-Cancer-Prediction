# Skin Cancer Prediction

This project aims to develop a machine learning model for predicting skin cancer based on image data. Inspired by the research paper titled "Skin Cancer Prediction Using Deep Learning Techniques", our project builds upon the techniques proposed in the paper to create a predictive system with practical applications.

## Dataset

The dataset used in this project comprises two main files: `HAM10000_metadata.csv`, containing metadata about the skin lesion images, and `hmnist_28_28_RGB.csv`, which provides RGB image data in CSV format. This dataset, available on Kaggle, consists of 10,000 images, making it a substantial resource for training and evaluating our predictive model.

## Source Code

### `model`

The `model` directory houses the code related to the machine learning model. Within this directory, you'll find `model.ipynb`, a Jupyter Notebook containing the code for model training and evaluation, and `skin.h5`, which stores a pre-trained model for skin cancer prediction.

### `static`

The `static` directory contains static files utilized by the web application. This includes assets such as images and icons, CSS files for styling the application interface, JavaScript files for client-side functionality, and any third-party libraries or frameworks required for the application.

### `tests`

The `tests` directory includes files for testing the application. These tests ensure the functionality and reliability of the system, helping to identify and resolve any potential issues.

## Web Application

The web application provides an accessible interface for users to interact with the skin cancer prediction system. It consists of several HTML pages, including the initial landing page (`first.html`), the main application page (`index.html`), the login page (`login.html`), and the prediction page (`prediction.html`). The Flask application code for serving the web application is contained within `app.py`.

## Usage

To utilize the skin cancer prediction system, ensure all dependencies listed in `requirements.txt` are installed. Then, run the Flask application using `python app.py`, and access the application through a web browser using the provided URLs.

## Accuracy

Through model training and evaluation, we achieved an accuracy of 97.56% in predicting skin cancer. This high level of accuracy demonstrates the effectiveness of our predictive model in identifying potential instances of skin cancer.

## Contributors

This project was a collaborative effort by a team of dedicated individuals, including:

- [Ansh Prakash](https://github.com/anshprakash6397)
- [Tanisha Chandani](https://github.com/tanishachandani)
- [AmulGupta](https://github.com/Amulgupta)
- [Sanskriti](https://github.com/SanskritiHub)
- [Sanskar Sinha](https://github.com/sanskar9067)


## Requirements

Make sure to have the following dependencies installed:

```bash
pip install scikit-learn==1.2.2
pip install flask==2.3.2
pip install matplotlib==3.7.1
pip install pandas==2.0.0
pip install numpy==1.23.5
pip install tensorflow==2.12.0
```

Make sure to replace `pip install` with `pip3 install` if you're using Python 3.x.

### Base Paper

The inspiration for our project and the base paper we referred to was "Skin Cancer Prediction Using Deep Learning Techniques". You can find the paper [here](https://ieeexplore.ieee.org/abstract/document/10126035/authors#authors).
