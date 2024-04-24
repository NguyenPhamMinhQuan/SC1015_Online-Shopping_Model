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
<div align="justify">We clean source data by removing all data rows with missing values. We then format the data such that every row entry represents a user interaction with one product in one particular user session. The event type is set to be the highest event possible (view(0), cart(1), or purchase(2), in that order) for that iteractions.</div>

<div align="justify">In order to not lose information about previous actions, we append a new variable called activity_count which is the number of acitivities a users made during one particular session. Finally, we append user_session_count which indicate how many time the user have accessed the online shopping flatform before (a form of user's history).</div>

<div align="justify">We then export Cart and Purchase event data only due to us unable to process the large amount of data had View events been included.</div>

#### 2. Data Mining and Visualization:
<div align="justify">We perform exploratory data analysis on 9 varibles and examine their relationship with the event type to identify which variable is a good predictors for a purchase of cart item, namely:</div>

1. Category of the product
2. Sub-category of the product (since this information is provided in our dataset).
3. Weekday: weekday of the event
4. Day of month: Date of event
5. Time period of the event: Morning (6am -2pm), Afternoon(2pm - 10pm) and Night(10pm - 6am)
6. User access history: Number of sessions accessed by user before this event. This show customer's loyalty or familiarity with the online shop.
7. Activity count: Number of activities user engage in in one session.
8. Brand of product
9. Price of product

<div align="justify">Among the 9 variables, only 6 shown to be good or adequate predictors of the event type variable:</div>

1. Weekday: weekday of the event
2. Day of month: Date of event
3. User access history: Number of sessions accessed by user before this event. This show customer's loyalty or familiarity with the online shop.
4. Activity count: Number of activities user engage in in one session.
5. Brand of product
6. Price of product

<div align="justify">We will use these 6 predictors to build and train our classification models.</div>

## Classification Models:
<div align="justify">We used 3 classification models, all based on classification trees:</div>

#### 1. Classification Tree
<div align="justify">A simple binary classification tree based on 6 predictors to predict event_type =['cart','purchase'].</div>
<div align="justify">We iterate through 20 of them to find the optimal depth of tree.</div>
<div align="justify">Finally we achieve a best accuracy of 62.46% at depth 19.</div>

#### 2. Random Forest Classification
<div align="justify">We seek to improve the classification Tree using a Random Forest Classifier. We build a model of 100 trees, each consider 2 random predictors among the 6.</div>
<div align="justify">The result, however, was lacking. We iterate through 10 Random Forest Classifiers (which take a very long time) and found that the best accuracy achieved was 63.04% at depth 16.</div>
<div align="justify">This lack of improvement can be attributed to the lack of overfitting problem in our classification tree and the relatively low variance in our sample (the 2 problems that Random Forest was designed to improve).</div>
<div align="justify">The lack of improvement and high computational cost make Random Forest Classifier a bad model for our problem.</div>

#### 3. Extreme Gradient Boost (XGBoost) Classification
<div align="justify">To further improve our model, we try using the Boosting method, namely: XGBoost classifier.</div>

<div align="justify">We observe that the model is more accurate (63.70% accuracy) and took far less time to train and test compared to the previous 2 models. We also observe that while we can increase the number of estimators (decision trees) used, the optimal is achieved at 1000. (This observation is made from a simple repetition of XGBoost Classifier with n_estimators =100, 500, 1000,2000,5000,10000 respectively)</div>

<div align="justify">However, there were room for improvement as we could have better tune our hyperparameters using cross-validation. However, literature review show that tuning of hyperparameters rarely significantly improve the accuracy.</div>

## Conclusion
#### Project outcome and Insights:
- There is a limit to classification accuracy using classification tree, regardless of the depth
- Thus, in order to enhance our model, we need to adopt a different algorithm or engineer better predictors (features)
- Number of acitivities in a session (how active a user is on the online shopping platform) is the best predictor for purchases of cart items. This is because the longer and more items users see and interacts, the more likely they will think about buying something, resulting in an eventual purchase.
- Surprisingly, day of the week (Mon-Fri) is also a good predictor. However, we cannot deduce a logical reason behind this due to limited information on the online shopping platform. This could have been due to customer demographic characteristics or a particular pattern in the shop operations (such as offering sales on Sunday-Monday)
- Price, brand, and user's familiarity (or history) with the platform do not contribute significantly to the prediction of purchases of cart items. This is because once an item is in cart, user's will no longer consider these variables as important considerations.
- XGBoost is one of the most efficient model to date and is the most suitable for building model on tabular data such as online shopping data.
- Yes, it is possible to predict customers' behaviours using machine learning with sufficient accuracy. Online shopping platform should employ machine learning model to boost their revenue.

#### Limitations and Future Directions
- Explore and classify the view-to-cart process. View represents 94% of activities on the platform and thus, being able to convert a small amount of views into cart or purchase will boost sale of the platform significantly. XGBoost can be applied to build a multi-class classifier without having to consider One-vs-Rest classifier approach.
- Scale our project by employing Dask to read and work on larger data files.
- Perform cross-validation and tuning for all models
- Engineer more features to examine such as BounceRate, Promotion and Sale, etc. given more data available.



## What did we learn from this project?

- Memory handling: StackOverflow, Del, and inplace=True
- Ensemble Modelling: Bagging and Boosting
- Tuning Hyperparameters with GridSearch
- Extreme Gradient Boost (XGBoost) Classifier
- Tuning of XGBoost using cross-validation (cv)
- Concepts of F-score and Feature Performance analysis (based on 'gain')
- Collaborating using GitHub


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
- <https://www.sciencedirect.com/topics/computer-science/ensemble-modeling>
- <https://towardsdatascience.com/machine-learning-multiclass-classification-with-imbalanced-data-set-29f6a177c1a>
