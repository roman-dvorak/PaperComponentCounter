from reportlab.lib.pagesizes import A3
from reportlab.pdfgen import canvas
from reportlab.lib.units import mm

# Název vytvářeného PDF souboru
pdf_filename = "meritko_A3.pdf"

# Vytvoření canvasu pro PDF
width, height = A3
c = canvas.Canvas(pdf_filename, pagesize=(height, width))

# Výška proužku měřítka v mm
strip_height = 30

# Počet proužků, které se vejdou na A3 list (výška A3 / výška proužku)
num_strips = int(height / mm / strip_height)

# Vytváření proužků měřítka
c.setFontSize(5)
c.setLineWidth(0.1)


for i in range(num_strips):
    # Nastavení pozice proužku
    strip_y_position = height - (i + 4.85) * strip_height * mm

    c.setLineWidth(0.1)
    c.line(0, strip_y_position-18, width, strip_y_position-18)

    # Vytvoření čar pro měřítko
    print(i)
    for j in range(400*i-5, 400*i+410, 1):  # Každý mm
        pj = j + 3*mm - 400*i
        c.setLineWidth(0.1)
        c.line(pj * mm, strip_y_position, pj * mm, strip_y_position + 2 * mm)
        c.setLineWidth(0.5)


        if j % 10 == 0:  # Hlavní značka po 8 mm
            c.line(pj * mm, strip_y_position, pj * mm, strip_y_position + 4.5 * mm)
            c.drawString(pj * mm - 1 * mm, strip_y_position - 2 * mm, f"{j}mm")
        

        if j % 40 == 0:  # Vedlejší značka po 4 mm
            c.setLineWidth(1)
            c.line(pj * mm, strip_y_position + 8 *mm, pj * mm, strip_y_position + 11.5 * mm)

        if j % 4 == 0:  # Vedlejší značka po 4 mm
            c.setLineWidth(0.1)
            c.line(pj * mm, strip_y_position + 8 *mm, pj * mm, strip_y_position + 11.5 * mm)
            c.drawString(pj * mm - 1 * mm, strip_y_position + 6 * mm, f"{int(j/4)}")

        if j % 80 == 0:  # Hlavní značka po 8 mm
            c.setLineWidth(1)
            c.line(pj * mm, strip_y_position + 15*mm, pj * mm, strip_y_position + 20 * mm)

        if j % 8 == 0:  # Hlavní značka po 8 mm
            c.setLineWidth(0.1)
            c.line(pj * mm, strip_y_position + 15*mm, pj * mm, strip_y_position + 20 * mm)
            c.drawString(pj * mm - 1 * mm, strip_y_position + 13 * mm, f"{int(j/8)}")


# Uložení PDF
c.save()
