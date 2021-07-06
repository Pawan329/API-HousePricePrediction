import mysql.connector
import pandas as pd

def fetchDataFromSql():
    try:
        mydb = mysql.connector.connect(host="localhost",
                                    user = "root",
                                    passwd = "root",
                                    database = "pawan_db")

        mycursor = mydb.cursor()
        mycursor.execute("select * from housedata")
        result = mycursor.fetchall()

        field_names = [i[0] for i in mycursor.description]
        # print(field_names)
        list_of_tuples = []

        for i in result:
            list_of_tuples.append(i)
            
        # print(list_of_tuples)
        df = pd.DataFrame(list_of_tuples, columns = field_names)
        return df

    except Exception as e:
        print(f"Error: {e}")

dataframe = fetchDataFromSql()
print(dataframe)

# Import the libraries for training data and linear regression
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

# We now instatiate a Linear Regression object
lr = LinearRegression()
x = dataframe[['Area', 'rooms','floors','garage']].values
y = dataframe['Price'].values

x_train, x_test, y_train, y_test = train_test_split( x, y, test_size=0.3, random_state=101)

# Now let's build the model using sklearn
lr.fit(x_train,y_train)

from joblib import dump, load

dump(lr, 'house_price_pred_model.pkl')
model_loading = load('house_price_pred_model.pkl') 
print("*"*50,"Prediction","*"*50)
prediction = model_loading.predict([[2800, 3, 2,1]])
print(prediction)

