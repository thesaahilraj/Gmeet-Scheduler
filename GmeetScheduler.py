import streamlit as st
import pyautogui
import os
import webbrowser as wb
import datetime
import time

'''
Welcome to G-Meet Scheduler
'''

now = datetime.time()
date_today = datetime.date.today()

start_time = st.time_input('Enter the Meeting Time')
start_date = st.date_input('Enter the Meeting Date')
meet_code = st.text_input('Enter the Meeting Code')

chromepath = 'C:\Program Files (x86)\Google\Chrome\Application\chrome.exe %s'

button = st.button(' Schedule Now! ')
if button:
    st.text('Scheduled Successfully!')
    while True:

        if (start_time == now and start_date == date_today):
            wb.open('http://www.https://meet.google.com/' + meet_code)
            time.sleep(10)
            pyautogui.keyDown('ctrl')
            pyautogui.press('d')
            time.sleep(1)
            pyautogui.press('e')
            pyautogui.keyUp('ctrl')

            time.sleep(3)
            pyautogui.click(1452, 582)  # Exact 'JOIN NOW' Coordinates
            break
