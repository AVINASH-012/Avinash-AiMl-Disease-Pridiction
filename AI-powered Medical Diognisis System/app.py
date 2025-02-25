import streamlit as st
import pickle
from streamlit_option_menu import option_menu
from PIL import Image
img = Image.open('avinash.png')

# Change Name & Logo
st.set_page_config(page_title="Disease Prediction", page_icon=img)

# Hiding Streamlit add-ons
hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)

# Adding Background Image
background_image_url = "https://img.freepik.com/premium-photo/3d-digital-human-face-artificial-intelligence-concept-white-background-generative-ai_852169-1096.jpg"  # Replace with your image URL

page_bg_img = f"""
<style>
[data-testid="stAppViewContainer"] {{
background-image: url({background_image_url});
background-size: cover;
background-position: center;
background-repeat: no-repeat;
background-attachment: fixed;
}}

[data-testid="stAppViewContainer"]::before {{
content: "";
position: absolute;
top: 0;
left: 0;
width: 100%;
height: 100%;
background-color: rgba(0,0,0,-0.2);
}}
</style>
"""
st.markdown(page_bg_img, unsafe_allow_html=True)

# Load the saved models
models = {
    'parkinsons': pickle.load(open('MODELS/parkinsons_model.sav', 'rb'))
}

# Create a dropdown menu for disease prediction
selected = st.selectbox(
    'Select a Disease to Predict',
    ['Diabetes Prediction',
     'Heart Disease Prediction',
     'Parkinsons Prediction',
     'Lung Cancer Prediction',
     'Hypo-Thyroid Prediction']
)

def display_input(label, tooltip, key, type="text"):
    if type == "text":
        return st.text_input(label, key=key, help=tooltip)
    elif type == "number":
        return st.number_input(label, key=key, help=tooltip, step=1)


# Parkinson's Prediction Page
if selected == "Parkinsons Prediction":
    st.title(":orange[Parkinson's Disease]")
    st.write("### :green[Enter the following details to predict Parkinson's disease:]")

    fo = display_input('MDVP:Fo(Hz)', 'Enter MDVP:Fo(Hz) value', 'fo', 'number')
    fhi = display_input('MDVP:Fhi(Hz)', 'Enter MDVP:Fhi(Hz) value', 'fhi', 'number')
    flo = display_input('MDVP:Flo(Hz)', 'Enter MDVP:Flo(Hz) value', 'flo', 'number')
    Jitter_percent = display_input('MDVP:Jitter(%)', 'Enter MDVP:Jitter(%) value', 'Jitter_percent', 'number')
    Jitter_Abs = display_input('MDVP:Jitter(Abs)', 'Enter MDVP:Jitter(Abs) value', 'Jitter_Abs', 'number')
    RAP = display_input('MDVP:RAP', 'Enter MDVP:RAP value', 'RAP', 'number')
    PPQ = display_input('MDVP:PPQ', 'Enter MDVP:PPQ value', 'PPQ', 'number')
    DDP = display_input('Jitter:DDP', 'Enter Jitter:DDP value', 'DDP', 'number')
    Shimmer = display_input('MDVP:Shimmer', 'Enter MDVP:Shimmer value', 'Shimmer', 'number')
    Shimmer_dB = display_input('MDVP:Shimmer(dB)', 'Enter MDVP:Shimmer(dB) value', 'Shimmer_dB', 'number')
    APQ3 = display_input('Shimmer:APQ3', 'Enter Shimmer:APQ3 value', 'APQ3', 'number')
    APQ5 = display_input('Shimmer:APQ5', 'Enter Shimmer:APQ5 value', 'APQ5', 'number')
    APQ = display_input('MDVP:APQ', 'Enter MDVP:APQ value', 'APQ', 'number')
    DDA = display_input('Shimmer:DDA', 'Enter Shimmer:DDA value', 'DDA', 'number')
    NHR = display_input('NHR', 'Enter NHR value', 'NHR', 'number')
    HNR = display_input('HNR', 'Enter HNR value', 'HNR', 'number')
    RPDE = display_input('RPDE', 'Enter RPDE value', 'RPDE', 'number')
    DFA = display_input('DFA', 'Enter DFA value', 'DFA', 'number')
    spread1 = display_input('Spread1', 'Enter spread1 value', 'spread1', 'number')
    spread2 = display_input('Spread2', 'Enter spread2 value', 'spread2', 'number')
    D2 = display_input('D2', 'Enter D2 value', 'D2', 'number')
    PPE = display_input('PPE', 'Enter PPE value', 'PPE', 'number')

    parkinsons_diagnosis = ''
    if st.button("Parkinson's Test Result"):
        parkinsons_prediction = models['parkinsons'].predict([[fo, fhi, flo, Jitter_percent, Jitter_Abs, RAP, PPQ, DDP, Shimmer, Shimmer_dB, APQ3, APQ5, APQ, DDA, NHR, HNR, RPDE, DFA, spread1, spread2, D2, PPE]])
        parkinsons_diagnosis = "The person has Parkinson's disease" if parkinsons_prediction[0] == 1 else "The person does not have Parkinson's disease"
        st.success(parkinsons_diagnosis)