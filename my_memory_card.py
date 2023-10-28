#создай приложение для запоминания информации
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (Qapplicaton, QWidget, QHBoxLayout, QGroupBox, QRLadioButton, QPushButton)


app = Qapplication([])


window = QWidget()
window.setWindowTitle('Меню Card')


'''Интерфейс приложения Memory Card'''
bth_OK = QPushButton('Ответить') #кнопка ответа
ib_Question = QLabel('В каком году была основана Мщсква?')
rbtn_1 =QRLadioButton('1147')
rbtn_2 =QRLadioButton('1242')
rbtn_3 =QRLadioButton('1861')
rbtn_4 =QRLadioButton('1943')


layout_ans1 = QHBoxLayout()
layout_ans2 = QHBoxLayout()
layout_ans3 = QHBoxLayout()
layout_ans2.addWidget(rbtn_1)
layout_ans2.addWidget(rbtn_2)
layout_ans3.addWidget(rbtn_3)
layout_ans3.addWidget(rbtn_4)


layout_ans1.addLayout(layout_ans2)
layout_ans1.addLayout(layout_ans3)



