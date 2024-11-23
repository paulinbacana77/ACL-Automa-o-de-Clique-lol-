import os
import cv2
import numpy as np
from PIL import Image
import pyautogui
import time
import tkinter as tk
from tkinter import messagebox
import keyboard  

template_path = r"caminho\do\arquivo\aqui"

if not os.path.exists(template_path):
    print(f"O arquivo não foi encontrado: {template_path}")
else:
    print(f"Arquivo encontrado: {template_path}")

    try:
        pil_image = Image.open(template_path)
        pil_image = pil_image.convert('L')  
        template = np.array(pil_image)
        print("Imagem carregada com sucesso usando PIL!")

        if template is None:
            print("Erro ao converter a imagem para o formato OpenCV.")
        else:
            print("Imagem convertida para OpenCV com sucesso!")

    except Exception as e:
        print(f"Erro ao carregar a imagem com PIL: {e}")

    if template is None:
        print("Tentando carregar com OpenCV...")
        template = cv2.imread(template_path, 0)  
        if template is None:
            print(f"Erro ao carregar a imagem com OpenCV no caminho: {template_path}")
        else:
            print("Imagem carregada com sucesso usando OpenCV!")


if template is not None:

    def show_success_message(message):
        root = tk.Tk()
        root.withdraw() 
        messagebox.showinfo("Info", message)
        root.destroy()

    show_success_message("Automação Clique iniciado. Pressione 'Q' para sair.")

    w, h = template.shape[::-1]

    while True:
        screenshot = pyautogui.screenshot()
        screenshot_np = np.array(screenshot)
        screenshot_gray = cv2.cvtColor(screenshot_np, cv2.COLOR_RGB2GRAY)

        result = cv2.matchTemplate(screenshot_gray, template, cv2.TM_CCOEFF_NORMED)
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)

        if max_val >= 0.7:
            print(f"Confiança: {max_val:.2f}")
            center_x = max_loc[0] + w // 2
            center_y = max_loc[1] + h // 2
            pyautogui.click(center_x, center_y)

        time.sleep(0.1)

        if keyboard.is_pressed('q'):
            show_success_message("Programa encerrado.")
            break
