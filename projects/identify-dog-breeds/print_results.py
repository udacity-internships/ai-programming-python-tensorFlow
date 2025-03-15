#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */AIPND-revision/intropyproject-classify-pet-images/print_results.py
#

# PROGRAMMER: Yazan Al-Sedih
# DATE CREATED: 15/3/2025
# REVISED DATE: 
# PURPOSE: Create a function print_results that prints the results statistics
#          from the results statistics dictionary (results_stats_dic). It 
#          should also allow the user to be able to print out cases of misclassified
#          dogs and cases of misclassified breeds of dog using the Results 
#          dictionary (results_dic).  
#         This function inputs:
#            - The results dictionary as results_dic within print_results 
#              function and results for the function call within main.
#            - The results statistics dictionary as results_stats_dic within 
#              print_results function and results_stats for the function call within main.
#            - The CNN model architecture as model within print_results function
#              and in_arg.arch for the function call within main. 
#            - Prints Incorrectly Classified Dogs as print_incorrect_dogs within
#              print_results function and set as either boolean value True or 
#              False in the function call within main (defaults to False)
#            - Prints Incorrectly Classified Breeds as print_incorrect_breed within
#              print_results function and set as either boolean value True or 
#              False in the function call within main (defaults to False)
#         This function does not output anything other than printing a summary
#         of the final results.
##

def print_results(results_dic, results_stats_dic, model, 
                  print_incorrect_dogs=False, print_incorrect_breed=False):
    """
    Prints summary results on the classification and then prints incorrectly 
    classified dogs and incorrectly classified dog breeds if requested.

    Parameters:
        results_dic - Dictionary containing image filenames as keys and a list as values.
                      The list contains:
                        - Index 0: Pet image label (string)
                        - Index 1: Classifier label (string)
                        - Index 2: 1 if labels match, 0 otherwise
                        - Index 3: 1 if pet image label is a dog, 0 otherwise
                        - Index 4: 1 if classifier label is a dog, 0 otherwise
        results_stats_dic - Dictionary that contains the results statistics (either
                            a percentage or a count), where the key is the statistic's
                            name and the value is the statistic's value.
        model - The CNN model architecture used for classification (string).
        print_incorrect_dogs - If True, prints misclassified dogs (default is False).
        print_incorrect_breed - If True, prints misclassified dog breeds (default is False).
    
    Returns:
        None - Only prints results.
    """

    # Print model architecture used
    print("\n*** Results Summary for CNN Model Architecture:", model.upper(), "***")

    # Print number of images, number of dog images, and number of not-dog images
    print("\nTotal Images:", results_stats_dic['n_images'])
    print("Number of Dog Images:", results_stats_dic['n_dogs_img'])
    print("Number of Non-Dog Images:", results_stats_dic['n_notdogs_img'])

    # Print computed statistics
    print("\n*** Statistics Summary ***")
    for key in results_stats_dic:
        if key.startswith('pct'):  # Print only percentage statistics
            print(f"{key}: {results_stats_dic[key]:.1f}%")

    # Print misclassified dogs (if requested)
    if print_incorrect_dogs and (results_stats_dic['n_correct_dogs'] + results_stats_dic['n_correct_notdogs'] != results_stats_dic['n_images']):
        print("\n*** Misclassified Dogs ***")
        for key, value in results_dic.items():
            if sum(value[3:]) == 1:  # One is a dog, but the other is not
                print(f"Pet Label: {value[0]:<25}   Classifier Label: {value[1]:<25}")

    # Print misclassified dog breeds (if requested)
    if print_incorrect_breed and (results_stats_dic['n_correct_dogs'] != results_stats_dic['n_correct_breed']):
        print("\n*** Misclassified Dog Breeds ***")
        for key, value in results_dic.items():
            if sum(value[3:]) == 2 and value[2] == 0:  # Both classified as dogs but different breeds
                print(f"Pet Label: {value[0]:<25}   Classifier Label: {value[1]:<25}")
