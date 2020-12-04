#Making Prediction
print(X_test)
y_pred = regressor.predict(X_test)

com_df = pd.DataFrame({"Actual" : y_test,"Predicted" : y_pred}) 

com_df

plt.xlabel("Hours Studied")
plt.ylabel("Percentage of Marks")
plt.scatter(s_data.Hours,s_data.Scores,color='red',marker='*')
plt.plot(s_data.Hours,regressor.predict(s_data[['Hours']]), color='green')
