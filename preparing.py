#Preparing the Data
X = s_data.iloc[:, :-1].values
y = s_data.iloc[:, 1].values
X = s_data.iloc[:, :-1].values
y = s_data.iloc[:, 1].values
X_train, X_test, y_train, y_test = train_test_split(X,y,
                                        test_size=0.2, random_state=0)
regressor = LinearRegression()
regressor.fit(X_train, y_train)

