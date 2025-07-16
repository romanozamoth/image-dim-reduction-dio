from PIL import Image
from tkinter import Tk, filedialog
import matplotlib.pyplot as plt

# Upload de imagem
root = Tk()
root.withdraw()  # Oculta a janela principal do Tkinter

file_path = filedialog.askopenfilename(title="Selecione uma imagem", filetypes=[("Imagens", "*.png *.jpg *.jpeg")])

if not file_path:
    raise ValueError("Nenhum arquivo selecionado.")

img_colorida = Image.open(file_path).convert("RGB")  # Garante que é RGB

# Converte para escala de cinza (0-255)
img_cinza = img_colorida.convert("L")

# Converte para imagem binária (0 ou 255)
# Aplicando limiar (threshold)
limiar = 128
img_binaria = img_cinza.point(lambda x: 255 if x > limiar else 0, mode='1')

# Plotando as 3 imagens
fig, axs = plt.subplots(1, 3, figsize=(15, 5))

# Imagem colorida
axs[0].imshow(img_colorida)
axs[0].set_title("Colorida")
axs[0].axis("off")

# Imagem em tons de cinza
axs[1].imshow(img_cinza, cmap='gray')
axs[1].set_title("Cinza")
axs[1].axis("off")

# Imagem binária (preto e branco)
axs[2].imshow(img_binaria, cmap='gray')
axs[2].set_title("Binária (Preto e Branco)")
axs[2].axis("off")

plt.tight_layout()
plt.show()