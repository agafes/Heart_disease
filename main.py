import streamlit as st
import pickle
from datetime import datetime

startTime = datetime.now()
# import znanych nam bibliotek

filename = "model_heart_disease.sv"
model = pickle.load(open(filename, 'rb'))
# otwieramy wcześniej wytrenowany model

sex_d = {0: "Kobieta", 1: "Mężczyzna"}
chest_pain_type_d = {0: "ASY", 1: "ATA", 2:"NAP"}
resting_ecg_d =  {0:"ST",1:"Normal",2:"LVH"}
exercise_angina_d = {0:"Tak", 1:"Nie"}
st_slotpe_d = {0:"Down",1:"Flat",2:"Up"}
fastingbs_d = {0:"Nie",1:"Tak"}
# o ile wcześniej kodowaliśmy nasze zmienne, to teraz wprowadzamy etykiety z ich nazewnictwem

def main():
    st.set_page_config(page_title="Heart Disease Prediction")
    overview = st.container()
    left, middle, right = st.columns(3)
    prediction = st.container()

    st.image("https://cdn.pixabay.com/photo/2018/01/10/23/53/rabbit-3075088_960_720.png")

    with overview:
        st.title("Heart Disease Prediction")

    with left:
        sex_radio = st.radio("Płeć", list(sex_d.keys()), format_func=lambda x: sex_d[x])

        chest_pain_type_radio = st.radio("Typ bólu w klatce piersiowej", list(chest_pain_type_d.keys()), index=2,
                                  format_func=lambda x: chest_pain_type_d[x])

        fastingbs_radio = st.radio("Czy poziom cukru na czczo powyżej 120", list(fastingbs_d.keys()), format_func=lambda x: fastingbs_d[x])
        resting_ecg_radio = st.radio("EKG spoczynkowe", list(resting_ecg_d.keys()), format_func=lambda x: resting_ecg_d[x])

    with middle:

        exercise_angina_radio =st.radio("Dławica piersiowa wywołana wysiłkiem fizycznym", list(exercise_angina_d.keys()), format_func=lambda x: exercise_angina_d[x])
        st_slotpe_radio = st.radio("(oldpeak) obniżenie odcinka ST wywołane wysiłkiem fizycznym w stosunku do odpoczynku",
                                   list(st_slotpe_d.keys()), format_func=lambda x: st_slotpe_d[x])
        restingbp_slider = st.slider("Ciśnienie spoczynkowe", min_value=0, max_value=200)
        cholesterol_slider = st.slider("Cholesterol", min_value=0, max_value=603)



    with right:
        age_slider = st.slider("Wiek", value=1, min_value=28, max_value=77)
        maxhr_slider = st.slider("Maksymalne tętno", min_value=60, max_value=202)
        oldpeak_slider = st.slider("(oldpeak) obniżenie odcinka ST wywołane wysiłkiem fizycznym w stosunku do odpoczynku"
                                   , min_value=-2.6, max_value=6.2, step=0.1)

    data = [[sex_radio,chest_pain_type_radio,fastingbs_radio,resting_ecg_radio,exercise_angina_radio,st_slotpe_radio,restingbp_slider,
             cholesterol_slider,age_slider,oldpeak_slider]]
    heart_disease = model.predict(data)
    hd_confidence = model.predict_proba(data)

    with prediction:
        st.subheader("Czy taka osoba ma chorobę serca?")
        st.subheader(("Tak" if heart_disease[0] == 1 else "Nie"))
        st.write("Pewność predykcji {0:.2f} %".format(hd_confidence[0][heart_disease][0] * 100))


if __name__ == "__main__":
    main()

