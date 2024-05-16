# csl/code/main.py
import sys
import os
import argparse

# Print current working directory for debugging
#print(f"Current working directory: {os.getcwd()}")

# Add the 'code' directory to the sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

#print("sys.path after modification:")
#print(sys.path)

from apply_filters import preprocess_images
from contour import analyze_contours
from statistical_analysis import perform_statistical_analysis

def main():
    parser = argparse.ArgumentParser(description="Run image preprocessing and analysis.")
    parser.add_argument('--filter', type=int, choices=[0, 1], default=1, help='Apply filter (1) or not (0)')
    args = parser.parse_args()

    if(args.filter == 1):
       print("Starting preprocessing of images...")
       preprocess_images()
       print("Preprocessing completed.")
    
    # Perform contour analysis
    print("Starting contour analysis...")
    thickness_distributions, normalized_thickness_distributions = analyze_contours(apply_filter=bool(args.filter))
    print("Contour analysis completed.")
    
    # Perform statistical analysis
    print("Starting statistical analysis...")
    styled_results = perform_statistical_analysis(normalized_thickness_distributions)
    print("Statistical analysis completed.")
    
if __name__ == "__main__":
    main()
