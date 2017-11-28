from docx import Document
from docx.shared import Pt, RGBColor
from docx.enum.style import WD_STYLE_TYPE

document = Document('Resume.docx')

obj_styles = document.styles
obj_charstyle = obj_styles.add_style('CommentsStyle', WD_STYLE_TYPE.CHARACTER)
obj_font = obj_charstyle.font
obj_font.size = Pt(1)
obj_font.name = 'Times New Roman'
obj_font.color.rgb = RGBColor(255,255,255)
# obj_font.color.rgb = RGBColor(0,0,0) #Creates a black scheme

paragraph = document.add_paragraph().add_run('HELLO WORLD', style='CommentsStyle')
# sections = document.sections
# print(len(sections))
# for x in sections:
#     print(sections)

#header = sections[0].header

#header.text = 'HELLO WORLD'


document.save('WellerResume.docx')