# Software Project Cost Estimator

A web-based application designed to provide accurate cost estimations for software projects using data science techniques. The estimator predicts costs based on inputs such as the number of lines of code, complexity, team experience, and development time.

## Overview

Estimating software project costs is a critical step in project planning and resource allocation. Manual estimation methods are often time-consuming, prone to errors, and lack precision. This project automates the estimation process using regression models, ensuring reliable and accurate predictions while saving time and effort.

---

## Target Audience

- **Software Project Managers**: Efficient planning and budgeting.
- **Freelancers**: Streamlined cost predictions for client proposals.
- **Organizations**: Improved resource management.
- **Students and Researchers**: Practical insights into project cost estimation.

---

## Key Features

1. **User-Friendly Interface**: Built using Streamlit for an interactive experience.
2. **Real-Time Predictions**: Instant cost estimates based on user inputs.
3. **Data Visualization**: Insights into datasets, including statistical summaries and correlations.
4. **Dynamic Filtering**: Flexible analysis with customizable filters.
5. **Model Insights**: Performance metrics of the regression model.

---

## Input Parameters

1. **Lines of Code (LOC)**:
   - **Description**: Total lines of code in the project.
   - **Input**: Slider (500 - 50,000; Step: 500)
2. **Complexity**:
   - **Description**: Complexity level of the project (1: Low, 5: High).
   - **Input**: Dropdown (1 - 5)
3. **Team Experience**:
   - **Description**: Average years of experience of the development team.
   - **Input**: Slider (1 - 15; Step: 1)
4. **Development Time**:
   - **Description**: Estimated time to complete the project (in months).
   - **Input**: Slider (1 - 24; Step: 1)

---

## Libraries and Technologies Used

- **Python**: Core programming language.
- **Streamlit**: Web interface and deployment.
- **Pandas**: Data manipulation and analysis.
- **NumPy**: Numerical computations.
- **Seaborn & Matplotlib**: Data visualization.
- **Scikit-learn**: Regression model implementation.

---

## Approach

1. **Data Preprocessing**:
   - Loaded and cleaned the dataset.
   - Removed missing values and constant columns.
2. **Model Training**:
   - Implemented a Linear Regression model.
   - Used an 80-20 training-testing split.
3. **Model Evaluation**:
   - Metrics: Mean Squared Error (MSE), R² Score.
4. **UI Integration**:
   - Streamlit interface for dynamic user interaction.
5. **Visualization**:
   - Insights via heatmaps and statistical summaries.

---

## Implementation Steps

1. **Dataset Loading**:
   - CSV file: `Software_Project_Cost_Estimator_Dataset.csv`.
2. **User Input Handling**:
   - Sliders and dropdowns in the sidebar.
3. **Prediction**:
   - Function to calculate project cost using the trained model.
4. **Dynamic Dataset Filtering**:
   - Analyze subsets of the dataset.
5. **Visualization**:
   - Statistical summaries and correlation heatmaps.

---

## Outputs

1. **Cost Estimation**:
   - Predicted cost in USD.
2. **Dataset Insights**:
   - Count, mean, standard deviation, and more.
3. **Correlations**:
   - Visual relationships between dataset features.

---

## Future Enhancements

- **Advanced Models**:
  - Use Random Forests or Gradient Boosting for better accuracy.
- **Expanded Features**:
  - Add project domain, risk factors, or team size.
- **Export Options**:
  - Download cost estimations and dataset insights as reports.
- **Deployment**:
  - Host the app on platforms like AWS, GCP, or Streamlit Cloud.

---

## Conclusion

The **Software Project Cost Estimator** simplifies the cost estimation process with its intuitive interface and data-driven predictions. It offers a reliable, efficient tool to improve project planning and management.

---

## Authors

- **Malik Majeed** (22PWBCS0908)  
- **Muhammad Musanif** (22PWBCS0927)

---

## Submission

**University**: University of Engineering and Technology, Peshawar, Pakistan  
**Department**: Computer Science & IT  
**Instructor**: Prof. Wajeeha Khalil  
**Date**: January 15, 2025  
**Semester**: BS CS 5th  
**Section**: B
