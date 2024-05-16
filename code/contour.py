# csl/code/contour.py
import os
import cv2
from matplotlib import pyplot as plt
import numpy as np


def draw_internal_thickness_line_1(image_path, output_path, thickness_profile_path):
    # Load the image from the path
    image = cv2.imread(image_path)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    _, binary = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)

    # Find contours
    contours, _ = cv2.findContours(binary, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    contour = max(contours, key=cv2.contourArea)  # Assuming largest contour

    # Create an empty image to draw individual contours
    contour_img = np.zeros_like(gray)
    cv2.drawContours(contour_img, [contour], -1, 255, 1)

    # Find the top and bottom boundaries of the contour
    rows, cols = contour_img.shape
    thickness_distribution = []
    max_thickness = 0
    max_thickness_position = (0, 0)
    for col in range(cols):
        column_pixels = contour_img[:, col]
        top = np.argmax(column_pixels)
        bottom = rows - np.argmax(column_pixels[::-1])
        thickness = bottom - top
        thickness_distribution.append(thickness)

        if thickness > max_thickness:
            max_thickness = thickness
            max_thickness_position = (col, top, bottom)

    # Normalize the thickness distribution
    normalized_thickness_distribution = np.array(thickness_distribution) / max(thickness_distribution)

    # Draw the contour
    cv2.drawContours(image, [contour], -1, (0, 255, 0), 1)

    # Draw the maximum thickness line
    col, top, bottom = max_thickness_position
    cv2.line(image, (col, top), (col, bottom - 1), (0, 0, 255), 2)

    # Save the image with the contour and the max thickness line
    base_name = os.path.basename(image_path)
    cv2.imwrite(os.path.join(output_path, base_name), image)

    # Save the actual thickness distribution plot
    plt.figure()
    plt.plot(thickness_distribution)
    plt.title(f'Actual Thickness Distribution - {base_name}')
    plt.xlabel('Position along contour')
    plt.ylabel('Actual Thickness')
    plt.savefig(os.path.join(thickness_profile_path, base_name.replace('.jpg', '_actual_thickness.png')))
    plt.close()

    # Save the normalized thickness distribution plot
    plt.figure()
    plt.plot(normalized_thickness_distribution)
    plt.title(f'Normalized Thickness Distribution - {base_name}')
    plt.xlabel('Position along contour')
    plt.ylabel('Normalized Thickness')
    plt.savefig(os.path.join(thickness_profile_path, base_name.replace('.jpg', '_normalized_thickness.png')))
    plt.close()

    # Save the normalized thickness frequency distribution plot
    plt.figure()
    plt.hist(normalized_thickness_distribution, bins=10, color='blue', alpha=0.7)
    plt.title(f'Normalized Thickness Frequency Distribution - {base_name}')
    plt.xlabel('Normalized Thickness')
    plt.ylabel('Frequency')
    plt.savefig(os.path.join(thickness_profile_path, base_name.replace('.jpg', '_thickness_frequency.png')))
    plt.close()

    return thickness_distribution, normalized_thickness_distribution


def draw_internal_thickness_line_2(image_path, output_path, thickness_profile_path):
    # Load the image from the path
    image = cv2.imread(image_path)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    _, binary = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

    # Find contours
    contours, _ = cv2.findContours(binary, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    contour = max(contours, key=cv2.contourArea)  # Assuming largest contour

    # Create an empty image to draw individual contours
    contour_img = np.zeros_like(gray)
    cv2.drawContours(contour_img, [contour], -1, 255, 1)

    # Find the top and bottom boundaries of the contour
    rows, cols = contour_img.shape
    thickness_distribution = []
    max_thickness = 0
    max_thickness_position = (0, 0)
    for col in range(cols):
        column_pixels = contour_img[:, col]
        top = np.argmax(column_pixels)
        bottom = rows - np.argmax(column_pixels[::-1])
        thickness = bottom - top
        thickness_distribution.append(thickness)

        if thickness > max_thickness:
            max_thickness = thickness
            max_thickness_position = (col, top, bottom)

    # Normalize the thickness distribution
    normalized_thickness_distribution = np.array(thickness_distribution) / max(thickness_distribution)

    # Draw the contour
    cv2.drawContours(image, [contour], -1, (0, 255, 0), 1)

    # Draw the maximum thickness line
    col, top, bottom = max_thickness_position
    cv2.line(image, (col, top), (col, bottom - 1), (0, 0, 255), 2)

    # Save the image with the contour and the max thickness line
    base_name = os.path.basename(image_path)
    cv2.imwrite(os.path.join(output_path, base_name), image)

    # Save the actual thickness distribution plot
    plt.figure()
    plt.plot(thickness_distribution)
    plt.title(f'Actual Thickness Distribution - {base_name}')
    plt.xlabel('Position along contour')
    plt.ylabel('Actual Thickness')
    plt.savefig(os.path.join(thickness_profile_path, base_name.replace('.jpg', '_actual_thickness.png')))
    plt.close()

    # Save the normalized thickness distribution plot
    plt.figure()
    plt.plot(normalized_thickness_distribution)
    plt.title(f'Normalized Thickness Distribution - {base_name}')
    plt.xlabel('Position along contour')
    plt.ylabel('Normalized Thickness')
    plt.savefig(os.path.join(thickness_profile_path, base_name.replace('.jpg', '_normalized_thickness.png')))
    plt.close()

    # Save the normalized thickness frequency distribution plot
    plt.figure()
    plt.hist(normalized_thickness_distribution, bins=10, color='blue', alpha=0.7)
    plt.title(f'Normalized Thickness Frequency Distribution - {base_name}')
    plt.xlabel('Normalized Thickness')
    plt.ylabel('Frequency')
    plt.savefig(os.path.join(thickness_profile_path, base_name.replace('.jpg', '_thickness_frequency.png')))
    plt.close()

    return thickness_distribution, normalized_thickness_distribution


def analyze_contours(apply_filter):
    
    base_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
    if apply_filter == 1:
        input_folder = os.path.join(base_dir, "csl/data/processed/pre_processed")
    else :     
        input_folder = os.path.join(base_dir, "csl/data/raw")
		
    post_processed_folder = os.path.join(base_dir, "csl/data/processed/contour_analysis/post_processed")
    thickness_profile_folder = os.path.join(base_dir, "csl/data/processed/contour_analysis/thickness_profiles")
     
    
    thickness_distributions = {}
    normalized_thickness_distributions = {}
    
    
    for label in ["good", "bad"]:
        input_path = os.path.join(input_folder, label)
        output_post_processed_path = os.path.join(post_processed_folder, label)
        output_thickness_profile_path = os.path.join(thickness_profile_folder, label)
        
        os.makedirs(output_post_processed_path, exist_ok=True)
        os.makedirs(output_thickness_profile_path, exist_ok=True)
        
        for filename in os.listdir(input_path):
            if filename.endswith('.png') or filename.endswith('.jpg'):
                image_path = os.path.join(input_path, filename)
                if apply_filter == 1:
                    thickness_distribution, normalized_distribution = draw_internal_thickness_line_2(
                    image_path, output_post_processed_path, output_thickness_profile_path)
                else :
                    thickness_distribution, normalized_distribution = draw_internal_thickness_line_1(
                    image_path, output_post_processed_path, output_thickness_profile_path) 
                
                base_name = os.path.basename(image_path)
                thickness_distributions[base_name] = thickness_distribution
                normalized_thickness_distributions[base_name] = normalized_distribution
    
    return thickness_distributions, normalized_thickness_distributions
