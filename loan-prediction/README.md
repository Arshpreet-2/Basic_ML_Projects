# Loan Approval Prediction

A machine learning classification project that analyzes historical loan application data and predicts whether a loan application is likely to be approved or rejected.

The project compares multiple classification algorithms and evaluates their performance using several classification metrics.

## Project Overview

The objective of this project is to explore factors associated with historical loan approval outcomes and build machine learning models for binary classification.

The dataset contains information about applicants, including:

* Gender
* Marital status
* Number of dependents
* Education
* Self-employment status
* Applicant income
* Co-applicant income
* Loan amount
* Loan term
* Credit history
* Property area

The target variable is **Loan Status**, representing the historical approval outcome.

## Technologies Used

* Python
* Pandas
* NumPy
* Matplotlib
* Seaborn
* Scikit-learn

## Machine Learning Workflow

```text
Dataset
   ↓
Data Inspection
   ↓
Missing Value Handling
   ↓
Exploratory Data Analysis
   ↓
Feature Preprocessing
   ↓
Train-Test Split
   ↓
Model Training
   ↓
Model Comparison
   ↓
Cross-Validation
   ↓
Hyperparameter Tuning
   ↓
Final Evaluation
```

## Exploratory Data Analysis

The project explores relationships between applicant characteristics and historical loan approval outcomes.

Visualizations include:

* Loan approval distribution
* Applicant income distribution across approval outcomes
* Credit history vs. loan approval
* Education vs. loan approval
* Property area vs. loan approval

The analysis particularly examines the relationship between **credit history** and historical loan approval outcomes.

## Data Preprocessing

The preprocessing pipeline includes:

* Removing the `Loan_ID` identifier
* Handling missing numerical values using median imputation
* Handling missing categorical values using the most frequent value
* One-hot encoding categorical variables
* Standardizing numerical features

A Scikit-learn `Pipeline` and `ColumnTransformer` are used to keep preprocessing consistent during model training and cross-validation.

## Models Used

Three classification algorithms are compared:

### 1. Logistic Regression

Used as a simple and interpretable baseline classification model.

### 2. Decision Tree

A tree-based model that can capture non-linear relationships and is relatively easy to interpret.

### 3. Random Forest

An ensemble of decision trees designed to improve predictive performance and reduce overfitting compared with a single decision tree.

## 📈 Model Evaluation

The models are evaluated using:

* **Accuracy**
* **Precision**
* **Recall**
* **F1 Score**

The project also generates a **confusion matrix** and classification report for the selected model.

The best-performing model is selected based on **F1 Score** rather than assuming a particular algorithm will perform best.

## Stratified 5-Fold Cross-Validation

Stratified 5-fold cross-validation is used to obtain a more reliable estimate of model performance.

Stratification helps maintain a similar proportion of the two loan-status classes across the different folds.

The mean accuracy and standard deviation across the five folds are reported for each model.

## Hyperparameter Tuning

The Random Forest model is further optimized using **GridSearchCV**.

The following parameters are explored:

* Number of trees (`n_estimators`)
* Maximum tree depth (`max_depth`)
* Minimum samples required for splitting (`min_samples_split`)

The best parameter combination is selected based on cross-validation accuracy.

## Decision Tree Depth Analysis

Decision Tree models are also trained with different maximum depths:

```text
2
5
15
```

Training and testing accuracy are compared to observe how tree depth affects model performance and potential overfitting.

## Project Structure

```text
loan-prediction/
│
├── loan_prediction.py
└── README.md
```

## Key Learning Outcomes

Through this project, I practiced:

* Data cleaning and missing-value handling
* Exploratory data analysis
* Categorical feature encoding
* Feature scaling
* Classification algorithms
* Model evaluation
* Stratified cross-validation
* Hyperparameter tuning with GridSearchCV
* Building preprocessing pipelines
* Comparing model performance
* Identifying potential overfitting through model-depth analysis

## Author

**Arshpreet Ahuja**

This project is part of my collection of machine learning projects exploring practical applications of data analysis and machine learning.
