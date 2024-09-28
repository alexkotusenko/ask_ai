#!/usr/bin/python3

import subprocess
import sys
from pathlib import Path

# possible errors: FileNotFoundError


# ARGUMENTS PASSED TO THIS SCRIPT
# 0th: this python's file path (when we go deep on the symbolic link) - so ~/scripts/ask_ai/main.py
# 1st: the QUESTION filepath entered into the bash script as an either absolute or relative path
# 2nd: the ANSWER filepath entered into the bash script as an either absoltue or relartive filepath
# 3rd: the filepath of the FOLDER this SCRIPT was run FROM - could be anywere but ITS A FOLDER AND NOT A FILE

def get_filepaths():
    filepaths = {
        "question_filepath": "",
        "answer_filepath": ""
    }
    if (len(sys.argv) == 4):
        # print("4 arguments were passed. Assigning arguments to file paths and returning")
        filepaths["question_filepath"] = sys.argv[1]
        filepaths["answer_filepath"] = sys.argv[2]
        this_file_path = Path(sys.argv[0])
        this_files_parent_folder = str(this_file_path.parent)
        filepaths["askquestion_filepath"] = this_files_parent_folder+"/askquestion"
        return filepaths
    else:
        exit_w_error_code(406)

def validate_file_paths(filepaths):
    # this function either does nothing (good case)
    # or crashes the program (if a file is not found)
    
    # we have 2 cases here:
    # an absolute file path like /home/whatever ... 
    # or a relative file path (relative to the directory this script is called from which can be anywhere)
    # an absolute filepath always starts with a / 
    # a non absolute file path starts either with the file name or the ./ dir specifier
    for key in filepaths:
        filepath = filepaths[key]
        # bad case: filepath is empty
        if (filepath == ""):
            exit_w_error_code(406)
        # pre-process filepath depending on what it starts with
        if (not filepath.startswith("/")):
            # the filepath is relative
            # update filepath
            # TODO i need to get the filepath of the fodler i am running the commadn from
            filepath = sys.argv[3]+"/"+filepath
            pass 
        else:
            pass # do not update the filepath
        # print(f"Checking filepath: {filepath}")
        try:
            with open(filepath, "r") as file:
                pass
        except FileNotFoundError:
            exit_w_error_code(404)

def exit_w_error_code(error_code):
    if (error_code == 406):
        print("ERROR: the provided input in unacceptable")
    elif (error_code == 404):
        print("ERROR: file not found")
    sys.exit(error_code)

def fetch_questions(filepath):
    questions = ""
    with open(filepath, "r") as file:
        questions = file.read()
    return questions

def pass_question(question_number, question, output_filepath, askquestion_filepath):
    # print(f"calling question with question number: {question_number} and the question being: {question}")
    subprocess.Popen([f"{askquestion_filepath}", str(question_number), question, output_filepath])

if __name__ == "__main__":
    # print(sys.argv)
    if len(sys.argv) != 4:
        exit_w_error_code(406)
    filepaths = get_filepaths() # crashes if anything but 3 arguments were provided
    validate_file_paths(filepaths) # crashes if a file is not found
    questions = fetch_questions(filepaths["question_filepath"])
    question_list = questions.strip().split("\n")
    # print(question_list)
    for i in range (len(question_list)):
        # argument $0 = ./askquestion
        # argument $1 = question number
        # argument $2 = question itself (string)
        # argument $3 = output file
        pass_question(i, question_list[i], filepaths["answer_filepath"], filepaths["askquestion_filepath"])
