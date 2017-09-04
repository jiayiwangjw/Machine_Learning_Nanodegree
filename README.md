# Udacity Machine Learning Nanodegree

Project implmentation for Udacity Machine Learning Nanodegree. These projects invovles different apsects of machine learning, including **Supervised Learning**, **Unsupervised Learning**, **Reinforcement Learning**, **Model Evaluation & Validation**, etc. 

Several python data analytic packages are used for the project implementation. 
* **Numpy**: Performs numerical operations. 
* **Pandas**: Data I/O, manipulation, and visualization.
* **Matplotlib, seaborn**: Data visualization
* **scikit-learn**: Builds, trains, and tests machine learning models.

Many datasets used in these projects can be found on [UC Irvine Machine Learning Repository](https://archive.ics.uci.edu/ml/index.php)

| Project                                                                                                                         | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
|---------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [titanic_survival_exploratio](https://github.com/jswong65/Machine_Learning_Nano_Degree/tree/master/titanic_survival_exploratio) | **An Intro project to Machine Learning.** Exploring various variables that can be applied to predict the survival rate of Titanic passengers, including socio-economic class, gender, age, fare, etc. The results implies **gender**, **age**, and **socio-economic class** can be the important variables for prediction.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| [boston_housing](https://github.com/jswong65/Machine_Learning_Nano_Degree/tree/master/boston_housing)                           | **Model Evaluation & Validation.** The goal of this project is Predicting Boston Housing Prices. <ul><li>Apply **DecisionTreeRegressor** to predict the housing prices.</li> <li>Evaluate a model with **R-squared** score, the **learning curve** and the **model complexity curve** - Bias-Variance Trade-Off.</li>  <li>Use **grid search**,  and **K-fold cross-validation** to find the parameters for optimizing a prediction model.</li></ul>                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| [finding_donors](https://github.com/jswong65/Machine_Learning_Nanodegree/tree/master/finding_donors)                            | **Supervised Learning.** The goal of this project is Finding Donors for Charity. <ul> <li>Data Preprocessing</li> <ul> <li>Log transformation for skewed continuous variables</li> <li>Data normalization for numerical variables (MinMaxScaler) </li> <li>One-hot encoding for categorical variables (pandas.get_dummies)</li> </ul> <li>Train, evaluate, and compare three different classifiers, including **KNeighborsClassifier**, **RandomForestClassifier** (bagging), **GradientBoostingClassifier** (boosting) with both accuracy and F-beta-score.</li> <li>Use **grid search** and **cross-validation** to find the parameters for model optimization.</li> <li>Use principal component analysis (PCA) to reduce the dimensions of the data</li> </ul>                                                                                                                                                                                                |
| [customer_segments](https://github.com/jswong65/Machine_Learning_Nano_Degree/tree/master/customer_segments)                     | **Unsupervised Learning**: The goal of this project is Creating Customer Segments.  <ul> <li>Feature Exploration</li> <ul> <li>Use **box plot** and **histogram** to examine the distribution of individual variables</li> <li>Leverage a **matrix of  scatter plot** and  a **heatmap** to study correlation between variables</li> <li>Apply **multiple coordinate ** to  investigate relationships between multiple variables</li> </ul> <li>Data Preprocessing</li> <ul> <li>Perform feature scaling (using natural logarithm) to reduce the skewness of highly skewed data</li> <li>Apply **Tukey's method** to identify the outliers to be removed</li> </ul> <li>Compare the **K-means clustering** and **Gaussian mixture model** (GMM) for data clustering.</li> <li>Apply **GMM** to perform data clustering, and leverage **silhouette coefficient** as well as **Bayesian information criterion** (BIC) to choose the number of clusters.</li> </ul> |
| [smartcab](https://github.com/jswong65/Machine_Learning_Nano_Degree/tree/master/smartcab)                                       | **Reinforcement Learning**: The goal of this project is Training a Smartcab to Drive <ul> <li></li> <li></li> <li></li> </ul>                                                                                                                                                       
