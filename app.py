import customtkinter as ctk
from tkinter import filedialog
from PIL import Image, ImageTk
from ImageGoNord import GoNord


class ImageConverterApp:
    def __init__(self):
        self.window = ctk.CTk()
        self.window.title("ImageToGoCatppuccin")
        self.window.geometry("900x600")
        self.window.configure(fg_color="#1e1e2e")
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("blue")
        
        self.image_path = None
        self.original_image = None
        
        # Título
        title = ctk.CTkLabel(self.window, text="ImageToGoCatppuccin", font=("Arial", 24, "bold"), text_color="#f5e0dc")
        title.pack(pady=20)
        subtitle = ctk.CTkLabel(self.window, text="A tool to bring any image to the catppuccin palette", font=("Arial", 14, "bold"), text_color="#cdd6f4")
        subtitle.pack(pady=20)       
        # Botón seleccionar imagen
        btn_select = ctk.CTkButton(self.window, text="Seleccionar Imagen", command=self.select_image, width=200, height=40, fg_color="#cba6f7", hover_color="#89b4fa", text_color="#cdd6f4")
        btn_select.pack(pady=10)
        
        # Frame para las imágenes
        self.images_frame = ctk.CTkFrame(self.window)
        self.images_frame.pack(pady=20, padx=20, fill="both", expand=True)
        self.images_frame.configure(fg_color="#181825")
        # Labels para antes y después
        self.label_before = ctk.CTkLabel(self.images_frame, text="Original", font=("Arial", 16), text_color="#cdd6f4")
        self.label_before.grid(row=0, column=0, padx=20, pady=10)
        
        self.label_after = ctk.CTkLabel(self.images_frame, text="Convertida", font=("Arial", 16), text_color="#cdd6f4")
        self.label_after.grid(row=0, column=1, padx=20, pady=10)
        
        # Canvas para mostrar imágenes
        self.canvas_before = ctk.CTkLabel(self.images_frame, text="")
        self.canvas_before.grid(row=1, column=0, padx=20, pady=10)
        
        self.canvas_after = ctk.CTkLabel(self.images_frame, text="")
        self.canvas_after.grid(row=1, column=1, padx=20, pady=10)

        label_loading = ctk.CTkLabel(self.window, text="Presione el boton convertir y luego espere a que la imagen termine de procesarse...", font=("Arial", 12), text_color="#cdd6f4")
        label_loading.pack(pady=10)
        # Botón convertir
        btn_convert = ctk.CTkButton(self.window, text="Convertir Imagen", command=self.convert_image, width=200, height=40, fg_color="#cba6f7", hover_color="#89b4fa", text_color="#cdd6f4")
        btn_convert.pack(pady=10)
        
        self.window.mainloop()
    
    def select_image(self):
        self.image_path = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg *.jpeg *.png")])
        if self.image_path:
            self.show_original()
    
    def show_original(self):
        img = Image.open(self.image_path)
        img.thumbnail((350, 350))
        self.original_image = img
        photo = ImageTk.PhotoImage(img)
        self.canvas_before.configure(image=photo)
        self.canvas_before.image = photo
    
    def convert_image(self):
        if not self.image_path:
            return
        
        go_nord = GoNord()
        image = go_nord.open_image(self.image_path)
        go_nord.enable_avg_algorithm()
        go_nord.reset_palette()
        
        # Colores
        go_nord.add_color_to_palette("#1e1e2e")
        go_nord.add_color_to_palette("#313244")
        go_nord.add_color_to_palette("#cdd6f4")
        go_nord.add_color_to_palette("#f38ba8")
        go_nord.add_color_to_palette("#a6e3a1")
        go_nord.add_color_to_palette("#89b4fa")
        go_nord.add_color_to_palette("#f9e2af")
        go_nord.add_color_to_palette("#cba6f7")
        
        go_nord.convert_image(image, save_path="output.jpg")
        # Mostrar resultado
        img_converted = Image.open("output.jpg")
        img_converted.thumbnail((350, 350))

        photo = ImageTk.PhotoImage(img_converted)
        self.canvas_after.configure(image=photo)
        self.canvas_after.image = photo
        label_loading = ctk.CTkLabel(self.window, text="Done!", font=("Arial", 18), text_color="#a6e3a1")
        label_loading.pack(pady=10)
if __name__ == "__main__":
    app = ImageConverterApp()