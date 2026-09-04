# LOAN PREDICTION

# 1. IMPORT LIBRARIES

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.compose import ColumnTransformer
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.model_selection import (
    train_test_split,
    StratifiedKFold,
    cross_val_score,
    GridSearchCV
)

from sklearn.linear_model import LogisticRegression
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier

from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    confusion_matrix,
    classification_report
)

# 2. LOAD AND UNDERSTAND THE DATASET

df = pd.read_csv("Loan prediction.csv")

print("=" * 60)
print("DATASET OVERVIEW")
print("=" * 60)

print("\nFirst 10 records:")
print(df.head(10))

print("\nDataset shape:")
print(df.shape)

print("\nFeatures:")
print(df.columns[:-1].tolist())

print("\nTarget variable:")
print(df.columns[-1])

print("\nDataset information:")
df.info()

print("\nMissing values:")
print(df.isnull().sum())

print("\nDescriptive statistics:")
print(df.describe())


# 3. DATA PREPROCESSING

# Remove Loan_ID because it is an identifier and does not
# provide useful predictive information.
df = df.drop("Loan_ID", axis=1)


# Separate features and target
X = df.drop("Loan_Status", axis=1)
y = df["Loan_Status"]


# Identify numerical and categorical columns
numerical_cols = [
    "ApplicantIncome",
    "CoapplicantIncome",
    "LoanAmount",
    "Loan_Amount_Term"
]

categorical_cols = [
    "Gender",
    "Married",
    "Dependents",
    "Education",
    "Self_Employed",
    "Credit_History",
    "Property_Area"
]


print("\nNumerical columns:")
print(numerical_cols)

print("\nCategorical columns:")
print(categorical_cols)


# 4. TRAIN-TEST SPLIT

# Stratification preserves the proportion of approved and
# rejected loans in both training and testing sets.

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    stratify=y,
    random_state=42
)

print("\nTraining set shape:", X_train.shape)
print("Testing set shape:", X_test.shape)


# 5. PREPROCESSING PIPELINE

from sklearn.impute import SimpleImputer


numerical_pipeline = Pipeline(
    steps=[
        ("imputer", SimpleImputer(strategy="median")),
        ("scaler", StandardScaler())
    ]
)


categorical_pipeline = Pipeline(
    steps=[
        ("imputer", SimpleImputer(strategy="most_frequent")),
        (
            "encoder",
            OneHotEncoder(
                handle_unknown="ignore",
                drop="first"
            )
        )
    ]
)


preprocessor = ColumnTransformer(
    transformers=[
        ("numerical", numerical_pipeline, numerical_cols),
        ("categorical", categorical_pipeline, categorical_cols)
    ]
)

# 6. DEFINE MACHINE LEARNING MODELS

models = {
    "Logistic Regression": LogisticRegression(
        max_iter=1000
    ),

    "Decision Tree": DecisionTreeClassifier(
        random_state=42
    ),

    "Random Forest": RandomForestClassifier(
        random_state=42
    )
}

# 7. TRAIN AND COMPARE MODELS

results = []

trained_models = {}


for name, model in models.items():

    pipeline = Pipeline(
        steps=[
            ("preprocessor", preprocessor),
            ("model", model)
        ]
    )

    pipeline.fit(X_train, y_train)

    y_pred = pipeline.predict(X_test)

    accuracy = accuracy_score(y_test, y_pred)
    precision = precision_score(
        y_test,
        y_pred,
        pos_label="Y"
    )
    recall = recall_score(
        y_test,
        y_pred,
        pos_label="Y"
    )
    f1 = f1_score(
        y_test,
        y_pred,
        pos_label="Y"
    )

    results.append([
        name,
        accuracy,
        precision,
        recall,
        f1
    ])

    trained_models[name] = pipeline


# Create comparison table
results_df = pd.DataFrame(
    results,
    columns=[
        "Model",
        "Accuracy",
        "Precision",
        "Recall",
        "F1 Score"
    ]
)

print("\n" + "=" * 60)
print("MODEL COMPARISON")
print("=" * 60)

print(
    results_df.to_string(
        index=False,
        float_format=lambda x: f"{x:.4f}"
    )
)


# 8. IDENTIFY BEST MODEL

best_model_row = results_df.loc[
    results_df["F1 Score"].idxmax()
]

best_model_name = best_model_row["Model"]

print("\nBest-performing model based on F1 Score:")
print(best_model_name)

print(
    f"F1 Score: {best_model_row['F1 Score']:.4f}"
)


# 9. CONFUSION MATRIX FOR BEST MODEL

best_model = trained_models[best_model_name]

best_predictions = best_model.predict(X_test)

cm = confusion_matrix(
    y_test,
    best_predictions,
    labels=["N", "Y"]
)

plt.figure(figsize=(7, 5))

