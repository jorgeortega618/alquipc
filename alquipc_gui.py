#!/usr/bin/env python3
import tkinter as tk
from tkinter import ttk, messagebox, scrolledtext
import json
from core import QuoteInput, cotizar, formato_resumen, to_dict, ValidationError

class AlquipcGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("ALQUIPC - Facturación de Alquiler de Portátiles")
        self.root.geometry("600x700")
        self.root.resizable(True, True)
        
        # Configurar estilo
        style = ttk.Style()
        style.theme_use('winnative')
        
        self.create_widgets()
        
    def create_widgets(self):
        # Frame principal con padding
        main_frame = ttk.Frame(self.root, padding="20")
        main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # Título
        title_label = ttk.Label(main_frame, text="ALQUIPC - Cotizador de Alquiler", 
                               font=('Arial', 16, 'bold'))
        title_label.grid(row=0, column=0, columnspan=2, pady=(0, 20))
        
        # ID Cliente
        ttk.Label(main_frame, text="ID Cliente:").grid(row=1, column=0, sticky=tk.W, pady=5)
        self.id_cliente = ttk.Entry(main_frame, width=20)
        self.id_cliente.grid(row=1, column=1, sticky=(tk.W, tk.E), pady=5, padx=(10, 0))
        self.id_cliente.insert(0, "C-001")  # Valor por defecto
        
        # Teléfono Cliente
        ttk.Label(main_frame, text="Teléfono Cliente:").grid(row=2, column=0, sticky=tk.W, pady=5)
        self.telefono_cliente = ttk.Entry(main_frame, width=20)
        self.telefono_cliente.grid(row=2, column=1, sticky=(tk.W, tk.E), pady=5, padx=(10, 0))
        self.telefono_cliente.insert(0, "3008000")  # Valor por defecto
        
        # Email Cliente
        ttk.Label(main_frame, text="Email Cliente:").grid(row=3, column=0, sticky=tk.W, pady=5)
        self.email_cliente = ttk.Entry(main_frame, width=20)
        self.email_cliente.grid(row=3, column=1, sticky=(tk.W, tk.E), pady=5, padx=(10, 0))
        self.email_cliente.insert(0, "jorge@gmail.com")  # Valor por defecto
        
        # Número de equipos
        ttk.Label(main_frame, text="Número de equipos (mín. 2):").grid(row=4, column=0, sticky=tk.W, pady=5)
        self.equipos = ttk.Spinbox(main_frame, from_=2, to=50, width=18)
        self.equipos.grid(row=4, column=1, sticky=(tk.W, tk.E), pady=5, padx=(10, 0))
        self.equipos.set("3")
        
        # Días iniciales
        ttk.Label(main_frame, text="Días iniciales:").grid(row=5, column=0, sticky=tk.W, pady=5)
        self.dias = ttk.Spinbox(main_frame, from_=1, to=365, width=18)
        self.dias.grid(row=5, column=1, sticky=(tk.W, tk.E), pady=5, padx=(10, 0))
        self.dias.set("2")
        
        # Días adicionales
        ttk.Label(main_frame, text="Días adicionales:").grid(row=6, column=0, sticky=tk.W, pady=5)
        self.extra = ttk.Spinbox(main_frame, from_=0, to=365, width=18)
        self.extra.grid(row=6, column=1, sticky=(tk.W, tk.E), pady=5, padx=(10, 0))
        self.extra.set("0")
        
        # Ubicación
        ttk.Label(main_frame, text="Ubicación del servicio:").grid(row=7, column=0, sticky=tk.W, pady=5)
        self.ubicacion = ttk.Combobox(main_frame, width=17, state="readonly")
        self.ubicacion['values'] = ('ciudad', 'fuera', 'local')
        self.ubicacion.grid(row=7, column=1, sticky=(tk.W, tk.E), pady=5, padx=(10, 0))
        self.ubicacion.set('ciudad')
        
        # Botones
        button_frame = ttk.Frame(main_frame)
        button_frame.grid(row=8, column=0, columnspan=2, pady=20)
        
        self.calcular_btn = ttk.Button(button_frame, text="💰 Calcular Cotización", 
                                      command=self.calcular_cotizacion)
        self.calcular_btn.pack(side=tk.LEFT, padx=(0, 10))
        
        self.limpiar_btn = ttk.Button(button_frame, text="🗑️ Limpiar", 
                                     command=self.limpiar_campos)
        self.limpiar_btn.pack(side=tk.LEFT)
        
        # Área de resultados
        ttk.Label(main_frame, text="Resultado:", font=('Arial', 12, 'bold')).grid(
            row=9, column=0, columnspan=2, sticky=tk.W, pady=(20, 5))
        
        self.resultado_text = scrolledtext.ScrolledText(main_frame, width=70, height=20, 
                                                       font=('Consolas', 10))
        self.resultado_text.grid(row=10, column=0, columnspan=2, sticky=(tk.W, tk.E, tk.N, tk.S), 
                                pady=5)
        
        # Configurar redimensionamiento
        main_frame.columnconfigure(1, weight=1)
        main_frame.rowconfigure(10, weight=1)
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)
        
    def calcular_cotizacion(self):
        try:
            # Obtener valores de la interfaz
            entrada = QuoteInput(
                n_equipos=int(self.equipos.get()),
                dias_iniciales=int(self.dias.get()),
                dias_adicionales=int(self.extra.get()),
                ubicacion=self.ubicacion.get(),
                id_cliente=self.id_cliente.get().strip(),
                telefono_cliente=self.telefono_cliente.get().strip(),
                email_cliente=self.email_cliente.get().strip()
            )
            
            # Calcular cotización
            resultado = cotizar(entrada)
            
            # Mostrar resultado
            self.resultado_text.delete(1.0, tk.END)
            resumen = formato_resumen(resultado)
            self.resultado_text.insert(tk.END, resumen)
            self.resultado_text.insert(tk.END, "\n\n" + "="*50 + "\n")
            self.resultado_text.insert(tk.END, "DATOS JSON:\n")
            self.resultado_text.insert(tk.END, json.dumps(to_dict(resultado), 
                                                         ensure_ascii=False, indent=2))
            
        except ValidationError as e:
            messagebox.showerror("Error de Validación", str(e))
        except ValueError as e:
            messagebox.showerror("Error de Entrada", 
                               "Por favor verifica que todos los campos numéricos sean válidos.")
        except Exception as e:
            messagebox.showerror("Error", f"Error inesperado: {str(e)}")
    
    def limpiar_campos(self):
        self.id_cliente.delete(0, tk.END)
        self.telefono_cliente.delete(0, tk.END)
        self.email_cliente.delete(0, tk.END)
        self.equipos.set("2")
        self.dias.set("1")
        self.extra.set("0")
        self.ubicacion.set("ciudad")
        self.resultado_text.delete(1.0, tk.END)

def main():
    root = tk.Tk()
    app = AlquipcGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()
