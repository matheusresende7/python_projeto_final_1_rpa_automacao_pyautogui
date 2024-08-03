# Importando as bibliotecas
import pyautogui as pag
import pyperclip

def escrever_texto(texto): # Função para escrever um texto
    pyperclip.copy(texto) # Copiando o texto passado
    pag.hotkey("ctrl", "v") # Colando o texto passado

def conversao_real (valor): # Função para converter um valor para real
    valor = f'{valor:,.2f}' # Formatando com divisor de milhares e separador de casas decimais
    valor = valor.replace(',', 'X').replace('.', ',').replace('X', '.') # Substituindo , por . e . por ,
    return valor

def conversao_numero (valor): # Função para converter um valor para real
    valor = f'{valor:,.0f}' # Formatando com divisor de milhares e separador de casas decimais
    valor = valor.replace(',', '.') # Substituindo , por . e . por ,
    return valor