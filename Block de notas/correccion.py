import os
from PySide6.QtGui import QAction, QIcon, QKeySequence, QTextCursor, QDesktopServices
from PySide6.QtWidgets import QApplication, QMainWindow, QToolBar, QToolButton, QDockWidget, QTextEdit, QInputDialog, QWhatsThis, QColorDialog, QMessageBox, QFileDialog
from PySide6.QtWebEngineWidgets import QWebEngineView
from PySide6.QtCore import Qt, QDir, QUrl

class VentanaPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Blog de notas")
        
        # Inicializar acciones primero
        self.crear_acciones()

        # Crear  menús    
        self.crear_menus()

        # Crear barra de herramientas y dock widget
        self.crear_barras_y_docks()

        # Crear área de texto en el dock
        self.crear_texto_en_dock("")

    def crear_acciones(self):
        self.crear_accion_ayuda()
        self.crear_accion_nuevo_bloc()
        self.crear_accion_abrir_archivo()
        self.crear_accion_guardar_archivo()
        self.crear_accion_deshacer()
        self.crear_accion_rehacer()
        self.crear_accion_cortar()
        self.crear_accion_copiar()
        self.crear_accion_pegar()
        self.crear_accion_buscar()
        self.crear_accion_reemplazar()
        self.crear_accion_reemplazar_todos()
        self.crear_accion_color_de_bloc()
        self.crear_accion_salir()
        self.crear_accion_navegar_exterior()
        self.crear_accion_navegar_interior()
        

    def crear_menus(self):
        # Crear menús    
        barra_menus = self.menuBar()
        menu_archivo = barra_menus.addMenu("&Archivo")
        #menu.addAction(self.accion_imprimir) 
        menu_archivo.addAction(self.accion_nuevo_bloc)
        menu_archivo.addAction(self.accion_abrir_archivo)
        menu_archivo.addAction(self.accion_guardar_archivo)
        menu_archivo.addAction(self.accion_salir)

        barra_menus2 = self.menuBar()
        menu_editar = barra_menus2.addMenu("&Edición")
        menu_editar.addAction(self.accion_cortar)
        menu_editar.addAction(self.accion_copiar)
        menu_editar.addAction(self.accion_pegar)
        menu_editar.addAction(self.accion_buscar)
        menu_editar.addAction(self.accion_reemplazar)
        menu_editar.addAction(self.accion_reemplazar_todo)
        
    def crear_barras_y_docks(self):
        # Crear dock widget
        self.dock_widget = QDockWidget("Dock 1", self)
        self.dock_widget.setAllowedAreas(Qt.TopDockWidgetArea)
        self.addDockWidget(Qt.TopDockWidgetArea, self.dock_widget)

        # Crear barra de herramientas
        self.barra_herramientas = QToolBar("Barra de herramientas 1")
        self.addToolBar(self.barra_herramientas)
        

        # Crear botones en la barra de herramientas
        self.crear_boton_nuevo_bloc()
        self.crear_abrir_archivo()
        self.crear_boton_guardar_archivo()
        self.crear_boton_deshacer()
        self.crear_boton_rehacer()
        self.crear_boton_cortar()
        self.crear_boton_copiar()
        self.crear_boton_pegar()
        self.crear_boton_buscar()
        self.crear_boton_reemplazar()
        self.crear_boton_reemplazar_todos()
        self.crear_boton_color_de_bloc()
        self.crear_boton_ayuda()
        self.crear_boton_navegar_exterior()
        self.crear_boton_navegar_interior()


    

    # Buttons 

    def crear_boton_nuevo_bloc(self):
        ruta_a_icono = os.path.join(os.path.dirname(__file__), "nuevoArchivo.png")
        self.boton_nuevo_bloc = QToolButton()
        self.boton_nuevo_bloc.setDefaultAction(self.accion_nuevo_bloc)  
        self.boton_nuevo_bloc.setIcon(QIcon(ruta_a_icono))
        self.boton_nuevo_bloc.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
        self.barra_herramientas.addWidget(self.boton_nuevo_bloc)

    def crear_abrir_archivo(self):
        ruta_a_icono = os.path.join(os.path.dirname(__file__), "abrirArchivo.png")
        self.boton_abrir_archivo = QToolButton()
        self.boton_abrir_archivo.setDefaultAction(self.accion_abrir_archivo)
        self.boton_abrir_archivo.setIcon(QIcon(ruta_a_icono))
        self.boton_abrir_archivo.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
        self.barra_herramientas.addWidget(self.boton_abrir_archivo)

    def crear_boton_guardar_archivo(self):
        ruta_a_icono = os.path.join(os.path.dirname(__file__), "guardarArchivo.png")
        self.boton_guardar_archivo = QToolButton()
        self.boton_guardar_archivo.setDefaultAction(self.accion_guardar_archivo)  
        self.boton_guardar_archivo.setIcon(QIcon(ruta_a_icono))
        self.boton_guardar_archivo.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
        self.barra_herramientas.addWidget(self.boton_guardar_archivo)

    def crear_boton_deshacer(self):
        ruta_a_icono = os.path.join(os.path.dirname(__file__), "deshacer.png")
        self.boton_deshacer = QToolButton()
        self.boton_deshacer.setDefaultAction(self.accion_deshacer) 
        self.boton_deshacer.setIcon(QIcon(ruta_a_icono))
        self.boton_deshacer.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
        self.barra_herramientas.addWidget(self.boton_deshacer)

    def crear_boton_rehacer(self):
        ruta_a_icono = os.path.join(os.path.dirname(__file__), "rehacer.png")
        self.boton_rehacer = QToolButton()
        self.boton_rehacer.setDefaultAction(self.accion_rehacer)  
        self.boton_rehacer.setIcon(QIcon(ruta_a_icono))
        self.boton_rehacer.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
        self.barra_herramientas.addWidget(self.boton_rehacer)

    def crear_boton_cortar(self):
        ruta_a_icono = os.path.join(os.path.dirname(__file__), "cortar.png")
        self.boton_cortar = QToolButton()
        self.boton_cortar.setDefaultAction(self.accion_cortar)  
        self.boton_cortar.setIcon(QIcon(ruta_a_icono))
        self.boton_cortar.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
        self.barra_herramientas.addWidget(self.boton_cortar)

    def crear_boton_copiar(self):
        ruta_a_icono = os.path.join(os.path.dirname(__file__), "copiar.png")
        self.boton_copiar = QToolButton()
        self.boton_copiar.setDefaultAction(self.accion_copiar) 
        self.boton_copiar.setIcon(QIcon(ruta_a_icono))
        self.boton_copiar.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
        self.barra_herramientas.addWidget(self.boton_copiar)

    def crear_boton_pegar(self):
        ruta_a_icono = os.path.join(os.path.dirname(__file__), "pegar.png")
        self.boton_pegar = QToolButton()
        self.boton_pegar.setDefaultAction(self.accion_pegar)  
        self.boton_pegar.setIcon(QIcon(ruta_a_icono))
        self.boton_pegar.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
        self.barra_herramientas.addWidget(self.boton_pegar)

    def crear_boton_buscar(self):
        ruta_a_icono = os.path.join(os.path.dirname(__file__), "buscar.png")
        self.boton_buscar = QToolButton()
        self.boton_buscar.setDefaultAction(self.accion_buscar) 
        self.boton_buscar.setIcon(QIcon(ruta_a_icono))
        self.boton_buscar.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
        self.barra_herramientas.addWidget(self.boton_buscar)

    def crear_boton_reemplazar(self):
        ruta_a_icono = os.path.join(os.path.dirname(__file__), "reemplazar.png")
        self.boton_reemplazar = QToolButton()
        self.boton_reemplazar.setDefaultAction(self.accion_reemplazar) 
        self.boton_reemplazar.setIcon(QIcon(ruta_a_icono))
        self.boton_reemplazar.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
        self.barra_herramientas.addWidget(self.boton_reemplazar)

    def crear_boton_reemplazar_todos(self):
        ruta_a_icono = os.path.join(os.path.dirname(__file__), "reemplazar.png")
        self.boton_reemplazar_todo = QToolButton()
        self.boton_reemplazar_todo.setDefaultAction(self.accion_reemplazar_todo) 
        self.boton_reemplazar_todo.setIcon(QIcon(ruta_a_icono))
        self.boton_reemplazar_todo.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
        self.barra_herramientas.addWidget(self.boton_reemplazar_todo)

    def crear_boton_color_de_bloc(self):
        ruta_a_icono = os.path.join(os.path.dirname(__file__), "color.png")
        self.boton_color = QToolButton()
        self.boton_color.setDefaultAction(self.accion_color_de_bloc) 
        self.boton_color.setIcon(QIcon(ruta_a_icono))
        self.boton_color.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
        self.barra_herramientas.addWidget(self.boton_color)

    def crear_boton_ayuda(self):
        ruta_a_icono = os.path.join(os.path.dirname(__file__), "help.png")
        self.boton_ayuda = QToolButton()
        self.boton_ayuda.setDefaultAction(self.accion_ayuda) 
        self.boton_ayuda.setIcon(QIcon(ruta_a_icono))
        self.boton_ayuda.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
        self.barra_herramientas.addWidget(self.boton_ayuda)

    def crear_boton_navegar_interior(self):
        ruta_a_icono = os.path.join(os.path.dirname(__file__), "Lonsdale.jpg")
        self.boton_navegar_interior = QToolButton()
        self.boton_navegar_interior.setDefaultAction(self.accion_navegar_interior) 
        self.boton_navegar_interior.setIcon(QIcon(ruta_a_icono))
        self.boton_navegar_interior.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
        self.barra_herramientas.addWidget(self.boton_navegar_interior)

    def crear_boton_navegar_exterior(self):
        ruta_a_icono = os.path.join(os.path.dirname(__file__), "Lonsdale.jpg")
        self.boton_navegar_exterior = QToolButton()
        self.boton_navegar_exterior.setDefaultAction(self.accion_navegar_exterior) 
        self.boton_navegar_exterior.setIcon(QIcon(ruta_a_icono))
        self.boton_navegar_exterior.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
        self.barra_herramientas.addWidget(self.boton_navegar_exterior)

    # Accions
    def crear_accion_imprimir(self):
        ruta_a_icono = os.path.join(os.path.dirname(__file__), "imprimir.png")
        self.accion = QAction(QIcon(ruta_a_icono), "Imprimir en dock", self)
        self.accion.setWhatsThis("Al ejecutar esta acción, se añadirá el texto 'Acción pulsada' en el dock.")
        self.accion.setShortcut(QKeySequence("Ctrl+p"))
        self.accion.triggered.connect(self.imprimir_por_dock)

    def crear_accion_ayuda(self):
        self.accion_ayuda = QAction("¿Qué es esto?", self)
        self.accion_ayuda.setWhatsThis("Esta acción muestra una explicación sobre el funcionamiento del botón")
        self.accion_ayuda.setShortcut(QKeySequence("Shift+F1"))
        self.accion_ayuda.triggered.connect(self.mostrar_ayuda)

    def crear_accion_nuevo_bloc(self):
        self.accion_nuevo_bloc = QAction("Nuevo Bloc", self)
        self.accion_nuevo_bloc.setWhatsThis("Crea un nuevo archivo en el bloc de notas")
        self.accion_nuevo_bloc.setShortcut(QKeySequence("Ctrl+N"))
        self.accion_nuevo_bloc.triggered.connect(self.nuevo_bloc)

    def crear_accion_abrir_archivo(self):
        self.accion_abrir_archivo = QAction("Abrir Archivo", self)
        self.accion_abrir_archivo.setWhatsThis("Abre un archivo existente")
        self.accion_abrir_archivo.setShortcut(QKeySequence("Ctrl+O"))
        self.accion_abrir_archivo.triggered.connect(self.abrir_archivo)

    def crear_accion_guardar_archivo(self):
        self.accion_guardar_archivo = QAction("Guardar Archivo", self)
        self.accion_guardar_archivo.setWhatsThis("Guarda el archivo actual")
        self.accion_guardar_archivo.setShortcut(QKeySequence("Ctrl+S"))
        self.accion_guardar_archivo.triggered.connect(self.guardar_archivo)

    def crear_accion_salir(self):
        self.accion_salir = QAction("Salir", self)
        self.accion_salir.setShortcut(QKeySequence("Ctrl+Q"))
        self.accion_salir.setStatusTip("Salir de la aplicación")
        self.accion_salir.triggered.connect(self.salir)

    def crear_accion_deshacer(self):
        self.accion_deshacer = QAction("Deshacer", self)
        self.accion_deshacer.setWhatsThis("Deshace la última acción")
        self.accion_deshacer.setShortcut(QKeySequence("Ctrl+Z"))
        self.accion_deshacer.triggered.connect(self.deshacer)

    def crear_accion_rehacer(self):
        self.accion_rehacer = QAction("Rehacer", self)
        self.accion_rehacer.setWhatsThis("Rehace la última acción deshecha")
        self.accion_rehacer.setShortcut(QKeySequence("Ctrl+Y"))
        self.accion_rehacer.triggered.connect(self.rehacer)

    def crear_accion_cortar(self):
        self.accion_cortar = QAction("Cortar", self)
        self.accion_cortar.setWhatsThis("Corta el texto seleccionado")
        self.accion_cortar.setShortcut(QKeySequence("Ctrl+X"))
        self.accion_cortar.triggered.connect(self.cortar)

    def crear_accion_copiar(self):
        self.accion_copiar = QAction("Copiar", self)
        self.accion_copiar.setWhatsThis("Copia el texto seleccionado")
        self.accion_copiar.setShortcut(QKeySequence("Ctrl+C"))
        self.accion_copiar.triggered.connect(self.copiar)

    def crear_accion_pegar(self):
        self.accion_pegar = QAction("Pegar", self)
        self.accion_pegar.setWhatsThis("Pega el texto copiado")
        self.accion_pegar.setShortcut(QKeySequence("Ctrl+V"))
        self.accion_pegar.triggered.connect(self.pegar)

    def crear_accion_buscar(self):
        self.accion_buscar = QAction("Buscar", self)
        self.accion_buscar.setWhatsThis("Busca texto en el documento")
        self.accion_buscar.setShortcut(QKeySequence("Ctrl+F"))
        self.accion_buscar.triggered.connect(self.buscar)

    def crear_accion_reemplazar(self):
        self.accion_reemplazar = QAction("Reemplazar", self)
        self.accion_reemplazar.setWhatsThis("Reemplaza texto en el documento")
        self.accion_reemplazar.setShortcut(QKeySequence("Ctrl+R"))
        self.accion_reemplazar.triggered.connect(self.reemplazar)

    def crear_accion_reemplazar_todos(self):
        self.accion_reemplazar_todo = QAction("Reemplazar todo", self)
        self.accion_reemplazar_todo.setWhatsThis("Reemplaza texto en el documento con le mismo nombre")
        self.accion_reemplazar_todo.setShortcut(QKeySequence("Ctrl+T"))
        self.accion_reemplazar_todo.triggered.connect(self.reemplazar_todos)

    def crear_accion_color_de_bloc(self):
        self.accion_color_de_bloc = QAction("Cambiar Color", self)
        self.accion_color_de_bloc.setWhatsThis("Cambia el color de fondo del bloc")
        self.accion_color_de_bloc.setShortcut(QKeySequence("Ctrl+Shift+C"))
        self.accion_color_de_bloc.triggered.connect(self.cambiar_color)


    def crear_accion_navegar_interior(self):
        self.accion_navegar_interior = QAction("Documentacion interior", self)
        self.accion_navegar_interior.setWhatsThis("Navega a la documentacion de forma interna")
        self.accion_navegar_interior.triggered.connect(self.abrir_navegador_interno)


    def crear_accion_navegar_exterior(self):
        self.accion_navegar_exterior = QAction("Documentacion exterior", self)
        self.accion_navegar_exterior.setWhatsThis("Navega al exterior de forma externa")
        self.accion_navegar_exterior.triggered.connect(self.abrir_navegador_externo)

    # Methods

    def salir(self):
        super().close() 

    def crear_texto_en_dock(self, texto):
        if not hasattr(self, 'text_edit'):
            self.text_edit = QTextEdit()
            self.dock_widget.setWidget(self.text_edit)
            self.text_edit.setWhatsThis("Aquí puedes escribir tus notas o cualquier texto que desees.")
        
        self.text_edit.append(texto)

    def mostrar_ayuda(self):
        if QWhatsThis.inWhatsThisMode():
            QWhatsThis.leaveWhatsThisMode()
        else:
            QWhatsThis.enterWhatsThisMode()

    def imprimir_por_dock(self):
        self.dock_widget.widget().append("Acción pulsada")

        

    def nuevo_bloc(self):
        if isinstance(self.dock_widget.widget(), QWebEngineView):
            self.text_edit = QTextEdit()
            self.dock_widget.setWidget(self.text_edit)
        else:
            self.dock_widget.widget().clear()
            self.dock_widget.widget().append("Nuevo texto")

       


    def abrir_archivo(self):
        # Abrir un cuadro de diálogo para seleccionar el archivo
        archivo, _ = QFileDialog.getOpenFileName(self, "Abrir archivo", "", "Text Files (*.txt);;All Files (*)")
        
        # Si se seleccionó un archivo
        if archivo:
            try:
                # Abrir el archivo y leer su contenido
                with open(archivo, 'r' , encoding='utf-8') as file:
                    contenido = file.read()
                    print(f"Contenido del archivo:\n{contenido}")  # Imprimir el contenido
                    # Colocar el contenido en el QTextEdit
                    self.text_edit.clear()
                    self.text_edit.append(contenido)
                    print("Documento abierto exitosamente...")
            except Exception as e:
                # Manejar errores en caso de que la lectura falle
                self.text_edit.append(f"Error al abrir el archivo: {str(e)}")


    def guardar_archivo(self):
        # Mostrar un cuadro de diálogo para seleccionar el archivo
        archivo, _ = QFileDialog.getSaveFileName(self, "Guardar archivo", "", "Text Files (*.txt);;All Files (*)")
        
        # Si se seleccionó un archivo
        if archivo:
            try:
                # Obtener el contenido del QTextEdit
                
                contenido = self.text_edit.toPlainText()
                
                # Guardar el contenido en el archivo
                with open(archivo, 'w') as file:
                    file.write(contenido)
                    self.text_edit.append("\nArchivo guardado exitosamente")
            except Exception as e:
                # Manejar errores en caso de que la escritura falle
                self.text_edit.append(f"Error al guardar el archivo: {str(e)}")
                

    def deshacer(self):
        self.dock_widget.widget().undo()

    def rehacer(self):
        self.dock_widget.widget().redo()

    def cortar(self):
        self.dock_widget.widget().cut()

    def copiar(self):
        self.dock_widget.widget().copy()

    def pegar(self):
        self.dock_widget.widget().paste()

    def buscar(self):
        # Mostrar un cuadro de diálogo para ingresar un texto
        text, ok = QInputDialog.getText(self, "Buscar", "Ingresa el texto a buscar:")

        if ok and text:
            # Obtener el cursor y buscar el texto
            cursor = self.dock_widget.widget().textCursor()  # Obtener el cursor del QTextEdit
            cursor.movePosition(QTextCursor.Start)  
            self.text_edit.setTextCursor(cursor)  # Establecer el cursor en el QTextEdit

            found = self.text_edit.find(text)  # Buscar el texto ingresado

            if found:
                QMessageBox.information(self, "Buscar", "Texto encontrado")
            else:
                QMessageBox.warning(self, "Buscar", "Texto no encontrado")
        else:
            QMessageBox.warning(self, "Advertencia", "No se ingresó texto.")

            


    def reemplazar(self):
        # Verificar si hay texto almacenado para reemplazar
        if not self.dock_widget.widget().toPlainText():  # self.dock_widget.widget(). devolvera el QTextEdit, sin perder la referencia 
            QMessageBox.warning(self, "Reemplazar", "No hay texto para reemplazar. Realiza una búsqueda primero.")
            return

        # Mostrar un cuadro de diálogo para ingresar el nuevo texto
        nuevo_texto, ok = QInputDialog.getText(self, "Reemplazar", "Ingresa el nuevo texto:")

        if ok and nuevo_texto:
            cursor = self.dock_widget.widget().textCursor()
            cursor.insertText(nuevo_texto)  
            self.text_edit = nuevo_texto 
        else:
            QMessageBox.warning(self, "Advertencia", "No se ingresó nuevo texto.")
            

    def reemplazar_todos(self):
        # Verificar si hay texto en el QTextEdit
        #contenido= self.dock_widget.widget().top
        if not self.dock_widget.widget().toPlainText():  # Comprueba si el texto está vacío
            QMessageBox.warning(self, "Reemplazar", "No hay texto para reemplazar. Escribe algo primero.")
            return

        # Mostrar un cuadro de diálogo para ingresar el texto que deseas reemplazar
        texto_viejo, ok = QInputDialog.getText(self, "Reemplazar", "Ingresa el texto que quieres reemplazar:")

        if ok and texto_viejo:
            # Obtener el texto actual del QTextEdit
            contenido = self.dock_widget.widget().toPlainText()

            # Verificar si el texto viejo está en el contenido
            if texto_viejo in contenido:
                # Mostrar un cuadro de diálogo para ingresar el nuevo texto
                nuevo_texto, ok = QInputDialog.getText(self, "Reemplazar", "Ingresa el nuevo texto:")
                if ok and nuevo_texto:
                    # Reemplazar el texto viejo con el nuevo texto
                    contenido_reemplazado = contenido.replace(texto_viejo, nuevo_texto)

                    # Actualizar el QTextEdit con el contenido modificado
                    self.dock_widget.widget().setPlainText(contenido_reemplazado)

                    QMessageBox.information(self, "Reemplazar", "Texto reemplazado con éxito.")
                else:
                    QMessageBox.warning(self, "Advertencia", "No se ingresó nuevo texto.")
            else:
                QMessageBox.warning(self, "Buscar", "Texto a reemplazar no encontrado.")
        else:
            QMessageBox.warning(self, "Advertencia", "No se ingresó texto a reemplazar.")



    def cambiar_color(self):
        color = QColorDialog.getColor()
        if color.isValid():
           self.text_edit.setStyleSheet("background-color: {};".format(color.name()))

    def configurar_whats_this(self):
        self.boton_nuevo_bloc.setWhatsThis("Este botón crea un nuevo bloc de notas.")
        self.boton_abrir_archivo.setWhatsThis("Este botón abre un archivo existente.")
        self.boton_guardar_archivo.setWhatsThis("Este botón guarda el contenido actual en un archivo.")
        self.boton_deshacer.setWhatsThis("Este botón deshace la última acción realizada.")
        self.boton_rehacer.setWhatsThis("Este botón rehace la última acción deshecha.")
        self.boton_cortar.setWhatsThis("Este botón corta el texto seleccionado.")
        self.boton_copiar.setWhatsThis("Este botón copia el texto seleccionado al portapapeles.")
        self.boton_pegar.setWhatsThis("Este botón pega el texto del portapapeles en la posición actual.")
        self.boton_buscar.setWhatsThis("Este botón abre una ventana para buscar texto en el bloc.")
        self.boton_reemplazar.setWhatsThis("Este botón abre una ventana para reemplazar texto en el bloc.")
        self.boton_color.setWhatsThis("Este botón permite cambiar el color de fondo del bloc de notas.")
        self.boton_ayuda.setWhatsThis("Este botón muestra ayuda sobre la aplicación.")
        self.dock_widget.setWhatsThis("Este es un área donde puedes ver los resultados de tus acciones.")


    def abrir_navegador_externo(self):
        # Construir la ruta absoluta
        ruta_absoluta = os.path.abspath("curso_python//DesarrolloDeInterfaces//Acciones//documentacion.html")

        # Verificar si el archivo existe antes de abrirlo
        if os.path.isfile(ruta_absoluta):
            QDesktopServices.openUrl(QUrl.fromLocalFile(ruta_absoluta))
        else:
            print("El archivo 'documentacion.html' no se encontró.")

    


    def abrir_navegador_interno(self):
        ruta_absoluta = QDir().absoluteFilePath("curso_python//DesarrolloDeInterfaces//Acciones//documentacion.html")
        view = QWebEngineView()
        view.load(QUrl.fromLocalFile(ruta_absoluta))


        self.dock_widget.setWidget(view)







if __name__ == "__main__":
    app = QApplication([])
    ventana1 = VentanaPrincipal()
    ventana1.show()
    app.exec()
