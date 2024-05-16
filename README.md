# csl
code to run thickness analysis on good and bad weld images

1. Create a Virtual Environment in the csl Folder:
   
		python3 -m venv csl_env

		source csl_env/bin/activate  # For Windows use `csl_env\Scripts\activate`

3. Install Dependencies:
   
		pip install -r requirements.txt

5. Ensure that the raw images are placed in the csl/data/raw/good and csl/data/raw/bad folders before running the project

6. Run the Project:
   
	With Filtering:

		python code/main.py --filter 1

	Withiout Filtering:

		python code/main.py --filter 0

7. If filter is used for pre-processing, filtered images are stored in csl/data/processed/pre_processed folder
8. Final images, thickness profiles and statistical testing results are stored in csl/data/processed/contour_analysis folder
