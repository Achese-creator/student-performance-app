# Student Performance Predictor

This project is a machine learning web application that predicts a student's expected exam score based on academic, personal, family, and school-related factors. The final model was deployed using Streamlit and also classifies the predicted score using the Nigerian grading system.

## Project Overview

The goal of this project is to build a student performance prediction system that can estimate a student's exam score from key input features such as study hours, attendance, previous scores, sleep hours, parental involvement, access to resources, motivation level, and other related factors.

Two regression models were trained and compared:

- Linear Regression
- XGBoost Regressor

Linear Regression was selected as the final model because it performed better across the evaluation metrics.

## Dataset

The dataset used for this project was obtained from Kaggle:

[Student Performance Factors Dataset](https://www.kaggle.com/datasets/ayeshaseherr/student-performance)

The target variable is Exam_Score
Features Used
The model uses the following input features:
Hours Studied
Attendance
Sleep Hours
Previous Scores
Tutoring Sessions
Physical Activity
Parental Involvement
Access to Resources
Extracurricular Activities
Motivation Level
Internet Access
Family Income
Teacher Quality
School Type
Peer Influence
Learning Disabilities
Parental Education Level
Distance from Home
Gender
Preprocessing
The preprocessing stage included:

Standard scaling for selected numerical count-based features
Min-max scaling for bounded numerical features
Ordinal encoding for ordered categorical variables
One-hot encoding for unordered categorical variables
A preprocessing pipeline was used to ensure that the same transformations were applied consistently during training and prediction.

Models And Performance
Linear Regression
Mean Absolute Error: 0.4103
Mean Squared Error: 2.3038
Root Mean Squared Error: 1.5178
R-squared Score: 0.8258
XGBoost Regressor
Mean Absolute Error: 0.6133
Mean Squared Error: 2.6883
Root Mean Squared Error: 1.6396
R-squared Score: 0.7967
Linear Regression performed better because it had lower error values and a higher R-squared score. This suggests that the relationship between the dataset features and exam score was mostly linear.

Nigerian Grading System
The app classifies predicted scores using the classic Nigerian grading system:

Score Range	Grade
70 and above	A
60 - 69	B
50 - 59	C
45 - 49	D
40 - 44	E
39 and below	F
Streamlit App
The app allows users to enter student information and receive:

Predicted exam score
Grade classification
Performance interpretation
Technologies Used
Python
Pandas
NumPy
Scikit-learn
Joblib
Streamlit
GitHub
Streamlit Community Cloud
How To Run Locally
Clone the repository:

git clone https://github.com/Achese-creator/student-performance-app.git
Navigate into the project folder:

cd student-performance-app
Create a virtual environment:

python -m venv venv
Activate the virtual environment:

venv\Scripts\activate
Install the required packages:

pip install -r requirements.txt
Run the Streamlit app:

streamlit run app.py
Deployment
The app was deployed using Streamlit Community Cloud. Python 3.12 was used to ensure compatibility with the scikit-learn version used to save the trained model.

Project Reflection
This project covered the full machine learning workflow, including data preprocessing, model training, model evaluation, deployment, and user interface development. It showed the importance of selecting appropriate preprocessing methods, comparing models using suitable metrics, and ensuring compatibility between the training and deployment environments.
