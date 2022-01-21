#WhileDGP v0.0.1(remasterizado)
#E-mail: lucasmaciel6690@gmail.com
#GitHub: lucasDSBR
import os
import json
import requests
import urllib.parse
import string
import time as time
from self import self
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver import Chrome
from selenium.webdriver.support.ui import Select
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.chrome.options import Options
from urllib.parse import urlsplit
from seleniumwire import webdriver
from urllib.parse import urlparse
from urllib.parse import urlparse as up
from urllib.request import urlopen
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By 


def buscaGrupo():
    print("\n########################## CONECTANDO-SE AO SITE ######################\n")

    opts = webdriver.ChromeOptions()
    opts.add_argument("--headless")
    opts.add_argument("--no-sandbox")
    opts.add_argument("--disable-dev-shm-usage")
    opts.add_argument("--disable-extensions")
    driver = webdriver.Chrome(executable_path='./chromedriver/chromedriver', options=opts)
    driver.get("http://dgp.cnpq.br/dgp/faces/consulta/consulta_parametrizada.jsf")

    
    driver.find_element(By.XPATH, '//*[@id="idFormConsultaParametrizada:buscaRefinada"]').click()
    time.sleep(1)
    #Selecionando Região
    driver.find_element(By.XPATH, "/html/body/div[3]/div/div/form[2]/span/fieldset/span[3]/span[1]/div[1]/div/div[1]").click()
    time.sleep(0.8)
    totRegiao = len(driver.find_elements(By.XPATH, '/html/body/div[9]/div/ul/li'))
    print("\n########################## SELECIONANDO REGIÃO ######################\n")
    i = 1
    while i < totRegiao :
        nome = driver.find_element(By.XPATH, '/html/body/div[9]/div/ul/li['+str(i)+']').text
        if(nome == 'Nordeste'):
            driver.find_element(By.XPATH, '/html/body/div[9]/div/ul/li['+str(i)+']').click()
            time.sleep(0.8)
            i = totRegiao
        print (nome)
        i = i + 1
    time.sleep(0.8)
    #Selecionando UF
    driver.find_element(By.XPATH, "/html/body/div[3]/div/div/form[2]/span/fieldset/span[3]/span[1]/div[2]/div/div[1]").click()
    time.sleep(0.8)
    totUF = len(driver.find_elements(By.XPATH, '/html/body/div[17]/div/ul/li'))
    i = 1
    while i < totUF :
        nome = driver.find_element(By.XPATH, '/html/body/div[17]/div/ul/li['+str(i)+']').text
        if(nome == 'Ceará'):
            driver.find_element(By.XPATH, '/html/body/div[17]/div/ul/li['+str(i)+']').click()
            time.sleep(0.8)
            i = totUF
        print (nome)
        i = i + 1
    time.sleep(0.8)
    
    #Selecionando Instituição
    print("\n########################## SELECIONANDO INSTITUICAO ######################\n")
    driver.find_element(By.XPATH, "/html/body/div[3]/div/div/form[2]/span/fieldset/span[3]/span[1]/div[3]/div/div[1]").click()
    time.sleep(1)
    totInstituicao = len(driver.find_elements(By.XPATH, '//*[@id="idFormConsultaParametrizada:idInst_panel"]/div/ul/li'))
    i = 1
    while i < totInstituicao :
        nome = driver.find_element(By.XPATH, '//*[@id="idFormConsultaParametrizada:idInst_panel"]/div/ul/li['+str(i)+']').text
        if(nome == 'Universidade da Integração Internacional da Lusofonia Afro-Brasileira'):
            driver.find_element(By.XPATH, '//*[@id="idFormConsultaParametrizada:idInst_panel"]/div/ul/li['+str(i)+']').click()
            time.sleep(0.8)
            i = totInstituicao
        print (nome)
        i = i + 1
    #pesquisando
    driver.find_element(By.XPATH, '//*[@id="idFormConsultaParametrizada:idPesquisar"]').click()

    #Selecionando o total de página
    time.sleep(20)
    driver.find_element(By.XPATH, "/html/body/div[3]/div/div/form[2]/span/div[1]/div[2]/select").click()
    driver.find_element(By.XPATH, "/html/body/div[3]/div/div/form[2]/span/div[1]/div[2]/select/option[3]").click()

    print("\n########################## INICIANDO COLETA DE DADOS ######################\n")
    #Contagem do total de páginas
    time.sleep(15)
    cont_pg0 = len(driver.find_elements(By.XPATH, '//*[@id="idFormConsultaParametrizada:resultadoDataList_paginator_bottom"]/span[3]/span'))
    print("TOTAL DE PÁGINAS: "+str(cont_pg0))


    ######## VOLTANDO PARA A PRIMEIRA PAGINA E COMEÇANDO A PEGAR INFORMAÇÕES ###########
    time.sleep(10)
    driver.find_element(By.XPATH, '//*[@id="idFormConsultaParametrizada:resultadoDataList_paginator_bottom"]/span[3]/span[1]').click()

    #contando novamente o total de páginas para realizar o loop
    time.sleep(10)
    cont_pg1 = len(driver.find_elements(By.XPATH, '//*[@id="idFormConsultaParametrizada:resultadoDataList_paginator_bottom"]/span[3]/span'))

    #loop para pegar informações
    time.sleep(5)
    dados_app2 = []
    dados = []
    i = 0
    while i < cont_pg1:
        #Parte em que ele conta as páginas
        driver.find_element(By.XPATH, '//*[@id="idFormConsultaParametrizada:resultadoDataList_paginator_bottom"]/span[3]/span['+str(i+1)+']').click()
        time.sleep(10)
        #contar o total de grupos daquela pagina
        tot_grupos = len((driver.find_elements(By.XPATH, '//*[@id="idFormConsultaParametrizada:resultadoDataList_content"]/ul/li')))
        #while para pegar informações grupo por grupo a partir do total de grupos:
        print(tot_grupos)
        j = 0
        while j < tot_grupos:
            time.sleep(5)
            driver.find_element(By.XPATH, '//*[@id="idFormConsultaParametrizada:resultadoDataList_list"]/li['+str(j+1)+']/div/div[1]/div/a').click()
            driver.window_handles
            driver.switch_to.window(driver.window_handles[1])
            time.sleep(1)
            #Contagem do total de alunos e pesquisadores no grupo
            cont_pesq = len(driver.find_elements(By.XPATH, '//*[@id="idFormVisualizarGrupoPesquisa:j_idt261_data"]/tr'))
            cont_alun = len(driver.find_elements(By.XPATH, '//*[@id="idFormVisualizarGrupoPesquisa:j_idt278_data"]/tr'))
            cont_pesq_egress = len(driver.find_elements(By.XPATH, '//*[@id="idFormVisualizarGrupoPesquisa:j_idt332_data"]/tr'))
            cont_alun_egress = len(driver.find_elements(By.XPATH, '//*[@id="idFormVisualizarGrupoPesquisa:j_idt344_data"]/tr'))
            
            #fracionando links para pegar apenas IDs dos grupos e Lattes
            #grupo:
            espelho_grupo = driver.find_element(By.XPATH, '//*[@id="idFormVisualizarGrupoPesquisa"]/div/div[2]').text
            parts = urlsplit(espelho_grupo)
            paths = parts.path.split('/')
            #pesquisador:
            
            #aluno:
            
            
            #guardando valores para o arquivo JSON
            espelho_grup = paths[-1]
            ano_formacao = driver.find_element(By.XPATH, '//*[@id="identificacao"]/fieldset/div[2]/div').text
            grupo_nome = driver.find_element(By.XPATH, '//*[@id="tituloImpressao"]/h1').text
            situacao_grupo = driver.find_element(By.XPATH, '//*[@id="identificacao"]/fieldset/div[1]/div').text

            if (situacao_grupo == 'Excluído'):
                driver.close()
                driver.switch_to.window(driver.window_handles[0])
                print("Grupo Excluído...")
                driver.execute_script("window.scrollTo(2,document.body.scrollHeight)")
                j = j + 1
            else:
                data_situacao = driver.find_element(By.XPATH, '//*[@id="identificacao"]/fieldset/div[3]/div').text
                data_ulti_envi = driver.find_element(By.XPATH, '//*[@id="identificacao"]/fieldset/div[4]/div').text
                contato = driver.find_element(By.XPATH, '//*[@id="endereco"]/fieldset/div[13]/div/a').text
                uf = driver.find_element(By.XPATH, '//*[@id="endereco"]/fieldset/div[5]/div').text

                
                localidade = driver.find_element(By.XPATH, '//*[@id="endereco"]/fieldset/div[6]/div').text
                lid_grupo = driver.find_element(By.XPATH, '//*[@id="identificacao"]/fieldset/div[5]/div').text
                lid_grupo = lid_grupo.replace('ui-button', '')
                area_predom = driver.find_element(By.XPATH, '//*[@id="identificacao"]/fieldset/div[6]/div').text
                instituicao = driver.find_element(By.XPATH, '//*[@id="identificacao"]/fieldset/div[7]/div').text
                espelho_link = driver.find_element(By.XPATH, '//*[@id="idFormVisualizarGrupoPesquisa"]/div/div[2]').text
                espelho_link = espelho_link.replace('Endereço para acessar este espelho: ', 'http://')
                #estrutura para guardar os dados no PRIMEIRO arquivo JSON
                grupo =    {
                                "grupo_pesquisa" : 
                                    {
                                        "identificacao":{
                                            "nome": grupo_nome,
                                            "situacao": situacao_grupo,
                                            "anoformacao": ano_formacao,
                                            "lider_es": lid_grupo,
                                            "area_predominante": area_predom,
                                            "UF": uf,
                                            "istituicao": instituicao,
                                            "total_pesq_ativ": cont_pesq,
                                            "total_alun_ativ": cont_alun,
                                            "total_pesq_egress": cont_pesq_egress,
                                            "total_alun_egress": cont_alun_egress,
                                            "espelho_grup": espelho_link
                                            
                                        }
                                    }
                                
                            }

                dados.append(grupo)
                driver.close()
                driver.switch_to.window(driver.window_handles[0])
                print("Dados do grupo coletados...")
                driver.execute_script("window.scrollTo(2,document.body.scrollHeight)")
                j = j + 1
        i = i + 1
    print('Gravando dados nos arquivos')
    #Enviando os dados ao arquivo "data.json"(ATUALIZANDO O ARQUIVO COM NOVOS DADOS)
    with open('grupos.json', 'w', encoding='utf-8') as f:
        json.dump(dados, f, ensure_ascii=False, indent=4)
    print('Dados gravados com sucesso!!')
buscaGrupo()


