import streamlit as st
import pyautogui
import os
import webbrowser as wb
from datetime import datetime
import time
import base64
'''
# Welcome to G-Meet Scheduler
### by @thesaahilraj
 
'''


@st.cache(allow_output_mutation=True)
def get_base64_of_bin_file(bin_file):
    with open(bin_file, 'rb') as f:
        data = f.read()
    return base64.b64encode(data).decode()


def set_png_as_page_bg(jpg_file):
    bin_str = get_base64_of_bin_file(jpg_file)
    page_bg_img = '''
    <style>
    body {
    background-image: url("data:image/jpg;base64,%s");
    background-size: cover;
    }
    </style>
    ''' % bin_str

    st.markdown(page_bg_img, unsafe_allow_html=True)
    return


set_png_as_page_bg('bg-image.jpg')

st.sidebar.header('Enter the Meeting Time')
hour = st.sidebar.slider('Enter Hour : ', min_value=00, max_value=23)
minute = st.sidebar.slider('Enter Minute: ', min_value=00, max_value=59)
seconds = st.sidebar.slider('Enter Seconds: ', min_value=00, max_value=59)
sched_time = str(hour) + str(minute) + str(seconds)

meet_code = st.text_input('Enter the Meeting Code')

chromepath = 'C:\Program Files (x86)\Google\Chrome\Application\chrome.exe %s'

button = st.button(' Schedule Now! ')
st.spinner()
if button:
    with st.spinner("Scheduling..."):
        time.sleep(3)
        st.success('Meet Scheduled!')
    while True:
        noww = datetime.now()
        if noww.strftime("%H%M%S") == sched_time:
            wb.open('https://meet.google.com/' + meet_code)
            time.sleep(7)
            pyautogui.hotkey('ctrl', 'd')
            time.sleep(2)
            pyautogui.hotkey('ctrl', 'e')

            time.sleep(2)
            pyautogui.moveTo(1345, 660, 1.5, pyautogui.easeOutQuad)
            pyautogui.click()  # Exact 'JOIN NOW' Coordinates
            break
st.stop()