sns.heatmap(
    cm,
    annot=True,
    fmt="d",
    cmap="Blues",
    xticklabels=["Rejected", "Approved"],
    yticklabels=["Rejected", "Approved"]
)

plt.xlabel("Predicted")
plt.ylabel("Actual")
plt.title(
    f"Confusion Matrix - {best_model_name}"
)

plt.tight_layout()
plt.show()


# 10. CLASSIFICATION REPORT

print("\n" + "=" * 60)
print("CLASSIFICATION REPORT")
print("=" * 60)

print(
    classification_report(
        y_test,
        best_predictions
    )
)


# 11. STRATIFIED 5-FOLD CROSS VALIDATION

print("\n" + "=" * 60)
print("STRATIFIED 5-FOLD CROSS VALIDATION")
print("=" * 60)

cv = StratifiedKFold(
    n_splits=5,
    shuffle=True,
    random_state=42
)


cv_results = []

for name, model in models.items():

    pipeline = Pipeline(
        steps=[
            ("preprocessor", preprocessor),
            ("model", model)
        ]
    )

    scores = cross_val_score(
        pipeline,
        X,
        y,
        cv=cv,
        scoring="accuracy"
    )

    cv_results.append([
        name,
        scores.mean(),
        scores.std()
    ])

    print(
        f"{name}: "
        f"Mean Accuracy = {scores.mean():.4f}, "
        f"Std = {scores.std():.4f}"
    )


cv_df = pd.DataFrame(
    cv_results,
    columns=[
        "Model",
        "Mean CV Accuracy",
        "Standard Deviation"
    ]
)


# 12. RANDOM FOREST HYPERPARAMETER TUNING

print("\n" + "=" * 60)
print("RANDOM FOREST HYPERPARAMETER TUNING")
print("=" * 60)


random_forest_pipeline = Pipeline(
    steps=[
        ("preprocessor", preprocessor),
        (
            "model",
            RandomForestClassifier(
                random_state=42
            )
        )
    ]
)


parameters = {
    "model__n_estimators": [50, 100, 200],
    "model__max_depth": [3, 5, 10],
    "model__min_samples_split": [2, 5, 10]
}


grid = GridSearchCV(
    random_forest_pipeline,
    parameters,
    cv=5,
    scoring="accuracy",
    n_jobs=-1
)

grid.fit(X_train, y_train)


print("\nBest parameters:")
print(grid.best_params_)

print(
    "\nBest cross-validation accuracy:",
    round(grid.best_score_, 4)
)


# Evaluate tuned Random Forest
tuned_predictions = grid.best_estimator_.predict(X_test)

tuned_accuracy = accuracy_score(
    y_test,
    tuned_predictions
)

tuned_precision = precision_score(
    y_test,
    tuned_predictions,
    pos_label="Y"
)

tuned_recall = recall_score(
    y_test,
    tuned_predictions,
    pos_label="Y"
)

tuned_f1 = f1_score(
    y_test,
    tuned_predictions,
    pos_label="Y"
)


print("\nTuned Random Forest Performance:")
print("Accuracy :", round(tuned_accuracy, 4))
print("Precision:", round(tuned_precision, 4))
print("Recall   :", round(tuned_recall, 4))
print("F1 Score :", round(tuned_f1, 4))


# 13. DECISION TREE DEPTH COMPARISON

print("\n" + "=" * 60)
print("DECISION TREE DEPTH COMPARISON")
print("=" * 60)


depths = [2, 5, 15]

dt_results = []


for depth in depths:

    dt_pipeline = Pipeline(
        steps=[
            ("preprocessor", preprocessor),
            (
                "model",
                DecisionTreeClassifier(
                    max_depth=depth,
                    random_state=42
                )
            )
        ]
    )

    dt_pipeline.fit(X_train, y_train)

    train_accuracy = dt_pipeline.score(
        X_train,
        y_train
    )

    test_accuracy = dt_pipeline.score(
        X_test,
        y_test
    )

    dt_results.append([
        depth,
        train_accuracy,
        test_accuracy
    ])


dt_df = pd.DataFrame(
    dt_results,
    columns=[
        "Max Depth",
        "Train Accuracy",
        "Test Accuracy"
    ]
)


print(
    dt_df.to_string(
        index=False,
        float_format=lambda x: f"{x:.4f}"
    )
)


# 14. FINAL

print("\n" + "=" * 60)
print("LOAN PREDICTION PROJECT - SUMMARY")
print("=" * 60)

print("Dataset size:", df.shape)

print("Models evaluated:")
for model_name in models:
    print("-", model_name)

print("\nBest model based on F1 Score:")
print(best_model_name)

print(
    f"F1 Score: {best_model_row['F1 Score']:.4f}"
)

print("\nTuned Random Forest Accuracy:")
print(f"{tuned_accuracy:.4f}")

print("\nProject completed successfully.")
print("=" * 60)
