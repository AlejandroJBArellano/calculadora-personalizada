import tkinter as tk
from tkinter import ttk
import math

class Calculadora:
    def __init__(self):
        self.ventana = tk.Tk()
        self.ventana.title("Calculadora Avanzada")
        self.ventana.geometry("400x600")
        self.ventana.configure(bg='#f0f0f0')
        
        # Variables
        self.numero_actual = ""
        self.primer_numero = 0
        self.operacion = ""
        self.resultado = 0
        
        # Display
        self.display_frame = ttk.Frame(self.ventana)
        self.display_frame.grid(row=0, column=0, columnspan=4, padx=10, pady=10, sticky="nsew")
        
        self.display = ttk.Entry(self.display_frame, justify="right", font=('Arial', 20))
        self.display.grid(row=0, column=0, sticky="nsew")
        self.display.insert(0, "0")
        
        # Crear y configurar los botones
        self.crear_botones()
        
        # Configurar el grid
        self.configurar_grid()
        
        # Bindings del teclado
        self.configurar_teclado()

    def configurar_grid(self):
        for i in range(7):
            self.ventana.grid_rowconfigure(i, weight=1)
        for i in range(4):
            self.ventana.grid_columnconfigure(i, weight=1)

    def crear_botones(self):
        # Estilo de los botones
        style = ttk.Style()
        style.configure('Calc.TButton', font=('Arial', 12))
        
        # Botones numéricos y operaciones básicas
        botones = [
            ['%', 'CE', 'C', '←'],
            ['1/x', 'x²', '√x', '÷'],
            ['7', '8', '9', '×'],
            ['4', '5', '6', '-'],
            ['1', '2', '3', '+'],
            ['±', '0', '.', '=']
        ]
        
        for i, fila in enumerate(botones):
            for j, texto in enumerate(fila):
                btn = ttk.Button(self.ventana, text=texto, style='Calc.TButton',
                               command=lambda t=texto: self.click_boton(t))
                btn.grid(row=i+1, column=j, padx=2, pady=2, sticky="nsew")

    def configurar_teclado(self):
        self.ventana.bind('<Return>', lambda _: self.click_boton('='))
        self.ventana.bind('<BackSpace>', lambda _: self.click_boton('←'))
        self.ventana.bind('<Escape>', lambda _: self.click_boton('C'))
        for num in range(10):
            self.ventana.bind(str(num), lambda _, n=num: self.click_boton(str(n)))
        self.ventana.bind('+', lambda _: self.click_boton('+'))
        self.ventana.bind('-', lambda _: self.click_boton('-'))
        self.ventana.bind('*', lambda _: self.click_boton('×'))
        self.ventana.bind('/', lambda _: self.click_boton('÷'))
        self.ventana.bind('.', lambda _: self.click_boton('.'))

    def click_boton(self, valor):
        if valor in '0123456789.':
            self.agregar_numero(valor)
        elif valor in '+-×÷':
            self.operacion_basica(valor)
        elif valor == '=':
            self.calcular_resultado()
        elif valor == 'C':
            self.limpiar()
        elif valor == 'CE':
            self.limpiar_entrada()
        elif valor == '←':
            self.borrar_ultimo()
        elif valor == '±':
            self.cambiar_signo()
        elif valor == '%':
            self.calcular_porcentaje()
        elif valor == 'x²':
            self.calcular_cuadrado()
        elif valor == '√x':
            self.calcular_raiz()
        elif valor == '1/x':
            self.calcular_reciproco()

    def agregar_numero(self, num):
        if self.display.get() == '0' and num != '.':
            self.display.delete(0, tk.END)
        elif num == '.' and '.' in self.display.get():
            return
        self.display.insert(tk.END, num)

    def operacion_basica(self, op):
        self.primer_numero = float(self.display.get())
        self.operacion = op
        self.display.delete(0, tk.END)
        self.display.insert(0, '0')

    def calcular_resultado(self):
        try:
            segundo_numero = float(self.display.get())
            if self.operacion == '+':
                resultado = self.primer_numero + segundo_numero
            elif self.operacion == '-':
                resultado = self.primer_numero - segundo_numero
            elif self.operacion == '×':
                resultado = self.primer_numero * segundo_numero
            elif self.operacion == '÷':
                if segundo_numero == 0:
                    resultado = "Error"
                else:
                    resultado = self.primer_numero / segundo_numero
            
            self.display.delete(0, tk.END)
            self.display.insert(0, str(resultado))
            self.operacion = ""
        except:
            self.display.delete(0, tk.END)
            self.display.insert(0, "Error")

    def limpiar(self):
        self.display.delete(0, tk.END)
        self.display.insert(0, '0')
        self.primer_numero = 0
        self.operacion = ""

    def limpiar_entrada(self):
        self.display.delete(0, tk.END)
        self.display.insert(0, '0')

    def borrar_ultimo(self):
        if len(self.display.get()) > 1:
            self.display.delete(len(self.display.get())-1, tk.END)
        else:
            self.display.delete(0, tk.END)
            self.display.insert(0, '0')

    def cambiar_signo(self):
        actual = float(self.display.get())
        self.display.delete(0, tk.END)
        self.display.insert(0, str(-actual))

    def calcular_porcentaje(self):
        try:
            actual = float(self.display.get())
            resultado = actual / 100
            self.display.delete(0, tk.END)
            self.display.insert(0, str(resultado))
        except:
            self.display.delete(0, tk.END)
            self.display.insert(0, "Error")

    def calcular_cuadrado(self):
        try:
            actual = float(self.display.get())
            resultado = actual ** 2
            self.display.delete(0, tk.END)
            self.display.insert(0, str(resultado))
        except:
            self.display.delete(0, tk.END)
            self.display.insert(0, "Error")

    def calcular_raiz(self):
        try:
            actual = float(self.display.get())
            if actual < 0:
                resultado = "Error"
            else:
                resultado = math.sqrt(actual)
            self.display.delete(0, tk.END)
            self.display.insert(0, str(resultado))
        except:
            self.display.delete(0, tk.END)
            self.display.insert(0, "Error")

    def calcular_reciproco(self):
        try:
            actual = float(self.display.get())
            if actual == 0:
                resultado = "Error"
            else:
                resultado = 1 / actual
            self.display.delete(0, tk.END)
            self.display.insert(0, str(resultado))
        except:
            self.display.delete(0, tk.END)
            self.display.insert(0, "Error")

    def iniciar(self):
        self.ventana.mainloop()

if __name__ == "__main__":
    calc = Calculadora()
    calc.iniciar()