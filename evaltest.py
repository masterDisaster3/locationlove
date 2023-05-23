import streamlit as st
from streamlit_js_eval import get_geolocation
import json


def clicked():
    start_tracking = True


button1 = st.button("Track", on_click = clicked)

start_tracking = False


    
while start_tracking:
    loc = get_geolocation()
    st.write(f"Your coordinates are {loc}")