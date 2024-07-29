# Text to Speech Application

## Overview

This Tkinter-based Text-to-Speech application allows users to convert text into speech. Users can customize the voice (Male/Female) and adjust the speech rate (Fast/Normal/Slow). The application also provides functionality to save the spoken text as an MP3 file.

## Features

- **Text-to-Speech Conversion**: Convert input text to speech with customizable voice and speed settings.
- **Voice Selection**: Choose between Male and Female voices.
- **Speed Control**: Adjust the speed of the speech (Fast, Normal, Slow).
- **Save to File**: Save the converted speech as an MP3 file.

## Requirements

- Python 3.x
- Tkinter (usually included with Python)
- pyttsx3

## Code Explanation

- **Initialization**: Sets up the Tkinter window and initializes the pyttsx3 engine.
- **speaknow Function**: Retrieves the text, selected voice, and speed, and then converts the text to speech.
- **download Function**: Saves the spoken text as an MP3 file to the user-selected directory.
- **GUI Elements**: Uses Tkinter widgets such as Label, Text, Combobox, and Button to create the user interface.

## Acknowledgements

- **Tkinter**: Python's standard GUI library.
- **pyttsx3**: Python library for text-to-speech conversion.
- **Pillow**: Python Imaging Library fork for handling images.

   
