Text to Speech Application
Overview

This Tkinter-based Text-to-Speech application allows users to convert text into speech. Users can customize the voice (Male/Female) and adjust the speech rate (Fast/Normal/Slow). The application also provides functionality to save the spoken text as an MP3 file.
Features

    Text-to-Speech Conversion: Convert input text to speech with customizable voice and speed settings.
    Voice Selection: Choose between Male and Female voices.
    Speed Control: Adjust the speed of the speech (Fast, Normal, Slow).
    Save to File: Save the converted speech to an MP3 file.

Requirements

    Python 3.x
    Tkinter
    pyttsx3
    Pillow (for image handling)

Installation

    Clone the repository:

    bash

git clone https://github.com/yourusername/your-repository.git

Navigate to the project directory:

bash

cd your-repository

Install the required packages:

bash

    pip install pyttsx3 Pillow

Usage

    Run the Application:

    bash

    python your_script_name.py

    Features:
        Text Area: Enter the text you want to convert to speech.
        Voice Selection: Choose between 'Male' and 'Female' voices from the dropdown menu.
        Speed Control: Select the speech speed from 'Fast', 'Normal', or 'Slow'.
        Speak Button: Click the 'SPEAK' button to hear the text spoken aloud.
        Save Button: Click the 'SAVE' button to save the spoken text as an MP3 file. A dialog will prompt you to select the save location.

Code Explanation

    Initialization: Sets up the Tkinter window and initializes the pyttsx3 engine.
    speaknow Function: Retrieves the text, selected voice, and speed, and then converts the text to speech.
    download Function: Saves the spoken text as an MP3 file to the user-selected directory.
    GUI Elements: Uses Tkinter widgets such as Label, Text, Combobox, and Button to create the user interface.

Screenshots

(Include screenshots of the application in use)
License

This project is licensed under the MIT License - see the LICENSE file for details.
Acknowledgements

    Tkinter: Python's standard GUI library.
    pyttsx3: Python library for text-to-speech conversion.
    Pillow: Python Imaging Library fork for handling images.
