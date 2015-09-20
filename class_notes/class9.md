# Class 9 Notes:  Basic Model Evaluation

* adding assert statements to encode your comments
* assert(data.numtweets> 1)
* bias variance
  * fig. 2 training data
  * fig. 3 the model/classification map
  * fig. 4 out of sample data (color coded with predictions)
  * fig. 5 predictions based on the training data
  * low bias - fits training data well, not necessarily test data
  * overfitting - low k; low bias, high variance; complex model
* unpacking
  * _, the_max = min_max([1,2,3])
  * the underscore lets developer know first variable is ignored
* train-test-split
  * train-test-split helps you pick your model
  * then use the optimal model to test against all of your data before releasing it to prod and using it on out-of-sample data
  * t-t-s has a high-variance nature to it
  * stratified sampling - tries to keep proportions of data
    * if 100 observations (80 guards, 10 forwards, 10 centers), when splitting, it’ll keep those proportions
* Linear Regression
  * feature selection
    * features that are highly correlated, best not to use both in mean square error
    * between weather vs humidity, better to use humidity because the data is continuous, more granular. weather only has 1,2,3,4 values
  * dummy encoding - less assumptions, but added more features, therefore increasing complexity of model, which could make model worse