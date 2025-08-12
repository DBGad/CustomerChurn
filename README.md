# Customer Churn Prediction 🚀  

[![Streamlit App](https://img.shields.io/badge/Live%20Demo-Streamlit-brightgreen?logo=streamlit)](https://customerchurn-dbgad.streamlit.app/)  

**Customer Churn Prediction** is a complete **end-to-end machine learning project** that predicts the likelihood of a customer leaving a business.  
The project integrates **data preprocessing**, **deep learning model training** with TensorFlow/Keras, and an **interactive Streamlit web application** for real-time predictions.  

---

## 🌟 Features  
- **Data Preprocessing Pipeline**  
  - Handles missing values  
  - Encodes categorical variables  
  - Scales numerical features  
- **Model Training**  
  - Deep learning classifier using TensorFlow/Keras  
  - Trained on historical customer data to detect churn patterns  
- **Model & Pipeline Saving**  
  - Saves model as `model.h5`  
  - Saves preprocessing pipeline as `preprocessor.pkl`  
- **Interactive Web App**  
  - Built with Streamlit  
  - Users can input customer details and instantly get churn predictions  
  - Clean and simple UI for business-friendly usage  
- **Live Deployment**  
  - Access the running app here: **[Customer Churn App](https://customerchurn-dbgad.streamlit.app/)**  

---

## 🛠 Tech Stack  
- **Python 3.x**  
- **TensorFlow / Keras** – Model building and training  
- **Scikit-learn** – Data preprocessing and evaluation  
- **Pandas / NumPy** – Data manipulation  
- **Streamlit** – Web app development and deployment  
- **Matplotlib / Plotly** – Optional visualizations  

---

## 🚀 Installation & Usage  

1. **Clone the repository**  
```bash
git clone https://github.com/DBGad/CustomerChurn.git
cd CustomerChurn
```
2. **Create a virtual environment**

```bash
python -m venv venv
venv\Scripts\activate    # Windows
source venv/bin/activate # Mac/Linux
```
3. **Install dependencies**

```bash
pip install -r requirements.txt
```
3. **Run the Streamlit app locally**

```bash
streamlit run app.py
```
Then open the browser at http://localhost:8501.

## 📊 How It Works
Data Preprocessing – Input data is cleaned, encoded, and scaled via a ColumnTransformer.

Prediction Model – A trained neural network outputs the probability of churn.

User Interface – The Streamlit app takes user inputs, runs them through the pipeline and model, and displays results with visual cues.

## 🔗 Live Demo
👉 Try it here: https://customerchurn-dbgad.streamlit.app/

