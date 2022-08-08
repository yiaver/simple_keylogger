from pyautogui import press


def leitor(arquivo= str):
    charsSemFiltro= list()
    with open(f"{arquivo}", "r") as arc:
        lista = [n for n in arc.read()]
        charsSemFiltro.append(lista)
    return charsSemFiltro


def filtro(chars :list,filter:list) -> list:
    filtrado = []
    for char in chars[0]:
        if char in filter:
            continue
        else:
            filtrado.append(char)
    return filtrado

def controler(lista_de_etapas = list):
    for n in lista_de_etapas:
        press(str(n))
    return "ok"
listinha= ["a","s",'d']
controler(leitor("keyboard")[0])
