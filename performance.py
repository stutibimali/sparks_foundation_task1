#Performance Model
print("Mean Absolute Error",metrics.mean_absolute_error(y_test,y_pred))
print("Mean Squared Error",metrics.mean_squared_error(y_test,y_pred))
print("r2 Score",metrics.r2_score(y_test,y_pred))
Mean Absolute Error 4.183859899002975
Mean Squared Error 21.5987693072174
r2 Score 0.9454906892105356
predicted_score = regressor.predict(np.array([[9.25]]))
print(predicted_score)
[93.69173249]
print(regressor.coef_)
[9.91065648]
regressor.intercept_
2.018160041434683
# y = mx + c
​
m = regressor.coef_
c = regressor.intercept_
y = (m*9.25) + c
print(y)
[93.69173249]
print("Conclusion : From the above, If the student studies for 9.25 hrs, the predicted score is {}"
      .format((predicted_score[0])))
Conclusion : From the above, If the student studies for 9.25 hrs, the predicted score is 93.69173248737538
