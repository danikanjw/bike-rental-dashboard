# Bike Sharing Dashboard

## Repository Directory Overview
- /dashboard: Contains the primary files shown in the dashboard.
- /data: Holds the datasets utilized for analysis (Bike Sharing Dataset).
- notebook.ipynb: Jupyter notebook file that includes the data analysis performed.
- README.md: A file providing details about this project.
- requirements.txt: A file listing the libraries employed in this project.

## Setup Environment - Anaconda
```
conda create --name main-ds python=3.9
conda activate main-ds
pip install -r requirements.txt
```

## Setup Environment - Shell/Terminal
```
mkdir proyek_analisis_data
cd proyek_analisis_data
pipenv install
pipenv shell
pip install -r requirements.txt
```

## Run steamlit app
```
streamlit run dashboard.py
```