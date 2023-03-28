from PyQt5 import (
    QtMultimedia, QtMultimediaWidgets,
    QtWidgets, QtCore, QtGui 
)

class PushButtonHover(QtWidgets.QPushButton):

    def __init__(self, parent=None):
        QtWidgets.QPushButton.__init__(self, parent)
        
        self.setMouseTracking(True)
        self.posicionX = int
        self.posicionY = int

    def enterEvent(self, *event):
        self.posicionX = self.pos().x()
        self.posicionY = self.pos().y()
        
        self.animacionCursor = QtCore.QPropertyAnimation(self, b"geometry")
        self.animacionCursor.setDuration(100)
        self.animacionCursor.setEndValue(QtCore.QRect(self.posicionX-10, self.posicionY, 40, 20))
        self.animacionCursor.start(QtCore.QAbstractAnimation.DeleteWhenStopped)
        
    def leaveEvent(self, *event):
        self.animacionNoCursor = QtCore.QPropertyAnimation(self, b"geometry")
        self.animacionNoCursor.setDuration(100)
        self.animacionNoCursor.setEndValue(QtCore.QRect(self.posicionX, self.posicionY, 20, 20))
        self.animacionNoCursor.start(QtCore.QAbstractAnimation.DeleteWhenStopped)

class Ui_Form(object):
    
    def __style__(self):
        with open('style.qss', 'r') as f: txt = f.read()
        return txt

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1372, 774)
        
        Form.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        Form.setAttribute(QtCore.Qt.WA_TranslucentBackground)

        Form.setStyleSheet(self.__style__())

        self.fr_fondo = QtWidgets.QFrame(Form)
        self.fr_fondo.setGeometry(QtCore.QRect(9, 9, 1417, 765))
        self.fr_fondo.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.fr_fondo.setFrameShadow(QtWidgets.QFrame.Raised)
        self.fr_fondo.setObjectName("fondo")

        self.camara(Form)

        self.fr_images = QtWidgets.QFrame(Form)
        self.fr_images.setStyleSheet(
            'background: cyan;\n'
            'border-radius: 5px;'
        )
        self.fr_images.setGeometry(65, 40, 0, 0)
        
        self.lbl_name = QtWidgets.QLabel(self.fr_fondo)
        self.lbl_name.setObjectName(u"lbl_name")
        self.lbl_name.setCursor(QtGui.QCursor(QtCore.Qt.BlankCursor))
        self.lbl_name.setGeometry(QtCore.QRect(55, 675, 241, 60))
        self.lbl_name.setAlignment(QtCore.Qt.AlignCenter)

        self.fr_borde_left = QtWidgets.QFrame(self.fr_fondo)
        self.fr_borde_left.setGeometry(QtCore.QRect(5, 5, 20, 755))
        self.fr_borde_left.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.fr_borde_left.setFrameShadow(QtWidgets.QFrame.Raised)
        self.fr_borde_left.setObjectName("fr_borde_left")

        self.fr_borde_right = QtWidgets.QFrame(self.fr_fondo)
        self.fr_borde_right.setGeometry(QtCore.QRect(1340, 5, 20, 755))
        self.fr_borde_right.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.fr_borde_right.setFrameShadow(QtWidgets.QFrame.Raised)
        self.fr_borde_right.setObjectName("fr_borde_right")

        self.fr_borde_top = QtWidgets.QFrame(self.fr_fondo)
        self.fr_borde_top.setGeometry(QtCore.QRect(5, 5, 1355, 20))
        self.fr_borde_top.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.fr_borde_top.setFrameShadow(QtWidgets.QFrame.Raised)
        self.fr_borde_top.setObjectName("fr_borde_top")

        self.fr_borde_bottom = QtWidgets.QFrame(self.fr_fondo)
        self.fr_borde_bottom.setGeometry(QtCore.QRect(5, 740, 1355, 20))
        self.fr_borde_bottom.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.fr_borde_bottom.setFrameShadow(QtWidgets.QFrame.Raised)
        self.fr_borde_bottom.setObjectName("fr_borde_bottom")

        self.fr_buttons = QtWidgets.QFrame(self.fr_fondo)
        self.fr_buttons.setGeometry(QtCore.QRect(602, 45, 160, 70))
        self.fr_buttons.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.fr_buttons.setFrameShadow(QtWidgets.QFrame.Raised)
        self.fr_buttons.setObjectName("fr_buttons")

        self.btn_minimizar = PushButtonHover(self.fr_buttons)
        self.btn_minimizar.setGeometry(QtCore.QRect(30, 25, 20, 20))
        self.btn_minimizar.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_minimizar.setObjectName("btn_minimizar")

        self.btn_maximizar = PushButtonHover(self.fr_buttons)
        self.btn_maximizar.setGeometry(QtCore.QRect(70, 25, 20, 20))
        self.btn_maximizar.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_maximizar.setObjectName("btn_maximizar")

        self.btn_cerrar = PushButtonHover(self.fr_buttons)
        self.btn_cerrar.setGeometry(QtCore.QRect(110, 25, 20, 20))
        self.btn_cerrar.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.btn_cerrar.setObjectName("btn_cerrar")

        self.retranslateUi(Form)
        self.btn_cerrar.clicked.connect(Form.close)
        self.btn_minimizar.clicked.connect(Form.showMinimized)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Visor"))
        self.lbl_name.setText(_translate("Form", "Francisco Velez"))
    
    def camara(self, Form): 
        num_x, num_y = 1305, 705
        self.paginaVisor = QtMultimediaWidgets.QVideoWidget()
        self.paginaVisor.resize(num_x, num_y)
        
        self.visor = QtMultimediaWidgets.QCameraViewfinder(self.paginaVisor)
        self.visor.resize(num_x, num_y)

        self.stackedWidget = QtWidgets.QStackedWidget(self.fr_fondo)
        self.stackedWidget.addWidget(self.paginaVisor)
        self.stackedWidget.resize(num_x, num_y)
        self.stackedWidget.move(30, 30)

        videoDevicesGroup = QtWidgets.QActionGroup(Form)
        videoDevicesGroup.setExclusive(True)

        dispositivoCamara = QtCore.QByteArray()

        for nombreDispositivo in QtMultimedia.QCamera.availableDevices():
            descripcion = QtMultimedia.QCamera.deviceDescription(nombreDispositivo)
            videoDeviceAction = QtWidgets.QAction(descripcion, videoDevicesGroup)
            videoDeviceAction.setCheckable(True)
            videoDeviceAction.setData(nombreDispositivo)

            if dispositivoCamara.isEmpty():
                dispositivoCamara = nombreDispositivo
                videoDeviceAction.setChecked(True)
                
        self.setCamara(dispositivoCamara)

    def setCamara(self, dispositivoCamara):
        if dispositivoCamara.isEmpty(): self.camara = QtMultimedia.QCamera()
        else: self.camara = QtMultimedia.QCamera(dispositivoCamara)

        self.capturaImagen = QtMultimedia.QCameraImageCapture(self.camara)
        self.camara.setViewfinder(self.visor)
        self.camara.isCaptureModeSupported(QtMultimedia.QCamera.CaptureStillImage)

        self.camara.start()
        self.paginaVisor.update()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()

    ui = Ui_Form()
    ui.setupUi(Form)

    Form.show()
    sys.exit(app.exec_())

#* Author: Francisco Velez
