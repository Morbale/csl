# csl/code/apply_filters.py
import os
import numpy as np
import cv2

# Function to apply filtering techniques
def apply_filters(image):
    # Convert to grayscale
    gray_frame = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    # Apply Gaussian blur
    blurred_frame = cv2.GaussianBlur(gray_frame, (5, 5), 0)
    # Apply adaptive thresholding
    adaptive_thresh_frame = cv2.adaptiveThreshold(blurred_frame, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 11, 2)
    # Apply erosion
    kernel = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5, 5))
    erosion = cv2.erode(adaptive_thresh_frame, kernel, iterations=1)
    # Apply dilation
    dilation = cv2.dilate(erosion, kernel, iterations=1)
    return dilation

def preprocess_images():
    base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
    input_folder = os.path.join(base_dir, "csl/data", "raw")
    output_folder = os.path.join(base_dir, "csl/data", "processed", "pre_processed")

    for label in ["good", "bad"]:
        input_path = os.path.join(input_folder, label)
        output_path = os.path.join(output_folder, label)
        os.makedirs(output_path, exist_ok=True)

        for filename in os.listdir(input_path):
            if filename.endswith('.png') or filename.endswith('.jpg'):
                # Read the image
                image_path = os.path.join(input_path, filename)
                
                cv_image = cv2.imread(image_path)

                # Apply filtering techniques
                final_image = apply_filters(cv_image)

                # Save the final image with "FILTERED" at the end of the filename
                base_name, extension = os.path.splitext(filename)
                filtered_name = base_name + '_FILTERED' + extension
                output_image_path = os.path.join(output_path, filtered_name)
                cv2.imwrite(output_image_path, final_image)
                

    print("Filtering complete.")
