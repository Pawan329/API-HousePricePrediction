# To load trained machine learning model
from joblib import load 

class house_price:
    def model(area, rooms, floors, garage):  # 4 parameters that will help to predict the price of house
        try:
            model = load('house_price_pred_model.pkl') # Loading pre-trained model
            price = model.predict([[area, rooms, floors, garage]]) # predicting price of house and storing in variable
            price = int(price)
            print(price)
            return price
        
        except Exception as e:
            return ({"Error: ": e})


# house_price.model(2000,2,1,1)