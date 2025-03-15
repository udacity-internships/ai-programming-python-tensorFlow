#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# PROGRAMMER: Yazan Al-Sedih
# DATE CREATED: 15/3/2025
# PURPOSE: Classifies pet images using a pretrained CNN model, compares these
#          classifications to the true identity of the pets in the images, and
#          summarizes how well the CNN performed on the image classification task.
#          Saves results in text files for different architectures.

# Imports python modules
import os
from time import time
from get_input_args import get_input_args
from get_pet_labels import get_pet_labels
from classify_images import classify_images
from adjust_results4_isadog import adjust_results4_isadog
from calculates_results_stats import calculates_results_stats
from print_results import print_results

def main():
    start_time = time()
    in_arg = get_input_args()
    
    # Determine output file based on input directory
    if "uploaded_images" in in_arg.dir:
        results_filename = f"{in_arg.arch}_uploaded-images.txt"
    else:
        results_filename = f"{in_arg.arch}_pet-images.txt"
    
    if not os.path.exists(in_arg.dir):
        print(f"Error: Directory '{in_arg.dir}' does not exist.")
        return
    
    results = get_pet_labels(in_arg.dir)
    classify_images(in_arg.dir, results, in_arg.arch)
    adjust_results4_isadog(results, in_arg.dogfile)
    results_stats = calculates_results_stats(results)
    
    with open(results_filename, "w", encoding="utf-8") as f:
        f.write(f"Command Line Arguments:\n")
        f.write(f"dir = {in_arg.dir}\n")
        f.write(f"arch = {in_arg.arch}\n")
        f.write(f"dogfile = {in_arg.dogfile}\n\n")
        
        f.write(f"Pet Image Label Dictionary has {len(results)} key-value pairs.\n")
        f.write("Below are some of them:\n")
        for i, (key, value) in enumerate(results.items()):
            if i < 10:
                f.write(f"{i+1} key: {key}  label: {value[0]}\n")
        
        f.write("\n--- MATCHES ---\n")
        for key, value in results.items():
            if value[2] == 1:
                f.write(f"{key}:\nReal: {value[0]}   Classifier: {value[1]}\n\n")
        
        f.write("\n--- NOT A MATCH ---\n")
        for key, value in results.items():
            if value[2] == 0:
                f.write(f"{key}:\nReal: {value[0]}   Classifier: {value[1]}\n\n")
        
        f.write("\n*** Results Summary for CNN Model Architecture: {} ***\n".format(in_arg.arch.upper()))
        f.write("Total Images: {}\n".format(results_stats["n_images"]))
        f.write("Number of Dog Images: {}\n".format(results_stats["n_dogs_img"]))
        f.write("Number of Non-Dog Images: {}\n".format(results_stats["n_notdogs_img"]))
        f.write("\n")
        
        f.write("*** Statistics Summary ***\n")
        f.write("pct_match: {:.1f}%\n".format(results_stats["pct_match"]))
        f.write("pct_correct_dogs: {:.1f}%\n".format(results_stats["pct_correct_dogs"]))
        f.write("pct_correct_notdogs: {:.1f}%\n".format(results_stats["pct_correct_notdogs"]))
        f.write("pct_correct_breed: {:.1f}%\n\n".format(results_stats["pct_correct_breed"]))
        
        f.write("*** Misclassified Dog Breeds ***\n")
        for key, value in results.items():
            if value[2] == 0 and value[3] == 1:
                f.write(f"Pet Label: {value[0]}   Classifier Label: {value[1]}\n")
        
        f.write("\n** Total Elapsed Runtime: {}:{}:{}\n".format(
            int((time() - start_time) / 3600),
            int(((time() - start_time) % 3600) / 60),
            int((time() - start_time) % 60)
        ))
    
    print(f"Results saved to {results_filename}")

if __name__ == "__main__":
    main()
