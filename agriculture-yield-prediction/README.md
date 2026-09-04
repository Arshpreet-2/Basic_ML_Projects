# Agriculture Yield Prediction

A machine learning project that explores agricultural data and predicts crop yield using **Linear Regression**.

The project covers the complete machine learning workflow, including data cleaning, exploratory data analysis, categorical feature encoding, model training, prediction, and evaluation.

## Project Overview

The goal of this project is to analyze how factors such as:

* Rainfall
* Temperature
* Humidity
* Nitrogen
* Fertilizer
* Soil Type
* Irrigation
* Crop Type
* Season

relate to agricultural yield and to build a regression model for predicting yield.

## Technologies Used

* Python
* Pandas
* NumPy
* Matplotlib
* Seaborn
* Plotly
* Scikit-learn

## Workflow

```text
Dataset
   ↓
Data Loading & Inspection
   ↓
Missing Value Handling
   ↓
Exploratory Data Analysis
   ↓
Correlation Analysis
   ↓
Categorical Feature Encoding
   ↓
Train-Test Split
   ↓
Linear Regression
   ↓
Prediction
   ↓
Model Evaluation
```

## Exploratory Data Analysis

The project analyzes:

* Distribution of rainfall, temperature, fertilizer and yield
* Crop type and soil type frequencies
* Relationships between agricultural factors and yield
* Correlations between numerical features
* Average yield across different crop and soil types

Visualizations include histograms, scatter plots and a correlation heatmap.

## Machine Learning Model

### Linear Regression

Linear Regression is used as the baseline regression model for predicting agricultural yield.

The dataset is divided into:

* **80% training data**
* **20% testing data**

Categorical features are converted into numerical features using one-hot encoding.

## Model Evaluation

The model is evaluated using:

* **Mean Absolute Error (MAE)**
* **Mean Squared Error (MSE)**
* **Root Mean Squared Error (RMSE)**
* **R² Score**

The actual evaluation results are printed when the Python script is executed.

## Project Structure

```text
agriculture-yield-prediction/
│
├── Agriculture_yield_prediction.py
└── README.md
```

## Key Learning Outcomes

Through this project, I practiced:

* Data preprocessing and missing-value handling
* Exploratory data analysis
* Data visualization
* Correlation analysis
* One-hot encoding
* Train-test splitting
* Linear regression
* Regression model evaluation
* Interpreting model coefficients

## Author

**Arshpreet Ahuja**

This project is part of my collection of machine learning projects exploring practical applications of ML and data analysis.
