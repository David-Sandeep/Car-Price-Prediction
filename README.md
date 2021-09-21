# Used-Car-Price-Prediction
#### As per reports Cars growth of new cars in the upcoming 5 years is an average of 3.5% while for used cars 5% and the ratio of used cars to new cars is increasing continuously. So the used cars market is increasing day by day and a consumer wants the best resale price of his car. Currently, if anyone wants to sell their car either they have to take their car to a respective company workshop or have to make an appointment for the company to get an estimate of the price. This process involves a lot of time and resources. Our Objective is to make a model for third-party companies that will make an estimate of the Price of the customer’s car directly from their online portal. This will save customers time and help the company to reduce its cost and also streamline the process of selling used cars.

  #### An end to end machine learning model for predicting the price of used cars.
  
# Deployed at: https://used-car-price-prediction0.herokuapp.com/

##  Tech Stack
• Front-End: HTML, CSS.

• Back-End: Flask.

• IDE: Jupyter notebook, Spyder.

## How to run this app
• First create a virtual environment by using this command

• conda create -n myenv python=3.6

• Activate the environment using the below command:

• conda activate myenv

• Then install all the packages by using the following command

• pip install -r requirements.txt

• Now for the final step. Run the app

• python app.py

## Dataset 
 https://www.kaggle.com/avikasliwal/used-cars-price-prediction from kaggle.
 
## Steps followed:
• loaded dataset from kaggle.

• Missing Values handled by mean,median.

• Data Analysis for Numerical Variables,continous Variables and Categorical Variables.

• Checked For Outliers and Handled.

• Feature Selection by Lasso Regression model.

• Performed Train Test split.

• Applied Linear Regression,Random Forest Regressor.

• used RandomizedSearchCV to perform hyperparameter tuning on Random forest regressor.

• saved the model and deployed in flask.






# • check a glimpse of the web app:
https://user-images.githubusercontent.com/54441866/133760223-a4acfd4c-5b0d-497b-b7cd-62308b9acebd.mp4





• This repository consists of files required to deploy a Machine Learning Web App created with Flask on Heroku platform.

