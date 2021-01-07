# Password Generator - Main Container

# Standard Libraries
import random

# External Libraries (Dependencies)
import PySimpleGUI as sg
import pyperclip

password = ""
input_define = ""
all_dict = ""
letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwyxz"
numbers = "1234567890"
symbols = r"~`!@#$%^&*()_-+={[}]|\:;',<.>/?" + '"'


def generate_password(pass_makeup):
    global input_define
    global password
    global all_dict
    all_dict = ""
    if pass_makeup[1] and pass_makeup[2] and pass_makeup[3]:
        input_define = "Dictionary contained letters, numbers, and symbols"
        all_dict += letters
        all_dict += numbers
        all_dict += symbols
        password = "".join(random.sample(all_dict, int(pass_makeup[0])))
    elif pass_makeup[1] and pass_makeup[2]:
        input_define = "Dictionary contained letters and numbers"
        all_dict += letters
        all_dict += numbers
        password = "".join(random.sample(all_dict, int(pass_makeup[0])))
    elif pass_makeup[2] and pass_makeup[3]:
        input_define = "Dictionary contained numbers and symbols"
        all_dict += numbers
        all_dict += symbols
        password = "".join(random.sample(all_dict, int(pass_makeup[0])))
    elif pass_makeup[1] and pass_makeup[3]:
        input_define = "Dictionary contained letters and symbols"
        all_dict += letters
        all_dict += symbols
        password = "".join(random.sample(all_dict, int(pass_makeup[0])))
    elif pass_makeup[1]:
        input_define = "Dictionary contained letters"
        all_dict += letters
        password = "".join(random.sample(all_dict, int(pass_makeup[0])))
    elif pass_makeup[2]:
        input_define = "Dictionary contained numbers"
        all_dict += numbers
        password = "".join([random.choice(all_dict) for _ in range(int(pass_makeup[0]))])
    elif pass_makeup[3]:
        input_define = "Dictionary contained symbols"
        all_dict += symbols
        password = "".join(random.sample(all_dict, int(pass_makeup[0])))
    else:
        sg.Popup("No checkboxes selected, try again!", auto_close=True,
                 auto_close_duration=5, title="PasswordGenerator-py")
    try:
        pyperclip.copy(password)
        print("Successfully copied password to clipboard")
    except Exception as exc:
        print("Returned the following exception when trying to copy to clipboard")
        print(str(exc))
        print("Traceback is as follows, please report this to the github")
        raise
    return password


theme = sg.theme("DarkBlue8")
layout = [[sg.Text("Password Length:"), sg.Slider(range=(8, 24), orientation='horizontal')],
          [sg.Text("Password Makeup:"), sg.Checkbox('Letters'), sg.Checkbox('Numbers'),
           sg.Checkbox('Symbols')],
          [sg.Text("_placeholder__placeholder__placeholder__placeholder_", visible=False, key="PASS")],
          [sg.Text("*Password is copied to clipboard", visible=False, key="COPY")],
          [sg.Button("Gen", focus=True), sg.Button("Exit")]]
window = sg.Window("PasswordGenerator-py", layout)

while True:
    event, values = window.read()
    if event == 'Gen':
        print("\n")
        print("Attempted generate")
        generate_password(values)
        print(f"Password length was selected as {int(values[0])} characters long")
        print(input_define)
        print(f"RETURNED: {password}")
        window.Element('PASS').Update(visible=True, value=f"Returned Password: {password}")
        window.Element('COPY').Update(visible=True)
    elif event == 'Exit' or event == sg.WIN_CLOSED:
        print("Generator cancelled.")
        window.close()
        exit(0)
