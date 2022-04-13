# HDSC2022 Capstone Project
## Hamoye-Prophet-Team

### Project Motivation
Many student secure different types of scholarships (full, partial, tutition-free), but some students end up losing them for many other reasons. 
Many among the reasons is that some don't know the total expenses those scholarships demand or marks reuired to sustain them. 
The goal of this project by team Prophets is to help predict the Total Expenses for a scholarship using this dataset.

### Project Process
Every machine learning project follows a workflow and phases, depending on the project specifications. Generally, these phases were followed by the 
team to achieve this result. The phases include:
[x] Data collection
[x] Exploratory Data Analysis
[x] Data Preparation (Feature Engineering)
[x] Modeling
[x] Deployment

### File Hierarchy
1. (Data folder)[]: The dataset contains information about the scholarship programs in China as of May 2019.
   - The data was collected by web scraping (here)[https://www.cucas.edu.cn/china_scholarships/]
   - The code to the web scraping program and data cleaning program can be accessed (here)[https://github.com/mcmuralishclint/CUCAS].
   - The file can be exported to csv format.

2. (Templates Folder)[]: This folder contains the webpage scripts (HTML, CSS and JAVASRIPT).
 
3. (App file)[]: This file contains the flask server deployment file.

4. (Model)[]: This is a serialised model file for offline batch prediction.

5. (Process File)[]: The minimised version file of th `prophet.ipynb` containing python codes for:
   - Data Visualisation
   - Data Preprocessing
   - Modeling
   - Hyperparameter tuning
   - Results Analysis

6. (prophet.ipynb)[]
   - The original file containing python codes for:
    
7. (Requirements File)[].txt
    - contains all libraries and their versions, some of them includes:
        - `pandas`
        - `numpy`
        - `matplotlib`
        - `seaborn`
        - `sklearn`
        - `xgboost`
        - `optuna`

### Contributors
Special Shoutout to the following contributors from our team
- Dimaria
- XYs
- HDjf
- Ftrud
- Hgfih
- bIhf[f

### Notes 
The note on this note can be improved upon, you reference the authors in your work.