# WhatsApp Message Spammer

## Overview
This is a simple Python script that automates sending spam messages via WhatsApp Web. It uses `pyautogui` for simulating keyboard and mouse actions and `webbrowser` to open WhatsApp Web.

> **Warning:** Use this script responsibly and ensure that you have permission to send messages to the target phone number. Spamming can lead to your account being banned.

## Requirements
- Python 3.x
- `pyautogui` library
- A stable internet connection
- Access to WhatsApp Web on your default browser

### Direct Download
If you want to use the spammer without installing Python, you can download the executable file directly from the following link:
- [Download Spam Tool](https://www.mediafire.com/file/xbzp97xvhjuxtz1/spammer.exe/file)

## Installation (for Script Users)

1. **Install Python**: Ensure Python is installed on your system. You can download it from [python.org](https://www.python.org/downloads/).

2. **Install the required library**:
   Open your command line interface and run:
   ```bash
   pip install pyautogui
## Usage
1. **Clone or Download the Repository:** Download the script file (whatsapp_spammer.py) to your local machine.

2. **Run the Script:** Open your command line interface and navigate to the directory where the script is located. Then execute:
     ```bash
        python whatsapp_spammer.py

3. Input Details:
 - PhoneNumber: Enter the phone number with the country code (e.g., +1234567890).
 - Spam Text: Enter the message you want to spam.
 - Spam Count: Enter the number of times you want to send the message (default is 10).

4. Wait for WhatsApp Web: The script will open WhatsApp Web in your default browser. Make sure you are logged in.

5. Spamming: The script will automatically locate the message input field and start sending the specified message.

## Important Notes
 - The script uses images (type_field_dark.png and type_field_light.png) to locate the input field. Make sure these images are present in the same directory as the script. You may need to capture them if they don’t exist.
 - Adjust the confidence level if necessary based on your screen resolution and the input field's visibility.

## Troubleshooting
 - Input Field Not Found: If the script cannot find the input field, ensure that:
    - WhatsApp Web is fully loaded.
    - The images used for locating the field are accurate.
- Error Messages: Any other errors will be printed to the console. Follow the prompts for resolution.

## Disclaimer
  Using this script for spamming is against WhatsApp's terms of service. Use it at your own risk, and consider the ethical implications of your actions.

## License
This project is open-source and free to use. However, use it responsibly and ethically.

## Contributing
Feel free to submit issues or pull requests if you have suggestions for improvements or fixes.
