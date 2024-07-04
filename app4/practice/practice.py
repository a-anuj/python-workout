from fpdf import FPDF
import glob
from pathlib import Path

pdf = FPDF(orientation="P", unit="mm", format="A4")
pdf.set_auto_page_break(auto=False, margin=0)
filepaths = glob.glob("files/*txt")
for filepath in filepaths:
    filename = Path(filepath)
    with open(filename, "r") as f:
        data = f.read()
    pdf.add_page()
    pdf.set_font("Times", style="B", size=20)
    pdf.cell(w=0, h=20, txt=f"{filename.stem.capitalize()}", ln=1, align="L")
    pdf.ln(2)
    pdf.set_font("Times", style="i", size=14)
    pdf.multi_cell(w=0, h=7, txt=data, align="L")
pdf.output("output.pdf")
