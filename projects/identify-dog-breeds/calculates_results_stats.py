#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */AIPND-revision/intropyproject-classify-pet-images/calculates_results_stats.py
#

# PROGRAMMER: Yazan Al-Sedih
# DATE CREATED: 15/3/2025                                  
# REVISED DATE: 
# PURPOSE: Create a function calculates_results_stats that calculates the 
#          statistics of the program run using the classifier's model 
#          architecture to classify the images. This function will use the 
#          results in the results dictionary to calculate these statistics. 
#          This function will then put the results statistics in a dictionary
#          (results_stats_dic) that's created and returned by this function.
#          This will allow the user of the program to determine the 'best' 
#          model for classifying the images. The statistics that are calculated
#          will be counts and percentages.

# TODO 5: Define calculates_results_stats function below
def calculates_results_stats(results_dic):
    """
    Calculates statistics of the classifier's performance and stores them in a dictionary.

    Parameters:
        results_dic (dict): Dictionary containing image filenames as keys and a list as values.
                            Each list contains:
                            - Index 0: Pet image label
                            - Index 1: Classifier label
                            - Index 2: 1 if labels match, 0 otherwise
                            - Index 3: 1 if pet image label is a dog, 0 otherwise
                            - Index 4: 1 if classifier label is a dog, 0 otherwise

    Returns:
        results_stats_dic (dict): Dictionary containing classification performance statistics.
    """

    # Initialize statistics dictionary
    results_stats_dic = {
        'n_images': len(results_dic),    # Total number of images
        'n_dogs_img': 0,                 # Number of dog images
        'n_notdogs_img': 0,              # Number of non-dog images
        'n_match': 0,                    # Number of label matches
        'n_correct_dogs': 0,             # Correctly classified dog images
        'n_correct_notdogs': 0,          # Correctly classified non-dog images
        'n_correct_breed': 0             # Correctly classified dog breeds
    }

    # Iterate through results dictionary to calculate counts
    for key, values in results_dic.items():
        pet_label_is_dog = values[3]
        classifier_label_is_dog = values[4]
        is_label_match = values[2]

        # Count number of dog images
        if pet_label_is_dog == 1:
            results_stats_dic['n_dogs_img'] += 1
            # Count correctly classified dog images
            if classifier_label_is_dog == 1:
                results_stats_dic['n_correct_dogs'] += 1
            # Count correctly classified breeds
            if is_label_match == 1:
                results_stats_dic['n_correct_breed'] += 1
        else:
            # Count number of non-dog images
            results_stats_dic['n_notdogs_img'] += 1
            # Count correctly classified non-dog images
            if classifier_label_is_dog == 0:
                results_stats_dic['n_correct_notdogs'] += 1

        # Count correctly matched labels
        if is_label_match == 1:
            results_stats_dic['n_match'] += 1

    # Calculate percentages (handle division by zero cases)
    results_stats_dic['pct_match'] = (
        (results_stats_dic['n_match'] / results_stats_dic['n_images']) * 100
        if results_stats_dic['n_images'] > 0 else 0
    )

    results_stats_dic['pct_correct_dogs'] = (
        (results_stats_dic['n_correct_dogs'] / results_stats_dic['n_dogs_img']) * 100
        if results_stats_dic['n_dogs_img'] > 0 else 0
    )

    results_stats_dic['pct_correct_notdogs'] = (
        (results_stats_dic['n_correct_notdogs'] / results_stats_dic['n_notdogs_img']) * 100
        if results_stats_dic['n_notdogs_img'] > 0 else 0
    )

    results_stats_dic['pct_correct_breed'] = (
        (results_stats_dic['n_correct_breed'] / results_stats_dic['n_dogs_img']) * 100
        if results_stats_dic['n_dogs_img'] > 0 else 0
    )

    return results_stats_dic
