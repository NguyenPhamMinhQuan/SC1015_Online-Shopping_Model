# Welcome to the Online-Shopping Model Repository!

## About

This is a Mini-Project for the module SC1015 (Introduction to Data Science and Artificial Intelligence) which focuses on online-shopping activities.

Source data retrieved from [eCommerce behavior data from multi category store by MICHAEL KECHINOV](https://www.kaggle.com/datasets/mkechinov/ecommerce-behavior-data-from-multi-category-store)

For more details on datasets, please view: [The Dataset Collections](https://github.com/NguyenPhamMinhQuan/SC1015_Online-Shopping_Model/blob/main/Dataset.md). 


## Table of Content

For detailed walkthrough of the code, please view the notebooks for each step of our analysis and the conclusion at the end of the final notebook. The notebook are as follow (please read them in order):
1. [Data Cleaning](https://github.com/NguyenPhamMinhQuan/SC1015_Online-Shopping_Model/blob/main/Data_Cleaning.ipynb)
2. [Data Mining and Visualization](https://github.com/NguyenPhamMinhQuan/SC1015_Online-Shopping_Model/blob/main/DataMining_and_Visualization.ipynb)
3. [Classification Tree Model](https://github.com/NguyenPhamMinhQuan/SC1015_Online-Shopping_Model/blob/main/ClassificationTree.ipynb)
4. [Random Forest Classification Model](https://github.com/NguyenPhamMinhQuan/SC1015_Online-Shopping_Model/blob/main/RandomForest.ipynb)
5. [XGBoost Classification Model](https://github.com/NguyenPhamMinhQuan/SC1015_Online-Shopping_Model/blob/main/XGBoost.ipynb)

  
## Contributors

- @NguyenPhamMinhQuan
- @dnyk7
- @Jwong611


## Problem Definition

- To predict the probability that a product that is already in cart is likely to be purchased by users.
- Which model would be the best to predict it?


## Data Cleaning, Mining and Visualization
#### 1. Data Cleaning:
We clean source data by removing all data rows with missing values. We then format the data such that every row entry represents a user interaction with one product in one particular user session. The event type is set to be the highest event possible (view(0), cart(1), or purchase(2), in that order) for that iteractions.\
In order to not lose information about previous actions, we append a new variable called activity_count which is the number of acitivities a users made during one particular session. Finally, we append user_session_count which indicate how many time the user have accessed the online shopping flatform before (a form of user's history).\
We then export Cart and Purchase event data only due to us unable to process the large amount of data had View events been included

#### 2. Data Mining and Visualization:
We perform exploratory data analysis on 9 varibles and their relationship with the event type to examine which variable is a good predictors for a purchase of cart item, namely:

1. Category of the product
2. Sub-category of the product (since this information is provided in our dataset).
3. Weekday: weekday of the event
4. Day of month: Date of event
5. Time period of the event: Morning (6am -2pm), Afternoon(2pm - 10pm) and Night(10pm - 6am)
6. User access history: Number of sessions accessed by user before this event. This show customer's loyalty or familiarity with the online shop.
7. Activity count: Number of activities user engage in in one session.
8. Brand of product
9. Price of product

Among the 9 variables, only 6 shown to be good or adequate predictors of the event type variable:

1. Weekday: weekday of the event
2. Day of month: Date of event
3. User access history: Number of sessions accessed by user before this event. This show customer's loyalty or familiarity with the online shop.
4. Activity count: Number of activities user engage in in one session.
5. Brand of product
6. Price of product

We will use these 6 predictors to build and train our classification models.

## Classification Models:
We used 3 classification models, all based on classification trees:

1. Classification Tree
2. Random Forest Classification
3. Extream Gradient Boost (XGBoost) Classification

All our model is an extension to the classification tree using ensemble 


## Conclusion

- There is a limit to classification accuracy using classification tree, regardless of the depth
- 
- Number of acitivities in a session (how active a user is on the online shopping platform) is the best predictor for purchases of cart items.
- Surprisingly, day of the 
- Resampling imbalanced data improved model performance especially on the minority class
- Logistic Regression did not perform well with non-linearly correlated variables
- Neural Networks along with SMOTEENN resampling method consistently did well in predicting good movies after 100 training attempts (around 72% accuracy, 70% recall)
- Yes, it is possible to predict if a movie is good with acceptable amount of accuracy and recall


## What did we learn from this project?

- Memory handling
- Neural Networks, Keras and Tensorflow
- Logistic Regression from sklearn
- API Usage
- Other packages such as tqdm, json, requests
- Collaborating using GitHub
- Concepts about Precision, Recall, and F1 Score


## References

- <https://www.kaggle.com/code/tshephisho/ecommerce-behaviour-using-xgboost/input>
- <https://slidesgo.com/theme/minimalist-business-slides#search-simple&position-6&results-3926&rs=search>
- <https://www.markdownguide.org/cheat-sheet/>
- <https://docs.github.com/en/repositories>
- <https://pandas.pydata.org/docs/reference/index.html>
- <https://numpy.org/doc/>
- <https://xgboost.readthedocs.io/en/stable/>
- <https://scikit-learn.org/stable/>
- <https://matplotlib.org/stable/index.html>
- <https://seaborn.pydata.org/>
- <https://towardsdatascience.com/ensemble-learning-bagging-boosting-3098079e5422>
- <https://medium.com/@thedatabeast/adaboost-gradient-boosting-xg-boost-similarities-differences-516874d644c6>
- <https://arxiv.org/pdf/2106.03253.pdf>
- <https://www.analyticsvidhya.com/blog/2016/03/complete-guide-parameter-tuning-xgboost-with-codes-python/>
- <https://docs.dask.org/en/stable/>
