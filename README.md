# Predicting Natural Gas Prices Using Machine Learning

## Project Overview

This project aims to develop a machine learning model capable of accurately predicting the price of natural gas. Natural gas prices are influenced by various factors such as supply-demand dynamics, geopolitical events, weather conditions, and economic indicators. By leveraging historical data and relevant contextual information, the model can learn patterns and relationships to forecast future price movements.

## Objectives

1. **Understand the Problem**: Determine whether the problem is a regression or classification problem.
2. **Data Preprocessing**: Clean and preprocess data using various techniques.
3. **Data Analysis**: Gain insights from the data through visualization.
4. **Model Application**: Apply appropriate machine learning algorithms.
5. **Model Evaluation**: Evaluate the accuracy of the model.
6. **Web Application Development**: Build a web application using the Flask framework for user interaction and prediction display.

## Project Structure

The project is organized as follows:

- **data/**: Directory containing the datasets used for training and testing the model.
- **models/**: Directory containing the trained machine learning models.
- **notebooks/**: Jupyter notebooks for data exploration, preprocessing, and model training.
- **static/**: Directory containing static files such as CSS.
- **templates/**: Directory containing HTML templates.
- **app.py**: Flask application file.
- **README.md**: Project documentation.

## Data Collection Plan

We collected comprehensive historical data and relevant contextual variables influencing natural gas prices, including:

1. **Historical Price Data**: From sources like EIA, IEA, Bloomberg, Quandl, and NYMEX.
2. **Supply and Demand Data**: Production levels, consumption data, import/export statistics.
3. **Geopolitical and Environmental Factors**: Political events, environmental regulations.
4. **Weather Data**: Heating and cooling degree days.
5. **Economic Indicators**: GDP growth rates, unemployment rates, industrial production indices.

## Data Preprocessing

Steps to preprocess the data include:

1. Importing necessary libraries.
2. Importing the dataset.
3. Handling missing data.
4. Label encoding and one-hot encoding for categorical variables.
5. Feature scaling.
6. Splitting data into training and testing sets.

## Model Building

We focused on regression algorithms suitable for the dataset, particularly Decision Tree Regression. The steps include:

1. Training the model with the preprocessed dataset.
2. Evaluating the model using metrics like Mean Squared Error (MSE) and R-squared.
3. Testing the model with real-world scenarios to ensure robustness.

## Web Application

We developed a web application using the Flask framework. The application includes:

- **app.py**: Main application file handling model prediction and routing.
- **templates/index.html**: User interface for input and displaying predictions.
- **static/css/styles.css**: Styling for the web interface.

### Deployment

We have deployed the project using Render's free subscription. You can access the application at [https://gaspricepredictor.onrender.com](https://gaspricepredictor.onrender.com).

Please note that due to the free subscription, the instance may spin down with inactivity, which can delay requests by 50 seconds or more.

## Future Scope

1. Explore advanced machine learning models like LSTM for better temporal predictions.
2. Implement real-time prediction capabilities.
3. Integrate the model with decision support systems.
4. Expand the geographical scope of the model.
5. Enhance the user interface for better usability and visualization.

## Conclusion

This project demonstrates the application of machine learning to predict natural gas prices, providing valuable insights and tools for stakeholders in the energy sector. By continuously improving the model and expanding its scope, we aim to create a robust and reliable prediction system.
