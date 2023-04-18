import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
from sklearn.linear_model import LinearRegression, LogisticRegression
from sklearn.tree import DecisionTreeRegressor, DecisionTreeClassifier
from sklearn.ensemble import RandomForestRegressor, RandomForestClassifier
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score, accuracy_score

# set page title and layout
st.set_page_config(page_title='Machine Learning App', layout='wide')

# create sidebar to upload dataset and select X and y values
st.sidebar.title('Upload Dataset and Select Features')
uploaded_file = st.sidebar.file_uploader('Upload CSV', type=['csv'])
if uploaded_file is not None:
    data = pd.read_csv(uploaded_file)
    st.sidebar.write(data.head())
    x_cols = st.sidebar.multiselect('Select Features (X)', data.columns)
    y_col = st.sidebar.selectbox('Select Target Variable (y)', data.columns)

# create sidebar to select regression or classification
st.sidebar.title('Select Model Type')
model_type = st.sidebar.selectbox('Select Model Type', ['Regression', 'Classification'])

# define function to plot interactive EDA
def plot_data():
    st.title('Interactive EDA')
    fig = px.scatter_matrix(data[x_cols + [y_col]], dimensions=x_cols + [y_col], color=y_col, height=700)
    st.plotly_chart(fig)

# define function to train models and show comparison charts
def train_models():
    st.title('Model Comparison')
    if model_type == 'Regression':
        models = {'Linear Regression': LinearRegression(),
                  'Decision Tree Regression': DecisionTreeRegressor(),
                  'Random Forest Regression': RandomForestRegressor()}
        metrics = {'Mean Squared Error': mean_squared_error,
                   'Mean Absolute Error': mean_absolute_error,
                   'R-squared': r2_score}
    else:
        models = {'Logistic Regression': LogisticRegression(),
                  'Decision Tree Classification': DecisionTreeClassifier(),
                  'Random Forest Classification': RandomForestClassifier()}
        metrics = {'Accuracy': accuracy_score}
    results = pd.DataFrame(columns=['Model', 'Metric', 'Score'])
    for model_name, model in models.items():
        model.fit(data[x_cols], data[y_col])
        for metric_name, metric in metrics.items():
            score = metric(data[y_col], model.predict(data[x_cols]))
            results = results.append({'Model': model_name, 'Metric': metric_name, 'Score': score}, ignore_index=True)
    for metric_name in metrics.keys():
        fig = px.bar(results[results['Metric'] == metric_name], x='Model', y='Score', color='Model', title=metric_name)
        st.plotly_chart(fig)

# create main app
def main():
    st.title('Machine Learning App')
    if uploaded_file is not None:
        plot_data()
        if st.sidebar.button('Train Models'):
            train_models()

# run the app
if __name__ == '__main__':
    main()