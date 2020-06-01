from reportlab.pdfgen.canvas import Canvas
from reportlab.lib.pagesizes import A4
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.lib import utils
from reportlab.platypus import SimpleDocTemplate, Table
from reportlab.platypus.tables import TableStyle
from reportlab.lib import colors

import count
import nftraf

t1 = count.tot()
t2 = nftraf.count()
t3 = round(t1 + t2, 2)
aW, aH = A4

numb = 21597
today = "18.05.2020" 
tdata = [['№', 'Наименование услуги:', 'Стоимость (руб):'], ['1', 'Мобильная связь', t1], ['2', 'Мобильный интернет', t2], ['', 'ИТОГО:', t3]]

canvas = Canvas("Schet.pdf", pagesize=A4)
pdfmetrics.registerFont(TTFont('FreeSans', 'FreeSans.ttf'))

canvas.setFont('FreeSans', 12)
img = utils.ImageReader('0001.jpg')
img_width, img_height = img.getSize()
aspect = img_height / float(img_width)
canvas.saveState()
canvas.drawImage('0001.jpg', 0, 0, width=600, height=(600 * aspect))
canvas.drawString(40, 790, "ПротяБанк")
canvas.drawString(70, 760, "101010101010")
canvas.drawString(200, 760, "010101010101")
canvas.drawString(40, 740, "Лабуда Иван Александрович")
canvas.drawString(370, 795, "27641971")
canvas.drawString(370, 780, "16384852134")
canvas.drawString(370, 760, "41264794469")

canvas.setFont('FreeSans', 20)
canvas.drawString(20, 690, "Счет на оплату № " + str(numb) + " от " + today + " г.")
canvas.line(20, 680, 550, 680)

canvas.setFont('FreeSans', 12)
canvas.drawString(20, 660, "Исполнитель: ПАО ВостокСвязь")
canvas.drawString(20, 640, "Заказчик: И.А. Лабуда")
canvas.drawString(20, 620, "Основание: Договор о предоставлении услуг связи №154862")

t = Table(tdata, style = [('FONT', (0,0),(-1,-1), 'FreeSans', 12),('GRID', (0,0), (-1,-1), 0.5, colors.black), ('BOX', (0,0),(-1,-1), 2, colors.black)], colWidths=[30, 390, 110])
t.wrapOn(canvas, aW, aH)
t.drawOn(canvas, 20, 520)

canvas.line(20, 500, 550, 500)
canvas.setFont('FreeSans', 12)
canvas.drawString(20, 480, "Руководитель:   Корк В. Д.")
canvas.drawString(20, 460, "Бухгалтер:   Норкин И. К.")


canvas.restoreState()
canvas.showPage()
canvas.save()
