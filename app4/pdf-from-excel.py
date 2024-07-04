import pandas as pd
import glob
from fpdf import FPDF
from pathlib import Path

filepaths = glob.glob("invoices/*.xlsx")
for filepath in filepaths:
    df = pd.read_excel(filepath, sheet_name="Sheet 1")
    pdf = FPDF(orientation="P", unit="mm", format="A4")
    pdf.add_page()

    filename = Path(filepath).stem
    invoice_num = filename.split("-")[0]
    invoice_date = filename.split("-")[1]

    pdf.set_font("Times", style="B", size=18)
    pdf.cell(w=0, h=9, txt=f"Invoice number : {invoice_num}", ln=1, align="L")

    pdf.set_font("Times", style="B", size=18)
    pdf.cell(w=0, h=9, txt=f"Date : {invoice_date}", ln=1, align="L")

    pdf.ln(3)

    columns = df.columns
    columns = [item.replace("_", " ").title() for item in columns]
    pdf.set_font("Times", style="B", size=12)
    pdf.cell(w=30, h=8, border=1, align="L", txt=columns[0])
    pdf.cell(w=50, h=8, border=1, align="L", txt=columns[1])
    pdf.cell(w=50, h=8, border=1, align="L", txt=columns[2])
    pdf.cell(w=30, h=8, border=1, align="L", txt=columns[3])
    pdf.cell(w=25, h=8, border=1, align="L", txt=columns[4], ln=1)

    for index, rows in df.iterrows():
        pdf.set_font("Times", style="", size=10)
        pdf.cell(w=30, h=8, border=1, align="L", txt=str(rows["product_id"]))
        pdf.cell(w=50, h=8, border=1, align="L", txt=str(rows["product_name"]))
        pdf.cell(w=50, h=8, border=1, align="L", txt=str(rows["amount_purchased"]))
        pdf.cell(w=30, h=8, border=1, align="L", txt=str(rows["price_per_unit"]))
        pdf.cell(w=25, h=8, border=1, align="L", txt=str(rows["total_price"]), ln=1)

    total_sum = df["total_price"].sum()
    pdf.set_font("Times", style="", size=10)
    pdf.cell(w=30, h=8, border=1, align="L", txt="")
    pdf.cell(w=50, h=8, border=1, align="L", txt="")
    pdf.cell(w=50, h=8, border=1, align="L", txt="")
    pdf.cell(w=30, h=8, border=1, align="L", txt="")
    pdf.cell(w=25, h=8, border=1, align="L", txt=str(total_sum), ln=1)

    pdf.set_font("Times", style="B", size=14)
    pdf.cell(w=50, h=8, align="L", txt=f"Total Amount is : {total_sum} Rs")

    pdf.output(f"pdf-generated/{filename}.pdf")
