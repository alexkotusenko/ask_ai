

## PULL REQUESTS ARE MORE THAN WELCOME!!

## General
This program should work on Linux and MacOS machines.
This is because the filepaths use forward slashes unlike windows, which uses backslashes. 
I might implement this feature in the future.

## Guidelines
Go to the "commandconfig" file and add ONLY ONE LINE specifying the AI commadn to be ran to it.
The one I used was:

ollama run ollama2-uncensored "$2"

Make sure to replace your question with "$2" (including quotation marks). This is needed because $2 stands for the 3rd argument passed to the bash script, which happens to be the current question being asked.

Also make sure that the run and askquestion scripts are executable. This can be done on MacOS and Linux with the following command:

chmod +x run && chmod +x askquestion

### Note to developer: TODO
- [ ] handle error in python script where the file passed by the user is a directory and not a file (currently it just crashes the app)
- [ ] add support for Windows filepaths with backslashes
