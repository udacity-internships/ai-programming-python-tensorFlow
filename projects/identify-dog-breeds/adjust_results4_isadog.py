#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */AIPND-revision/intropyproject-classify-pet-images/adjust_results4_isadog.py

# PROGRAMMER: 
# DATE CREATED:                                 
# REVISED DATE: 
# PURPOSE: Adjusts the results dictionary to determine if classifier correctly 
#          classified images 'as a dog' or 'not a dog' especially when not a match.
#          Demonstrates if model architecture correctly classifies dog images even if
#          it gets dog breed wrong (not a match).

def adjust_results4_isadog(results_dic, dogfile):
    """
    Adjusts the results dictionary to determine if classifier correctly 
    classified images 'as a dog' or 'not a dog' especially when not a match. 

    Parameters:
      results_dic - Dictionary with:
                      Key: filename
                      Value: List [pet_label, classifier_label, match (1/0)]
      dogfile - Text file containing valid dog names (one per line)

    Returns:
      None - Modifies results_dic in place
    """

    # Create a dictionary of valid dog names
    dognames_dic = {}

    # Read the dog names from file
    with open(dogfile, "r") as f:
        for line in f:
            dog_name = line.strip().lower()
            if dog_name not in dognames_dic:
                dognames_dic[dog_name] = 1

    # Iterate through results dictionary and check if labels are dogs
    for key in results_dic:
        pet_label = results_dic[key][0]
        classifier_label = results_dic[key][1]

        # Check if pet label is a dog
        is_pet_dog = 1 if pet_label in dognames_dic else 0

        # Check if classifier label is a dog (can contain multiple names)
        classifier_labels = classifier_label.split(", ")
        is_classified_dog = any(label in dognames_dic for label in classifier_labels)

        # Add results to dictionary
        results_dic[key].extend([is_pet_dog, is_classified_dog])
