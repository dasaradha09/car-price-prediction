import streamlit as st
import pickle
import numpy as np
model_file=open('C:/projects/30days/day15/model.pkl','rb')
ss_file=open('C:/projects/30days/day15/ss.pkl','rb')
model=pickle.load(model_file)
ss=pickle.load(ss_file)

def predict(values):
    values=np.asarray(values)
    values=values.reshape(1,-1)
    predicted_value=model.predict(ss.transform(values))
    return predicted_value
def main():
    st.header('CAR PRICE PREDITION')
    year=st.text_input("enter car which year model")
    present_price=st.text_input("enter present price of car")
    kms_driven=st.text_input("enter how many kilometers you car driven")
    fuel_type=st.text_input("enter fuel type of car : 2 for petrol , 1 for diesel , 0 for cng")
    seller_type=st.text_input("enter 1 for you are dealer or 0 for if you are owner")
    transmision=st.text_input("enter transmission type 1 for manual 0 for automatic")
    owner=st.text_input("enter text of previous owners that car have:")
    lst=[year,present_price,kms_driven,fuel_type,seller_type,transmision,owner]
    enter=st.button('predict')
    if enter:
        predicted_price,values=predict(lst)
        predicted_price=round(predicted_price[0],2)
        s=str(predicted_price)+' lakhs'
        st.subheader(s)
    
if '__main__'==__name__:
    main()