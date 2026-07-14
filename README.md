# Cyber Threat Intelligence - Machine Learning Classification

## CMP7239 Applied Machine Learning Coursework

**Student ID:** 25198619

---

## 📋 Project Overview

This project applies machine learning techniques to classify and prioritize malicious IP addresses using the **Global Cyber Threat Intelligence Dataset 2026**.

### Models Used:
- **Decision Tree** - Interpretable rule-based classification
- **Random Forest** - High accuracy ensemble learning
- **Isolation Forest** - Unsupervised anomaly detection

---

## 📊 Dataset

| Attribute | Details |
|-----------|---------|
| Source | Kaggle - Global Cyber Threat Intelligence Dataset 2026 |
| Records | 6,250 |
| Features | 16 |
| Format | CSV |

**Dataset Link:** [Global Cyber Threat Intelligence Dataset 2026](https://www.kaggle.com/datasets/chuneeb/global-cyber-threat-intelligence-dataset-2026)


---

## 📊 Results

| Model | Accuracy | Precision | Recall | F1-Score |
|-------|----------|-----------|--------|----------|
| Decision Tree | 1.0000 | 1.0000 | 1.0000 | 1.0000 |
| Random Forest | 1.0000 | 1.0000 | 1.0000 | 1.0000 |
| Isolation Forest | 0.9237 | 1.0000 | 0.9237 | 0.9603 |

**Key Finding:** Isolation Forest identified **477 anomalies** (7.63% of records).

---

## 🔧 Requirements

```bash
pip install pandas numpy scikit-learn matplotlib seaborn

# Navigate to code folder
cd code

# Run data exploration
python step1_load_data.py
python step2_view_data.py
python step3_data_types.py
python step4_missing_values.py
python step5_unique_values.py
python step6_value_counts.py
python step7_country_chart.py
python step8_weekday_chart.py
python step9_continent_chart.py
python step10_hour_chart.py
python step11_save_data.py
python step12_summary.py

# Run machine learning models
python ml_step1_load_data.py
python ml_step2_encode.py
python ml_step3_split.py
python ml_step4_decision_tree.py
python ml_step5_random_forest.py
python ml_step6_isolation_forest.py
python ml_step7_compare.py
python ml_step8_charts.py

🔗 Dataset Source
Global Cyber Threat Intelligence Dataset 2026 - Kaggle

📝 Author
Sahibjit Kaur
Student ID: 25198619
Module: CMP7239 - Applied Machine Learning
Birmingham City University



