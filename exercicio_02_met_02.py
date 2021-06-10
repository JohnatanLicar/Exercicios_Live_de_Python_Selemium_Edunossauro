from selenium.webdriver import Firefox
from time import sleep
navegador = Firefox()
navegador.get('https://curso-python-selenium.netlify.app/exercicio_02.html')
sleep(3)
clique = navegador.find_element_by_tag_name('a')
while True:
    clique.click()
    elemento = navegador.find_elements_by_tag_name('p')[-1].text
    if elemento.count('ganhou:'):
        break

"""
exercicio de numero 2, metodo 2 seobre Selemium com @edunossauro...
"""