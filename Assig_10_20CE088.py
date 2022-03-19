from fpdf import FPDF

# save FPDF() class into a
# variable pdf
pdf = FPDF()

# Add a page
pdf.add_page()

# set style and size of font
# that you want in the pdf
pdf.set_font("Arial", size=15)

# create a cell
t1 = "CHARUSAT UNIVERSITY OF SCIENCE & TECHNOLOGY"
pdf.cell(200, 10, txt=t1,ln=1, align='C')

# add another cell
t2 = "SEMESTER GRADE REPORT"
pdf.cell(200, 10, txt=t2,ln=2, align='C')

pdf.set_font("Arial", size=10)
# Open txt file in read mode
f = open("initials.txt", "r")

for i in f:
    pdf.cell(200, 10, txt = i, ln = 1, align = "L")
f = open("secondary.txt", "r")

for i in f:
    pdf.cell(200, 10, txt = i, ln = 1, align = "L")

f = open("ter.txt", "r")

for i in f:
    pdf.cell(200, 10, txt = i, ln = 1, align = "L")

f = open("secondary.txt", "r")

for i in f:
    pdf.cell(200, 10, txt = i, ln = 1, align = "L")

f = open("qua.txt", "r")

for i in f:
    pdf.cell(200, 10, txt = i, ln = 1, align = "L")

# save the pdf with name .pdf
pdf.output("my_sem3_result.pdf")