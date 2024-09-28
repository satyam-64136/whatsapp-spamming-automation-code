from time import sleep
import pyautogui
import webbrowser

logo = """
        ███████╗ █████╗ ████████╗██╗   ██╗ █████╗ ███╗   ███╗
        ██╔════╝██╔══██╗╚══██╔══╝╚██╗ ██╔╝██╔══██╗████╗ ████║
        ███████╗███████║   ██║    ╚████╔╝ ███████║██╔████╔██║
        ╚════██║██╔══██║   ██║     ╚██╔╝  ██╔══██║██║╚██╔╝██║
        ███████║██║  ██║   ██║      ██║   ██║  ██║██║ ╚═╝ ██║
   by   ╚══════╝╚═╝  ╚═╝   ╚═╝      ╚═╝   ╚═╝  ╚═╝╚═╝     ╚═╝
   \n
   Note: Please make sure you are already logged into WhatsApp.
   \n
"""
print(logo)

# Get user input for phone number and spam details
PhoneNumber = int(input("Enter PhoneNumber with country code: "))
sleep(0.1)
spam_text = input('Enter the text which you want to spam: ')
spam_counter = int(input('Enter the number of times you want to spam (Default=10): ') or 10)
sleep(1)

# Open WhatsApp Web
webbrowser.open(f"https://wa.me/+{PhoneNumber}")
sleep(6)

try:
    location = (pyautogui.locateOnScreen("type_field_dark.png", confidence=0.6) or pyautogui.locateOnScreen('type_field_light.png', confidence=0.6))
    
    if location is None:
        raise Exception("Input field not found on the screen.")
    
    pyautogui.click(location)

    # Function to spam the message
    def spammer():
        for i in range(spam_counter):
            pyautogui.typewrite(spam_text)
            sleep(0.025)
            pyautogui.press("enter")
            sleep(0.025)

    spammer()

except Exception as e:
    print(f"Error: {e}")
input("Press Enter to exit...")