# DATA 606 Capstone Project: Building Risk Prediction Models for Diabetes Using Machine Learning

Prepared by: Leslie Li, Satyaki Dixit, Shreshta Phogat

📖 [**Full Project Guide on Medium**](https://medium.com/@leslie.knightley/building-risk-predictions-models-for-diabetes-using-machine-learning-9e6513bf6b9d)
## Background

**Severity**
Diabetes is among the most prevalent chronic diseases in the United States, impacting millions of Americans each year and exerting a significant financial burden on the economy. 

**Scale**
The Centers for Disease Control and Prevention has indicated that as of 2018, 34.2 million Americans have diabetes and 88 million have pre-diabetes. Diagnosed diabetes cost roughly $327 million dollars and total costs with undiagnosed diabetes and pre-diabetes approaching $400 billion dollars annually.

**Significance**
Early diagnosis can lead to lifestyle changes and more effective treatment, making predictive models for diabetes risk important tools for public and public health officials.

## Literatrue Overview
- University of Rochester School of Medicine and Dentistry built risk prediction models for Type 2 Diabetes using supervised ML models such as SVM, Decision Tree, and Logistic Regression models. (Xie et al, 2019)
- Department of Mathematics and Statistics from York University used threshold method and the class weight to improve sensitivity - the proportion of diabetes patients correctly predicted by models such as Decision Tree and Random Forest. (Lai et al, 2019)
- Department of Endocrinology and Metabolism from Peking University People's Hospital found that sex, age, history of diabetes, waist circumference, BMI, SBP were important risk factors related to diabetes. (Zhou et al, 2013)
- Insufficient sleep duration and/or sleep restriction in the laboratory, poor sleep quality, and sleep disorders such as insomnia and sleep apnea have all been associated with diabetes risk (Grandner, 2016). 

## Two Challenges 
*Challenge 1:* There is considerable heterogeneity in previous studies regarding machine learning techniques used, making it challenging to identify the optimal one. 

*Challenge 2:* There is a lack of transparency about the features used to train the models, which reduces their interpretability, a feature utterly relevant to the doctor.

## Data Source
- [The Behavioral Risk Factor Surveillance System's survey responses in 2015](https://www.cdc.gov/brfss/annual_data/2015/pdf/overview_2015.pdf)
- Health-related telephone surveys collecting state data about U.S. residents regarding their health-related risk behaviors, chronic health conditions, and use of preventive services.

## Research Questions
- What risk factors are most predictive of diabetes risk?
- What is the association among different variables?
- Which ML models contribute to more accurate prediction?
- What are the optimal validation metrics to measure model performance?

## Methodology
- Select essential risk factors for analysis after literature review
- EDA with dichotomy and transformation
- Use multivariable weighted logistic regression models to measure associations among factors
- Apply supervised ML models and metrics

## Data Overview
### Shape
- 323 numerical features
  - 7 categorical features
  - 244 columns have missing values 
- 441,456 survey responses (rows)
- Not balanced with a size at 541.28 MB

## A Glimpse of Attributes
- High BP
- High cholesterol, cholesterol check
- BMI
- Smoke history, stoke history
- Coronary heart disease (CHD) or myocardial infarction
- Physical activity in past 30 days
- Fruit, vegetables, drinks consumption habit
- Health care coverage, doctor visit frequency, health scale
- Mental health
- Sex, age, education, income level
- Sleep/disordered breathing

## Web Application Overview

![demo_preview](https://user-images.githubusercontent.com/60702562/210373376-f2ca7a4c-599b-4b01-b89d-0e28c0fd8762.png)
