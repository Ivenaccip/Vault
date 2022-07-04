#Este código esta bien y ya corre. Tiene Shortcuts, además de que manda un mensaje de usar el marca textos, pero aun no exta implementado el highlight
from email import message
from tkinter import *
from tkinter import messagebox
from tkinter import filedialog

from matplotlib.pyplot import text
from pyparsing import col

#Esta clase es para cuando iniciemos cada sesión
class Ventana(Frame):
    def __init__(self, master):
        """
        This function start a window

        Args:
            - Title
            - Geometry
            - Protocol
            - Position x n' y
            - Font and Size

        Return:
            - A GUI window with 700x500+380+20 geometry with a 'Block' as a title
        """
        #Esta es la información del block al inicio
        super().__init__(master)
        self.master.title('Block')
        self.master.geometry('700x500+380+20')
        self.master.protocol("WM_DELETE_WINDOW", self.salir) #Estamos ejecutando el método salir

        #Variables de los métodos en class
        #Eliminar barra de titulo
        self.x = 0
        self.y = 0
        #Tamaño y tipo de fuente default
        self.n = 12 
        self.f = 'Arial'

        self.widgets()
        #Responsive
        self.master.columnconfigure(0, weight = 1)
        self.master.rowconfigure(0, weight=1)
    
    def widgets(self):
        """
        Menu's funtion

        Args:
            - Master Menu

        Return:
            - Shortcuts for New, Save, Open and Exit.
            - Shortcuts for Undo, Cut, Copy, Paste, Delete and Markdown
            - 
        """
        menu = Menu(self.master)
        self.master.configure(menu = menu)

        #Tearoff es para que no muestre lineas la UI
        archivo = Menu(menu, tearoff=0)
        archivo.add_command(label = "Nuevo", command = self.nueva_ventana) #Nueva ventana es el método a ejecutar, más abajo encontraremos los métodos
        archivo.add_command(label= "Abrir", command = self.abrir_archivo)
        archivo.add_command(label = "Guardar", command= self.guardar_archivo)
        archivo.add_separator()# Crea una linea divisor de opciones
        archivo.add_command(label="Salir", command=self.master.quit)

        #Short Cuts
        edicion = Menu(menu, tearoff=0)
        edicion.add_command(label = "Deshacer", accelerator='Ctrl+Z',command= lambda: self.texto.edit_undo())
        edicion.add_separator()
        edicion.add_command(label= "Cortar", accelerator='Ctrl+X', command = lambda: self.master.focus_get().event_generate("<<Cut>>"))
        edicion.add_command(label = "Copiar", accelerator='Ctrl+C', command= lambda: self.master.focus_get().event_generate("<<Copy>>"))
        edicion.add_command(label = "Pegar", accelerator='Ctrl+V', command= lambda: self.master.focus_get().event_generate("<<Paste>>"))
        edicion.add_command(label = "Eliminar", accelerator='Supr', command= lambda: self.master.focus_get().event_generate("<<Clear>>"))
        edicion.add_separator()
        edicion.add_command(label = "Subrayar", accelerator= 'Ctrl+S', command = self.marcar)


        #Este es para el menu
        menu.add_cascade(label="Archivo", menu=archivo)
        menu.add_cascade(label="Edicion", menu=edicion)

        #Texto
        self.texto = Text(self.master, font = ('Arial', 12), undo = True, insertbackground = 'red')
        self.texto.grid(column = 0, row = 0, sticky = 'nsew')
        ladox = Scrollbar(self.master, orient = 'horizontal', command= self.texto.xview)
        ladox.grid(column=0, row = 1, sticky='ew')
        ladoy = Scrollbar(self.master, orient ='vertical', command = self.texto.yview)
        ladoy.grid(column = 1, row = 0, sticky='ns')
        self.texto.configure(xscrollcommand = ladox.set, yscrollcommand = ladoy.set)
        self.barra_estado = Label(self.master, font = ('Segoe UI Symbol', 10))

    def nameTag(self, Vault, text):
        TagVault = StringVar()
        TagVault = Vault.get()

        print(type(TagVault))
        text.tag_add(str(TagVault), "1.0", "1.4")
        text.tag_config(str(TagVault), background = "yellow", foreground = "black")
        ventana.mainloop()
        
    #Error, el self no fue registrado dentro de la actividad de la función
    #Error dado: Ventana.nameTag() takes 3 positional arguments but 4 were given
    #Descripción, no aparece el botón
    def marcar(self):
        """
        Message Box for Marckdown

        Args:
            - Listener for marckdown

        Return:
            - Message box
        """
        #valor = messagebox.askyesno('Marcar Text', '¿Quieres subrayar este text?', parent=self.master)
        #if valor == True:
        #    pass
        #else:
        #    pass
        ventana_tag = Tk()
        text = Text(ventana)
        ventana_tag.title("Nombre Boveda")

        marcarFrame = Frame(ventana_tag)
        marcarFrame.grid()

        Label(marcarFrame, text="¿Cómo se llama esta boveda?", fg = "black", font = ("Arial", 12)).grid(row = 0, column=0, sticky="w", padx=5, pady=1)
        
        Vault = StringVar()
        nameVault = Entry(marcarFrame, textvariable=Vault)
        nameVault.grid(row = 3, column=0, sticky='nsew', padx=10, pady=1)

        botonEnviar = Button(marcarFrame, text="Nombrar boveda", fg = "black", command=self.nameTag(self, Vault, text))
        botonEnviar.grid(row = 4, column=0, padx=5, pady=10)

        ventana_tag.master.quit()


    def guardar_archivo(self):
        """
        Message Box for Save Document

        Args:
            - Listener for save Document

        Return:
            - Message box
        """
        try:
            filename = filedialog.asksaveasfilename(default = '.txt')
            archivo =open(filename, 'w')
            archivo.write(self.texto.get('1.0', 'end'))
            archivo.close()

            messagebox.showinfo('Guardar Archivo', 'Archivo Guardado en: ' + str(filename))
        except:
            messagebox.showinfo('Guardar Archivo', 'Archivo no Guardado \n Error')

    def abrir_archivo(self):
        """
        Message Box for Open Document

        Args:
            - Listener for Open Document

        Return:
            - Message box
        """
        direccion = filedialog.askopenfilename(initialdir='/',
        title = 'Archivo',
        filetype = (('txt files','*.txt*'),('All files', '*.*'))
        )
        if direccion != '':
            archivo = open(direccion, 'r')
            contenido = archivo.read()
            self.texto.delete('1.0', 'end')
            self.texto.insert('1.0', contenido)
            self.master.title(direccion)


    def nueva_ventana(self):
        """
        Message Box for New Window

        Args:
            - Listener for new window

        Return:
            - Message box
        """
        if self.texto.get != '':
            valor = messagebox.askyesno('Guardar', '¿Quieres Guardar?', parent = self.master)
            if valor == True:
                self.guardar_archivo()
            else:
                self.texto.delete('1.0', 'end')

    def salir(self):
        """
        Message Box for Exit

        Args:
            - Listener for exit

        Return:
            - Message box
        """
        valor = messagebox.askyesno('Salir', '¿Deseas Salir?', parent = self.master)
        if valor == True:
            self.master.destroy()
            self.master.quit()

if __name__ == "__main__":
    ventana = Tk()
    app = Ventana(ventana)
    app.mainloop()