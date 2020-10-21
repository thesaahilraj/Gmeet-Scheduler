import streamlit as st
import pyautogui
import os
import webbrowser as wb
from datetime import datetime
import time

'''
Welcome to G-Meet Scheduler
'''


st.text('Enter the Meeting Time')
hour = st.slider('Enter Hour : ', min_value=00, max_value=23)
minute = st.slider('Enter Minute: ', min_value=00, max_value=59)
seconds = st.slider('Enter Seconds: ', min_value=00, max_value=59)
sched_time = str(hour) + str(minute) + str(seconds)

meet_code = st.text_input('Enter the Meeting Code')

chromepath = 'C:\Program Files (x86)\Google\Chrome\Application\chrome.exe %s'

button = st.button(' Schedule Now! ')
if button:
    st.text('Scheduled Successfully!')
    while True:
        noww = datetime.now()
        if noww.strftime("%H%M%S") == sched_time:
            wb.open('https://meet.google.com/' + meet_code)
            time.sleep(20)
            pyautogui.hotkey('ctrl', 'd')
            time.sleep(5)
            pyautogui.hotkey('ctrl', 'e')

            time.sleep(3)
            pyautogui.click(1452, 582)  # Exact 'JOIN NOW' Coordinates
            break
