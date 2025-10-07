import streamlit as st
import pandas as pd
import joblib

# Load the trained model pipeline
try:
    model = joblib.load('cafe_sales_model.pkl')
except FileNotFoundError:
    st.error("Model file not found. Please run model_training.py first to generate the model file.")
    st.stop()


# --- Streamlit Page Configuration ---
st.set_page_config(
    page_title="Cafe Sales Forecaster",
    page_icon="☕",
    layout="centered" # Use centered layout for the base
)

# --- Custom CSS for Centering and Styling ---
st.markdown("""
<style>
    /* Center the title */
    h1 {
        text-align: center;
    }
    /* Center the subtitle markdown text */
    div[data-testid="stMarkdown"] p {
        text-align: center;
    }
    /* Styling for the prediction button */
    .stButton>button {
        width: 100%;
        border-radius: 10px;
    }
    /* Styling for the success message (prediction) */
    .stSuccess {
        background-color: #e0f2f1;
        border-radius: 10px;
        padding: 1rem;
        text-align: center;
        font-size: 1.2rem;
        font-weight: bold;
        margin-top: 1rem;
    }
</style>
""", unsafe_allow_html=True)


# --- UI Elements ---
st.title('☕ Cafe Sales Forecaster')
st.markdown("Predict the total amount a customer will spend based on their order details.")


# --- Two-Column Layout for Inputs ---
col1, col2 = st.columns(2)

with col1:
    item = st.selectbox(
        'Select Item',
        ('Coffee', 'Cake', 'Cookie', 'Salad', 'Smoothie', 'Tea', 'Juice', 'Sandwich')
    )
    quantity = st.number_input('Quantity', min_value=1, max_value=20, value=1, step=1)
    payment_method = st.selectbox(
        'Payment Method',
        ('Credit Card', 'Cash', 'Digital Wallet')
    )
    location = st.selectbox(
        'Location',
        ('Takeaway', 'In-store')
    )

with col2:
    weekday = st.selectbox(
        'Day of the Week',
        ('Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday')
    )
    day = st.slider('Day of the Month', 1, 31, 15)
    month = st.slider('Month', 1, 12, 6)
    is_weekend = st.checkbox('Is it a weekend?', value=(weekday in ['Saturday', 'Sunday']))


# --- Prediction Logic (Button is below the columns) ---
if st.button('Predict Total Spend', type="primary"):
    input_data = pd.DataFrame({
        'quantity': [quantity],
        'day': [day],
        'month': [month],
        'is_weekend': [is_weekend],
        'item': [item],
        'payment_method': [payment_method],
        'location': [location],
        'weekday': [weekday]
    })

    try:
        prediction = model.predict(input_data)
        predicted_spend = prediction[0]
        # Store prediction in session state to display it cleanly
        st.session_state.prediction = predicted_spend
    except Exception as e:
        st.error(f"An error occurred during prediction: {e}")
        st.session_state.prediction = None


# --- Display Prediction ---
# This part is outside the button's "if" block to keep the result visible
if 'prediction' in st.session_state and st.session_state.prediction is not None:

    st.success(f"Predicted Total Spend: ${st.session_state.prediction:.2f}")
