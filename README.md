# csl
code to run thickness analysis on good and bad weld images

1. Create a Virtual Environment in the csl Folder:
	python3 -m venv csl_env
	source csl_env/bin/activate  # For Windows use `csl_env\Scripts\activate`

2. Install Dependencies:
	pip install -r requirements.txt

3. Ensure that the raw images are placed in the csl/data/raw/good and csl/data/raw/bad folders before running the project

4. Run the Project:
	With Filtering:
		python code/main.py --filter 1
	Withiout Filtering:
		python code/main.py --filter 0
