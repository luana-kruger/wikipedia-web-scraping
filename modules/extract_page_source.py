
# # Import Modules

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import StaleElementReferenceException

### Automating Search with Chrome WebDriver

def extract_page_source(url, theme):
    
    # Inicializa uma nova instância do navegador Chrome
    driver = webdriver.Chrome()

    # Navega para a página desejada
    driver.get(url)

    # Localiza o botão de pesquisa na página usando o XPATH e clica nele para iniciar a pesquisa
    search_button = driver.find_element(By.XPATH,'//*[@id="p-search"]/a/span[1]')
    search_button.click()

    # Localiza o campo de pesquisa na página usando o atributo NAME
    search_box = driver.find_element(By.NAME, 'search')

    # Envia o termo de pesquisa
    search_box.send_keys(theme)
    # search_box.submit()
    driver.find_element(By.XPATH,'//*[@id="searchform"]/div/button').click()


    ### Processing Search Results 

    ## Advanced search (exemplo de tema: 'valor historico do dolar' ou 'comida brasileira')
    adv_search = driver.find_elements(By.XPATH, '//*[@id="firstHeading"]')

    ## Página de desambiguação (exemplo de tema: 'seleção brasileira')
    pg_disambig = driver.find_elements(By.XPATH, '//*[@id="disambig"]/table/tbody/tr/td[1]/span/a/img')

    ## Para os casos de 'Pesquisa avançada' e 'Página de desambiguação': 
    ## >> iremos escolher a primeira página que estiver disponível

    if pg_disambig:
        print('Página de desambiguação')
        driver.find_element(By.XPATH, '//*[@id="mw-content-text"]/div[1]/ul/li[1]/a').click()
    elif adv_search:
        if adv_search[0].text == 'Resultados da pesquisa':
            print('Página de Pesquisa avançada')
            driver.find_element(By.XPATH, '//*[@id="mw-content-text"]/div[3]/div[4]/ul/li[1]/div[2]/div[2]/div[1]/a').click()
        else:
            print('Página Wiki')


    print('Salvando página wiki html ... ')
    html_page = driver.page_source

    print('Página salva com sucesso!')
    driver.quit()

    return html_page