from fpdf import FPDF
import pandas

pdf = FPDF(orientation="P", unit="mm", format="A4")
pdf.set_auto_page_break(auto=False, margin=0)

df = pandas.read_csv(r"C:\Users\Anuj\Desktop\python-20app-course\app3\topics.csv")
for index, rows in df.iterrows():
    # Set the header
    pdf.add_page()
    pdf.set_font(family="Times", size=28, style="B")
    pdf.set_text_color(48, 86, 121)
    pdf.cell(w=0, h=28, ln=1, txt=rows["Topic"], border=0, align="L")
    # pdf.line(10,30,200,30)
    for i in range(40, 298, 10):
        pdf.line(10, i, 200, i)

    # Set the footer
    pdf.ln(245)
    pdf.set_font(family="Times", size=14, style="I")
    pdf.set_text_color(48, 86, 121)
    pdf.cell(w=0, h=10, txt=rows["Topic"], border=0, align="R")

    for i in range(1, int(rows["Pages"])):
        pdf.add_page()
        pdf.ln(270)
        pdf.set_text_color(48, 86, 121)
        pdf.set_font(family="Times", size=14, style="I")
        pdf.cell(w=0, h=10, ln=1, txt=rows["Topic"], border=0, align="R")
        for i in range(20, 298, 10):
            pdf.line(10, i, 200, i)

pdf.output("new-output-lined.pdf")
