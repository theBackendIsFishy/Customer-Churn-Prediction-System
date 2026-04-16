# 📊 Customer Churn Prediction App

A machine learning-powered web application built with **Streamlit** to predict whether a customer is likely to churn based on key features.

---

## 🚀 Project Overview

Customer churn is a critical problem for subscription-based businesses.
This project uses a **Logistic Regression model** to predict churn probability based on customer behavior and service usage.

The app provides:

* 📈 Real-time churn prediction
* 📊 Probability-based risk levels
* 🧾 Clean dashboard interface

---

## 🧠 Machine Learning Workflow

1. Data Preprocessing

   * Label Encoding for categorical features
   * Feature scaling using StandardScaler

2. Feature Selection

   * Selected top 5 important features:

     * Tenure
     * Online Security
     * Tech Support
     * Contract
     * Total Charges

3. Model Training

   * Logistic Regression Classifier

4. Evaluation

   * Accuracy comparison
   * Confusion Matrix & Visualization

---

## 🖥️ Streamlit App Features

* 🎯 User-friendly sidebar inputs
* 👤 Customer summary card
* 📢 Risk-based prediction output:

  * 🔴 High Risk
  * 🟠 Medium Risk
  * 🟡 Low Risk
  * 🟢 Safe
* 📈 Probability progress bar
* 🌙 Fully compatible with Dark/Light mode

---

## 📂 Project Structure

```
├── app.py              # Streamlit application
├── model.pkl           # Trained Logistic Regression model
├── scaler.pkl          # Scaler used for preprocessing
├── Telco_Customer_Churn_Dataset.csv         # Dataset (if included)
└── README.md           # Project documentation
```

---

## ⚙️ Installation & Setup

### 1. Clone Repository

```
git clone https://github.com/theBackendIsFishy/Customer-Churn-Prediction-System.git
cd churn-prediction
```

### 2. Install Dependencies

```
pip install -r requirements.txt
```

### 3. Run Application

```
streamlit run app.py
```

---

## 🧪 Example Inputs

| Tenure | Online Security | Tech Support | Contract       | Total Charges |
| ------ | --------------- | ------------ | -------------- | ------------- |
| 1      | No              | No           | Month-to-month | 50            |
| 60     | Yes             | Yes          | Two year       | 5000          |

---

## 📊 Sample Output

* 🔴 High Risk (e.g., 85%) → Likely to churn
* 🟢 Safe (e.g., 90%) → Likely to stay

---

## 🛠️ Tech Stack

* Python
* Streamlit
* Scikit-learn
* Pandas
* NumPy
* Matplotlib

---

## 📌 Future Improvements

* 📉 Add ROC Curve visualization
* 🤖 Compare multiple models (Decision Tree, Random Forest)
* ☁️ Deploy on Streamlit Cloud
* 📊 Add interactive charts

---

## 🤝 Contributing

Contributions are welcome!
Feel free to fork the repo and submit a pull request.

---

## 📜 License

This project is open-source and available under the MIT License.

---

## 👨‍💻 Author

Himanshu
GitHub: https://github.com/theBackendIsFishy