#Performance Model
print("Mean Absolute Error",metrics.mean_absolute_error(y_test,y_pred))
print("Mean Squared Error",metrics.mean_squared_error(y_test,y_pred))
print("r2 Score",metrics.r2_score(y_test,y_pred))

predicted_score = regressor.predict(np.array([[9.25]]))
print(predicted_score)

print(regressor.coef_)

regressor.intercept_

# y = mx + c

m = regressor.coef_
c = regressor.intercept_
y = (m*9.25) + c
print(y)

print("Conclusion : From the above, If the student studies for 9.25 hrs, the predicted score is {}"
      .format((predicted_score[0])))

