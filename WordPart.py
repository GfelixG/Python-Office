from docx import Document
from docx.enum.style import WD_STYLE_TYPE
from docx.enum.text import WD_TAB_ALIGNMENT
from docx.shared import Pt


document = Document()

data = {
    []
}

style = document.styles

h = style.add_style('h', WD_STYLE_TYPE.PARAGRAPH)
h.font.name = 'Arial'
h.font.size = Pt(14)
h.font.bold = True
h.font.underline = True

sections = document.sections
header = document.sections[0].header
header.add_paragraph("M  E  M  O  R  I  A  L          D  E  S  C  R  I  T  I  V  O", style='h')
header.alignment = WD_TAB_ALIGNMENT.CENTER

document.save('Memorial_Descritivo.docx')
