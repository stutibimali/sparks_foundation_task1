#Plotting
# Plotting the regression line
line = regressor.coef_*X+regressor.intercept_
​
# Plotting for the test data
plt.scatter(X, y)
plt.plot(X, line);
plt.show()
