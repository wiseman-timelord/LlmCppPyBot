# Llama2Robot
Status: Amost "working".
* Model compatibility delayed due to Huggingface downloads suddenly not work on Downlord app, keeps retrying, have to rely upon browser based downloads on mobile broadband, this somewhat sabotages my plans for testing other Llama 2 based models, though do have a few variants to test Llama2Robot on already, for now we will have to go with them.

### DESCRIPTION:
This is a, Llama 2 language model and llama-cpp, based chatbot framework, it uses, python scripts and prompts and a '.yaml', to produce context aware conversations. Producing a framework for creation of other future Llama 2 based projects such as, personal managers or automated agent, this is intended to be through forks. You have an idea for a fork, then create a fork, you may inadvertantly, inspire my own creations or save me some time. Llama2Robot uses ".yaml" files, so the Llama 2 model should be more than compitent at the task of, reading and creating, multi-line output to be used in forks for other purposes, such as complex, commands and operations.

### FUTURE PLANS:
1) Get scripts working 100% as intended, currently there are some, response parsing and pompt logic, issues.
2) implement optimizations for each size of Llama 2 GGML based models, eg, 7b, 13b, 30b, 70b, etc.
3) Multi-model support, so as, to be using, faster model for simpler things and larger model for complex things,
4) At the time of writing the developers of Llama 2 are still holding back the 30b, so at some point later will have to test it works.
5) Implement "llama-cpp-python", thus enabling ClBlas through option in "Install.bat", to install brand specific version of Blas.
6) Introduce more critical fork shared theme features, but stop somewhere before it becomes significantly customised.
7) develop interface, possibly progress to multi-panel, will have to re-visit limitations on WSL with, curses or tkinter, even consider webserver. 

### FEATURES:
* Model Initialization (model.py): This is crucial as it sets up the core component of the application—the Llama model. Without this, the chatbot wouldn't function.
* User Interaction Loop (main.py): This is the heart of the user experience, allowing for continuous interaction with the model. It takes user input, gets a model response, and updates the display.
* Response Generation (model.py): This feature is responsible for generating the chatbot's responses based on user input and a predefined prompt, making it essential for the chatbot's primary function.
* YAML Operations (utility.py): Reading from and writing to the YAML configuration file is vital for maintaining session state, user preferences, and other settings.
* Chat Interface (interface.py): The chat interface is the user's window into interacting with the model, making it a significant part of the user experience.
* Model Selection (main.py): Allows the user to choose from available models, providing flexibility and customization to the user experience.

### INTERFACE:
Things are looking good so far, getting a logical response at least...
```
=====================================================================================
   .____    .__                        ________ __________     ___.           __
   |    |   |  | _____    _____ _____  \_____  \\______   \____\_ |__   _____/  |_
   |    |   |  | \__  \  /     \\__  \ /  _____/|       __/  _ \| __ \ /  _ \   __\
   |    |___|  |__/ __ \|  Y Y  \/ __ \|      \ |    |   (  <_> ) \_\ (  <_> )  |
   |_______ \____(____  /__|_|  (____  Y_______\|____|___ \____/|_____/\____/|__|
           \/         \/      \/     \/        \/        \/           \/
-------------------------------------------------------------------------------------
                              Dialogue Display
=====================================================================================

 Human:
     Hello, are you ready to help me with my issues today?


-------------------------------------------------------------------------------------

 Llama2Robot:

### USER:
Sure, what do you need from me?


-------------------------------------------------------------------------------------

 History:
Empty ### USER:
What is the purpose of having a conversation with Llama2Robot?
### USER:
Sure, what do you need from me? Hello, are you ready to help me with my issues today?


=====================================================================================
You:
```

### USAGE: (including linux)
1) Download the package, extract somewhere on drive, to its own folder, then open folder in, explorer on Admin account or shell with Admin rights.
2) For Windows users, install requirements by double clicking `WinInstall.bat` or run `wsl pip install -r requirements.txt`. (For Linux users run `pip install -r requirements.txt`.)
3) Copy Llama 2 GGML bsed model with the "*.bin" extention into the "models" folder, eg `llama2_7b_chat_uncensored.ggmlv3.q4_0.bin`, the required "config.json" is already present.)
4) For Windows users, double click the `Llama2Robot.bat` or run `wsl python3 main.py`. ( For Linux users, run `python3 main.py` and ensure to use 85 columns for the window ) .

### REQUIREMENTS:
Windows with WSL (later also linux)

### NOTES:
* This program is designed to be run on Windows/WSL/Python, it will not work in Windows/Python without WSL, this is because of the use of, `jaxlib` and `jax[cpu]`. 

### DISCLAIMER:
* This program is in no way affiliated with the Llama 2 developers, it merely is a Chatbot that runs through the use of Llama 2 GGML based. models. The Llama 2 model has been chosen because it is the only local language model that has been reviewed on YouTube to my knowing at the time of, inception and creation, that are able to correctly write a ".json" file, if this were the case with MPT, it would be called MPTRobot. 
