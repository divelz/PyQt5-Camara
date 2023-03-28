from Ui_visor import Ui_Form, QtWidgets, QtCore, QtGui

class windowApp(QtWidgets.QMainWindow): 

    def __init__(self, parent=None, *args): 
        super(windowApp, self).__init__(parent=parent) 
        self.visor = "main-1"
        self.runA = [True, True]

        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.dactos()
        
        #? Mover ventana
        self.ui.fr_fondo.mouseMoveEvent = self.mover_ventana
	
    ##? mover ventana
    def mousePressEvent(self, event):
        self.clickPosition = event.globalPos()

    def mover_ventana(self, event):
        try:
            if self.isMaximized() == False: 
                if event.buttons() == QtCore.Qt.LeftButton:
                    self.move(self.pos() + event.globalPos() - self.clickPosition)
                    self.clickPosition = event.globalPos()
                    event.accept()
        except: pass
    
    def dactos(self):
        self.animacion_2 = False
        self.opc = 'none'

        self.width_cont = 20
        self.width_ = self.ui.fr_borde_bottom.geometry().width()
        self.width_dis = self.width_ - self.width_cont

        self.height_cont = 20
        self.height_ = self.ui.fr_borde_left.geometry().height()
        self.height_dis = self.height_ - self.height_cont

        self.wm_cont = 0
        self.width_menu = self.ui.fr_buttons.geometry().width()

        self.name_cont = 0
        self.name_return = ''
        self.name = self.ui.lbl_name.text().split()

    #  ********** ********** Animaciones ********** ********** #
    def inicial_animacion(self): #* Animacion de imagenes
        if self.cont_x <= self.num_x-5: self.cont_x += 5

        if self.cont_y <= self.num_y-5 and self.cont_x <= 10 or \
            self.cont_y <= self.num_y-5 and self.cont_x >= (self.num_x-5//2): self.cont_y += 5
        
        self.ui.fr_images.setGeometry(65, 40, self.cont_x, self.cont_y)

        if self.cont_x == self.num_x and self.cont_y == self.num_y:
            self.ui.fr_images.setStyleSheet(
                f'background-image: url({self.nameArch[0][self.numArch]}); \n'
                'background-repeat: no-repeat; \n'
                'background-position: center center; \n'
                'border-radius: 10px;'
            )
            self.timerM.stop()
    
    def run_animacion(self):
        if self.opc != 'run':
            self.dactos()

            self.timer = QtCore.QTimer()

            if self.visor == "main-1" and self.runA[0]:
                self.timer.timeout.connect(self.animacion)

            if self.visor == "main-2" and self.runA[1]:
                self.timer.timeout.connect(self.animacionM1)
            
            self.timer.start(80)
            self.opc = 'run'

        else: self.opc = 'run'
    
    def animacion(self):
        self.runA[0] = False

        self.ui.lbl_name.setText(self.return_(self.name[0], self.name_cont))
        self.ui.fr_buttons.setGeometry(QtCore.QRect(602, 40, self.wm_cont, 70))

        self.ui.fr_borde_left.setGeometry(QtCore.QRect(5, 5, 20, 0))
        self.ui.fr_borde_right.setGeometry(QtCore.QRect(1340, 5, 20, 0))

        self.ui.fr_borde_bottom.setGeometry(QtCore.QRect(5, 740, self.width_cont, 20))
        self.ui.fr_borde_top.setGeometry(QtCore.QRect(self.width_dis, 5, self.width_cont, 20))

        if self.animacion_2: 
            self.animacion2()

        elif self.width_cont >= self.width_: 
            self.width_cont -= 5
            self.width_dis += 10

            self.ui.fr_borde_bottom.setGeometry(QtCore.QRect(5, 740, self.width_cont, 20))
            self.ui.fr_borde_top.setGeometry(QtCore.QRect(self.width_dis, 5, self.width_cont+5, 20))
            self.animacion_2 = True
            self.name_cont = 0
            
            self.timer.stop()
            self.timer.timeout.connect(self.animacion2)
            self.timer.start(75)

        else:
            self.width_cont += 20
            self.width_dis = self.width_ - self.width_cont

            if self.width_cont >= (self.width_+5)//2 and self.wm_cont <= 150:
                self.wm_cont += 10
            
            if self.verificar1(140, self.width_cont):
                self.name_cont += 1

    def animacion2(self):
        self.ui.lbl_name.setText('{0} {1}'.format(self.name[0], self.return_(self.name[1], self.name_cont) ))
        self.ui.fr_borde_left.setGeometry(QtCore.QRect(5, 5, 20, self.height_cont))
        self.ui.fr_borde_right.setGeometry(QtCore.QRect(1340, self.height_dis, 20, self.height_cont))

        if self.height_cont >= self.height_: 
            self.height_cont -= 5
            self.height_dis += 10

            self.ui.fr_borde_left.setGeometry(QtCore.QRect(5, 5, 20, self.height_cont))
            self.ui.fr_borde_right.setGeometry(QtCore.QRect(1340, self.height_dis, 20, self.height_cont-5))

            self.timer.stop()
            self.runA[0] = True
            self.opc = 'none'
            self.dactos()

        else: 
            self.height_cont += 20
            self.height_dis = self.height_ - self.height_cont
            
            if self.verificar1(140, self.height_cont):
                self.name_cont += 1
    
    def animacionM1(self):
        self.runA[1] = False

        self.ui.fr_borde_left.setGeometry(QtCore.QRect(5, 5, 20, 0))
        self.ui.fr_borde_right.setGeometry(QtCore.QRect(338, 5, 20, 0))

        self.ui.fr_borde_top.setGeometry(QtCore.QRect(5, 5, self.width_cont+8, 20))
        self.ui.fr_borde_bottom.setGeometry(QtCore.QRect(5, 210, self.width_cont+8, 20))

        if self.width_cont+20 >= self.width_: 
            self.timer.stop()
            self.timer.timeout.connect(self.animacionM2)
            self.timer.start(80)

        else:
            self.width_cont += 20
            self.width_dis = self.width_ - self.width_cont

    def animacionM2(self):
            self.ui.fr_borde_left.setGeometry(QtCore.QRect(5, 5, 20, self.height_cont))
            self.ui.fr_borde_right.setGeometry(QtCore.QRect(338, 5, 20, self.height_cont+5))

            if self.height_cont >= self.height_-1: 
                self.timer.stop()
                self.runA[1] = True
                self.opc = 'none'

            else: 
                self.height_cont += 20
                self.height_dis = self.height_ - self.height_cont
    
    def reiniciar_animacion(self):
        try: self.timer.stop()
        except: pass

        if self.visor == "main-1":
            self.ui.fr_borde_top.setGeometry(QtCore.QRect(5, 5, 1351, 20))
            self.ui.fr_borde_bottom.setGeometry(QtCore.QRect(5, 740, 1355, 20))
            self.ui.fr_borde_left.setGeometry(QtCore.QRect(5, 5, 20, 755))
            self.ui.fr_borde_right.setGeometry(QtCore.QRect(1340, 5, 20, 755))
            
            self.ui.fr_buttons.setGeometry(QtCore.QRect(602, 40, 160, 70))
            self.ui.lbl_name.setText('Francisco Velez')

            self.runA = [True, True]
            self.opc = 'none'
            self.dactos()

        else: 
            self.ui.fr_borde_left.setGeometry(QtCore.QRect(5, 5, 20, 221))
            self.ui.fr_borde_right.setGeometry(QtCore.QRect(338, 5, 20, 225))
            self.ui.fr_borde_top.setGeometry(QtCore.QRect(5, 5, 351, 20))
            self.ui.fr_borde_bottom.setGeometry(QtCore.QRect(5, 210, 348, 20))

            self.runA = [True, True]
            self.opc = 'none'
            self.dactos()

    #  ********** ********** Imagenes ********** ********** #
    
    def mostrarImagen(self, lado=''):
        if self.timerM.isActive(): return ''

        if lado == 'left' and self.numArch != 0: self.numArch -= 1
        if lado == 'right' and self.numArch != len(self.nameArch[0])-1: self.numArch += 1

        self.ui.fr_images.setStyleSheet(
            f'background-image: url({self.nameArch[0][self.numArch]}); \n'
            'background-repeat: no-repeat; \n'
            'background-position: center center; \n'
            'border-radius: 10px;'
        )

    def ocultarImages(self):
        if self.fotosOcultar == False:
            try: self.timerM.stop()
            except: pass 

            self.timerO = QtCore.QTimer()
            self.timerO.timeout.connect(self.fotos_ocultar)
            self.fotosOcultar = True 
            self.timerO.start(25)
            
            self.ui.visor.show()
            self.ui.camara.start()
            self.ui.paginaVisor.show()
            self.ui.stackedWidget.show()

        else:
            self.fotosOcultar = False
            self.timerO.stop()

    def fotos_ocultar(self): 
        if self.cont_x >= 5 and self.cont_x >= 15: self.cont_x -= 5
        if self.cont_y >= 5 and self.cont_x <= 10: self.cont_y -= 5

        self.ui.fr_images.setGeometry(65, 40, self.cont_x, self.cont_y)

    def mostrarImages(self):
        if self.modo_fotos == False:
            try: self.timerO.stop()
            except: pass

            self.dact = QtWidgets.QFileDialog(self)
            self.nameArch = self.dact.getOpenFileNames(filter='*.png (*.png);\n Todos (*.*);')
            self.numArch = 0
            
            if self.nameArch != ([], ''):
                self.ui.camara.stop()
                self.ui.visor.close()
                self.ui.paginaVisor.close()
                self.ui.stackedWidget.close()
                
                self.timerM = QtCore.QTimer()
                self.timerM.timeout.connect(self.inicial_animacion)
                self.modo_fotos = True 
                self.timerM.start(25)

        else:
            self.modo_fotos = False
            self.timerM.stop()
    
    #  ********** ********** Funciones ********** ********** #
    
    def visorMain(self):
        if self.visor != "main-1":
            self.ui.lbl_name.show()
            self.ui.fr_buttons.show()
            self.visor = "main-1"

            self.resize(1372, 774)
            
            self.ui.fr_fondo.setGeometry(QtCore.QRect(9, 9, 1417, 765))
            self.ui.fr_images.setGeometry(65, 40, 0, 0)
            self.ui.lbl_name.setGeometry(QtCore.QRect(55, 675, 241, 60))

            self.ui.fr_borde_left.setGeometry(QtCore.QRect(5, 5, 20, 755))
            self.ui.fr_borde_right.setGeometry(QtCore.QRect(1340, 5, 20, 755))
            self.ui.fr_borde_top.setGeometry(QtCore.QRect(5, 5, 1355, 20))
            self.ui.fr_borde_bottom.setGeometry(QtCore.QRect(5, 740, 1355, 20))

            self.ui.fr_buttons.setGeometry(QtCore.QRect(602, 45, 160, 70))

            self.ui.btn_minimizar.setGeometry(QtCore.QRect(30, 25, 20, 20))
            self.ui.btn_maximizar.setGeometry(QtCore.QRect(70, 25, 20, 20))

            self.ui.btn_cerrar.setGeometry(QtCore.QRect(110, 25, 20, 20))
        
            num_x, num_y = 1305, 705
            self.ui.paginaVisor.resize(num_x, num_y)        
            self.ui.visor.resize(num_x, num_y)
            self.ui.stackedWidget.resize(num_x, num_y)
            self.ui.stackedWidget.move(30, 30)

    def return_(self, text, num):
        if num == 0: return ''
        else: return text[0:num]
    
    def verificar1(self, num1, num2): 
        var_ = list(range(num1, num2+num1, num1))
        if num2 in var_: return True 
        else: return False 

#* Author: Francisco Velez
