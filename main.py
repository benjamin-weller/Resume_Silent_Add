import re
import sys
import os
from docx import Document
from docx.shared import Pt, RGBColor
from docx.enum.style import WD_STYLE_TYPE
import pyperclip


def change_to_dir():
    if (len(sys.argv) < 3 or not pyperclip.paste()):
        print("Please call the program in this format: programName pathToInputFile outputFileName\nAdditionally please have the text you would like added to the resume on your clipboard.")
    else:
        index_for_snipping = sys.argv[1].rfind("\\")
        #I have to increment the index because it includes the \ and I need to get rid of that
        input_file_name = sys.argv[1][index_for_snipping+1:]
        os.chdir(sys.argv[1][:index_for_snipping])
        return input_file_name

def insert_to_doc(file_name):
    document = Document(file_name)

    #Create a new style for me to use
    obj_styles = document.styles
    obj_charstyle = obj_styles.add_style('CommentsStyle', WD_STYLE_TYPE.CHARACTER)
    obj_font = obj_charstyle.font
    obj_font.size = Pt(1)
    obj_font.name = 'Times New Roman'
    obj_font.color.rgb = RGBColor(255,255,255)

    #String clensing, removing all white space that would just be "extra", trying to get everything on to one line
    string = re.sub(r"\s{1,}", " ", pyperclip.paste())

    document.add_paragraph().add_run(string, style='CommentsStyle')
    document.save(sys.argv[2])

if __name__ == "__main__":
    file_name = change_to_dir()
    insert_to_doc(file_name)