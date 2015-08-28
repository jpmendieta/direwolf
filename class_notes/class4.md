# Class 4 Notes:  Exploratory Data Analysis

* Pandas!
  * panda tables have an index column (which is not considered part of the data)
  * can give index a col name — `index_col=‘user_id’`
  * **head** is like **limit** `users.occupation.value_counts().head(3)` returns top 3
    * alternate way to limit: `users.occupation.value_counts()[:3]`
  *  `users.age < 20` broadcasts <20 check across all the rows in the series
  