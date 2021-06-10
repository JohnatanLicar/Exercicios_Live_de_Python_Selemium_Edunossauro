from selenium.webdriver import Firefox
from time import sleep
navegador = Firefox()
navegador.get('https://curso-python-selenium.netlify.app/exercicio_02.html')
sleep(3)
num = navegador.find_elements_by_tag_name('p')[-1].text.split()[-1]
clique = navegador.find_element_by_tag_name('a')
while True:
    clique.click()
    varre_tag_a = navegador.find_elements_by_tag_name('p')[-1].text
    if varre_tag_a.count(num):
        break


"""
exercicio de numero 2, metodo 1 seobre Selemium com @edunossauro...
"""