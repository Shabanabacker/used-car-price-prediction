# Used Car Price Prediction Project

## Project Overview

The Used Car Price Prediction Project aims to develop a machine learning model to predict the prices of used cars based on their features. The project includes data collection, data preprocessing, model development, and the deployment of an interactive web application using Streamlit. This tool will assist both customers and sales representatives in estimating car prices accurately.

## Project Workflow

### 1. Data Collection
**Source Files:**
- `bangalore_cars.csv`
- `chennai_cars.csv`
- `delhi_cars.csv`
- `hyderabad_cars.csv`
- `jaipur_cars.csv`
- `kolkata_cars.csv`

These files contain details about used cars, including their features and prices.

### 2. Data Cleaning and Preparation
**Steps Performed:**
- **Handling Missing Values:** Addressed missing data in the dataset.
- **Standardizing Data Formats:** Removed commas, special characters, and other non-numeric symbols from numerical columns.
- **Feature Engineering:** Created new features to enhance model performance.
- **Data Transformation:** Converted categorical features into numerical values using techniques like label encoding.
- **Normalization:** Scaled numerical features using Min-Max scaling.

### 3. Exploratory Data Analysis (EDA)
**Steps Performed:**
- **Data Visualization:** Created visualizations to identify patterns and correlations using scatter plots, histograms, box plots, and correlation heatmaps.
- **Feature Selection:** Identified important features that significantly impact car prices.

### 4. Model Development
**Approach:**
- **Model Selection:** Evaluated various regression models, including:
  - Linear Regression
  - Decision Trees
  - Random Forest
  - Gradient Boosting Machines
  - K-Nearest Neighbors (KNN)
- **Model Training:** Trained the chosen models using the prepared dataset.
- **Model Evaluation:** Assessed model performance using metrics such as:
  - Mean Absolute Error (MAE)
  - Mean Squared Error (MSE)
  - R-squared
- **Hyperparameter Tuning:** Optimized model parameters using grid search.
- **Final Model:** Selected the Random Forest algorithm for price prediction.

### 5. Deployment
**Streamlit Application:**
- **Development:** Created a Streamlit web application that allows users to input car features and receive price predictions.

### 6. Documentation and Testing
**Documentation:**
- **Code Documentation:** Included comments and explanations within the code for clarity.

## Tools and Technologies Used
- **Python & Pandas:** For data cleaning and preprocessing.
- **Scikit-learn:** For developing and evaluating machine learning models.
- **Streamlit:** For creating and deploying the web application.
- **Jupyter Notebook:** For performing EDA and model development.

## Installation and Setup

### Prerequisites
- Python with the following packages: `Pandas`, `Scikit-learn`, `Streamlit`.
- Jupyter Notebook for development and testing.

### Steps

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/Shabanabacker/used-car-price-prediction.git
