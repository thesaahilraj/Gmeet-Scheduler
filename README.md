# Gmeet-Scheduler
A streamlit based Python Script which lets user to Join a Scheduled Google meeting automatically with the camera off and microphone muted.

### INSTALLATION
1. Clone the Repository
` git clone https://github.com/thesaahilraj/Gmeet-Scheduler.git `

2. Open the Command Prompt and Download the Required Modules 
` pip install -r requirements.txt `

3. Now Execute the Streamlit File
` Streamlit run GMeetScheduler.py `

### How to Use :
1. Use the slider on the Sidebar as per Hour and Minute to Set the starting time.
2. Now Enter the Google Meet code on the Meeting Code Input field
3. Click on __Schedule Now__ and Relax.
It will automatically open up the browser with the meet link and will mute the microphone and turn off the camera and will then Automatically click on __Join Now__.

### Fixing Errors: 
If you face any error in the Join Now Part , 
Run ` join-now-posi.py ` 
Get the Join Now cursor Position in (x,y) term.
Now goto GmeetScheduler.py and Open it using an IDE 
Go to Line #65
`  pyautogui.moveTo(X, Y, 1.5, pyautogui.easeOutQuad) `
Enter the X and Y Location and Run the Program using Streamlit. 
