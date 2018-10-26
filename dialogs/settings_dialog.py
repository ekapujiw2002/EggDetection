from PyQt5.QtWidgets import QWidget, QSlider, QLabel, QApplication, QVBoxLayout, QLineEdit, QHBoxLayout, QGroupBox, \
    QFormLayout
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap, QIntValidator

import sys

class Settings(QWidget):

    def __init__(self):

        super().__init__()

        self.onlyInt = QIntValidator()

        self.initUI()


    def initUI(self):

        self.setWindowTitle('Settings')
        self.setFixedSize(300, 400)

        mainLayout = QVBoxLayout()

        self.lblBorderSize = QLabel('Border Size: 0')
        lblRadius = QLabel('Radius')
        lblArea = QLabel('Area')

        self.sldBorderSize = QSlider(Qt.Horizontal, self)
        self.sldBorderSize.setMinimum(20)




        self.lblBorderSize.setAlignment(Qt.AlignCenter)
        lblRadius.setAlignment(Qt.AlignCenter)
        lblArea.setAlignment(Qt.AlignCenter)


        self.sldBorderSize.setFocusPolicy(Qt.NoFocus)

        self.sldBorderSize.valueChanged[int].connect(self.changeValue)

        self.sldBorderSize.setValue(40)



        # add Layouts in Vertical Layout
        mainLayout.addWidget(self.lblBorderSize)
        mainLayout.addWidget(self.sldBorderSize)

        mainLayout.addWidget(lblRadius)

        # row group layout 1
        groupLayoutRadius = QGroupBox('')

        vRadiusLayout = QVBoxLayout()
        vRadiusLayout.addLayout(self.getLabelRadiusHorizontalLayout())
        vRadiusLayout.addLayout(self.getLineEditRadiusHorizontalLayout())
        groupLayoutRadius.setLayout(vRadiusLayout)

        mainLayout.addWidget(groupLayoutRadius)

        mainLayout.addWidget(lblArea)


        # row group layout 2
        groupLayoutArea = QGroupBox('')

        vAreaLayout = QVBoxLayout()
        vAreaLayout.addLayout(self.getLabelAreaHorizontalLayout())
        vAreaLayout.addLayout(self.getLineEditAreaHorizontalLayout())

        groupLayoutArea.setLayout(vAreaLayout)

        mainLayout.addWidget(groupLayoutArea)



        mainLayout.addSpacing(15)
        mainLayout.addStretch()



        self.setLayout(mainLayout)
        self.show()


    def getLabelRadiusHorizontalLayout(self):
        hLayout = QHBoxLayout()

        lblRadiusMin = QLabel()
        lblRadiusMax = QLabel()

        lblRadiusMin.setText('Min')
        lblRadiusMax.setText('Max')

        lblRadiusMin.setAlignment(Qt.AlignCenter)
        lblRadiusMax.setAlignment(Qt.AlignCenter)

        hLayout.addWidget(lblRadiusMin)
        hLayout.addWidget(lblRadiusMax)

        return hLayout

    def getLineEditRadiusHorizontalLayout(self):
        hLayout = QHBoxLayout()

        self.leRadiusMin = QLineEdit()
        self.leRadiusMax = QLineEdit()

        self.leRadiusMin.setText('10')
        self.leRadiusMax.setText('30')

        #self.leRadiusMin.textChanged[str].connect(self.textChange)
        #self.leRadiusMax.textChanged[str].connect(self.textChange)

        self.leRadiusMin.setMaxLength(3)
        self.leRadiusMax.setMaxLength(3)


        self.leRadiusMin.setValidator(self.onlyInt)
        self.leRadiusMax.setValidator(self.onlyInt)

        hLayout.addWidget(self.leRadiusMin)
        hLayout.addWidget(self.leRadiusMax)


        return hLayout

    def getLabelAreaHorizontalLayout(self):
        hLayout = QHBoxLayout()

        lblAreaMin = QLabel()
        lblAreaMax = QLabel()

        lblAreaMin.setText('Min')
        lblAreaMax.setText('Max')

        lblAreaMin.setAlignment(Qt.AlignCenter)
        lblAreaMax.setAlignment(Qt.AlignCenter)

        hLayout.addWidget(lblAreaMin)
        hLayout.addWidget(lblAreaMax)

        return hLayout

    def getLineEditAreaHorizontalLayout(self):
        hLayout = QHBoxLayout()

        self.leAreaMin = QLineEdit()
        self.leAreaMax = QLineEdit()

        self.leAreaMin.setText('370')
        self.leAreaMax.setText('1100')

        #self.leAreaMin.textChanged[str].connect(self.textChange)
        #self.leAreaMax.textChanged[str].connect(self.textChange)

        self.leAreaMin.setMaxLength(4)
        self.leAreaMax.setMaxLength(4)

        self.leAreaMin.setValidator(self.onlyInt)
        self.leAreaMax.setValidator(self.onlyInt)

        hLayout.addWidget(self.leAreaMin)
        hLayout.addWidget(self.leAreaMax)

        return hLayout

    def changeValue(self, value):
        self.lblBorderSize.setText('Border Size: ' + str(value))

    '''def textChange(self, value):
        sender = self.sender()

        if sender == self.leRadiusMin:
            print('leRadiusMin')
        elif sender == self.leRadiusMax:
            print('leRadiusMax')
        elif sender ==  self.leAreaMin:
            print('leAreaMin')
        elif sender == self.leAreaMax:
            print('leAreaMax')'''

    def getRadius(self):
        return (self.leRadiusMin.text(), self.leRadiusMax.text())

    def getArea(self):
        return (self.leAreaMin.text(), self.leAreaMax.text())

    def getBorderSizeValue(self):
        return self.sldBorderSize.value()