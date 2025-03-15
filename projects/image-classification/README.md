# **Image Classification using TensorFlow**

## **Project Overview**
This project is a deep learning-based image classification model built using **TensorFlow** and **Keras**, with a pre-trained model from **TensorFlow Hub**. The goal is to classify images of flowers into different categories.

## **Project Structure**
```
image-classification/
│── assets/                     # Contains sample images
│── test_images/                # Contains test images
│── .ipynb_checkpoints/         # Checkpoints for Jupyter Notebook
│── Project_Image_Classifier_Project.ipynb  # Jupyter Notebook with the complete workflow
│── Project_Image_Classifier_Project.html   # HTML report of the notebook
│── README.md                   # Project documentation
│── flower_classifier.h5         # Trained model file
│── label_map.json               # Mapping of class indices to flower names
│── predict.py                   # Python script for inference
│── requirements.txt             # Dependencies required for the project
```

## **Installation & Setup**
### **1. Clone the Repository**
```bash
git clone https://github.com/your-repository/image-classification.git
cd image-classification
```

### **2. Create a Virtual Environment**
```bash
python -m venv env
source env/bin/activate  # For macOS/Linux
env\Scripts\activate     # For Windows
```

### **3. Install Dependencies**
```bash
pip install -r requirements.txt
```

## **Usage**
### **1. Running the Model for Prediction**
To predict an image's category, use:
```bash
python predict.py <image_path> <model_path> --top_k 5 --category_names label_map.json
```
#### **Arguments:**
- `<image_path>`: Path to the image file.
- `<model_path>`: Path to the trained model file (e.g., `flower_classifier.h5`).
- `--top_k`: (Optional) Number of top predictions to display.
- `--category_names`: (Optional) Path to a JSON file mapping class labels to actual flower names.

### **Example Usage**
```bash
python predict.py test_images/flower.jpg flower_classifier.h5 --top_k 3 --category_names label_map.json
```

## **Model Details**
- The model is trained using **transfer learning** with a pre-trained feature extractor from **TensorFlow Hub**.
- The dataset used is a **flower classification dataset**, which consists of various flower species.
- The final model is saved as **flower_classifier.h5**.

## **Results**
The model outputs the **top-K predictions** along with their probabilities. It maps the predicted class indices to actual flower names using `label_map.json`.

## **License**
This project is open-source and available for educational purposes.
