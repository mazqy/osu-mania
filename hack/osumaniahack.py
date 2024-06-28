import pyautogui
import keyboard
import time

print('Press the button "q" to start autoclicking...')
def check_pixels_and_press_keys():
    while True:
        start_time = time.time()
        
        # Verifica o pixel na posição (530, 627) para a cor branca (RGB: 255, 255, 255)
        if pyautogui.pixel(530, 560) == (255, 255, 255):
            keyboard.press('d')
            keyboard.release('d')
        
        # Verifica o pixel na posição (630, 627) para uma cor específica (RGB: 0, 175, 255)
        if pyautogui.pixel(630, 560) == (0, 175, 255):
            keyboard.press('f')
            keyboard.release('f')
        
        # Verifica o pixel na posição (730, 627) para uma cor específica (RGB: 0, 175, 255)
        if pyautogui.pixel(730, 560) == (0, 175, 255):
            keyboard.press('j')
            keyboard.release('j')
        
        # Verifica o pixel na posição (830, 510) para a cor branca (RGB: 255, 255, 255)
        if pyautogui.pixel(830, 560) == (255, 255, 255):
            keyboard.press('k')
            keyboard.release('k')
        
        # Calcula o tempo decorrido e ajusta a pausa para manter 60 FPS
        elapsed_time = time.time() - start_time
        time_to_sleep = max(0, (1/390) - elapsed_time)
        time.sleep(time_to_sleep)

# Loop principal
while True:
    # Inicia a verificação se a tecla "q" for pressionada
    if keyboard.is_pressed("q"):
        print("Autoclick initialized...")
        check_pixels_and_press_keys()
