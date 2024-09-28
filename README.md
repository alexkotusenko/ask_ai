# AI question / answer script
This script aims to use locally installed language models to quickly get answers to your questions using only two file paths

> [!WARNING]  
> If you're on Windows, see the _Compatibility_ section below

## Usage
The entry point of this program is the _run_ script

It will prompt you to enter the filepath for the file containing a list of questions (one question per line, no empty lines, every line will be read) and the filepath for the file the answers will be dumped into. The answers will be appended to the end of the file, so there is no need to worry about information getting overwritten.

The script runs on the background, so you will regain control of your shell once you input the filepaths. 
If you're not able to regain control of the shell, press enter a couple times and see what happens

You can pass the file path for both files in two ways:
1. relative (ex: ```questions.txt``` or ```./questions.txt```)
2. absolute (ex: ```/home/username/Documents/questions.txt```)

> [!WARNING]
> Please refrain from using ```~``` or ```$HOME``` as a shortcut for the home directory, I don't think it works (use the full absolute filepath in that case)

## Setup Guidelines
1. #### Specifying the AI command

Go to the "commandconfig" file and add ONLY ONE LINE specifying the AI commadn to be ran to it.
The one I used was:

```bash
ollama run ollama2-uncensored "$2"
```

Make sure to replace your question with ```"$2"``` (**including quotation marks**). This is needed because ```"$2"``` stands for the 3rd argument passed to the bash script, which happens to be the current question being asked.

2. #### Making the scripts executable

Also make sure that the run and askquestion scripts are executable. This can be done on MacOS and Linux with the following command:

```bash
chmod +x run && chmod +x askquestion
```

3. #### (optional) Symbolic links

If you want to integrate this program into your workflow, you're welcome to do so by using symbolic links.
Just go to the directory you want to add the symbolic link to and run the following command

```bash
cd <folder/to/add/the/symbolic/link/to>
ln -s </path/to/ask_ai>/run <shortcut/name>
```

The symbolic link will not break the program (at least on Unix-based systems) and is the recommended approach to integrating this program into your workflow

## Compatibility
This program should work on Linux and MacOS machines.
This is because the filepaths use forward slashes unlike Windows, which uses backslashes. 
I might implement this feature in the future.


## Contributing
Pull requests are more than welcome.

### Note to developer: TODO
- [ ] handle error in python script where the file passed by the user is a directory and not a file (currently it just crashes the app)
- [ ] add support for Windows filepaths with backslashes
