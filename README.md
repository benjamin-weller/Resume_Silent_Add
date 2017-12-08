# Resume_Silent_Add

# Idea:

The idea is simple, have a resume that gets past the automated scanners. I will do that by simply make my resume contain all the keywords they are looking for in the job description. The condition for success is simple, I want the machine to be able to read and find the keywords in my document, but I don’t want a human to be able to recognize the difference (and I don't want to have a two page resume). 

I’m taking a lot of information from: https://biginterview.com/blog/2015/03/applicant-tracking-system.html

# Solution:

Taking the above criteria, the solution becomes pretty clear, I need my resume to be indistinguishable to the human, but still contain the content. Thus the solution is easy, make the text invisible by making the font white while on a white page, and have the font size be super tiny such that it doesn’t spill onto a new page. Using my above source I know I don’t really want to add too much to headers and footers and as such the most reliable way would be to append it to the end of the document in a new paragraph.

My solution follows the idea outlined above, it takes the path to the resume, the name of the desired output, and appends tiny size one white font of whatever is on the clipboard to the end of the resume file.
