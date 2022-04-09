# HDSC2022 Capstone Project
## By Hamoye-Prophet-Team

The data was collected through web scraping https://www.cucas.edu.cn/china_scholarships/
The code to the web scraping program and data cleaning program is stored in https://github.com/mcmuralishclint/CUCAS
The dataset contains information about the scholarship programs in China as of May 2019.

### The files in the project are as follows:

China_Scholarship_EDA.ipynb - Exploratory Data Analysis and some conclusions from various graphs <br />
prophet.ipynb - Predicting China Scholarship additional cost and the amount to spend on Accomodation <br />
prophet_re.ipynb(Main Project model) - Predicting Total Expense <br />
model.pkl - The best model as pickled file for offline batch prediction

### Contents of the files:

China_Scholarship_EDA.ipynb :
1. EDA
2. Multicollinearity
3. Univariate Analysis
4. Bivariate Analysis


prophet.ipynb :
1. Data Visualisation
2. Data Preprocessing for model 1(Predicting tuition_fees_to_pay)
3. Training model 1(Predicting tuition_fees_to_pay)
4. Data Preprocessing for model 2 (Predicting )
5. Training model 2(Predicting accomodation_to_pay)

prophet_re.ipynb :
1. Data Preprocessing
2. Inspect columns in new data
3. Modelling
4. Random Forest
5. XGBoost
6. Results Analysis
