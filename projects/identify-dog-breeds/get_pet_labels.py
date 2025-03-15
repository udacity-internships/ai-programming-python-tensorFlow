import os

def get_pet_labels(image_dir):
    """
    Creates a dictionary of pet labels (results_dic) based on the filenames 
    of the image files. These pet image labels are used to check the accuracy 
    of the labels returned by the classifier function. 
    
    Parameters:
     image_dir - The (full) path to the folder of images that are to be
                 classified by the classifier function (string)
                 
    Returns:
      results_dic - Dictionary where:
          - Key: Image filename (string)
          - Value: List containing one item:
              - Index 0: Pet image label (string)
    """

    # Check if directory exists
    if not os.path.exists(image_dir):
        print(f"❌ Error: Directory '{image_dir}' does not exist.")
        return None

    # Initialize results dictionary
    results_dic = {}

    # Get the filenames in the directory
    filenames = os.listdir(image_dir)

    # Check if directory is empty
    if not filenames:
        print(f"⚠️ Warning: Directory '{image_dir}' is empty.")
        return None

    for filename in filenames:
        # Ignore hidden/system files
        if filename.startswith('.'):
            continue

        # Extract pet label from filename
        pet_label = os.path.splitext(filename)[0]  # Remove file extension
        pet_label = pet_label.replace('_', ' ')    # Replace underscores with spaces
        pet_label = ''.join([c if c.isalpha() or c == ' ' else '' for c in pet_label])  # Remove digits
        pet_label = pet_label.lower().strip()      # Convert to lowercase & strip spaces

        # Add filename and label to dictionary
        if filename not in results_dic:
            results_dic[filename] = [pet_label]
        else:
            print(f"⚠️ Warning: Duplicate filename found - {filename}")

    # Check if any labels were created
    if not results_dic:
        print(f"❌ Error: No valid image labels found in '{image_dir}'.")
        return None

    print(f"✅ Successfully created labels for {len(results_dic)} images.")
    return results_dic
