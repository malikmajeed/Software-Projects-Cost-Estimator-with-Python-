import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# Set up Streamlit page configuration
st.set_page_config(
    page_title="Software Project Cost Estimator",
    page_icon="💻💰",
    layout="wide"
)


import base64
import streamlit as st

def get_base64_image(image_path):
    with open(image_path, "rb") as file:
        return base64.b64encode(file.read()).decode("utf-8")

# Base64 encoded images
malik_image_data = get_base64_image("./Malik Majeed Png.jpg")
musanif_image_data = get_base64_image("./Muhammad Musanif.png")  

# CSS Styling
st.markdown("""
    <style>
        .header-container {
            position: sticky;
            top: 0;
            background: linear-gradient(90deg, rgba(131,172,176,1) 0%, rgba(213,235,235,1) 47%, rgba(115,164,174,1) 100%);
            z-index: 1000;
            padding: 10px 20px;
            border-bottom: 2px solid #004080;
            display: flex;
            justify-content: space-between;
            align-items: center;
        }
        .profile {
            display: flex;
            align-items: center;
        }
        .profile img {
            paddings:0;
            border-radius: 50%;
            margin-right: 10px;
             width: 80px;
            height: 80px;
            object-fit: cover;
        }
        .profile-info{
        display:flex;
        flex-direction:column;
        justify-content: center;
        align-items: start;
        }
        .profile-info h4 {
            margin: 0;
            font-size: 20px;
            color: #004080;
        }
        .profile-info p {
            margin: 0;
            font-size: 16px;
            color: black;
        }
    </style>
""", unsafe_allow_html=True)

# Sticky Header with Base64 Images
st.markdown(f"""
    <div class="header-container">
        <div class="profile">
            <img src="data:image/jpeg;base64,{malik_image_data}" alt="Malik Majeed" style="width:50px;height:50px;"/>
            <div class="profile-info">
                <h4>Malik Majeed</h4>
                <p>22pwbcs0908</p>
            </div>
        </div>
        <div class="profile">
            <img src="data:image/jpeg;base64,{musanif_image_data}" alt="Muhammad Musanif" style="width:50px;height:50px;"/>
            <div class="profile-info">
                <h4>Muhammad Musanif</h4>
                <p>22pwbcs0927</p>
            </div>
        </div>
    </div>
""", unsafe_allow_html=True)


# Load dataset
# Cache dataset loading for efficiency
@st.cache_data
def load_data():
    return pd.read_csv('Software_Project_Cost_Estimator_Dataset.csv')

data = load_data()


# Train the model
X = data[['Lines_of_Code', 'Complexity', 'Team_Experience', 'Development_Time']]
y = data['Cost']
model = LinearRegression()
model.fit(X, y)

# Title and description
st.title("💻 Software Project Cost Estimator 💰")
st.markdown("""
Welcome to the Software Project Cost Estimator! Use this tool to predict the cost of your software project 
based on various parameters. Get insights into your dataset, visualize feature correlations, and estimate costs with ease!
""")

# Sidebar inputs
st.sidebar.header("🔧 Input Project Details")
lines_of_code = st.sidebar.number_input("Lines of Code (LOC)", min_value=500, max_value=50000, value=1000, step=500)
complexity = st.sidebar.select_slider("Complexity Level", options=[1, 2, 3, 4, 5], value=3)
team_experience = st.sidebar.number_input("Team Experience (Years)", min_value=1, max_value=15, value=5, step=1)
development_time = st.sidebar.number_input("Development Time (Months)", min_value=1, max_value=24, value=6, step=1)

# Predict button
if st.sidebar.button("💡 Estimate Cost"):
    input_data = np.array([[lines_of_code, complexity, team_experience, development_time]])
    cost_estimate = model.predict(input_data)
    st.success(f"Estimated Project Cost: **${cost_estimate[0]:,.2f}**")


st.subheader("📊 Dataset Insights")
st.write(data.describe())



st.subheader("📈 Distribution of Cost")
fig, ax = plt.subplots()
sns.histplot(data['Cost'], kde=True, ax=ax, color='blue')
ax.set_title("Distribution of Project Costs")
st.pyplot(fig)


st.subheader("🔍 Feature Correlations")
fig, ax = plt.subplots(figsize=(10, 6))
sns.heatmap(data.corr(), annot=True, cmap='coolwarm', ax=ax)
st.pyplot(fig)


st.markdown("---")

# Footer
st.markdown("""
**Created with ❤️. Thanks to Dr. Wajeeha Khalil - UET Peshawar**
""")
