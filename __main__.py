from Visor import windowApp, QtWidgets, QtCore, QtGui
from json import load
import sys

class MainApp(windowApp): 

    def __init__(self, parent=None, *args): 
        super(MainApp, self).__init__(parent=parent) 

        self.modo_fotos = False
        self.fotosOcultar = False
        self.num_x, self.num_y = 1255, 705
        self.cont_x, self.cont_y = 0, 0
        self.dis_x, self.dis_y = 5, 5

        self.atajos()
        self.ui.btn_maximizar.clicked.connect(self.visorMini)

    def borde_(self, modo=''):
        if modo == 'close':
            self.ui.fr_borde_bottom.close()
            self.ui.fr_borde_left.close()
            self.ui.fr_borde_right.close()
            self.ui.fr_borde_top.close()

        if modo == 'show':
            self.ui.fr_borde_bottom.show()
            self.ui.fr_borde_left.show()
            self.ui.fr_borde_right.show()
            self.ui.fr_borde_top.show()

    def atajos(self): 
        with open('info.json', 'r') as f: self.atajos_ = load(f)['atajos']

        def atajos_(info):
            return QtWidgets.QShortcut( QtGui.QKeySequence(info), self)

        self.sc_moveTo_centro = atajos_(self.atajos_['moveTo_centro'])        
        self.sc_moveTo_centro.activated.connect(lambda: self.move(-6, -5))
        
        self.sc_moveToLeft = atajos_(self.atajos_['moveToLeft'])        
        self.sc_moveToLeft.activated.connect(lambda: self.moveTo("Left"))

        self.sc_moveToRight = atajos_(self.atajos_['moveToRight'])        
        self.sc_moveToRight.activated.connect(lambda: self.moveTo("Right"))

        self.sc_moveToTop = atajos_(self.atajos_['moveToTop'])        
        self.sc_moveToTop.activated.connect(lambda: self.moveTo("Top"))
        
        self.sc_moveToBottom = atajos_(self.atajos_['moveToBottom'])        
        self.sc_moveToBottom.activated.connect(lambda: self.moveTo("Bottom"))
        
        self.sc_minimized = atajos_(self.atajos_['minimized'])    
        self.sc_minimized.activated.connect(self.showMinimized)
        
        self.sc_close_borde = atajos_(self.atajos_['close_borde'])    
        self.sc_close_borde.activated.connect(lambda: self.borde_('close'))
        
        self.sc_show_borde = atajos_(self.atajos_['show_borde'])
        self.sc_show_borde.activated.connect(lambda: self.borde_('show'))
        
        self.sc_cerrar = atajos_(self.atajos_['cerrar'])
        self.sc_cerrar.activated.connect(self.close)
        
        self.sc_runAnimacion = atajos_(self.atajos_['runAnimacion'])
        self.sc_runAnimacion.activated.connect(self.run_animacion)
        
        self.sc_stopAnimacion = atajos_(self.atajos_['stopAnimacion'])  
        self.sc_stopAnimacion.activated.connect(self.reiniciar_animacion)
        
        self.sc_VisorM = atajos_(self.atajos_['VisorMain'])
        self.sc_VisorM.activated.connect(self.visorMain)

        self.sc_VisorSecond = atajos_(self.atajos_['VisorMain2'])
        self.sc_VisorSecond.activated.connect(self.visorMini)

    def visorMini(self):
        if self.visor != "main-2":
            self.ui.fr_buttons.close()
            self.ui.lbl_name.close()
            self.visor = "main-2"

            self.resize(384, 254)
            self.ui.fr_fondo.setGeometry(QtCore.QRect(10, 9, 364, 234))

            self.ui.fr_borde_left.setGeometry(QtCore.QRect(5, 5, 20, 221))
            self.ui.fr_borde_right.setGeometry(QtCore.QRect(338, 5, 20, 225))
            
            self.ui.fr_borde_top.setGeometry(QtCore.QRect(5, 5, 351, 20))
            self.ui.fr_borde_bottom.setGeometry(QtCore.QRect(5, 210, 348, 20))

            num_x, num_y = 292, 204
            self.ui.paginaVisor.resize(num_x, num_y)
            self.ui.visor.resize(num_x, num_y)
            self.ui.stackedWidget.resize(num_x, num_y)
            self.ui.stackedWidget.move(35, 15)

    def indicar(self, func):
        if self.visor == "main-1":
            func()

        else: pass
    
    def moveTo(self, opc=""):
        x = self.geometry().x()
        y = self.geometry().y()

        sx = 10 if opc == "Left" else (-10 if opc == "Right" else 0)
        sy = -10 if opc == "Top" else (10 if opc == "Bottom" else 0)

        self.move(x+sx, y+sy)

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv) 
    window = MainApp() 
    window.show() 
    sys.exit(app.exec_())

#* Author: Francisco Velez