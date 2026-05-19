#print("hola mundo")
import vgamepad as vg
import keyboard
import signal

# Inicializar el mando virtual
gamepad = vg.VX360Gamepad()

def al_presionar_a(e):
    # 'e' es el evento que envía la librería
    print("Evento: Tecla A presionada físicamente")
    gamepad.press_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_A)
    gamepad.update()

def al_soltar_a(e):
    print("Evento: Tecla A soltada físicamente")
    gamepad.release_button(button=vg.XUSB_BUTTON.XUSB_GAMEPAD_A)
    gamepad.update()

# Configurar los "escuchadores" de eventos para la tecla 'a'
keyboard.on_press_key("a", al_presionar_a)
keyboard.on_release_key("a", al_soltar_a)

print("Sistema iniciado por EVENTOS. Presiona 'a' para activar el mando.")
print("Presiona 'Ctrl+C' en la terminal para salir.")

# Bloqueamos el programa principal para que no se cierre, 
# pero sin consumir CPU, esperando una señal de interrupción.
signal.pause() if hasattr(signal, 'pause') else keyboard.wait('esc')