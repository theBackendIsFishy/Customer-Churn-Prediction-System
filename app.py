import streamlit as st
import numpy as np
import pickle

# ----------------------------
# Load Model & Scaler
# ----------------------------
model = pickle.load(open("model.pkl", "rb"))
scaler = pickle.load(open("scaler.pkl", "rb"))

# ----------------------------
# Page Config
# ----------------------------
st.set_page_config(page_title="Churn Prediction", layout="wide")

st.title("📊 Customer Churn Prediction Dashboard")

# ----------------------------
# Sidebar Inputs
# ----------------------------
st.sidebar.header("🧾 Customer Inputs")

# Numerical
tenure = st.sidebar.number_input("Tenure (months)", min_value=0)
total_charges = st.sidebar.number_input("Total Charges", min_value=0.0)

# Mappings
online_security_map = {
    "No": 0,
    "No internet service": 1,
    "Yes": 2
}

tech_support_map = {
    "No": 0,
    "No internet service": 1,
    "Yes": 2
}

contract_map = {
    "Month-to-month": 0,
    "One year": 1,
    "Two year": 2
}

# Dropdowns
online_security_label = st.sidebar.selectbox(
    "Online Security", list(online_security_map.keys())
)
online_security = online_security_map[online_security_label]

tech_support_label = st.sidebar.selectbox(
    "Tech Support", list(tech_support_map.keys())
)
tech_support = tech_support_map[tech_support_label]

contract_label = st.sidebar.selectbox(
    "Contract Type", list(contract_map.keys())
)
contract = contract_map[contract_label]

predict_btn = st.sidebar.button("🔍 Predict")

# ----------------------------
# Main Layout (2 Columns)
# ----------------------------
col1, col2 = st.columns(2)

# ----------------------------
# Customer Summary Card
# ----------------------------
# with col1:
#     st.subheader("👤 Customer Summary")

#     st.markdown(f"""
#     <div style="
#         padding:15px;
#         border-radius:10px;
#         background-color:#f0f2f6;
#         ">
#         <b>Tenure:</b> {tenure} months <br>
#         <b>Total Charges:</b> ₹{total_charges:.2f} <br>
#         <b>Online Security:</b> {online_security_label} <br>
#         <b>Tech Support:</b> {tech_support_label} <br>
#         <b>Contract:</b> {contract_label}
#     </div>
#     """, unsafe_allow_html=True)
with col1:
    st.subheader("👤 Customer Summary")

    with st.container():
        st.markdown("### 🧾 Details")

        st.write(f"**Tenure:** {tenure} months")
        st.write(f"**Total Charges:** ₹{total_charges:.2f}")
        st.write(f"**Online Security:** {online_security_label}")
        st.write(f"**Tech Support:** {tech_support_label}")
        st.write(f"**Contract:** {contract_label}")
# ----------------------------
# Prediction Section
# ----------------------------
with col2:
    st.subheader("📢 Prediction Result")

    if predict_btn:

        # Prepare input
        input_data = np.array([[tenure, online_security, tech_support, contract, total_charges]])

        # Scale
        input_scaled = scaler.transform(input_data)

        # Predict
        prediction = model.predict(input_scaled)[0]
        probability = model.predict_proba(input_scaled)[0][1]

        # Output
        if prediction == 1:
            if probability > 0.75:
                st.error(f"🔴 High Risk ({probability*100:.1f}%)")
            elif probability > 0.60:
                st.warning(f"🟠 Medium Risk ({probability*100:.1f}%)")
            else:
                st.info(f"🟡 Low Risk ({probability*100:.1f}%)")
        else:
            st.success(f"🟢 Customer likely to stay ({(1-probability)*100:.1f}% confidence)")

        # Progress bar
        st.write("### 📈 Churn Probability")
        st.progress(int(probability * 100))
        st.write(f"{probability*100:.2f}% chance of churn")

    else:
        st.info("👈 Enter details in sidebar and click Predict")