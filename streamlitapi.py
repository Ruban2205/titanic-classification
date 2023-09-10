import pickle
import streamlit as st  
import numpy as np 

model_file = pickle.load(open('notebook/model.pkl','rb'))

def pred_output(user_input): 
    model_input = np.array(user_input)
    ypred = model_file.predict(model_input.reshape(-1,7))
    return ypred[0]


def main(): 
    st.title("Titanic Classification - rubangino.in")

    # Input Variables 
    passenger_class = st.text_input("Enter the passenger class: ")
    sex = st.text_input("Enter your sex (Male/Female): ")

    if sex == "Male" or sex == "male": 
        sex = 0
    elif sex == "Female" or sex == "female": 
        sex = 1
    else: 
        st.error('Invalid Input!', icon="🚨")

    # st.success(sex)

    age = st.text_input("Enter your age: ")
    sibsp = st.text_input("Enter your Siblings: ")
    parch = st.text_input("Enter your parch: ")
    fare = st.text_input("Enter your Fare: ")
    embarked = st.text_input("Enter your Embarked: ")

    # Button to predict
    if st.button('Predict'): 
        user_input = [passenger_class, sex, age, sibsp, parch, fare, embarked]
        make_prediction = pred_output(user_input)  

        if make_prediction == 0: 
            make_prediction = "Not Survived :("
        elif make_prediction == 1: 
            make_prediction = "Survived :)"

        st.success(make_prediction)

if __name__ == '__main__': 
    main()


# SEX - Male=0 Female=1
# Embarked - C=Cherbourg Q=Queentown S=Southampton