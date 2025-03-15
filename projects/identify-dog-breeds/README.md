# Identify Dog Breeds

## Overview
This project classifies images of dogs and other objects using pre-trained Convolutional Neural Networks (CNNs). It compares the predicted labels with the actual pet labels to determine classification accuracy. The project supports multiple CNN architectures, including **ResNet, AlexNet, and VGG**.

## Features
- Uses pre-trained **CNN models** to classify images.
- Compares classification results against actual pet labels.
- Generates detailed results and accuracy statistics.
- Supports batch processing for multiple images.
- Classifies both **dog and non-dog images**.
- Outputs results in formatted text files for easy analysis.

## Directory Structure
```
identify-dog-breeds/
│── pet_images/                # Directory for provided pet images
│── uploaded_images/           # Directory for uploaded images
│── __pycache__/               # Python cache files (ignored by Git)
│── venv/                      # Virtual environment (ignored by Git)
│── check_images.py            # Main script to classify images
│── get_pet_labels.py          # Extracts labels from filenames
│── classify_images.py         # Uses CNN model to classify images
│── adjust_results4_isadog.py  # Identifies whether a label is a dog
│── calculates_results_stats.py # Computes classification statistics
│── print_results.py           # Displays classification results
│── dognames.txt               # List of recognized dog breeds
│── requirements.txt           # Required Python packages
│── run_models_batch.sh        # Shell script to process pet_images
│── run_models_batch_uploaded.sh # Shell script to process uploaded images
│── README.md                  # Project documentation
```

## Setup and Installation
### 1. Clone the Repository
```sh
git clone https://github.com/your-username/identify-dog-breeds.git
cd identify-dog-breeds
```

### 2. Create and Activate Virtual Environment
```sh
python -m venv .venv
source .venv/bin/activate   # On macOS/Linux
.venv\Scripts\activate      # On Windows
```

### 3. Install Dependencies
```sh
pip install -r requirements.txt
```

## Usage
### Classifying Provided Images
To classify images from the **pet_images/** directory, run:
```sh
python check_images.py --dir pet_images/ --arch resnet --dogfile dognames.txt
```
Replace `resnet` with `alexnet` or `vgg` to use different architectures.

### Classifying Uploaded Images
To classify images from **uploaded_images/**, run:
```sh
python check_images.py --dir uploaded_images/ --arch resnet --dogfile dognames.txt
```

### Running Batch Processing
Instead of running individual commands, you can execute all three models using:
```sh
bash run_models_batch.sh
bash run_models_batch_uploaded.sh
```

## Example Output
```
Command Line Arguments:
 dir = uploaded_images/
 arch = vgg
 dogfile = dognames.txt

Pet Image Label Dictionary has 4 key-value pairs.
Below are 4 of them:
 1 key: Chihuahua_01.jpg   label: chihuahua
 2 key: Chihuahua_02.jpg   label: chihuahua
 3 key: Coffee_mug_01.jpg  label: coffee mug
 4 key: Siamese_cat_01.jpg label: siamese cat

*** Results Summary for CNN Model Architecture: VGG ***
N Images            : 4
N Dog Images        : 2
N Not-Dog Images    : 2
Pct Match           : 100.00%
Pct Correct Dogs    : 100.00%
Pct Correct Breed   : 100.00%
Pct Correct Notdogs : 100.00%
```

## Contributing
If you would like to contribute to this project, please submit a pull request or open an issue on [GitHub](https://github.com/your-username/identify-dog-breeds).

## License
This project is open-source and available under the **MIT License**.

---
Developed by **Yazan Al-Sedih** - 2025 🚀

