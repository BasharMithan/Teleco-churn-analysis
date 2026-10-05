# Teleco Churn Analysis

An exploratory data analysis of a telecom company's customer base, using Python, Pandas, and Matplotlib/Seaborn. The goal is to clean the data, understand who churns, and turn the patterns into insights a business could act on.

## Problem Statement

Customer churn (customers leaving the service) is costly, because keeping an existing customer is generally cheaper than acquiring a new one. This project asks:

- Which customers are most likely to churn?
- How do contract type, tenure, pricing, and add-on services relate to churn?
- What practical steps could reduce churn?

## Dataset

- Source: [Telco Customer Churn on Kaggle (IBM sample dataset)](https://www.kaggle.com/datasets/blastchar/telco-customer-churn)
- Size: 7,043 customers, 21 columns
- Target variable: Churn (Yes/No). About 26.5% of customers churned, so the classes are imbalanced.

| Group | Columns |
| - | - |
| Demographics | `gender`, `SeniorCitizen`, `Partner`, `Dependents` |
| Account | `tenure`, `Contract`, `PaperlessBilling`, `PaymentMethod` |
| Services | `PhoneService`, `MultipleLines`, `InternetService`, `OnlineSecurity`, `OnlineBackup`, `DeviceProtection`, `TechSupport`, `StreamingTV`, `StreamingMovies` |
| Charges | `MonthlyCharges`, `TotalCharges` |
| Target | `Churn` |

The raw file is included in `data/raw/`. It can also be re-downloaded with the script in `source/`.
