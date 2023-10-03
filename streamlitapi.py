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
    passenger_class = st.text_input("Enter the passenger class: (1/2/3)")

    sex = st.text_input("Enter your sex (Male/Female): ")
    if sex == "Male" or sex == "male": 
        sex = 0
    elif sex == "Female" or sex == "female": 
        sex = 1
    else: 
        st.error('Invalid Input!', icon="🚨")

    # st.success(sex)

    age = st.text_input("Enter their age: ")

    sibsp = st.text_input("Enter their Siblings: ")

    parch = st.text_input("Enter their parch: ")

    fare = st.text_input("Enter their ticket Fare: ")

    embarked = st.text_input("Enter their Port of Embarked: (C=Cherbourg | Q=Queentown | S=Southampton) ")
    if embarked == "C" or embarked == "c": 
        embarked = 1
    elif embarked == "S" or embarked == "s": 
        embarked = 0
    elif embarked == "Q" or embarked == "q": 
        embarked = 2
    else: 
        st.error("Invalid Input!", icon="🚨")

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