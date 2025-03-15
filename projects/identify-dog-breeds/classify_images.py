#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */AIPND-revision/intropyproject-classify-pet-images/classify_images.py

# PROGRAMMER: 
# DATE CREATED:                                 
# REVISED DATE: 
# PURPOSE: Create a function classify_images that uses the classifier function 
#          to create the classifier labels and then compares the classifier 
#          labels to the pet image labels.

# Imports classifier function for using CNN to classify images 
from classifier import classifier 

def classify_images(images_dir, results_dic, model):
    """
    Creates classifier labels with classifier function, compares pet labels to 
    the classifier labels, and adds the classifier label and the comparison of 
    the labels to the results dictionary.

    Parameters: 
      images_dir - The (full) path to the folder of images that are to be
                   classified by the classifier function (string)
      results_dic - Results Dictionary with 'key' as image filename and 'value'
                    as a List. Where the list will contain the following items: 
                  index 0 = pet image label (string)
                --- where index 1 & index 2 are added by this function ---
                  NEW - index 1 = classifier label (string)
                  NEW - index 2 = 1/0 (int) where 1 = match between pet image
                    and classifier labels and 0 = no match between labels
      model - Indicates which CNN model architecture will be used by the 
              classifier function to classify the pet images,
              values must be either: resnet alexnet vgg (string)

    Returns:
           None - results_dic is mutable data type so no return needed.         
    """
    for key in results_dic:
        # Get full path for image file
        image_path = f"{images_dir}/{key}"

        # Run classifier function and get labels
        model_label = classifier(image_path, model).lower().strip()

        # Check if pet label is found in classifier label
        pet_label = results_dic[key][0]
        is_match = 1 if pet_label in model_label else 0

        # Update results dictionary
        results_dic[key].extend([model_label, is_match])
