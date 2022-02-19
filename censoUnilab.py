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
    # Opts.add_argument("--headless")
    opts.add_argument("--no-sandbox")
    opts.add_argument("--disable-dev-shm-usage")
    opts.add_argument("--disable-extensions")
    driver = webdriver.Chrome(executable_path='./chromedriver.exe', options=opts)
    driver.get("http://dgp.cnpq.br/dgp/faces/consulta/consulta_parametrizada.jsf")

    
    driver.find_element(By.XPATH, '//*[@id="idFormConsultaParametrizada:buscaRefinada"]').click()
    time.sleep(1)
    # Selecionando Região
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
    # Selecionando UF
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
    
    # Selecionando Instituição
    print("\n########################## SELECIONANDO INSTITUICAO ######################\n")
    driver.find_element(By.XPATH, "/html/body/div[3]/div/div/form[2]/span/fieldset/span[3]/span[1]/div[3]/div/div[1]").click()
    time.sleep(1)
    totInstituicao = len(driver.find_elements(By.XPATH, '//*[@id="idFormConsultaParametrizada:idInst_panel"]/div/ul/li'))
    i = 1
    while i < totInstituicao :
        nome = driver.find_element(By.XPATH, '//*[@id="idFormConsultaParametrizada:idInst_panel"]/div/ul/li['+str(i)+']').text
        #Universidade da Integração Internacional da Lusofonia Afro-Brasileira
        if(nome == 'Universidade da Integração Internacional da Lusofonia Afro-Brasileira'):
            driver.find_element(By.XPATH, '//*[@id="idFormConsultaParametrizada:idInst_panel"]/div/ul/li['+str(i)+']').click()
            time.sleep(0.8)
            i = totInstituicao
        print (nome)
        i = i + 1
    # Pesquisando
    driver.find_element(By.XPATH, '//*[@id="idFormConsultaParametrizada:idPesquisar"]').click()

    # Selecionando o total de página
    time.sleep(10)
    driver.find_element(By.XPATH, "/html/body/div[3]/div/div/form[2]/span/div[1]/div[2]/select").click()
    driver.find_element(By.XPATH, "/html/body/div[3]/div/div/form[2]/span/div[1]/div[2]/select/option[3]").click()

    print("\n########################## INICIANDO COLETA DE DADOS ######################\n")
    # Contagem do total de páginas
    time.sleep(10)
    cont_pg0 = len(driver.find_elements(By.XPATH, '//*[@id="idFormConsultaParametrizada:resultadoDataList_paginator_bottom"]/span[3]/span'))
    print("TOTAL DE PÁGINAS: "+str(cont_pg0))


    ######## VOLTANDO PARA A PRIMEIRA PAGINA E COMEÇANDO A PEGAR INFORMAÇÕES ###########
    time.sleep(5)
    driver.find_element(By.XPATH, '//*[@id="idFormConsultaParametrizada:resultadoDataList_paginator_bottom"]/span[3]/span[1]').click()

    # Contando novamente o total de páginas para realizar o loop
    time.sleep(5)
    cont_pg1 = len(driver.find_elements(By.XPATH, '//*[@id="idFormConsultaParametrizada:resultadoDataList_paginator_bottom"]/span[3]/span'))

    # Loop para pegar informações
    time.sleep(5)
    dados_app2 = []
    dadossss = []
    i = 1
    while i < cont_pg1:
        # Parte em que ele conta as páginas
        driver.find_element(By.XPATH, '//*[@id="idFormConsultaParametrizada:resultadoDataList_paginator_bottom"]/span[3]/span['+str(i+1)+']').click()
        time.sleep(10)
        # Contar o total de grupos daquela pagina
        tot_grupos = len((driver.find_elements(By.XPATH, '//*[@id="idFormConsultaParametrizada:resultadoDataList_content"]/ul/li')))
        # While para pegar informações grupo por grupo a partir do total de grupos:
        print("Total de grupos: ", tot_grupos)
        y = 32
        while y < 33:
            print("Grupo: ", y)
            time.sleep(5)
            driver.find_element(By.XPATH, '//*[@id="idFormConsultaParametrizada:resultadoDataList_list"]/li['+str(y+1)+']/div/div[1]/div/a').click()
            driver.window_handles
            driver.switch_to.window(driver.window_handles[1])
            time.sleep(1)
            producaoPesquisadores = []
            pesquisadores = []
            estudantes = []
            # Contagem do total de alunos e pesquisadores no grupo
            cont_pesq = len(driver.find_elements(By.XPATH, '//*[@id="idFormVisualizarGrupoPesquisa:j_idt261_data"]/tr'))
            cont_alun = len(driver.find_elements(By.XPATH, '//*[@id="idFormVisualizarGrupoPesquisa:j_idt278_data"]/tr'))
            cont_pesq_egress = len(driver.find_elements(By.XPATH, '//*[@id="idFormVisualizarGrupoPesquisa:j_idt332_data"]/tr'))
            cont_alun_egress = len(driver.find_elements(By.XPATH, '//*[@id="idFormVisualizarGrupoPesquisa:j_idt344_data"]/tr'))
            if cont_pesq > 0:
                h = 0
                while h < cont_pesq:
                    nome = driver.find_element(By.XPATH, '//*[@id="idFormVisualizarGrupoPesquisa:j_idt261_data"]/tr['+str(h+1)+']/td[1]').text
                    titulacaoMaxima = driver.find_element(By.XPATH, '//*[@id="idFormVisualizarGrupoPesquisa:j_idt261_data"]/tr['+str(h+1)+']/td[2]').text
                    pesquisadores.append({ 'pesquisador_Nome': nome, 'titulacao_Maxima': titulacaoMaxima})
                    h = h + 1
            
            if cont_alun > 0:
                l = 0
                while l < cont_alun:
                    alunoNome = driver.find_element(By.XPATH, '//*[@id="idFormVisualizarGrupoPesquisa:j_idt278_data"]/tr['+str(l+1)+']/td[1]').text
                    nivelTreinamento = driver.find_element(By.XPATH, '//*[@id="idFormVisualizarGrupoPesquisa:j_idt278_data"]/tr['+str(l+1)+']/td[2]').text
                    estudantes.append({'aluno_Nome': alunoNome, 'nivel_Treinamento': nivelTreinamento})
                    l = l + 1
            # Fracionando links para pegar apenas IDs dos grupos e Lattes
            # Grupo:
            espelho_grupo = driver.find_element(By.XPATH, '//*[@id="idFormVisualizarGrupoPesquisa"]/div/div[2]').text
            parts = urlsplit(espelho_grupo)
            paths = parts.path.split('/')
            # Pesquisador:
            
            # Aluno:
            
            
            # Guardando valores para o arquivo JSON
            espelho_grup = paths[-1]
            ano_formacao = driver.find_element(By.XPATH, '//*[@id="identificacao"]/fieldset/div[2]/div').text
            grupo_nome = driver.find_element(By.XPATH, '//*[@id="tituloImpressao"]/h1').text
            situacao_grupo = driver.find_element(By.XPATH, '//*[@id="identificacao"]/fieldset/div[1]/div').text

            if (situacao_grupo == 'Excluído'):
                driver.close()
                driver.switch_to.window(driver.window_handles[0])
                print("Grupo Excluído...")
                driver.execute_script("window.scrollTo(2,document.body.scrollHeight)")
                y = y + 1
            else:
                dadosContato = []
                data_situacao = driver.find_element(By.XPATH, '//*[@id="identificacao"]/fieldset/div[3]/div').text
                data_ulti_envi = driver.find_element(By.XPATH, '//*[@id="identificacao"]/fieldset/div[4]/div').text
                email = driver.find_element(By.XPATH, '//*[@id="endereco"]/fieldset/div[13]/div/a').text
                uf = driver.find_element(By.XPATH, '//*[@id="endereco"]/fieldset/div[5]/div').text
                telefone = driver.find_element(By.XPATH, '//*[@id="endereco"]/fieldset/div[11]/div').text
                
                dadosContato.append({'telefone': telefone, 'email': email})
                
                
                localidade = driver.find_element(By.XPATH, '//*[@id="endereco"]/fieldset/div[6]/div').text
                lid_grupo = driver.find_element(By.XPATH, '//*[@id="identificacao"]/fieldset/div[5]/div').text
                lid_grupo = lid_grupo.replace('ui-button', '')
                area_predom = driver.find_element(By.XPATH, '//*[@id="identificacao"]/fieldset/div[6]/div').text
                instituicao = driver.find_element(By.XPATH, '//*[@id="identificacao"]/fieldset/div[7]/div').text
                espelho_link = driver.find_element(By.XPATH, '//*[@id="idFormVisualizarGrupoPesquisa"]/div/div[2]').text
                espelho_link = espelho_link.replace('Endereço para acessar este espelho: ', 'http://')

                # Pegando dados de produção dos ultimos 5 anos   
            
                print("\n\nPESQUISADORES(NOMES):\n")
                
                # Estrutura de loop para pegar e mostrar o total de pesquisadores(nomes):        
                nomes = []
                i = 0
                while  i < cont_pesq:
                    nomes.insert(i, driver.find_element_by_xpath('//*[@id="idFormVisualizarGrupoPesquisa:j_idt261_data"]/tr['+str(i+1)+']/td[1]').text)
                    driver.find_element_by_xpath('//*[@id="idFormVisualizarGrupoPesquisa:j_idt261:'+str(i)+':j_idt274"]').click()
                    print(str([i+1])+": "+driver.find_element_by_xpath('//*[@id="idFormVisualizarGrupoPesquisa:j_idt261_data"]/tr['+str(i+1)+']/td[1]').text)
                    i = i + 1
                    
                    #Estrutura de repetição para pegar os links dos curriculos(curriculo lattes)
                    if i == cont_pesq:
                        lattes = []
                        i = 0
                        while i < cont_pesq:
                            driver.window_handles
                            driver.switch_to.window(driver.window_handles[-1])
                            lattes.insert(i, driver.current_url)
                            driver.close()
                            i = i + 1
                # Loop para pegar IDs dos links(lattes)
                ids = []
                m = 0
                while m < len(lattes):
                    link = urlparse(lattes[m])
                    link_convert = urllib.parse.parse_qs(link.query)
                    link_convert = str(link_convert['id'])
                    link_convert = link_convert.replace("[", "")
                    link_convert = link_convert.replace("]", "")
                    link_convert = link_convert.replace("'", "")
                    ids.insert(m, link_convert)
                    m = m + 1
                # Voltando para primeira aba para iniciar a coleta de dados de produção
                driver.switch_to.window(driver.window_handles[1])
                
                
                ########################################################### FIM ###########################################################



                ################################### PEGANDO INDICADORES DE PRODUÇÃO DE CADA PESQUISADOR ###################################
                # Loop para entrar nas páginas:
                e = 0
                valor_cond = 1
                
                while e < len(ids):
                    # Abrindo todas as páginas para pegar dados de produção:
                    driver.execute_script('window.open("http://buscatextual.cnpq.br/buscatextual/graficos.do?metodo=apresentar&codRHCript='+str(ids[e])+'&nome='+str(nomes[e])+'&chamadaExterna=true")')
                    e = e + 1
                    
                # Loop para pegar os dados:
                # resposta = input("\nDigite '1' para ralizar coleta dos dados de anos específicos do pesquisador;\nDigite '2' para realizar a coleta dos dados de todos os anos do pesquisador. \n")
                # resposta = int(resposta)

                if int(valor_cond) == 1:
                    print("Iniciando a coleta...\nPor favor, aguarde!")
                    s = 0
                    while s < len(ids):
                        
                        # voltando para primeira aba do navegador:
                        
                        driver.switch_to.window(driver.window_handles[-s-1])
                        
                        # if driver.find_element(By.XPATH, '/html/body/form/div/div/div/div/div/div/div/div[1]/div/div[2]/b'):
                        # print("Sem dados")
                        # Selecionando o dropdown e contando o total
                        
                        cont_ano = len(driver.find_elements_by_xpath('//*[@id="anoInicio"]/option'))
                        # pegando todos os anos para mostrar depois:
                        if cont_ano != 0:
                            anos = []
                            l = 1
                            while l < cont_ano:
                                driver.find_element_by_xpath('//*[@id="anoInicio"]').click()
                                # time.sleep(0.1)
                                anos.insert(l, driver.find_element_by_xpath('//*[@id="anoInicio"]/option['+str(l+1)+']').text)
                                l = l + 1
                            # mostrando os anos para o usuário escolher
                            print(anos)
                            anosLoop = 0
                            if len(anos) < 5:
                                anosLoop = len(anos)
                            else:
                                anosLoop = 5
                                
                            if anosLoop <= len(anos):
                                j = anosLoop
                                while j > 0:
                                    # Iniciando a busca de dados:
                                    driver.find_element_by_xpath('//*[@id="anoInicio"]').click()
                                    valor_ano = driver.find_element_by_xpath('//*[@id="anoInicio"]/option['+str(j+1)+']').text
                                    nome_ = driver.find_element_by_xpath('/html/body/form/div/div/div/div/div[1]/div/div/div[1]/div/div[1]/h1').text
                                    if nome_ == "Silvia Helena Roberto de Sena - Indicadores da Produção":
                                        if j == 0:
                                            j = 0
                                    print(nome_)
                                    driver.find_element_by_xpath('//*[@id="anoInicio"]').click()
                                    driver.find_element_by_xpath('//*[@id="anoInicio"]/option['+str(j+1)+']').click()
                                    driver.find_element_by_xpath('//*[@id="anoInicio"]').click()
                                    
                                    # Iniciando a coleta de dados por ano:
                                    cont_tabs = len(driver.find_elements_by_xpath('//*[@class="grafico"]'))
                                    if cont_tabs == 9:
                                        cont_lin = len(driver.find_elements_by_xpath('//*[@class="grafico"][9]/div/div/div/table/tbody/tr'))
                                        nome = nomes[s]
                                        if cont_lin == 11:
                                            valor1 = driver.find_element_by_xpath('//*[@class="grafico"][9]/div/div/div/table/tbody/tr[2]/td[1]').text
                                            valor11 = driver.find_element_by_xpath('//*[@class="grafico"][9]/div/div/div/table/tbody/tr[2]/td[2]').text
                                            valor2 = driver.find_element_by_xpath('//*[@class="grafico"][9]/div/div/div/table/tbody/tr[3]/td[1]').text
                                            valor22 = driver.find_element_by_xpath('//*[@class="grafico"][9]/div/div/div/table/tbody/tr[3]/td[2]').text
                                            valor3 = driver.find_element_by_xpath('//*[@class="grafico"][9]/div/div/div/table/tbody/tr[4]/td[1]').text
                                            valor33 = driver.find_element_by_xpath('//*[@class="grafico"][9]/div/div/div/table/tbody/tr[4]/td[2]').text
                                            valor4 = driver.find_element_by_xpath('//*[@class="grafico"][9]/div/div/div/table/tbody/tr[5]/td[1]').text
                                            valor44 = driver.find_element_by_xpath('//*[@class="grafico"][9]/div/div/div/table/tbody/tr[5]/td[2]').text
                                            valor5 = driver.find_element_by_xpath('//*[@class="grafico"][9]/div/div/div/table/tbody/tr[6]/td[1]').text
                                            valor55 = driver.find_element_by_xpath('//*[@class="grafico"][9]/div/div/div/table/tbody/tr[6]/td[2]').text
                                            valor6 = driver.find_element_by_xpath('//*[@class="grafico"][9]/div/div/div/table/tbody/tr[7]/td[1]').text
                                            valor66 = driver.find_element_by_xpath('//*[@class="grafico"][9]/div/div/div/table/tbody/tr[7]/td[2]').text
                                            valor7 = driver.find_element_by_xpath('//*[@class="grafico"][9]/div/div/div/table/tbody/tr[8]/td[1]').text
                                            valor77 = driver.find_element_by_xpath('//*[@class="grafico"][9]/div/div/div/table/tbody/tr[8]/td[2]').text
                                            valor8 = driver.find_element_by_xpath('//*[@class="grafico"][9]/div/div/div/table/tbody/tr[9]/td[1]').text
                                            valor88 = driver.find_element_by_xpath('//*[@class="grafico"][9]/div/div/div/table/tbody/tr[9]/td[2]').text
                                            valor9 = driver.find_element_by_xpath('//*[@class="grafico"][9]/div/div/div/table/tbody/tr[10]/td[1]').text
                                            valor99 = driver.find_element_by_xpath('//*[@class="grafico"][9]/div/div/div/table/tbody/tr[10]/td[2]').text
                                            valor10 = driver.find_element_by_xpath('//*[@class="grafico"][9]/div/div/div/table/tbody/tr[11]/td[1]').text
                                            valor1010 = driver.find_element_by_xpath('//*[@class="grafico"][9]/div/div/div/table/tbody/tr[11]/td[2]').text
                                            grupo = {
                                                            "pesquisador":
                                                                [{
                                                                    "identificacao":[{
                                                                        
                                                                            
                                                                            "pesquisador": nome, "producao":[{
                                                                                "ano": valor_ano,
                                                                                valor1: valor11,
                                                                                valor2: valor22,
                                                                                valor3: valor33,
                                                                                valor4: valor44,
                                                                                valor5: valor55,
                                                                                valor6: valor66,
                                                                                valor7: valor77,
                                                                                valor8: valor88,
                                                                                valor9: valor99,
                                                                                valor10: valor1010
                                                                                }]
                                                                        }]
                                                                }]
                                                    }
                                        if cont_lin == 10:
                                            valor1 = driver.find_element_by_xpath('//*[@class="grafico"][9]/div/div/div/table/tbody/tr[2]/td[1]').text
                                            valor11 = driver.find_element_by_xpath('//*[@class="grafico"][9]/div/div/div/table/tbody/tr[2]/td[2]').text
                                            valor2 = driver.find_element_by_xpath('//*[@class="grafico"][9]/div/div/div/table/tbody/tr[3]/td[1]').text
                                            valor22 = driver.find_element_by_xpath('//*[@class="grafico"][9]/div/div/div/table/tbody/tr[3]/td[2]').text
                                            valor3 = driver.find_element_by_xpath('//*[@class="grafico"][9]/div/div/div/table/tbody/tr[4]/td[1]').text
                                            valor33 = driver.find_element_by_xpath('//*[@class="grafico"][9]/div/div/div/table/tbody/tr[4]/td[2]').text
                                            valor4 = driver.find_element_by_xpath('//*[@class="grafico"][9]/div/div/div/table/tbody/tr[5]/td[1]').text
                                            valor44 = driver.find_element_by_xpath('//*[@class="grafico"][9]/div/div/div/table/tbody/tr[5]/td[2]').text
                                            valor5 = driver.find_element_by_xpath('//*[@class="grafico"][9]/div/div/div/table/tbody/tr[6]/td[1]').text
                                            valor55 = driver.find_element_by_xpath('//*[@class="grafico"][9]/div/div/div/table/tbody/tr[6]/td[2]').text
                                            valor6 = driver.find_element_by_xpath('//*[@class="grafico"][9]/div/div/div/table/tbody/tr[7]/td[1]').text
                                            valor66 = driver.find_element_by_xpath('//*[@class="grafico"][9]/div/div/div/table/tbody/tr[7]/td[2]').text
                                            valor7 = driver.find_element_by_xpath('//*[@class="grafico"][9]/div/div/div/table/tbody/tr[8]/td[1]').text
                                            valor77 = driver.find_element_by_xpath('//*[@class="grafico"][9]/div/div/div/table/tbody/tr[8]/td[2]').text
                                            valor8 = driver.find_element_by_xpath('//*[@class="grafico"][9]/div/div/div/table/tbody/tr[9]/td[1]').text
                                            valor88 = driver.find_element_by_xpath('//*[@class="grafico"][9]/div/div/div/table/tbody/tr[9]/td[2]').text
                                            valor9 = driver.find_element_by_xpath('//*[@class="grafico"][9]/div/div/div/table/tbody/tr[10]/td[1]').text
                                            valor99 = driver.find_element_by_xpath('//*[@class="grafico"][9]/div/div/div/table/tbody/tr[10]/td[2]').text
                                            grupo = {
                                                            "pesquisador":
                                                                [{
                                                                    "identificacao":[{
                                                                        
                                                                        
                                                                            "pesquisador": nome, "producao":[{
                                                                                "ano": valor_ano,
                                                                                valor1: valor11,
                                                                                valor2: valor22,
                                                                                valor3: valor33,
                                                                                valor4: valor44,
                                                                                valor5: valor55,
                                                                                valor6: valor66,
                                                                                valor7: valor77,
                                                                                valor8: valor88,
                                                                                valor9: valor99
                                                                                }]
                                                                        }]
                                                                }]
                                                    }
                                        if cont_lin == 9:
                                            valor1 = driver.find_element_by_xpath('//*[@class="grafico"][9]/div/div/div/table/tbody/tr[2]/td[1]').text
                                            valor11 = driver.find_element_by_xpath('//*[@class="grafico"][9]/div/div/div/table/tbody/tr[2]/td[2]').text
                                            valor2 = driver.find_element_by_xpath('//*[@class="grafico"][9]/div/div/div/table/tbody/tr[3]/td[1]').text
                                            valor22 = driver.find_element_by_xpath('//*[@class="grafico"][9]/div/div/div/table/tbody/tr[3]/td[2]').text
                                            valor3 = driver.find_element_by_xpath('//*[@class="grafico"][9]/div/div/div/table/tbody/tr[4]/td[1]').text
                                            valor33 = driver.find_element_by_xpath('//*[@class="grafico"][9]/div/div/div/table/tbody/tr[4]/td[2]').text
                                            valor4 = driver.find_element_by_xpath('//*[@class="grafico"][9]/div/div/div/table/tbody/tr[5]/td[1]').text
                                            valor44 = driver.find_element_by_xpath('//*[@class="grafico"][9]/div/div/div/table/tbody/tr[5]/td[2]').text
                                            valor5 = driver.find_element_by_xpath('//*[@class="grafico"][9]/div/div/div/table/tbody/tr[6]/td[1]').text
                                            valor55 = driver.find_element_by_xpath('//*[@class="grafico"][9]/div/div/div/table/tbody/tr[6]/td[2]').text
                                            valor6 = driver.find_element_by_xpath('//*[@class="grafico"][9]/div/div/div/table/tbody/tr[7]/td[1]').text
                                            valor66 = driver.find_element_by_xpath('//*[@class="grafico"][9]/div/div/div/table/tbody/tr[7]/td[2]').text
                                            valor7 = driver.find_element_by_xpath('//*[@class="grafico"][9]/div/div/div/table/tbody/tr[8]/td[1]').text
                                            valor77 = driver.find_element_by_xpath('//*[@class="grafico"][9]/div/div/div/table/tbody/tr[8]/td[2]').text
                                            valor8 = driver.find_element_by_xpath('//*[@class="grafico"][9]/div/div/div/table/tbody/tr[9]/td[1]').text
                                            valor88 = driver.find_element_by_xpath('//*[@class="grafico"][9]/div/div/div/table/tbody/tr[9]/td[2]').text
                                            grupo = {
                                                            "pesquisador":
                                                                [{
                                                                    "identificacao":[{
                                                                        
                                                                        
                                                                            "pesquisador": nome, "producao":[{
                                                                                "ano": valor_ano,
                                                                                valor1: valor11,
                                                                                valor2: valor22,
                                                                                valor3: valor33,
                                                                                valor4: valor44,
                                                                                valor5: valor55,
                                                                                valor6: valor66,
                                                                                valor7: valor77,
                                                                                valor8: valor88
                                                                                }]
                                                                        }]
                                                                }]
                                                    }
                                        if cont_lin == 8:
                                            valor1 = driver.find_element_by_xpath('//*[@class="grafico"][9]/div/div/div/table/tbody/tr[2]/td[1]').text
                                            valor11 = driver.find_element_by_xpath('//*[@class="grafico"][9]/div/div/div/table/tbody/tr[2]/td[2]').text
                                            valor2 = driver.find_element_by_xpath('//*[@class="grafico"][9]/div/div/div/table/tbody/tr[3]/td[1]').text
                                            valor22 = driver.find_element_by_xpath('//*[@class="grafico"][9]/div/div/div/table/tbody/tr[3]/td[2]').text
                                            valor3 = driver.find_element_by_xpath('//*[@class="grafico"][9]/div/div/div/table/tbody/tr[4]/td[1]').text
                                            valor33 = driver.find_element_by_xpath('//*[@class="grafico"][9]/div/div/div/table/tbody/tr[4]/td[2]').text
                                            valor4 = driver.find_element_by_xpath('//*[@class="grafico"][9]/div/div/div/table/tbody/tr[5]/td[1]').text
                                            valor44 = driver.find_element_by_xpath('//*[@class="grafico"][9]/div/div/div/table/tbody/tr[5]/td[2]').text
                                            valor5 = driver.find_element_by_xpath('//*[@class="grafico"][9]/div/div/div/table/tbody/tr[6]/td[1]').text
                                            valor55 = driver.find_element_by_xpath('//*[@class="grafico"][9]/div/div/div/table/tbody/tr[6]/td[2]').text
                                            valor6 = driver.find_element_by_xpath('//*[@class="grafico"][9]/div/div/div/table/tbody/tr[7]/td[1]').text
                                            valor66 = driver.find_element_by_xpath('//*[@class="grafico"][9]/div/div/div/table/tbody/tr[7]/td[2]').text
                                            valor7 = driver.find_element_by_xpath('//*[@class="grafico"][9]/div/div/div/table/tbody/tr[8]/td[1]').text
                                            valor77 = driver.find_element_by_xpath('//*[@class="grafico"][9]/div/div/div/table/tbody/tr[8]/td[2]').text
                                            grupo = {
                                                            "pesquisador":
                                                                [{
                                                                    "identificacao":[{
                                                                        
                                                                        
                                                                            "pesquisador": nome, "producao":[{
                                                                                "ano": valor_ano,
                                                                                valor1: valor11,
                                                                                valor2: valor22,
                                                                                valor3: valor33,
                                                                                valor4: valor44,
                                                                                valor5: valor55,
                                                                                valor6: valor66,
                                                                                valor7: valor77
                                                                                }]
                                                                        }]
                                                                }]
                                                    }


                                        if cont_lin == 7:
                                            valor1 = driver.find_element_by_xpath('//*[@class="grafico"][9]/div/div/div/table/tbody/tr[2]/td[1]').text
                                            valor11 = driver.find_element_by_xpath('//*[@class="grafico"][9]/div/div/div/table/tbody/tr[2]/td[2]').text
                                            valor2 = driver.find_element_by_xpath('//*[@class="grafico"][9]/div/div/div/table/tbody/tr[3]/td[1]').text
                                            valor22 = driver.find_element_by_xpath('//*[@class="grafico"][9]/div/div/div/table/tbody/tr[3]/td[2]').text
                                            valor3 = driver.find_element_by_xpath('//*[@class="grafico"][9]/div/div/div/table/tbody/tr[4]/td[1]').text
                                            valor33 = driver.find_element_by_xpath('//*[@class="grafico"][9]/div/div/div/table/tbody/tr[4]/td[2]').text
                                            valor4 = driver.find_element_by_xpath('//*[@class="grafico"][9]/div/div/div/table/tbody/tr[5]/td[1]').text
                                            valor44 = driver.find_element_by_xpath('//*[@class="grafico"][9]/div/div/div/table/tbody/tr[5]/td[2]').text
                                            valor5 = driver.find_element_by_xpath('//*[@class="grafico"][9]/div/div/div/table/tbody/tr[6]/td[1]').text
                                            valor55 = driver.find_element_by_xpath('//*[@class="grafico"][9]/div/div/div/table/tbody/tr[6]/td[2]').text
                                            valor6 = driver.find_element_by_xpath('//*[@class="grafico"][9]/div/div/div/table/tbody/tr[7]/td[1]').text
                                            valor66 = driver.find_element_by_xpath('//*[@class="grafico"][9]/div/div/div/table/tbody/tr[7]/td[2]').text
                                            grupo = {
                                                            "pesquisador":
                                                                [{
                                                                    "identificacao":[{
                                                                        
                                                                        
                                                                            "pesquisador": nome, "producao":[{
                                                                                "ano": valor_ano,
                                                                                valor1: valor11,
                                                                                valor2: valor22,
                                                                                valor3: valor33,
                                                                                valor4: valor44,
                                                                                valor5: valor55,
                                                                                valor6: valor66
                                                                                }]
                                                                        }]
                                                                }]
                                                    }


                                        if cont_lin == 6:
                                            valor1 = driver.find_element_by_xpath('//*[@class="grafico"][9]/div/div/div/table/tbody/tr[2]/td[1]').text
                                            valor11 = driver.find_element_by_xpath('//*[@class="grafico"][9]/div/div/div/table/tbody/tr[2]/td[2]').text
                                            valor2 = driver.find_element_by_xpath('//*[@class="grafico"][9]/div/div/div/table/tbody/tr[3]/td[1]').text
                                            valor22 = driver.find_element_by_xpath('//*[@class="grafico"][9]/div/div/div/table/tbody/tr[3]/td[2]').text
                                            valor3 = driver.find_element_by_xpath('//*[@class="grafico"][9]/div/div/div/table/tbody/tr[4]/td[1]').text
                                            valor33 = driver.find_element_by_xpath('//*[@class="grafico"][9]/div/div/div/table/tbody/tr[4]/td[2]').text
                                            valor4 = driver.find_element_by_xpath('//*[@class="grafico"][9]/div/div/div/table/tbody/tr[5]/td[1]').text
                                            valor44 = driver.find_element_by_xpath('//*[@class="grafico"][9]/div/div/div/table/tbody/tr[5]/td[2]').text
                                            valor5 = driver.find_element_by_xpath('//*[@class="grafico"][9]/div/div/div/table/tbody/tr[6]/td[1]').text
                                            valor55 = driver.find_element_by_xpath('//*[@class="grafico"][9]/div/div/div/table/tbody/tr[6]/td[2]').text
                                            grupo = {
                                                            "pesquisador":
                                                                [{
                                                                    "identificacao":[{
                                                                        
                                                                        
                                                                            "pesquisador": nome, "producao":[{
                                                                                "ano": valor_ano,
                                                                                valor1: valor11,
                                                                                valor2: valor22,
                                                                                valor3: valor33,
                                                                                valor4: valor44,
                                                                                valor5: valor55
                                                                                }]
                                                                        }]
                                                                }]
                                                    }


                                        if cont_lin == 5:
                                            valor1 = driver.find_element_by_xpath('//*[@class="grafico"][9]/div/div/div/table/tbody/tr[2]/td[1]').text
                                            valor11 = driver.find_element_by_xpath('//*[@class="grafico"][9]/div/div/div/table/tbody/tr[2]/td[2]').text
                                            valor2 = driver.find_element_by_xpath('//*[@class="grafico"][9]/div/div/div/table/tbody/tr[3]/td[1]').text
                                            valor22 = driver.find_element_by_xpath('//*[@class="grafico"][9]/div/div/div/table/tbody/tr[3]/td[2]').text
                                            valor3 = driver.find_element_by_xpath('//*[@class="grafico"][9]/div/div/div/table/tbody/tr[4]/td[1]').text
                                            valor33 = driver.find_element_by_xpath('//*[@class="grafico"][9]/div/div/div/table/tbody/tr[4]/td[2]').text
                                            valor4 = driver.find_element_by_xpath('//*[@class="grafico"][9]/div/div/div/table/tbody/tr[5]/td[1]').text
                                            valor44 = driver.find_element_by_xpath('//*[@class="grafico"][9]/div/div/div/table/tbody/tr[5]/td[2]').text
                                            grupo = {
                                                            "pesquisador":
                                                                [{
                                                                    "identificacao":[{
                                                                        
                                                                        
                                                                            "pesquisador": nome, "producao":[{
                                                                                "ano": valor_ano,
                                                                                valor1: valor11,
                                                                                valor2: valor22,
                                                                                valor3: valor33,
                                                                                valor4: valor44
                                                                                }]
                                                                        }]
                                                                }]
                                                    }


                                        if cont_lin == 4:
                                            valor1 = driver.find_element_by_xpath('//*[@class="grafico"][9]/div/div/div/table/tbody/tr[2]/td[1]').text
                                            valor11 = driver.find_element_by_xpath('//*[@class="grafico"][9]/div/div/div/table/tbody/tr[2]/td[2]').text
                                            valor2 = driver.find_element_by_xpath('//*[@class="grafico"][9]/div/div/div/table/tbody/tr[3]/td[1]').text
                                            valor22 = driver.find_element_by_xpath('//*[@class="grafico"][9]/div/div/div/table/tbody/tr[3]/td[2]').text
                                            valor3 = driver.find_element_by_xpath('//*[@class="grafico"][9]/div/div/div/table/tbody/tr[4]/td[1]').text
                                            valor33 = driver.find_element_by_xpath('//*[@class="grafico"][9]/div/div/div/table/tbody/tr[4]/td[2]').text
                                            grupo = {
                                                            "pesquisador":
                                                                [{
                                                                    "identificacao":[{
                                                                        
                                                                        
                                                                            "pesquisador": nome, "producao":[{
                                                                                "ano": valor_ano,
                                                                                valor1: valor11,
                                                                                valor2: valor22,
                                                                                valor3: valor33
                                                                                }]
                                                                        }]
                                                                }]
                                                    }


                                        if cont_lin == 3:
                                            valor1 = driver.find_element_by_xpath('//*[@class="grafico"][9]/div/div/div/table/tbody/tr[2]/td[1]').text
                                            valor11 = driver.find_element_by_xpath('//*[@class="grafico"][9]/div/div/div/table/tbody/tr[2]/td[2]').text
                                            valor2 = driver.find_element_by_xpath('//*[@class="grafico"][9]/div/div/div/table/tbody/tr[3]/td[1]').text
                                            valor22 = driver.find_element_by_xpath('//*[@class="grafico"][9]/div/div/div/table/tbody/tr[3]/td[2]').text
                                            grupo = {
                                                            "pesquisador":
                                                                [{
                                                                    "identificacao":[{
                                                                        
                                                                        
                                                                            "pesquisador": nome, "producao":[{
                                                                                "ano": valor_ano,
                                                                                valor1: valor11,
                                                                                valor2: valor22
                                                                                }]
                                                                        }]
                                                                }]
                                                    }


                                        if cont_lin == 2:
                                            valor1 = driver.find_element_by_xpath('//*[@class="grafico"][9]/div/div/div/table/tbody/tr[2]/td[1]').text
                                            valor11 = driver.find_element_by_xpath('//*[@class="grafico"][9]/div/div/div/table/tbody/tr[2]/td[2]').text
                                            grupo = {
                                                            "pesquisador":
                                                                [{
                                                                    "identificacao":[{
                                                                        
                                                                        
                                                                            "pesquisador": nome, "producao":[{
                                                                                "ano": valor_ano,
                                                                                valor1: valor11
                                                                                }]
                                                                        }]
                                                                }]
                                                    }    
                                    elif cont_tabs == 8:
                                        cont_lin = len(driver.find_elements_by_xpath('//*[@class="grafico"][8]/div/div/div/table/tbody/tr'))
                                        nome = nomes[s]
                                        if cont_lin == 11:
                                            valor1 = driver.find_element_by_xpath('//*[@class="grafico"][8]/div/div/div/table/tbody/tr[2]/td[1]').text
                                            valor11 = driver.find_element_by_xpath('//*[@class="grafico"][8]/div/div/div/table/tbody/tr[2]/td[2]').text
                                            valor2 = driver.find_element_by_xpath('//*[@class="grafico"][8]/div/div/div/table/tbody/tr[3]/td[1]').text
                                            valor22 = driver.find_element_by_xpath('//*[@class="grafico"][8]/div/div/div/table/tbody/tr[3]/td[2]').text
                                            valor3 = driver.find_element_by_xpath('//*[@class="grafico"][8]/div/div/div/table/tbody/tr[4]/td[1]').text
                                            valor33 = driver.find_element_by_xpath('//*[@class="grafico"][8]/div/div/div/table/tbody/tr[4]/td[2]').text
                                            valor4 = driver.find_element_by_xpath('//*[@class="grafico"][8]/div/div/div/table/tbody/tr[5]/td[1]').text
                                            valor44 = driver.find_element_by_xpath('//*[@class="grafico"][8]/div/div/div/table/tbody/tr[5]/td[2]').text
                                            valor5 = driver.find_element_by_xpath('//*[@class="grafico"][8]/div/div/div/table/tbody/tr[6]/td[1]').text
                                            valor55 = driver.find_element_by_xpath('//*[@class="grafico"][8]/div/div/div/table/tbody/tr[6]/td[2]').text
                                            valor6 = driver.find_element_by_xpath('//*[@class="grafico"][8]/div/div/div/table/tbody/tr[7]/td[1]').text
                                            valor66 = driver.find_element_by_xpath('//*[@class="grafico"][8]/div/div/div/table/tbody/tr[7]/td[2]').text
                                            valor7 = driver.find_element_by_xpath('//*[@class="grafico"][8]/div/div/div/table/tbody/tr[8]/td[1]').text
                                            valor77 = driver.find_element_by_xpath('//*[@class="grafico"][8]/div/div/div/table/tbody/tr[8]/td[2]').text
                                            valor8 = driver.find_element_by_xpath('//*[@class="grafico"][8]/div/div/div/table/tbody/tr[9]/td[1]').text
                                            valor88 = driver.find_element_by_xpath('//*[@class="grafico"][8]/div/div/div/table/tbody/tr[9]/td[2]').text
                                            valor9 = driver.find_element_by_xpath('//*[@class="grafico"][8]/div/div/div/table/tbody/tr[10]/td[1]').text
                                            valor99 = driver.find_element_by_xpath('//*[@class="grafico"][8]/div/div/div/table/tbody/tr[10]/td[2]').text
                                            valor10 = driver.find_element_by_xpath('//*[@class="grafico"][8]/div/div/div/table/tbody/tr[11]/td[1]').text
                                            valor1010 = driver.find_element_by_xpath('//*[@class="grafico"][8]/div/div/div/table/tbody/tr[11]/td[2]').text
                                            grupo = {
                                                            "pesquisador":
                                                                [{
                                                                    "identificacao":[{
                                                                        
                                                                        
                                                                            "pesquisador": nome, "producao":[{
                                                                                "ano": valor_ano,
                                                                                valor1: valor11,
                                                                                valor2: valor22,
                                                                                valor3: valor33,
                                                                                valor4: valor44,
                                                                                valor5: valor55,
                                                                                valor6: valor66,
                                                                                valor7: valor77,
                                                                                valor8: valor88,
                                                                                valor9: valor99,
                                                                                valor10: valor1010
                                                                                }]
                                                                        }]
                                                                }]
                                                    }
                                        if cont_lin == 10:
                                            valor1 = driver.find_element_by_xpath('//*[@class="grafico"][8]/div/div/div/table/tbody/tr[2]/td[1]').text
                                            valor11 = driver.find_element_by_xpath('//*[@class="grafico"][8]/div/div/div/table/tbody/tr[2]/td[2]').text
                                            valor2 = driver.find_element_by_xpath('//*[@class="grafico"][8]/div/div/div/table/tbody/tr[3]/td[1]').text
                                            valor22 = driver.find_element_by_xpath('//*[@class="grafico"][8]/div/div/div/table/tbody/tr[3]/td[2]').text
                                            valor3 = driver.find_element_by_xpath('//*[@class="grafico"][8]/div/div/div/table/tbody/tr[4]/td[1]').text
                                            valor33 = driver.find_element_by_xpath('//*[@class="grafico"][8]/div/div/div/table/tbody/tr[4]/td[2]').text
                                            valor4 = driver.find_element_by_xpath('//*[@class="grafico"][8]/div/div/div/table/tbody/tr[5]/td[1]').text
                                            valor44 = driver.find_element_by_xpath('//*[@class="grafico"][8]/div/div/div/table/tbody/tr[5]/td[2]').text
                                            valor5 = driver.find_element_by_xpath('//*[@class="grafico"][8]/div/div/div/table/tbody/tr[6]/td[1]').text
                                            valor55 = driver.find_element_by_xpath('//*[@class="grafico"][8]/div/div/div/table/tbody/tr[6]/td[2]').text
                                            valor6 = driver.find_element_by_xpath('//*[@class="grafico"][8]/div/div/div/table/tbody/tr[7]/td[1]').text
                                            valor66 = driver.find_element_by_xpath('//*[@class="grafico"][8]/div/div/div/table/tbody/tr[7]/td[2]').text
                                            valor7 = driver.find_element_by_xpath('//*[@class="grafico"][8]/div/div/div/table/tbody/tr[8]/td[1]').text
                                            valor77 = driver.find_element_by_xpath('//*[@class="grafico"][8]/div/div/div/table/tbody/tr[8]/td[2]').text
                                            valor8 = driver.find_element_by_xpath('//*[@class="grafico"][8]/div/div/div/table/tbody/tr[9]/td[1]').text
                                            valor88 = driver.find_element_by_xpath('//*[@class="grafico"][8]/div/div/div/table/tbody/tr[9]/td[2]').text
                                            valor9 = driver.find_element_by_xpath('//*[@class="grafico"][8]/div/div/div/table/tbody/tr[10]/td[1]').text
                                            valor99 = driver.find_element_by_xpath('//*[@class="grafico"][8]/div/div/div/table/tbody/tr[10]/td[2]').text
                                            grupo = {
                                                            "pesquisador":
                                                                [{
                                                                    "identificacao":[{
                                                                        
                                                                        
                                                                            "pesquisador": nome, "producao":[{
                                                                                "ano": valor_ano,
                                                                                valor1: valor11,
                                                                                valor2: valor22,
                                                                                valor3: valor33,
                                                                                valor4: valor44,
                                                                                valor5: valor55,
                                                                                valor6: valor66,
                                                                                valor7: valor77,
                                                                                valor8: valor88,
                                                                                valor9: valor99
                                                                                }]
                                                                        }]
                                                                }]
                                                    }
                                        if cont_lin == 9:
                                            valor1 = driver.find_element_by_xpath('//*[@class="grafico"][8]/div/div/div/table/tbody/tr[2]/td[1]').text
                                            valor11 = driver.find_element_by_xpath('//*[@class="grafico"][8]/div/div/div/table/tbody/tr[2]/td[2]').text
                                            valor2 = driver.find_element_by_xpath('//*[@class="grafico"][8]/div/div/div/table/tbody/tr[3]/td[1]').text
                                            valor22 = driver.find_element_by_xpath('//*[@class="grafico"][8]/div/div/div/table/tbody/tr[3]/td[2]').text
                                            valor3 = driver.find_element_by_xpath('//*[@class="grafico"][8]/div/div/div/table/tbody/tr[4]/td[1]').text
                                            valor33 = driver.find_element_by_xpath('//*[@class="grafico"][8]/div/div/div/table/tbody/tr[4]/td[2]').text
                                            valor4 = driver.find_element_by_xpath('//*[@class="grafico"][8]/div/div/div/table/tbody/tr[5]/td[1]').text
                                            valor44 = driver.find_element_by_xpath('//*[@class="grafico"][8]/div/div/div/table/tbody/tr[5]/td[2]').text
                                            valor5 = driver.find_element_by_xpath('//*[@class="grafico"][8]/div/div/div/table/tbody/tr[6]/td[1]').text
                                            valor55 = driver.find_element_by_xpath('//*[@class="grafico"][8]/div/div/div/table/tbody/tr[6]/td[2]').text
                                            valor6 = driver.find_element_by_xpath('//*[@class="grafico"][8]/div/div/div/table/tbody/tr[7]/td[1]').text
                                            valor66 = driver.find_element_by_xpath('//*[@class="grafico"][8]/div/div/div/table/tbody/tr[7]/td[2]').text
                                            valor7 = driver.find_element_by_xpath('//*[@class="grafico"][8]/div/div/div/table/tbody/tr[8]/td[1]').text
                                            valor77 = driver.find_element_by_xpath('//*[@class="grafico"][8]/div/div/div/table/tbody/tr[8]/td[2]').text
                                            valor8 = driver.find_element_by_xpath('//*[@class="grafico"][8]/div/div/div/table/tbody/tr[9]/td[1]').text
                                            valor88 = driver.find_element_by_xpath('//*[@class="grafico"][8]/div/div/div/table/tbody/tr[9]/td[2]').text
                                            grupo = {
                                                            "pesquisador":
                                                                [{
                                                                    "identificacao":[{
                                                                        
                                                                        
                                                                            "pesquisador": nome, "producao":[{
                                                                                "ano": valor_ano,
                                                                                valor1: valor11,
                                                                                valor2: valor22,
                                                                                valor3: valor33,
                                                                                valor4: valor44,
                                                                                valor5: valor55,
                                                                                valor6: valor66,
                                                                                valor7: valor77,
                                                                                valor8: valor88
                                                                                }]
                                                                        }]
                                                                }]
                                                    }
                                        if cont_lin == 8:
                                            valor1 = driver.find_element_by_xpath('//*[@class="grafico"][8]/div/div/div/table/tbody/tr[2]/td[1]').text
                                            valor11 = driver.find_element_by_xpath('//*[@class="grafico"][8]/div/div/div/table/tbody/tr[2]/td[2]').text
                                            valor2 = driver.find_element_by_xpath('//*[@class="grafico"][8]/div/div/div/table/tbody/tr[3]/td[1]').text
                                            valor22 = driver.find_element_by_xpath('//*[@class="grafico"][8]/div/div/div/table/tbody/tr[3]/td[2]').text
                                            valor3 = driver.find_element_by_xpath('//*[@class="grafico"][8]/div/div/div/table/tbody/tr[4]/td[1]').text
                                            valor33 = driver.find_element_by_xpath('//*[@class="grafico"][8]/div/div/div/table/tbody/tr[4]/td[2]').text
                                            valor4 = driver.find_element_by_xpath('//*[@class="grafico"][8]/div/div/div/table/tbody/tr[5]/td[1]').text
                                            valor44 = driver.find_element_by_xpath('//*[@class="grafico"][8]/div/div/div/table/tbody/tr[5]/td[2]').text
                                            valor5 = driver.find_element_by_xpath('//*[@class="grafico"][8]/div/div/div/table/tbody/tr[6]/td[1]').text
                                            valor55 = driver.find_element_by_xpath('//*[@class="grafico"][8]/div/div/div/table/tbody/tr[6]/td[2]').text
                                            valor6 = driver.find_element_by_xpath('//*[@class="grafico"][8]/div/div/div/table/tbody/tr[7]/td[1]').text
                                            valor66 = driver.find_element_by_xpath('//*[@class="grafico"][8]/div/div/div/table/tbody/tr[7]/td[2]').text
                                            valor7 = driver.find_element_by_xpath('//*[@class="grafico"][8]/div/div/div/table/tbody/tr[8]/td[1]').text
                                            valor77 = driver.find_element_by_xpath('//*[@class="grafico"][8]/div/div/div/table/tbody/tr[8]/td[2]').text
                                            grupo = {
                                                            "pesquisador":
                                                                [{
                                                                    "identificacao":[{
                                                                        
                                                                        
                                                                            "pesquisador": nome, "producao":[{
                                                                                "ano": valor_ano,
                                                                                valor1: valor11,
                                                                                valor2: valor22,
                                                                                valor3: valor33,
                                                                                valor4: valor44,
                                                                                valor5: valor55,
                                                                                valor6: valor66,
                                                                                valor7: valor77
                                                                                }]
                                                                        }]
                                                                }]
                                                    }
                                        if cont_lin == 7:
                                            valor1 = driver.find_element_by_xpath('//*[@class="grafico"][8]/div/div/div/table/tbody/tr[2]/td[1]').text
                                            valor11 = driver.find_element_by_xpath('//*[@class="grafico"][8]/div/div/div/table/tbody/tr[2]/td[2]').text
                                            valor2 = driver.find_element_by_xpath('//*[@class="grafico"][8]/div/div/div/table/tbody/tr[3]/td[1]').text
                                            valor22 = driver.find_element_by_xpath('//*[@class="grafico"][8]/div/div/div/table/tbody/tr[3]/td[2]').text
                                            valor3 = driver.find_element_by_xpath('//*[@class="grafico"][8]/div/div/div/table/tbody/tr[4]/td[1]').text
                                            valor33 = driver.find_element_by_xpath('//*[@class="grafico"][8]/div/div/div/table/tbody/tr[4]/td[2]').text
                                            valor4 = driver.find_element_by_xpath('//*[@class="grafico"][8]/div/div/div/table/tbody/tr[5]/td[1]').text
                                            valor44 = driver.find_element_by_xpath('//*[@class="grafico"][8]/div/div/div/table/tbody/tr[5]/td[2]').text
                                            valor5 = driver.find_element_by_xpath('//*[@class="grafico"][8]/div/div/div/table/tbody/tr[6]/td[1]').text
                                            valor55 = driver.find_element_by_xpath('//*[@class="grafico"][8]/div/div/div/table/tbody/tr[6]/td[2]').text
                                            valor6 = driver.find_element_by_xpath('//*[@class="grafico"][8]/div/div/div/table/tbody/tr[7]/td[1]').text
                                            valor66 = driver.find_element_by_xpath('//*[@class="grafico"][8]/div/div/div/table/tbody/tr[7]/td[2]').text
                                            grupo = {
                                                            "pesquisador":
                                                                [{
                                                                    "identificacao":[{
                                                                        
                                                                        
                                                                            "pesquisador": nome, "producao":[{
                                                                                "ano": valor_ano,
                                                                                valor1: valor11,
                                                                                valor2: valor22,
                                                                                valor3: valor33,
                                                                                valor4: valor44,
                                                                                valor5: valor55,
                                                                                valor6: valor66
                                                                                }]
                                                                        }]
                                                                }]
                                                    }
                                        if cont_lin == 6:
                                            valor1 = driver.find_element_by_xpath('//*[@class="grafico"][8]/div/div/div/table/tbody/tr[2]/td[1]').text
                                            valor11 = driver.find_element_by_xpath('//*[@class="grafico"][8]/div/div/div/table/tbody/tr[2]/td[2]').text
                                            valor2 = driver.find_element_by_xpath('//*[@class="grafico"][8]/div/div/div/table/tbody/tr[3]/td[1]').text
                                            valor22 = driver.find_element_by_xpath('//*[@class="grafico"][8]/div/div/div/table/tbody/tr[3]/td[2]').text
                                            valor3 = driver.find_element_by_xpath('//*[@class="grafico"][8]/div/div/div/table/tbody/tr[4]/td[1]').text
                                            valor33 = driver.find_element_by_xpath('//*[@class="grafico"][8]/div/div/div/table/tbody/tr[4]/td[2]').text
                                            valor4 = driver.find_element_by_xpath('//*[@class="grafico"][8]/div/div/div/table/tbody/tr[5]/td[1]').text
                                            valor44 = driver.find_element_by_xpath('//*[@class="grafico"][8]/div/div/div/table/tbody/tr[5]/td[2]').text
                                            valor5 = driver.find_element_by_xpath('//*[@class="grafico"][8]/div/div/div/table/tbody/tr[6]/td[1]').text
                                            valor55 = driver.find_element_by_xpath('//*[@class="grafico"][8]/div/div/div/table/tbody/tr[6]/td[2]').text
                                            grupo = {
                                                            "pesquisador":
                                                                [{
                                                                    "identificacao":[{
                                                                        
                                                                        
                                                                            "pesquisador": nome, "producao":[{
                                                                                "ano": valor_ano,
                                                                                valor1: valor11,
                                                                                valor2: valor22,
                                                                                valor3: valor33,
                                                                                valor4: valor44,
                                                                                valor5: valor55
                                                                                }]
                                                                        }]
                                                                }]
                                                    }
                                        if cont_lin == 5:
                                            valor1 = driver.find_element_by_xpath('//*[@class="grafico"][8]/div/div/div/table/tbody/tr[2]/td[1]').text
                                            valor11 = driver.find_element_by_xpath('//*[@class="grafico"][8]/div/div/div/table/tbody/tr[2]/td[2]').text
                                            valor2 = driver.find_element_by_xpath('//*[@class="grafico"][8]/div/div/div/table/tbody/tr[3]/td[1]').text
                                            valor22 = driver.find_element_by_xpath('//*[@class="grafico"][8]/div/div/div/table/tbody/tr[3]/td[2]').text
                                            valor3 = driver.find_element_by_xpath('//*[@class="grafico"][8]/div/div/div/table/tbody/tr[4]/td[1]').text
                                            valor33 = driver.find_element_by_xpath('//*[@class="grafico"][8]/div/div/div/table/tbody/tr[4]/td[2]').text
                                            valor4 = driver.find_element_by_xpath('//*[@class="grafico"][8]/div/div/div/table/tbody/tr[5]/td[1]').text
                                            valor44 = driver.find_element_by_xpath('//*[@class="grafico"][8]/div/div/div/table/tbody/tr[5]/td[2]').text
                                            grupo = {
                                                            "pesquisador":
                                                                [{
                                                                    "identificacao":[{
                                                                        
                                                                        
                                                                            "pesquisador": nome, "producao":[{
                                                                                "ano": valor_ano,
                                                                                valor1: valor11,
                                                                                valor2: valor22,
                                                                                valor3: valor33,
                                                                                valor4: valor44
                                                                                }]
                                                                        }]
                                                                }]
                                                    }
                                        if cont_lin == 4:
                                            valor1 = driver.find_element_by_xpath('//*[@class="grafico"][8]/div/div/div/table/tbody/tr[2]/td[1]').text
                                            valor11 = driver.find_element_by_xpath('//*[@class="grafico"][8]/div/div/div/table/tbody/tr[2]/td[2]').text
                                            valor2 = driver.find_element_by_xpath('//*[@class="grafico"][8]/div/div/div/table/tbody/tr[3]/td[1]').text
                                            valor22 = driver.find_element_by_xpath('//*[@class="grafico"][8]/div/div/div/table/tbody/tr[3]/td[2]').text
                                            valor3 = driver.find_element_by_xpath('//*[@class="grafico"][8]/div/div/div/table/tbody/tr[4]/td[1]').text
                                            valor33 = driver.find_element_by_xpath('//*[@class="grafico"][8]/div/div/div/table/tbody/tr[4]/td[2]').text
                                            grupo = {
                                                            "pesquisador":
                                                                [{
                                                                    "identificacao":[{
                                                                        
                                                                        
                                                                            "pesquisador": nome, "producao":[{
                                                                                "ano": valor_ano,
                                                                                valor1: valor11,
                                                                                valor2: valor22,
                                                                                valor3: valor33
                                                                                }]
                                                                        }]
                                                                }]
                                                    }
                                        if cont_lin == 3:
                                            valor1 = driver.find_element_by_xpath('//*[@class="grafico"][8]/div/div/div/table/tbody/tr[2]/td[1]').text
                                            valor11 = driver.find_element_by_xpath('//*[@class="grafico"][8]/div/div/div/table/tbody/tr[2]/td[2]').text
                                            valor2 = driver.find_element_by_xpath('//*[@class="grafico"][8]/div/div/div/table/tbody/tr[3]/td[1]').text
                                            valor22 = driver.find_element_by_xpath('//*[@class="grafico"][8]/div/div/div/table/tbody/tr[3]/td[2]').text
                                            grupo = {
                                                            "pesquisador":
                                                                [{
                                                                    "identificacao":[{
                                                                        
                                                                        
                                                                            "pesquisador": nome, "producao":[{
                                                                                "ano": valor_ano,
                                                                                valor1: valor11,
                                                                                valor2: valor22
                                                                                }]
                                                                        }]
                                                                }]
                                                    }
                                        if cont_lin == 2:
                                            valor1 = driver.find_element_by_xpath('//*[@class="grafico"][8]/div/div/div/table/tbody/tr[2]/td[1]').text
                                            valor11 = driver.find_element_by_xpath('//*[@class="grafico"][8]/div/div/div/table/tbody/tr[2]/td[2]').text
                                            grupo = {
                                                            "pesquisador":
                                                                [{
                                                                    "identificacao":[{
                                                                        
                                                                        
                                                                            "pesquisador": nome, "producao":[{
                                                                                "ano": valor_ano,
                                                                                valor1: valor11
                                                                                }]
                                                                        }]
                                                                }]
                                                    }
                                    elif cont_tabs == 7:
                                        cont_lin = len(driver.find_elements_by_xpath('//*[@class="grafico"][7]/div/div/div/table/tbody/tr'))
                                        nome = nomes[s]
                                        if cont_lin == 11:
                                            valor1 = driver.find_element_by_xpath('//*[@class="grafico"][7]/div/div/div/table/tbody/tr[2]/td[1]').text
                                            valor11 = driver.find_element_by_xpath('//*[@class="grafico"][7]/div/div/div/table/tbody/tr[2]/td[2]').text
                                            valor2 = driver.find_element_by_xpath('//*[@class="grafico"][7]/div/div/div/table/tbody/tr[3]/td[1]').text
                                            valor22 = driver.find_element_by_xpath('//*[@class="grafico"][7]/div/div/div/table/tbody/tr[3]/td[2]').text
                                            valor3 = driver.find_element_by_xpath('//*[@class="grafico"][7]/div/div/div/table/tbody/tr[4]/td[1]').text
                                            valor33 = driver.find_element_by_xpath('//*[@class="grafico"][7]/div/div/div/table/tbody/tr[4]/td[2]').text
                                            valor4 = driver.find_element_by_xpath('//*[@class="grafico"][7]/div/div/div/table/tbody/tr[5]/td[1]').text
                                            valor44 = driver.find_element_by_xpath('//*[@class="grafico"][7]/div/div/div/table/tbody/tr[5]/td[2]').text
                                            valor5 = driver.find_element_by_xpath('//*[@class="grafico"][7]/div/div/div/table/tbody/tr[6]/td[1]').text
                                            valor55 = driver.find_element_by_xpath('//*[@class="grafico"][7]/div/div/div/table/tbody/tr[6]/td[2]').text
                                            valor6 = driver.find_element_by_xpath('//*[@class="grafico"][7]/div/div/div/table/tbody/tr[7]/td[1]').text
                                            valor66 = driver.find_element_by_xpath('//*[@class="grafico"][7]/div/div/div/table/tbody/tr[7]/td[2]').text
                                            valor7 = driver.find_element_by_xpath('//*[@class="grafico"][7]/div/div/div/table/tbody/tr[8]/td[1]').text
                                            valor77 = driver.find_element_by_xpath('//*[@class="grafico"][7]/div/div/div/table/tbody/tr[8]/td[2]').text
                                            valor8 = driver.find_element_by_xpath('//*[@class="grafico"][7]/div/div/div/table/tbody/tr[9]/td[1]').text
                                            valor88 = driver.find_element_by_xpath('//*[@class="grafico"][7]/div/div/div/table/tbody/tr[9]/td[2]').text
                                            valor9 = driver.find_element_by_xpath('//*[@class="grafico"][7]/div/div/div/table/tbody/tr[10]/td[1]').text
                                            valor99 = driver.find_element_by_xpath('//*[@class="grafico"][7]/div/div/div/table/tbody/tr[10]/td[2]').text
                                            valor10 = driver.find_element_by_xpath('//*[@class="grafico"][7]/div/div/div/table/tbody/tr[11]/td[1]').text
                                            valor1010 = driver.find_element_by_xpath('//*[@class="grafico"][7]/div/div/div/table/tbody/tr[11]/td[2]').text
                                            grupo = {
                                                            "pesquisador":
                                                                [{
                                                                    "identificacao":[{
                                                                        
                                                                        
                                                                            "pesquisador": nome, "producao":[{
                                                                                "ano": valor_ano,
                                                                                valor1: valor11,
                                                                                valor2: valor22,
                                                                                valor3: valor33,
                                                                                valor4: valor44,
                                                                                valor5: valor55,
                                                                                valor6: valor66,
                                                                                valor7: valor77,
                                                                                valor8: valor88,
                                                                                valor9: valor99,
                                                                                valor10: valor1010
                                                                                }]
                                                                        }]
                                                                }]
                                                    }
                                        if cont_lin == 10:
                                            valor1 = driver.find_element_by_xpath('//*[@class="grafico"][7]/div/div/div/table/tbody/tr[2]/td[1]').text
                                            valor11 = driver.find_element_by_xpath('//*[@class="grafico"][7]/div/div/div/table/tbody/tr[2]/td[2]').text
                                            valor2 = driver.find_element_by_xpath('//*[@class="grafico"][7]/div/div/div/table/tbody/tr[3]/td[1]').text
                                            valor22 = driver.find_element_by_xpath('//*[@class="grafico"][7]/div/div/div/table/tbody/tr[3]/td[2]').text
                                            valor3 = driver.find_element_by_xpath('//*[@class="grafico"][7]/div/div/div/table/tbody/tr[4]/td[1]').text
                                            valor33 = driver.find_element_by_xpath('//*[@class="grafico"][7]/div/div/div/table/tbody/tr[4]/td[2]').text
                                            valor4 = driver.find_element_by_xpath('//*[@class="grafico"][7]/div/div/div/table/tbody/tr[5]/td[1]').text
                                            valor44 = driver.find_element_by_xpath('//*[@class="grafico"][7]/div/div/div/table/tbody/tr[5]/td[2]').text
                                            valor5 = driver.find_element_by_xpath('//*[@class="grafico"][7]/div/div/div/table/tbody/tr[6]/td[1]').text
                                            valor55 = driver.find_element_by_xpath('//*[@class="grafico"][7]/div/div/div/table/tbody/tr[6]/td[2]').text
                                            valor6 = driver.find_element_by_xpath('//*[@class="grafico"][7]/div/div/div/table/tbody/tr[7]/td[1]').text
                                            valor66 = driver.find_element_by_xpath('//*[@class="grafico"][7]/div/div/div/table/tbody/tr[7]/td[2]').text
                                            valor7 = driver.find_element_by_xpath('//*[@class="grafico"][7]/div/div/div/table/tbody/tr[8]/td[1]').text
                                            valor77 = driver.find_element_by_xpath('//*[@class="grafico"][7]/div/div/div/table/tbody/tr[8]/td[2]').text
                                            valor8 = driver.find_element_by_xpath('//*[@class="grafico"][7]/div/div/div/table/tbody/tr[9]/td[1]').text
                                            valor88 = driver.find_element_by_xpath('//*[@class="grafico"][7]/div/div/div/table/tbody/tr[9]/td[2]').text
                                            valor9 = driver.find_element_by_xpath('//*[@class="grafico"][7]/div/div/div/table/tbody/tr[10]/td[1]').text
                                            valor99 = driver.find_element_by_xpath('//*[@class="grafico"][7]/div/div/div/table/tbody/tr[10]/td[2]').text
                                            grupo = {
                                                            "pesquisador":
                                                                [{
                                                                    "identificacao":[{
                                                                        
                                                                        
                                                                            "pesquisador": nome, "producao":[{
                                                                                "ano": valor_ano,
                                                                                valor1: valor11,
                                                                                valor2: valor22,
                                                                                valor3: valor33,
                                                                                valor4: valor44,
                                                                                valor5: valor55,
                                                                                valor6: valor66,
                                                                                valor7: valor77,
                                                                                valor8: valor88,
                                                                                valor9: valor99
                                                                                }]
                                                                        }]
                                                                }]
                                                    }
                                        if cont_lin == 9:
                                            valor1 = driver.find_element_by_xpath('//*[@class="grafico"][7]/div/div/div/table/tbody/tr[2]/td[1]').text
                                            valor11 = driver.find_element_by_xpath('//*[@class="grafico"][7]/div/div/div/table/tbody/tr[2]/td[2]').text
                                            valor2 = driver.find_element_by_xpath('//*[@class="grafico"][7]/div/div/div/table/tbody/tr[3]/td[1]').text
                                            valor22 = driver.find_element_by_xpath('//*[@class="grafico"][7]/div/div/div/table/tbody/tr[3]/td[2]').text
                                            valor3 = driver.find_element_by_xpath('//*[@class="grafico"][7]/div/div/div/table/tbody/tr[4]/td[1]').text
                                            valor33 = driver.find_element_by_xpath('//*[@class="grafico"][7]/div/div/div/table/tbody/tr[4]/td[2]').text
                                            valor4 = driver.find_element_by_xpath('//*[@class="grafico"][7]/div/div/div/table/tbody/tr[5]/td[1]').text
                                            valor44 = driver.find_element_by_xpath('//*[@class="grafico"][7]/div/div/div/table/tbody/tr[5]/td[2]').text
                                            valor5 = driver.find_element_by_xpath('//*[@class="grafico"][7]/div/div/div/table/tbody/tr[6]/td[1]').text
                                            valor55 = driver.find_element_by_xpath('//*[@class="grafico"][7]/div/div/div/table/tbody/tr[6]/td[2]').text
                                            valor6 = driver.find_element_by_xpath('//*[@class="grafico"][7]/div/div/div/table/tbody/tr[7]/td[1]').text
                                            valor66 = driver.find_element_by_xpath('//*[@class="grafico"][7]/div/div/div/table/tbody/tr[7]/td[2]').text
                                            valor7 = driver.find_element_by_xpath('//*[@class="grafico"][7]/div/div/div/table/tbody/tr[8]/td[1]').text
                                            valor77 = driver.find_element_by_xpath('//*[@class="grafico"][7]/div/div/div/table/tbody/tr[8]/td[2]').text
                                            valor8 = driver.find_element_by_xpath('//*[@class="grafico"][7]/div/div/div/table/tbody/tr[9]/td[1]').text
                                            valor88 = driver.find_element_by_xpath('//*[@class="grafico"][7]/div/div/div/table/tbody/tr[9]/td[2]').text
                                            grupo = {
                                                            "pesquisador":
                                                                [{
                                                                    "identificacao":[{
                                                                        
                                                                        
                                                                            "pesquisador": nome, "producao":[{
                                                                                "ano": valor_ano,
                                                                                valor1: valor11,
                                                                                valor2: valor22,
                                                                                valor3: valor33,
                                                                                valor4: valor44,
                                                                                valor5: valor55,
                                                                                valor6: valor66,
                                                                                valor7: valor77,
                                                                                valor8: valor88
                                                                                }]
                                                                        }]
                                                                }]
                                                    }
                                        if cont_lin == 8:
                                            valor1 = driver.find_element_by_xpath('//*[@class="grafico"][7]/div/div/div/table/tbody/tr[2]/td[1]').text
                                            valor11 = driver.find_element_by_xpath('//*[@class="grafico"][7]/div/div/div/table/tbody/tr[2]/td[2]').text
                                            valor2 = driver.find_element_by_xpath('//*[@class="grafico"][7]/div/div/div/table/tbody/tr[3]/td[1]').text
                                            valor22 = driver.find_element_by_xpath('//*[@class="grafico"][7]/div/div/div/table/tbody/tr[3]/td[2]').text
                                            valor3 = driver.find_element_by_xpath('//*[@class="grafico"][7]/div/div/div/table/tbody/tr[4]/td[1]').text
                                            valor33 = driver.find_element_by_xpath('//*[@class="grafico"][7]/div/div/div/table/tbody/tr[4]/td[2]').text
                                            valor4 = driver.find_element_by_xpath('//*[@class="grafico"][7]/div/div/div/table/tbody/tr[5]/td[1]').text
                                            valor44 = driver.find_element_by_xpath('//*[@class="grafico"][7]/div/div/div/table/tbody/tr[5]/td[2]').text
                                            valor5 = driver.find_element_by_xpath('//*[@class="grafico"][7]/div/div/div/table/tbody/tr[6]/td[1]').text
                                            valor55 = driver.find_element_by_xpath('//*[@class="grafico"][7]/div/div/div/table/tbody/tr[6]/td[2]').text
                                            valor6 = driver.find_element_by_xpath('//*[@class="grafico"][7]/div/div/div/table/tbody/tr[7]/td[1]').text
                                            valor66 = driver.find_element_by_xpath('//*[@class="grafico"][7]/div/div/div/table/tbody/tr[7]/td[2]').text
                                            valor7 = driver.find_element_by_xpath('//*[@class="grafico"][7]/div/div/div/table/tbody/tr[8]/td[1]').text
                                            valor77 = driver.find_element_by_xpath('//*[@class="grafico"][7]/div/div/div/table/tbody/tr[8]/td[2]').text
                                            grupo = {
                                                            "pesquisador":
                                                                [{
                                                                    "identificacao":[{
                                                                        
                                                                        
                                                                            "pesquisador": nome, "producao":[{
                                                                                "ano": valor_ano,
                                                                                valor1: valor11,
                                                                                valor2: valor22,
                                                                                valor3: valor33,
                                                                                valor4: valor44,
                                                                                valor5: valor55,
                                                                                valor6: valor66,
                                                                                valor7: valor77
                                                                                }]
                                                                        }]
                                                                }]
                                                    }
                                        if cont_lin == 7:
                                            valor1 = driver.find_element_by_xpath('//*[@class="grafico"][7]/div/div/div/table/tbody/tr[2]/td[1]').text
                                            valor11 = driver.find_element_by_xpath('//*[@class="grafico"][7]/div/div/div/table/tbody/tr[2]/td[2]').text
                                            valor2 = driver.find_element_by_xpath('//*[@class="grafico"][7]/div/div/div/table/tbody/tr[3]/td[1]').text
                                            valor22 = driver.find_element_by_xpath('//*[@class="grafico"][7]/div/div/div/table/tbody/tr[3]/td[2]').text
                                            valor3 = driver.find_element_by_xpath('//*[@class="grafico"][7]/div/div/div/table/tbody/tr[4]/td[1]').text
                                            valor33 = driver.find_element_by_xpath('//*[@class="grafico"][7]/div/div/div/table/tbody/tr[4]/td[2]').text
                                            valor4 = driver.find_element_by_xpath('//*[@class="grafico"][7]/div/div/div/table/tbody/tr[5]/td[1]').text
                                            valor44 = driver.find_element_by_xpath('//*[@class="grafico"][7]/div/div/div/table/tbody/tr[5]/td[2]').text
                                            valor5 = driver.find_element_by_xpath('//*[@class="grafico"][7]/div/div/div/table/tbody/tr[6]/td[1]').text
                                            valor55 = driver.find_element_by_xpath('//*[@class="grafico"][7]/div/div/div/table/tbody/tr[6]/td[2]').text
                                            valor6 = driver.find_element_by_xpath('//*[@class="grafico"][7]/div/div/div/table/tbody/tr[7]/td[1]').text
                                            valor66 = driver.find_element_by_xpath('//*[@class="grafico"][7]/div/div/div/table/tbody/tr[7]/td[2]').text
                                            grupo = {
                                                            "pesquisador":
                                                                [{
                                                                    "identificacao":[{
                                                                        
                                                                        
                                                                            "pesquisador": nome, "producao":[{
                                                                                "ano": valor_ano,
                                                                                valor1: valor11,
                                                                                valor2: valor22,
                                                                                valor3: valor33,
                                                                                valor4: valor44,
                                                                                valor5: valor55,
                                                                                valor6: valor66
                                                                                }]
                                                                        }]
                                                                }]
                                                    }
                                        if cont_lin == 6:
                                            valor1 = driver.find_element_by_xpath('//*[@class="grafico"][7]/div/div/div/table/tbody/tr[2]/td[1]').text
                                            valor11 = driver.find_element_by_xpath('//*[@class="grafico"][7]/div/div/div/table/tbody/tr[2]/td[2]').text
                                            valor2 = driver.find_element_by_xpath('//*[@class="grafico"][7]/div/div/div/table/tbody/tr[3]/td[1]').text
                                            valor22 = driver.find_element_by_xpath('//*[@class="grafico"][7]/div/div/div/table/tbody/tr[3]/td[2]').text
                                            valor3 = driver.find_element_by_xpath('//*[@class="grafico"][7]/div/div/div/table/tbody/tr[4]/td[1]').text
                                            valor33 = driver.find_element_by_xpath('//*[@class="grafico"][7]/div/div/div/table/tbody/tr[4]/td[2]').text
                                            valor4 = driver.find_element_by_xpath('//*[@class="grafico"][7]/div/div/div/table/tbody/tr[5]/td[1]').text
                                            valor44 = driver.find_element_by_xpath('//*[@class="grafico"][7]/div/div/div/table/tbody/tr[5]/td[2]').text
                                            valor5 = driver.find_element_by_xpath('//*[@class="grafico"][7]/div/div/div/table/tbody/tr[6]/td[1]').text
                                            valor55 = driver.find_element_by_xpath('//*[@class="grafico"][7]/div/div/div/table/tbody/tr[6]/td[2]').text
                                            grupo = {
                                                            "pesquisador":
                                                                [{
                                                                    "identificacao":[{
                                                                        
                                                                        
                                                                            "pesquisador": nome, "producao":[{
                                                                                "ano": valor_ano,
                                                                                valor1: valor11,
                                                                                valor2: valor22,
                                                                                valor3: valor33,
                                                                                valor4: valor44,
                                                                                valor5: valor55
                                                                                }]
                                                                        }]
                                                                }]
                                                    }
                                        if cont_lin == 5:
                                            valor1 = driver.find_element_by_xpath('//*[@class="grafico"][7]/div/div/div/table/tbody/tr[2]/td[1]').text
                                            valor11 = driver.find_element_by_xpath('//*[@class="grafico"][7]/div/div/div/table/tbody/tr[2]/td[2]').text
                                            valor2 = driver.find_element_by_xpath('//*[@class="grafico"][7]/div/div/div/table/tbody/tr[3]/td[1]').text
                                            valor22 = driver.find_element_by_xpath('//*[@class="grafico"][7]/div/div/div/table/tbody/tr[3]/td[2]').text
                                            valor3 = driver.find_element_by_xpath('//*[@class="grafico"][7]/div/div/div/table/tbody/tr[4]/td[1]').text
                                            valor33 = driver.find_element_by_xpath('//*[@class="grafico"][7]/div/div/div/table/tbody/tr[4]/td[2]').text
                                            valor4 = driver.find_element_by_xpath('//*[@class="grafico"][7]/div/div/div/table/tbody/tr[5]/td[1]').text
                                            valor44 = driver.find_element_by_xpath('//*[@class="grafico"][7]/div/div/div/table/tbody/tr[5]/td[2]').text
                                            grupo = {
                                                            "pesquisador":
                                                                [{
                                                                    "identificacao":[{
                                                                        
                                                                        
                                                                            "pesquisador": nome, "producao":[{
                                                                                "ano": valor_ano,
                                                                                valor1: valor11,
                                                                                valor2: valor22,
                                                                                valor3: valor33,
                                                                                valor4: valor44
                                                                                }]
                                                                        }]
                                                                }]
                                                    }
                                        if cont_lin == 4:
                                            valor1 = driver.find_element_by_xpath('//*[@class="grafico"][7]/div/div/div/table/tbody/tr[2]/td[1]').text
                                            valor11 = driver.find_element_by_xpath('//*[@class="grafico"][7]/div/div/div/table/tbody/tr[2]/td[2]').text
                                            valor2 = driver.find_element_by_xpath('//*[@class="grafico"][7]/div/div/div/table/tbody/tr[3]/td[1]').text
                                            valor22 = driver.find_element_by_xpath('//*[@class="grafico"][7]/div/div/div/table/tbody/tr[3]/td[2]').text
                                            valor3 = driver.find_element_by_xpath('//*[@class="grafico"][7]/div/div/div/table/tbody/tr[4]/td[1]').text
                                            valor33 = driver.find_element_by_xpath('//*[@class="grafico"][7]/div/div/div/table/tbody/tr[4]/td[2]').text
                                            grupo = {
                                                            "pesquisador":
                                                                [{
                                                                    "identificacao":[{
                                                                        
                                                                        
                                                                            "pesquisador": nome, "producao":[{
                                                                                "ano": valor_ano,
                                                                                valor1: valor11,
                                                                                valor2: valor22,
                                                                                valor3: valor33
                                                                                }]
                                                                        }]
                                                                }]
                                                    }
                                        if cont_lin == 3:
                                            valor1 = driver.find_element_by_xpath('//*[@class="grafico"][7]/div/div/div/table/tbody/tr[2]/td[1]').text
                                            valor11 = driver.find_element_by_xpath('//*[@class="grafico"][7]/div/div/div/table/tbody/tr[2]/td[2]').text
                                            valor2 = driver.find_element_by_xpath('//*[@class="grafico"][7]/div/div/div/table/tbody/tr[3]/td[1]').text
                                            valor22 = driver.find_element_by_xpath('//*[@class="grafico"][7]/div/div/div/table/tbody/tr[3]/td[2]').text
                                            grupo = {
                                                            "pesquisador":
                                                                [{
                                                                    "identificacao":[{
                                                                        
                                                                        
                                                                            "pesquisador": nome, "producao":[{
                                                                                "ano": valor_ano,
                                                                                valor1: valor11,
                                                                                valor2: valor22
                                                                                }]
                                                                        }]
                                                                }]
                                                    }
                                        if cont_lin == 2:
                                            valor1 = driver.find_element_by_xpath('//*[@class="grafico"][7]/div/div/div/table/tbody/tr[2]/td[1]').text
                                            valor11 = driver.find_element_by_xpath('//*[@class="grafico"][7]/div/div/div/table/tbody/tr[2]/td[2]').text
                                            grupo = {
                                                            "pesquisador":
                                                                [{
                                                                    "identificacao":[{
                                                                        
                                                                        
                                                                            "pesquisador": nome, "producao":[{
                                                                                "ano": valor_ano,
                                                                                valor1: valor11
                                                                                }]
                                                                        }]
                                                                }]
                                                    }
                                    elif cont_tabs == 6:
                                        cont_lin = len(driver.find_elements_by_xpath('//*[@class="grafico"][6]/div/div/div/table/tbody/tr'))
                                        nome = nomes[s]
                                        if cont_lin == 12:
                                            valor1 = driver.find_element_by_xpath('//*[@class="grafico"][6]/div/div/div/table/tbody/tr[2]/td[1]').text
                                            valor11 = driver.find_element_by_xpath('//*[@class="grafico"][6]/div/div/div/table/tbody/tr[2]/td[2]').text
                                            valor2 = driver.find_element_by_xpath('//*[@class="grafico"][6]/div/div/div/table/tbody/tr[3]/td[1]').text
                                            valor22 = driver.find_element_by_xpath('//*[@class="grafico"][6]/div/div/div/table/tbody/tr[3]/td[2]').text
                                            valor3 = driver.find_element_by_xpath('//*[@class="grafico"][6]/div/div/div/table/tbody/tr[4]/td[1]').text
                                            valor33 = driver.find_element_by_xpath('//*[@class="grafico"][6]/div/div/div/table/tbody/tr[4]/td[2]').text
                                            valor4 = driver.find_element_by_xpath('//*[@class="grafico"][6]/div/div/div/table/tbody/tr[5]/td[1]').text
                                            valor44 = driver.find_element_by_xpath('//*[@class="grafico"][6]/div/div/div/table/tbody/tr[5]/td[2]').text
                                            valor5 = driver.find_element_by_xpath('//*[@class="grafico"][6]/div/div/div/table/tbody/tr[6]/td[1]').text
                                            valor55 = driver.find_element_by_xpath('//*[@class="grafico"][6]/div/div/div/table/tbody/tr[6]/td[2]').text
                                            valor6 = driver.find_element_by_xpath('//*[@class="grafico"][6]/div/div/div/table/tbody/tr[7]/td[1]').text
                                            valor66 = driver.find_element_by_xpath('//*[@class="grafico"][6]/div/div/div/table/tbody/tr[7]/td[2]').text
                                            valor7 = driver.find_element_by_xpath('//*[@class="grafico"][6]/div/div/div/table/tbody/tr[8]/td[1]').text
                                            valor77 = driver.find_element_by_xpath('//*[@class="grafico"][6]/div/div/div/table/tbody/tr[8]/td[2]').text
                                            valor8 = driver.find_element_by_xpath('//*[@class="grafico"][6]/div/div/div/table/tbody/tr[9]/td[1]').text
                                            valor88 = driver.find_element_by_xpath('//*[@class="grafico"][6]/div/div/div/table/tbody/tr[9]/td[2]').text
                                            valor9 = driver.find_element_by_xpath('//*[@class="grafico"][6]/div/div/div/table/tbody/tr[10]/td[1]').text
                                            valor99 = driver.find_element_by_xpath('//*[@class="grafico"][6]/div/div/div/table/tbody/tr[10]/td[2]').text
                                            valor10 = driver.find_element_by_xpath('//*[@class="grafico"][6]/div/div/div/table/tbody/tr[11]/td[1]').text
                                            valor1010 = driver.find_element_by_xpath('//*[@class="grafico"][6]/div/div/div/table/tbody/tr[11]/td[2]').text
                                            valor11 = driver.find_element_by_xpath('//*[@class="grafico"][6]/div/div/div/table/tbody/tr[12]/td[1]').text
                                            valor1111 = driver.find_element_by_xpath('//*[@class="grafico"][6]/div/div/div/table/tbody/tr[12]/td[2]').text
                                            grupo = {
                                                            "pesquisador":
                                                                [{
                                                                    "identificacao":[{
                                                                        
                                                                        
                                                                            "pesquisador": nome, "producao":[{
                                                                                "ano": valor_ano,
                                                                                valor1: valor11,
                                                                                valor2: valor22,
                                                                                valor3: valor33,
                                                                                valor4: valor44,
                                                                                valor5: valor55,
                                                                                valor6: valor66,
                                                                                valor7: valor77,
                                                                                valor8: valor88,
                                                                                valor9: valor99,
                                                                                valor10: valor1010,
                                                                                valor11: valor1111
                                                                                }]
                                                                        }]
                                                                }]
                                                    }
                                        if cont_lin == 11:
                                            valor1 = driver.find_element_by_xpath('//*[@class="grafico"][6]/div/div/div/table/tbody/tr[2]/td[1]').text
                                            valor11 = driver.find_element_by_xpath('//*[@class="grafico"][6]/div/div/div/table/tbody/tr[2]/td[2]').text
                                            valor2 = driver.find_element_by_xpath('//*[@class="grafico"][6]/div/div/div/table/tbody/tr[3]/td[1]').text
                                            valor22 = driver.find_element_by_xpath('//*[@class="grafico"][6]/div/div/div/table/tbody/tr[3]/td[2]').text
                                            valor3 = driver.find_element_by_xpath('//*[@class="grafico"][6]/div/div/div/table/tbody/tr[4]/td[1]').text
                                            valor33 = driver.find_element_by_xpath('//*[@class="grafico"][6]/div/div/div/table/tbody/tr[4]/td[2]').text
                                            valor4 = driver.find_element_by_xpath('//*[@class="grafico"][6]/div/div/div/table/tbody/tr[5]/td[1]').text
                                            valor44 = driver.find_element_by_xpath('//*[@class="grafico"][6]/div/div/div/table/tbody/tr[5]/td[2]').text
                                            valor5 = driver.find_element_by_xpath('//*[@class="grafico"][6]/div/div/div/table/tbody/tr[6]/td[1]').text
                                            valor55 = driver.find_element_by_xpath('//*[@class="grafico"][6]/div/div/div/table/tbody/tr[6]/td[2]').text
                                            valor6 = driver.find_element_by_xpath('//*[@class="grafico"][6]/div/div/div/table/tbody/tr[7]/td[1]').text
                                            valor66 = driver.find_element_by_xpath('//*[@class="grafico"][6]/div/div/div/table/tbody/tr[7]/td[2]').text
                                            valor7 = driver.find_element_by_xpath('//*[@class="grafico"][6]/div/div/div/table/tbody/tr[8]/td[1]').text
                                            valor77 = driver.find_element_by_xpath('//*[@class="grafico"][6]/div/div/div/table/tbody/tr[8]/td[2]').text
                                            valor8 = driver.find_element_by_xpath('//*[@class="grafico"][6]/div/div/div/table/tbody/tr[9]/td[1]').text
                                            valor88 = driver.find_element_by_xpath('//*[@class="grafico"][6]/div/div/div/table/tbody/tr[9]/td[2]').text
                                            valor9 = driver.find_element_by_xpath('//*[@class="grafico"][6]/div/div/div/table/tbody/tr[10]/td[1]').text
                                            valor99 = driver.find_element_by_xpath('//*[@class="grafico"][6]/div/div/div/table/tbody/tr[10]/td[2]').text
                                            valor10 = driver.find_element_by_xpath('//*[@class="grafico"][6]/div/div/div/table/tbody/tr[11]/td[1]').text
                                            valor1010 = driver.find_element_by_xpath('//*[@class="grafico"][6]/div/div/div/table/tbody/tr[11]/td[2]').text
                                            grupo = {
                                                            "pesquisador":
                                                                [{
                                                                    "identificacao":[{
                                                                        
                                                                        
                                                                            "pesquisador": nome, "producao":[{
                                                                                "ano": valor_ano,
                                                                                valor1: valor11,
                                                                                valor2: valor22,
                                                                                valor3: valor33,
                                                                                valor4: valor44,
                                                                                valor5: valor55,
                                                                                valor6: valor66,
                                                                                valor7: valor77,
                                                                                valor8: valor88,
                                                                                valor9: valor99,
                                                                                valor10: valor1010
                                                                                }]
                                                                        }]
                                                                }]
                                                    }
                                        if cont_lin == 10:
                                            valor1 = driver.find_element_by_xpath('//*[@class="grafico"][6]/div/div/div/table/tbody/tr[2]/td[1]').text
                                            valor11 = driver.find_element_by_xpath('//*[@class="grafico"][6]/div/div/div/table/tbody/tr[2]/td[2]').text
                                            valor2 = driver.find_element_by_xpath('//*[@class="grafico"][6]/div/div/div/table/tbody/tr[3]/td[1]').text
                                            valor22 = driver.find_element_by_xpath('//*[@class="grafico"][6]/div/div/div/table/tbody/tr[3]/td[2]').text
                                            valor3 = driver.find_element_by_xpath('//*[@class="grafico"][6]/div/div/div/table/tbody/tr[4]/td[1]').text
                                            valor33 = driver.find_element_by_xpath('//*[@class="grafico"][6]/div/div/div/table/tbody/tr[4]/td[2]').text
                                            valor4 = driver.find_element_by_xpath('//*[@class="grafico"][6]/div/div/div/table/tbody/tr[5]/td[1]').text
                                            valor44 = driver.find_element_by_xpath('//*[@class="grafico"][6]/div/div/div/table/tbody/tr[5]/td[2]').text
                                            valor5 = driver.find_element_by_xpath('//*[@class="grafico"][6]/div/div/div/table/tbody/tr[6]/td[1]').text
                                            valor55 = driver.find_element_by_xpath('//*[@class="grafico"][6]/div/div/div/table/tbody/tr[6]/td[2]').text
                                            valor6 = driver.find_element_by_xpath('//*[@class="grafico"][6]/div/div/div/table/tbody/tr[7]/td[1]').text
                                            valor66 = driver.find_element_by_xpath('//*[@class="grafico"][6]/div/div/div/table/tbody/tr[7]/td[2]').text
                                            valor7 = driver.find_element_by_xpath('//*[@class="grafico"][6]/div/div/div/table/tbody/tr[8]/td[1]').text
                                            valor77 = driver.find_element_by_xpath('//*[@class="grafico"][6]/div/div/div/table/tbody/tr[8]/td[2]').text
                                            valor8 = driver.find_element_by_xpath('//*[@class="grafico"][6]/div/div/div/table/tbody/tr[9]/td[1]').text
                                            valor88 = driver.find_element_by_xpath('//*[@class="grafico"][6]/div/div/div/table/tbody/tr[9]/td[2]').text
                                            valor9 = driver.find_element_by_xpath('//*[@class="grafico"][6]/div/div/div/table/tbody/tr[10]/td[1]').text
                                            valor99 = driver.find_element_by_xpath('//*[@class="grafico"][6]/div/div/div/table/tbody/tr[10]/td[2]').text
                                            grupo = {
                                                            "pesquisador":
                                                                [{
                                                                    "identificacao":[{
                                                                        
                                                                        
                                                                            "pesquisador": nome, "producao":[{
                                                                                "ano": valor_ano,
                                                                                valor1: valor11,
                                                                                valor2: valor22,
                                                                                valor3: valor33,
                                                                                valor4: valor44,
                                                                                valor5: valor55,
                                                                                valor6: valor66,
                                                                                valor7: valor77,
                                                                                valor8: valor88,
                                                                                valor9: valor99
                                                                                }]
                                                                        }]
                                                                }]
                                                    }
                                        if cont_lin == 9:
                                            valor1 = driver.find_element_by_xpath('//*[@class="grafico"][6]/div/div/div/table/tbody/tr[2]/td[1]').text
                                            valor11 = driver.find_element_by_xpath('//*[@class="grafico"][6]/div/div/div/table/tbody/tr[2]/td[2]').text
                                            valor2 = driver.find_element_by_xpath('//*[@class="grafico"][6]/div/div/div/table/tbody/tr[3]/td[1]').text
                                            valor22 = driver.find_element_by_xpath('//*[@class="grafico"][6]/div/div/div/table/tbody/tr[3]/td[2]').text
                                            valor3 = driver.find_element_by_xpath('//*[@class="grafico"][6]/div/div/div/table/tbody/tr[4]/td[1]').text
                                            valor33 = driver.find_element_by_xpath('//*[@class="grafico"][6]/div/div/div/table/tbody/tr[4]/td[2]').text
                                            valor4 = driver.find_element_by_xpath('//*[@class="grafico"][6]/div/div/div/table/tbody/tr[5]/td[1]').text
                                            valor44 = driver.find_element_by_xpath('//*[@class="grafico"][6]/div/div/div/table/tbody/tr[5]/td[2]').text
                                            valor5 = driver.find_element_by_xpath('//*[@class="grafico"][6]/div/div/div/table/tbody/tr[6]/td[1]').text
                                            valor55 = driver.find_element_by_xpath('//*[@class="grafico"][6]/div/div/div/table/tbody/tr[6]/td[2]').text
                                            valor6 = driver.find_element_by_xpath('//*[@class="grafico"][6]/div/div/div/table/tbody/tr[7]/td[1]').text
                                            valor66 = driver.find_element_by_xpath('//*[@class="grafico"][6]/div/div/div/table/tbody/tr[7]/td[2]').text
                                            valor7 = driver.find_element_by_xpath('//*[@class="grafico"][6]/div/div/div/table/tbody/tr[8]/td[1]').text
                                            valor77 = driver.find_element_by_xpath('//*[@class="grafico"][6]/div/div/div/table/tbody/tr[8]/td[2]').text
                                            valor8 = driver.find_element_by_xpath('//*[@class="grafico"][6]/div/div/div/table/tbody/tr[9]/td[1]').text
                                            valor88 = driver.find_element_by_xpath('//*[@class="grafico"][6]/div/div/div/table/tbody/tr[9]/td[2]').text
                                            grupo = {
                                                            "pesquisador":
                                                                [{
                                                                    "identificacao":[{
                                                                        
                                                                        
                                                                            "pesquisador": nome, "producao":[{
                                                                                "ano": valor_ano,
                                                                                valor1: valor11,
                                                                                valor2: valor22,
                                                                                valor3: valor33,
                                                                                valor4: valor44,
                                                                                valor5: valor55,
                                                                                valor6: valor66,
                                                                                valor7: valor77,
                                                                                valor8: valor88
                                                                                }]
                                                                        }]
                                                                }]
                                                    }
                                        if cont_lin == 8:
                                            valor1 = driver.find_element_by_xpath('//*[@class="grafico"][6]/div/div/div/table/tbody/tr[2]/td[1]').text
                                            valor11 = driver.find_element_by_xpath('//*[@class="grafico"][6]/div/div/div/table/tbody/tr[2]/td[2]').text
                                            valor2 = driver.find_element_by_xpath('//*[@class="grafico"][6]/div/div/div/table/tbody/tr[3]/td[1]').text
                                            valor22 = driver.find_element_by_xpath('//*[@class="grafico"][6]/div/div/div/table/tbody/tr[3]/td[2]').text
                                            valor3 = driver.find_element_by_xpath('//*[@class="grafico"][6]/div/div/div/table/tbody/tr[4]/td[1]').text
                                            valor33 = driver.find_element_by_xpath('//*[@class="grafico"][6]/div/div/div/table/tbody/tr[4]/td[2]').text
                                            valor4 = driver.find_element_by_xpath('//*[@class="grafico"][6]/div/div/div/table/tbody/tr[5]/td[1]').text
                                            valor44 = driver.find_element_by_xpath('//*[@class="grafico"][6]/div/div/div/table/tbody/tr[5]/td[2]').text
                                            valor5 = driver.find_element_by_xpath('//*[@class="grafico"][6]/div/div/div/table/tbody/tr[6]/td[1]').text
                                            valor55 = driver.find_element_by_xpath('//*[@class="grafico"][6]/div/div/div/table/tbody/tr[6]/td[2]').text
                                            valor6 = driver.find_element_by_xpath('//*[@class="grafico"][6]/div/div/div/table/tbody/tr[7]/td[1]').text
                                            valor66 = driver.find_element_by_xpath('//*[@class="grafico"][6]/div/div/div/table/tbody/tr[7]/td[2]').text
                                            valor7 = driver.find_element_by_xpath('//*[@class="grafico"][6]/div/div/div/table/tbody/tr[8]/td[1]').text
                                            valor77 = driver.find_element_by_xpath('//*[@class="grafico"][6]/div/div/div/table/tbody/tr[8]/td[2]').text
                                            grupo = {
                                                            "pesquisador":
                                                                [{
                                                                    "identificacao":[{
                                                                        
                                                                        
                                                                            "pesquisador": nome, "producao":[{
                                                                                "ano": valor_ano,
                                                                                valor1: valor11,
                                                                                valor2: valor22,
                                                                                valor3: valor33,
                                                                                valor4: valor44,
                                                                                valor5: valor55,
                                                                                valor6: valor66,
                                                                                valor7: valor77
                                                                                }]
                                                                        }]
                                                                }]
                                                    }
                                        if cont_lin == 7:
                                            valor1 = driver.find_element_by_xpath('//*[@class="grafico"][6]/div/div/div/table/tbody/tr[2]/td[1]').text
                                            valor11 = driver.find_element_by_xpath('//*[@class="grafico"][6]/div/div/div/table/tbody/tr[2]/td[2]').text
                                            valor2 = driver.find_element_by_xpath('//*[@class="grafico"][6]/div/div/div/table/tbody/tr[3]/td[1]').text
                                            valor22 = driver.find_element_by_xpath('//*[@class="grafico"][6]/div/div/div/table/tbody/tr[3]/td[2]').text
                                            valor3 = driver.find_element_by_xpath('//*[@class="grafico"][6]/div/div/div/table/tbody/tr[4]/td[1]').text
                                            valor33 = driver.find_element_by_xpath('//*[@class="grafico"][6]/div/div/div/table/tbody/tr[4]/td[2]').text
                                            valor4 = driver.find_element_by_xpath('//*[@class="grafico"][6]/div/div/div/table/tbody/tr[5]/td[1]').text
                                            valor44 = driver.find_element_by_xpath('//*[@class="grafico"][6]/div/div/div/table/tbody/tr[5]/td[2]').text
                                            valor5 = driver.find_element_by_xpath('//*[@class="grafico"][6]/div/div/div/table/tbody/tr[6]/td[1]').text
                                            valor55 = driver.find_element_by_xpath('//*[@class="grafico"][6]/div/div/div/table/tbody/tr[6]/td[2]').text
                                            valor6 = driver.find_element_by_xpath('//*[@class="grafico"][6]/div/div/div/table/tbody/tr[7]/td[1]').text
                                            valor66 = driver.find_element_by_xpath('//*[@class="grafico"][6]/div/div/div/table/tbody/tr[7]/td[2]').text
                                            grupo = {
                                                            "pesquisador":
                                                                [{
                                                                    "identificacao":[{
                                                                        
                                                                        
                                                                            "pesquisador": nome, "producao":[{
                                                                                "ano": valor_ano,
                                                                                valor1: valor11,
                                                                                valor2: valor22,
                                                                                valor3: valor33,
                                                                                valor4: valor44,
                                                                                valor5: valor55,
                                                                                valor6: valor66
                                                                                }]
                                                                        }]
                                                                }]
                                                    }
                                        if cont_lin == 6:
                                            valor1 = driver.find_element_by_xpath('//*[@class="grafico"][6]/div/div/div/table/tbody/tr[2]/td[1]').text
                                            valor11 = driver.find_element_by_xpath('//*[@class="grafico"][6]/div/div/div/table/tbody/tr[2]/td[2]').text
                                            valor2 = driver.find_element_by_xpath('//*[@class="grafico"][6]/div/div/div/table/tbody/tr[3]/td[1]').text
                                            valor22 = driver.find_element_by_xpath('//*[@class="grafico"][6]/div/div/div/table/tbody/tr[3]/td[2]').text
                                            valor3 = driver.find_element_by_xpath('//*[@class="grafico"][6]/div/div/div/table/tbody/tr[4]/td[1]').text
                                            valor33 = driver.find_element_by_xpath('//*[@class="grafico"][6]/div/div/div/table/tbody/tr[4]/td[2]').text
                                            valor4 = driver.find_element_by_xpath('//*[@class="grafico"][6]/div/div/div/table/tbody/tr[5]/td[1]').text
                                            valor44 = driver.find_element_by_xpath('//*[@class="grafico"][6]/div/div/div/table/tbody/tr[5]/td[2]').text
                                            valor5 = driver.find_element_by_xpath('//*[@class="grafico"][6]/div/div/div/table/tbody/tr[6]/td[1]').text
                                            valor55 = driver.find_element_by_xpath('//*[@class="grafico"][6]/div/div/div/table/tbody/tr[6]/td[2]').text
                                            grupo = {
                                                            "pesquisador":
                                                                [{
                                                                    "identificacao":[{
                                                                        
                                                                        
                                                                            "pesquisador": nome, "producao":[{
                                                                                "ano": valor_ano,
                                                                                valor1: valor11,
                                                                                valor2: valor22,
                                                                                valor3: valor33,
                                                                                valor4: valor44,
                                                                                valor5: valor55
                                                                                }]
                                                                        }]
                                                                }]
                                                    }
                                        if cont_lin == 5:
                                            valor1 = driver.find_element_by_xpath('//*[@class="grafico"][6]/div/div/div/table/tbody/tr[2]/td[1]').text
                                            valor11 = driver.find_element_by_xpath('//*[@class="grafico"][6]/div/div/div/table/tbody/tr[2]/td[2]').text
                                            valor2 = driver.find_element_by_xpath('//*[@class="grafico"][6]/div/div/div/table/tbody/tr[3]/td[1]').text
                                            valor22 = driver.find_element_by_xpath('//*[@class="grafico"][6]/div/div/div/table/tbody/tr[3]/td[2]').text
                                            valor3 = driver.find_element_by_xpath('//*[@class="grafico"][6]/div/div/div/table/tbody/tr[4]/td[1]').text
                                            valor33 = driver.find_element_by_xpath('//*[@class="grafico"][6]/div/div/div/table/tbody/tr[4]/td[2]').text
                                            valor4 = driver.find_element_by_xpath('//*[@class="grafico"][6]/div/div/div/table/tbody/tr[5]/td[1]').text
                                            valor44 = driver.find_element_by_xpath('//*[@class="grafico"][6]/div/div/div/table/tbody/tr[5]/td[2]').text
                                            grupo = {
                                                            "pesquisador":
                                                                [{
                                                                    "identificacao":[{
                                                                        
                                                                        
                                                                            "pesquisador": nome, "producao":[{
                                                                                "ano": valor_ano,
                                                                                valor1: valor11,
                                                                                valor2: valor22,
                                                                                valor3: valor33,
                                                                                valor4: valor44
                                                                                }]
                                                                        }]
                                                                }]
                                                    }
                                        if cont_lin == 4:
                                            valor1 = driver.find_element_by_xpath('//*[@class="grafico"][6]/div/div/div/table/tbody/tr[2]/td[1]').text
                                            valor11 = driver.find_element_by_xpath('//*[@class="grafico"][6]/div/div/div/table/tbody/tr[2]/td[2]').text
                                            valor2 = driver.find_element_by_xpath('//*[@class="grafico"][6]/div/div/div/table/tbody/tr[3]/td[1]').text
                                            valor22 = driver.find_element_by_xpath('//*[@class="grafico"][6]/div/div/div/table/tbody/tr[3]/td[2]').text
                                            valor3 = driver.find_element_by_xpath('//*[@class="grafico"][6]/div/div/div/table/tbody/tr[4]/td[1]').text
                                            valor33 = driver.find_element_by_xpath('//*[@class="grafico"][6]/div/div/div/table/tbody/tr[4]/td[2]').text
                                            grupo = {
                                                            "pesquisador":
                                                                [{
                                                                    "identificacao":[{
                                                                        
                                                                        
                                                                            "pesquisador": nome, "producao":[{
                                                                                "ano": valor_ano,
                                                                                valor1: valor11,
                                                                                valor2: valor22,
                                                                                valor3: valor33
                                                                                }]
                                                                        }]
                                                                }]
                                                    }
                                        if cont_lin == 3:
                                            valor1 = driver.find_element_by_xpath('//*[@class="grafico"][6]/div/div/div/table/tbody/tr[2]/td[1]').text
                                            valor11 = driver.find_element_by_xpath('//*[@class="grafico"][6]/div/div/div/table/tbody/tr[2]/td[2]').text
                                            valor2 = driver.find_element_by_xpath('//*[@class="grafico"][6]/div/div/div/table/tbody/tr[3]/td[1]').text
                                            valor22 = driver.find_element_by_xpath('//*[@class="grafico"][6]/div/div/div/table/tbody/tr[3]/td[2]').text
                                            grupo = {
                                                            "pesquisador":
                                                                [{
                                                                    "identificacao":[{
                                                                        
                                                                        
                                                                            "pesquisador": nome, "producao":[{
                                                                                "ano": valor_ano,
                                                                                valor1: valor11,
                                                                                valor2: valor22
                                                                                }]
                                                                        }]
                                                                }]
                                                    }
                                        if cont_lin == 2:
                                            valor1 = driver.find_element_by_xpath('//*[@class="grafico"][6]/div/div/div/table/tbody/tr[2]/td[1]').text
                                            valor11 = driver.find_element_by_xpath('//*[@class="grafico"][6]/div/div/div/table/tbody/tr[2]/td[2]').text
                                            grupo = {
                                                            "pesquisador":
                                                                [{
                                                                    "identificacao":[{
                                                                        
                                                                        
                                                                            "pesquisador": nome, "producao":[{
                                                                                "ano": valor_ano,
                                                                                valor1: valor11
                                                                                }]
                                                                        }]
                                                                }]
                                                    }
                                    elif cont_tabs == 5:
                                        cont_lin = len(driver.find_elements_by_xpath('//*[@class="grafico"][5]/div/div/div/table/tbody/tr'))
                                        nome = nomes[s]
                                        if cont_lin == 11:
                                            valor1 = driver.find_element_by_xpath('//*[@class="grafico"][5]/div/div/div/table/tbody/tr[2]/td[1]').text
                                            valor11 = driver.find_element_by_xpath('//*[@class="grafico"][5]/div/div/div/table/tbody/tr[2]/td[2]').text
                                            valor2 = driver.find_element_by_xpath('//*[@class="grafico"][5]/div/div/div/table/tbody/tr[3]/td[1]').text
                                            valor22 = driver.find_element_by_xpath('//*[@class="grafico"][5]/div/div/div/table/tbody/tr[3]/td[2]').text
                                            valor3 = driver.find_element_by_xpath('//*[@class="grafico"][5]/div/div/div/table/tbody/tr[4]/td[1]').text
                                            valor33 = driver.find_element_by_xpath('//*[@class="grafico"][5]/div/div/div/table/tbody/tr[4]/td[2]').text
                                            valor4 = driver.find_element_by_xpath('//*[@class="grafico"][5]/div/div/div/table/tbody/tr[5]/td[1]').text
                                            valor44 = driver.find_element_by_xpath('//*[@class="grafico"][5]/div/div/div/table/tbody/tr[5]/td[2]').text
                                            valor5 = driver.find_element_by_xpath('//*[@class="grafico"][5]/div/div/div/table/tbody/tr[6]/td[1]').text
                                            valor55 = driver.find_element_by_xpath('//*[@class="grafico"][5]/div/div/div/table/tbody/tr[6]/td[2]').text
                                            valor6 = driver.find_element_by_xpath('//*[@class="grafico"][5]/div/div/div/table/tbody/tr[7]/td[1]').text
                                            valor66 = driver.find_element_by_xpath('//*[@class="grafico"][5]/div/div/div/table/tbody/tr[7]/td[2]').text
                                            valor7 = driver.find_element_by_xpath('//*[@class="grafico"][5]/div/div/div/table/tbody/tr[8]/td[1]').text
                                            valor77 = driver.find_element_by_xpath('//*[@class="grafico"][5]/div/div/div/table/tbody/tr[8]/td[2]').text
                                            valor8 = driver.find_element_by_xpath('//*[@class="grafico"][5]/div/div/div/table/tbody/tr[9]/td[1]').text
                                            valor88 = driver.find_element_by_xpath('//*[@class="grafico"][5]/div/div/div/table/tbody/tr[9]/td[2]').text
                                            valor9 = driver.find_element_by_xpath('//*[@class="grafico"][5]/div/div/div/table/tbody/tr[10]/td[1]').text
                                            valor99 = driver.find_element_by_xpath('//*[@class="grafico"][5]/div/div/div/table/tbody/tr[10]/td[2]').text
                                            valor10 = driver.find_element_by_xpath('//*[@class="grafico"][5]/div/div/div/table/tbody/tr[11]/td[1]').text
                                            valor1010 = driver.find_element_by_xpath('//*[@class="grafico"][5]/div/div/div/table/tbody/tr[11]/td[2]').text
                                            grupo = {
                                                            "pesquisador":
                                                                [{
                                                                    "identificacao":[{
                                                                        
                                                                        
                                                                            "pesquisador": nome, "producao":[{
                                                                                "ano": valor_ano,
                                                                                valor1: valor11,
                                                                                valor2: valor22,
                                                                                valor3: valor33,
                                                                                valor4: valor44,
                                                                                valor5: valor55,
                                                                                valor6: valor66,
                                                                                valor7: valor77,
                                                                                valor8: valor88,
                                                                                valor9: valor99,
                                                                                valor10: valor1010
                                                                                }]
                                                                        }]
                                                                }]
                                                    }
                                        if cont_lin == 10:
                                            valor1 = driver.find_element_by_xpath('//*[@class="grafico"][5]/div/div/div/table/tbody/tr[2]/td[1]').text
                                            valor11 = driver.find_element_by_xpath('//*[@class="grafico"][5]/div/div/div/table/tbody/tr[2]/td[2]').text
                                            valor2 = driver.find_element_by_xpath('//*[@class="grafico"][5]/div/div/div/table/tbody/tr[3]/td[1]').text
                                            valor22 = driver.find_element_by_xpath('//*[@class="grafico"][5]/div/div/div/table/tbody/tr[3]/td[2]').text
                                            valor3 = driver.find_element_by_xpath('//*[@class="grafico"][5]/div/div/div/table/tbody/tr[4]/td[1]').text
                                            valor33 = driver.find_element_by_xpath('//*[@class="grafico"][5]/div/div/div/table/tbody/tr[4]/td[2]').text
                                            valor4 = driver.find_element_by_xpath('//*[@class="grafico"][5]/div/div/div/table/tbody/tr[5]/td[1]').text
                                            valor44 = driver.find_element_by_xpath('//*[@class="grafico"][5]/div/div/div/table/tbody/tr[5]/td[2]').text
                                            valor5 = driver.find_element_by_xpath('//*[@class="grafico"][5]/div/div/div/table/tbody/tr[6]/td[1]').text
                                            valor55 = driver.find_element_by_xpath('//*[@class="grafico"][5]/div/div/div/table/tbody/tr[6]/td[2]').text
                                            valor6 = driver.find_element_by_xpath('//*[@class="grafico"][5]/div/div/div/table/tbody/tr[7]/td[1]').text
                                            valor66 = driver.find_element_by_xpath('//*[@class="grafico"][5]/div/div/div/table/tbody/tr[7]/td[2]').text
                                            valor7 = driver.find_element_by_xpath('//*[@class="grafico"][5]/div/div/div/table/tbody/tr[8]/td[1]').text
                                            valor77 = driver.find_element_by_xpath('//*[@class="grafico"][5]/div/div/div/table/tbody/tr[8]/td[2]').text
                                            valor8 = driver.find_element_by_xpath('//*[@class="grafico"][5]/div/div/div/table/tbody/tr[9]/td[1]').text
                                            valor88 = driver.find_element_by_xpath('//*[@class="grafico"][5]/div/div/div/table/tbody/tr[9]/td[2]').text
                                            valor9 = driver.find_element_by_xpath('//*[@class="grafico"][5]/div/div/div/table/tbody/tr[10]/td[1]').text
                                            valor99 = driver.find_element_by_xpath('//*[@class="grafico"][5]/div/div/div/table/tbody/tr[10]/td[2]').text
                                            grupo = {
                                                            "pesquisador":
                                                                [{
                                                                    "identificacao":[{
                                                                        
                                                                        
                                                                            "pesquisador": nome, "producao":[{
                                                                                "ano": valor_ano,
                                                                                valor1: valor11,
                                                                                valor2: valor22,
                                                                                valor3: valor33,
                                                                                valor4: valor44,
                                                                                valor5: valor55,
                                                                                valor6: valor66,
                                                                                valor7: valor77,
                                                                                valor8: valor88,
                                                                                valor9: valor99
                                                                                }]
                                                                        }]
                                                                }]
                                                    }
                                        if cont_lin == 9:
                                            valor1 = driver.find_element_by_xpath('//*[@class="grafico"][5]/div/div/div/table/tbody/tr[2]/td[1]').text
                                            valor11 = driver.find_element_by_xpath('//*[@class="grafico"][5]/div/div/div/table/tbody/tr[2]/td[2]').text
                                            valor2 = driver.find_element_by_xpath('//*[@class="grafico"][5]/div/div/div/table/tbody/tr[3]/td[1]').text
                                            valor22 = driver.find_element_by_xpath('//*[@class="grafico"][5]/div/div/div/table/tbody/tr[3]/td[2]').text
                                            valor3 = driver.find_element_by_xpath('//*[@class="grafico"][5]/div/div/div/table/tbody/tr[4]/td[1]').text
                                            valor33 = driver.find_element_by_xpath('//*[@class="grafico"][5]/div/div/div/table/tbody/tr[4]/td[2]').text
                                            valor4 = driver.find_element_by_xpath('//*[@class="grafico"][5]/div/div/div/table/tbody/tr[5]/td[1]').text
                                            valor44 = driver.find_element_by_xpath('//*[@class="grafico"][5]/div/div/div/table/tbody/tr[5]/td[2]').text
                                            valor5 = driver.find_element_by_xpath('//*[@class="grafico"][5]/div/div/div/table/tbody/tr[6]/td[1]').text
                                            valor55 = driver.find_element_by_xpath('//*[@class="grafico"][5]/div/div/div/table/tbody/tr[6]/td[2]').text
                                            valor6 = driver.find_element_by_xpath('//*[@class="grafico"][5]/div/div/div/table/tbody/tr[7]/td[1]').text
                                            valor66 = driver.find_element_by_xpath('//*[@class="grafico"][5]/div/div/div/table/tbody/tr[7]/td[2]').text
                                            valor7 = driver.find_element_by_xpath('//*[@class="grafico"][5]/div/div/div/table/tbody/tr[8]/td[1]').text
                                            valor77 = driver.find_element_by_xpath('//*[@class="grafico"][5]/div/div/div/table/tbody/tr[8]/td[2]').text
                                            valor8 = driver.find_element_by_xpath('//*[@class="grafico"][5]/div/div/div/table/tbody/tr[9]/td[1]').text
                                            valor88 = driver.find_element_by_xpath('//*[@class="grafico"][5]/div/div/div/table/tbody/tr[9]/td[2]').text
                                            grupo = {
                                                            "pesquisador":
                                                                [{
                                                                    "identificacao":[{
                                                                        
                                                                        
                                                                            "pesquisador": nome, "producao":[{
                                                                                "ano": valor_ano,
                                                                                valor1: valor11,
                                                                                valor2: valor22,
                                                                                valor3: valor33,
                                                                                valor4: valor44,
                                                                                valor5: valor55,
                                                                                valor6: valor66,
                                                                                valor7: valor77,
                                                                                valor8: valor88
                                                                                }]
                                                                        }]
                                                                }]
                                                    }
                                        if cont_lin == 8:
                                            valor1 = driver.find_element_by_xpath('//*[@class="grafico"][5]/div/div/div/table/tbody/tr[2]/td[1]').text
                                            valor11 = driver.find_element_by_xpath('//*[@class="grafico"][5]/div/div/div/table/tbody/tr[2]/td[2]').text
                                            valor2 = driver.find_element_by_xpath('//*[@class="grafico"][5]/div/div/div/table/tbody/tr[3]/td[1]').text
                                            valor22 = driver.find_element_by_xpath('//*[@class="grafico"][5]/div/div/div/table/tbody/tr[3]/td[2]').text
                                            valor3 = driver.find_element_by_xpath('//*[@class="grafico"][5]/div/div/div/table/tbody/tr[4]/td[1]').text
                                            valor33 = driver.find_element_by_xpath('//*[@class="grafico"][5]/div/div/div/table/tbody/tr[4]/td[2]').text
                                            valor4 = driver.find_element_by_xpath('//*[@class="grafico"][5]/div/div/div/table/tbody/tr[5]/td[1]').text
                                            valor44 = driver.find_element_by_xpath('//*[@class="grafico"][5]/div/div/div/table/tbody/tr[5]/td[2]').text
                                            valor5 = driver.find_element_by_xpath('//*[@class="grafico"][5]/div/div/div/table/tbody/tr[6]/td[1]').text
                                            valor55 = driver.find_element_by_xpath('//*[@class="grafico"][5]/div/div/div/table/tbody/tr[6]/td[2]').text
                                            valor6 = driver.find_element_by_xpath('//*[@class="grafico"][5]/div/div/div/table/tbody/tr[7]/td[1]').text
                                            valor66 = driver.find_element_by_xpath('//*[@class="grafico"][5]/div/div/div/table/tbody/tr[7]/td[2]').text
                                            valor7 = driver.find_element_by_xpath('//*[@class="grafico"][5]/div/div/div/table/tbody/tr[8]/td[1]').text
                                            valor77 = driver.find_element_by_xpath('//*[@class="grafico"][5]/div/div/div/table/tbody/tr[8]/td[2]').text
                                            grupo = {
                                                            "pesquisador":
                                                                [{
                                                                    "identificacao":[{
                                                                        
                                                                        
                                                                            "pesquisador": nome, "producao":[{
                                                                                "ano": valor_ano,
                                                                                valor1: valor11,
                                                                                valor2: valor22,
                                                                                valor3: valor33,
                                                                                valor4: valor44,
                                                                                valor5: valor55,
                                                                                valor6: valor66,
                                                                                valor7: valor77
                                                                                }]
                                                                        }]
                                                                }]
                                                    }
                                        if cont_lin == 7:
                                            valor1 = driver.find_element_by_xpath('//*[@class="grafico"][5]/div/div/div/table/tbody/tr[2]/td[1]').text
                                            valor11 = driver.find_element_by_xpath('//*[@class="grafico"][5]/div/div/div/table/tbody/tr[2]/td[2]').text
                                            valor2 = driver.find_element_by_xpath('//*[@class="grafico"][5]/div/div/div/table/tbody/tr[3]/td[1]').text
                                            valor22 = driver.find_element_by_xpath('//*[@class="grafico"][5]/div/div/div/table/tbody/tr[3]/td[2]').text
                                            valor3 = driver.find_element_by_xpath('//*[@class="grafico"][5]/div/div/div/table/tbody/tr[4]/td[1]').text
                                            valor33 = driver.find_element_by_xpath('//*[@class="grafico"][5]/div/div/div/table/tbody/tr[4]/td[2]').text
                                            valor4 = driver.find_element_by_xpath('//*[@class="grafico"][5]/div/div/div/table/tbody/tr[5]/td[1]').text
                                            valor44 = driver.find_element_by_xpath('//*[@class="grafico"][5]/div/div/div/table/tbody/tr[5]/td[2]').text
                                            valor5 = driver.find_element_by_xpath('//*[@class="grafico"][5]/div/div/div/table/tbody/tr[6]/td[1]').text
                                            valor55 = driver.find_element_by_xpath('//*[@class="grafico"][5]/div/div/div/table/tbody/tr[6]/td[2]').text
                                            valor6 = driver.find_element_by_xpath('//*[@class="grafico"][5]/div/div/div/table/tbody/tr[7]/td[1]').text
                                            valor66 = driver.find_element_by_xpath('//*[@class="grafico"][5]/div/div/div/table/tbody/tr[7]/td[2]').text
                                            grupo = {
                                                            "pesquisador":
                                                                [{
                                                                    "identificacao":[{
                                                                        
                                                                        
                                                                            "pesquisador": nome, "producao":[{
                                                                                "ano": valor_ano,
                                                                                valor1: valor11,
                                                                                valor2: valor22,
                                                                                valor3: valor33,
                                                                                valor4: valor44,
                                                                                valor5: valor55,
                                                                                valor6: valor66
                                                                                }]
                                                                        }]
                                                                }]
                                                    }
                                        if cont_lin == 6:
                                            valor1 = driver.find_element_by_xpath('//*[@class="grafico"][5]/div/div/div/table/tbody/tr[2]/td[1]').text
                                            valor11 = driver.find_element_by_xpath('//*[@class="grafico"][5]/div/div/div/table/tbody/tr[2]/td[2]').text
                                            valor2 = driver.find_element_by_xpath('//*[@class="grafico"][5]/div/div/div/table/tbody/tr[3]/td[1]').text
                                            valor22 = driver.find_element_by_xpath('//*[@class="grafico"][5]/div/div/div/table/tbody/tr[3]/td[2]').text
                                            valor3 = driver.find_element_by_xpath('//*[@class="grafico"][5]/div/div/div/table/tbody/tr[4]/td[1]').text
                                            valor33 = driver.find_element_by_xpath('//*[@class="grafico"][5]/div/div/div/table/tbody/tr[4]/td[2]').text
                                            valor4 = driver.find_element_by_xpath('//*[@class="grafico"][5]/div/div/div/table/tbody/tr[5]/td[1]').text
                                            valor44 = driver.find_element_by_xpath('//*[@class="grafico"][5]/div/div/div/table/tbody/tr[5]/td[2]').text
                                            valor5 = driver.find_element_by_xpath('//*[@class="grafico"][5]/div/div/div/table/tbody/tr[6]/td[1]').text
                                            valor55 = driver.find_element_by_xpath('//*[@class="grafico"][5]/div/div/div/table/tbody/tr[6]/td[2]').text
                                            grupo = {
                                                            "pesquisador":
                                                                [{
                                                                    "identificacao":[{
                                                                        
                                                                        
                                                                            "pesquisador": nome, "producao":[{
                                                                                "ano": valor_ano,
                                                                                valor1: valor11,
                                                                                valor2: valor22,
                                                                                valor3: valor33,
                                                                                valor4: valor44,
                                                                                valor5: valor55
                                                                                }]
                                                                        }]
                                                                }]
                                                    }
                                        if cont_lin == 5:
                                            valor1 = driver.find_element_by_xpath('//*[@class="grafico"][5]/div/div/div/table/tbody/tr[2]/td[1]').text
                                            valor11 = driver.find_element_by_xpath('//*[@class="grafico"][5]/div/div/div/table/tbody/tr[2]/td[2]').text
                                            valor2 = driver.find_element_by_xpath('//*[@class="grafico"][5]/div/div/div/table/tbody/tr[3]/td[1]').text
                                            valor22 = driver.find_element_by_xpath('//*[@class="grafico"][5]/div/div/div/table/tbody/tr[3]/td[2]').text
                                            valor3 = driver.find_element_by_xpath('//*[@class="grafico"][5]/div/div/div/table/tbody/tr[4]/td[1]').text
                                            valor33 = driver.find_element_by_xpath('//*[@class="grafico"][5]/div/div/div/table/tbody/tr[4]/td[2]').text
                                            valor4 = driver.find_element_by_xpath('//*[@class="grafico"][5]/div/div/div/table/tbody/tr[5]/td[1]').text
                                            valor44 = driver.find_element_by_xpath('//*[@class="grafico"][5]/div/div/div/table/tbody/tr[5]/td[2]').text
                                            grupo = {
                                                            "pesquisador":
                                                                [{
                                                                    "identificacao":[{
                                                                        
                                                                        
                                                                            "pesquisador": nome, "producao":[{
                                                                                "ano": valor_ano,
                                                                                valor1: valor11,
                                                                                valor2: valor22,
                                                                                valor3: valor33,
                                                                                valor4: valor44
                                                                                }]
                                                                        }]
                                                                }]
                                                    }
                                        if cont_lin == 4:
                                            valor1 = driver.find_element_by_xpath('//*[@class="grafico"][5]/div/div/div/table/tbody/tr[2]/td[1]').text
                                            valor11 = driver.find_element_by_xpath('//*[@class="grafico"][5]/div/div/div/table/tbody/tr[2]/td[2]').text
                                            valor2 = driver.find_element_by_xpath('//*[@class="grafico"][5]/div/div/div/table/tbody/tr[3]/td[1]').text
                                            valor22 = driver.find_element_by_xpath('//*[@class="grafico"][5]/div/div/div/table/tbody/tr[3]/td[2]').text
                                            valor3 = driver.find_element_by_xpath('//*[@class="grafico"][5]/div/div/div/table/tbody/tr[4]/td[1]').text
                                            valor33 = driver.find_element_by_xpath('//*[@class="grafico"][5]/div/div/div/table/tbody/tr[4]/td[2]').text
                                            grupo = {
                                                            "pesquisador":
                                                                [{
                                                                    "identificacao":[{
                                                                        
                                                                        
                                                                            "pesquisador": nome, "producao":[{
                                                                                "ano": valor_ano,
                                                                                valor1: valor11,
                                                                                valor2: valor22,
                                                                                valor3: valor33
                                                                                }]
                                                                        }]
                                                                }]
                                                    }
                                        if cont_lin == 3:
                                            valor1 = driver.find_element_by_xpath('//*[@class="grafico"][5]/div/div/div/table/tbody/tr[2]/td[1]').text
                                            valor11 = driver.find_element_by_xpath('//*[@class="grafico"][5]/div/div/div/table/tbody/tr[2]/td[2]').text
                                            valor2 = driver.find_element_by_xpath('//*[@class="grafico"][5]/div/div/div/table/tbody/tr[3]/td[1]').text
                                            valor22 = driver.find_element_by_xpath('//*[@class="grafico"][5]/div/div/div/table/tbody/tr[3]/td[2]').text
                                            grupo = {
                                                            "pesquisador":
                                                                [{
                                                                    "identificacao":[{
                                                                        
                                                                        
                                                                            "pesquisador": nome, "producao":[{
                                                                                "ano": valor_ano,
                                                                                valor1: valor11,
                                                                                valor2: valor22
                                                                                }]
                                                                        }]
                                                                }]
                                                    }
                                        if cont_lin == 2:
                                            valor1 = driver.find_element_by_xpath('//*[@class="grafico"][5]/div/div/div/table/tbody/tr[2]/td[1]').text
                                            valor11 = driver.find_element_by_xpath('//*[@class="grafico"][5]/div/div/div/table/tbody/tr[2]/td[2]').text
                                            grupo = {
                                                            "pesquisador":
                                                                [{
                                                                    "identificacao":[{
                                                                        
                                                                        
                                                                            "pesquisador": nome, "producao":[{
                                                                                "ano": valor_ano,
                                                                                valor1: valor11
                                                                                }]
                                                                        }]
                                                                }]
                                                    }
                                    elif cont_tabs == 4:
                                        cont_lin = len(driver.find_elements_by_xpath('//*[@class="grafico"][4]/div/div/div/table/tbody/tr'))
                                        nome = nomes[s]
                                        if cont_lin == 11:
                                            valor1 = driver.find_element_by_xpath('//*[@class="grafico"][4]/div/div/div/table/tbody/tr[2]/td[1]').text
                                            valor11 = driver.find_element_by_xpath('//*[@class="grafico"][4]/div/div/div/table/tbody/tr[2]/td[2]').text
                                            valor2 = driver.find_element_by_xpath('//*[@class="grafico"][4]/div/div/div/table/tbody/tr[3]/td[1]').text
                                            valor22 = driver.find_element_by_xpath('//*[@class="grafico"][4]/div/div/div/table/tbody/tr[3]/td[2]').text
                                            valor3 = driver.find_element_by_xpath('//*[@class="grafico"][4]/div/div/div/table/tbody/tr[4]/td[1]').text
                                            valor33 = driver.find_element_by_xpath('//*[@class="grafico"][4]/div/div/div/table/tbody/tr[4]/td[2]').text
                                            valor4 = driver.find_element_by_xpath('//*[@class="grafico"][4]/div/div/div/table/tbody/tr[5]/td[1]').text
                                            valor44 = driver.find_element_by_xpath('//*[@class="grafico"][4]/div/div/div/table/tbody/tr[5]/td[2]').text
                                            valor5 = driver.find_element_by_xpath('//*[@class="grafico"][4]/div/div/div/table/tbody/tr[6]/td[1]').text
                                            valor55 = driver.find_element_by_xpath('//*[@class="grafico"][4]/div/div/div/table/tbody/tr[6]/td[2]').text
                                            valor6 = driver.find_element_by_xpath('//*[@class="grafico"][4]/div/div/div/table/tbody/tr[7]/td[1]').text
                                            valor66 = driver.find_element_by_xpath('//*[@class="grafico"][4]/div/div/div/table/tbody/tr[7]/td[2]').text
                                            valor7 = driver.find_element_by_xpath('//*[@class="grafico"][4]/div/div/div/table/tbody/tr[8]/td[1]').text
                                            valor77 = driver.find_element_by_xpath('//*[@class="grafico"][4]/div/div/div/table/tbody/tr[8]/td[2]').text
                                            valor8 = driver.find_element_by_xpath('//*[@class="grafico"][4]/div/div/div/table/tbody/tr[9]/td[1]').text
                                            valor88 = driver.find_element_by_xpath('//*[@class="grafico"][4]/div/div/div/table/tbody/tr[9]/td[2]').text
                                            valor9 = driver.find_element_by_xpath('//*[@class="grafico"][4]/div/div/div/table/tbody/tr[10]/td[1]').text
                                            valor99 = driver.find_element_by_xpath('//*[@class="grafico"][4]/div/div/div/table/tbody/tr[10]/td[2]').text
                                            valor10 = driver.find_element_by_xpath('//*[@class="grafico"][4]/div/div/div/table/tbody/tr[11]/td[1]').text
                                            valor1010 = driver.find_element_by_xpath('//*[@class="grafico"][4]/div/div/div/table/tbody/tr[11]/td[2]').text
                                            grupo = {
                                                            "pesquisador":
                                                                [{
                                                                    "identificacao":[{
                                                                        
                                                                        
                                                                            "pesquisador": nome, "producao":[{
                                                                                "ano": valor_ano,
                                                                                valor1: valor11,
                                                                                valor2: valor22,
                                                                                valor3: valor33,
                                                                                valor4: valor44,
                                                                                valor5: valor55,
                                                                                valor6: valor66,
                                                                                valor7: valor77,
                                                                                valor8: valor88,
                                                                                valor9: valor99,
                                                                                valor10: valor1010
                                                                                }]
                                                                        }]
                                                                }]
                                                    }
                                        if cont_lin == 10:
                                            valor1 = driver.find_element_by_xpath('//*[@class="grafico"][4]/div/div/div/table/tbody/tr[2]/td[1]').text
                                            valor11 = driver.find_element_by_xpath('//*[@class="grafico"][4]/div/div/div/table/tbody/tr[2]/td[2]').text
                                            valor2 = driver.find_element_by_xpath('//*[@class="grafico"][4]/div/div/div/table/tbody/tr[3]/td[1]').text
                                            valor22 = driver.find_element_by_xpath('//*[@class="grafico"][4]/div/div/div/table/tbody/tr[3]/td[2]').text
                                            valor3 = driver.find_element_by_xpath('//*[@class="grafico"][4]/div/div/div/table/tbody/tr[4]/td[1]').text
                                            valor33 = driver.find_element_by_xpath('//*[@class="grafico"][4]/div/div/div/table/tbody/tr[4]/td[2]').text
                                            valor4 = driver.find_element_by_xpath('//*[@class="grafico"][4]/div/div/div/table/tbody/tr[5]/td[1]').text
                                            valor44 = driver.find_element_by_xpath('//*[@class="grafico"][4]/div/div/div/table/tbody/tr[5]/td[2]').text
                                            valor5 = driver.find_element_by_xpath('//*[@class="grafico"][4]/div/div/div/table/tbody/tr[6]/td[1]').text
                                            valor55 = driver.find_element_by_xpath('//*[@class="grafico"][4]/div/div/div/table/tbody/tr[6]/td[2]').text
                                            valor6 = driver.find_element_by_xpath('//*[@class="grafico"][4]/div/div/div/table/tbody/tr[7]/td[1]').text
                                            valor66 = driver.find_element_by_xpath('//*[@class="grafico"][4]/div/div/div/table/tbody/tr[7]/td[2]').text
                                            valor7 = driver.find_element_by_xpath('//*[@class="grafico"][4]/div/div/div/table/tbody/tr[8]/td[1]').text
                                            valor77 = driver.find_element_by_xpath('//*[@class="grafico"][4]/div/div/div/table/tbody/tr[8]/td[2]').text
                                            valor8 = driver.find_element_by_xpath('//*[@class="grafico"][4]/div/div/div/table/tbody/tr[9]/td[1]').text
                                            valor88 = driver.find_element_by_xpath('//*[@class="grafico"][4]/div/div/div/table/tbody/tr[9]/td[2]').text
                                            valor9 = driver.find_element_by_xpath('//*[@class="grafico"][4]/div/div/div/table/tbody/tr[10]/td[1]').text
                                            valor99 = driver.find_element_by_xpath('//*[@class="grafico"][4]/div/div/div/table/tbody/tr[10]/td[2]').text
                                            grupo = {
                                                            "pesquisador":
                                                                [{
                                                                    "identificacao":[{
                                                                        
                                                                        
                                                                            "pesquisador": nome, "producao":[{
                                                                                "ano": valor_ano,
                                                                                valor1: valor11,
                                                                                valor2: valor22,
                                                                                valor3: valor33,
                                                                                valor4: valor44,
                                                                                valor5: valor55,
                                                                                valor6: valor66,
                                                                                valor7: valor77,
                                                                                valor8: valor88,
                                                                                valor9: valor99
                                                                                }]
                                                                        }]
                                                                }]
                                                    }
                                        if cont_lin == 9:
                                            valor1 = driver.find_element_by_xpath('//*[@class="grafico"][4]/div/div/div/table/tbody/tr[2]/td[1]').text
                                            valor11 = driver.find_element_by_xpath('//*[@class="grafico"][4]/div/div/div/table/tbody/tr[2]/td[2]').text
                                            valor2 = driver.find_element_by_xpath('//*[@class="grafico"][4]/div/div/div/table/tbody/tr[3]/td[1]').text
                                            valor22 = driver.find_element_by_xpath('//*[@class="grafico"][4]/div/div/div/table/tbody/tr[3]/td[2]').text
                                            valor3 = driver.find_element_by_xpath('//*[@class="grafico"][4]/div/div/div/table/tbody/tr[4]/td[1]').text
                                            valor33 = driver.find_element_by_xpath('//*[@class="grafico"][4]/div/div/div/table/tbody/tr[4]/td[2]').text
                                            valor4 = driver.find_element_by_xpath('//*[@class="grafico"][4]/div/div/div/table/tbody/tr[5]/td[1]').text
                                            valor44 = driver.find_element_by_xpath('//*[@class="grafico"][4]/div/div/div/table/tbody/tr[5]/td[2]').text
                                            valor5 = driver.find_element_by_xpath('//*[@class="grafico"][4]/div/div/div/table/tbody/tr[6]/td[1]').text
                                            valor55 = driver.find_element_by_xpath('//*[@class="grafico"][4]/div/div/div/table/tbody/tr[6]/td[2]').text
                                            valor6 = driver.find_element_by_xpath('//*[@class="grafico"][4]/div/div/div/table/tbody/tr[7]/td[1]').text
                                            valor66 = driver.find_element_by_xpath('//*[@class="grafico"][4]/div/div/div/table/tbody/tr[7]/td[2]').text
                                            valor7 = driver.find_element_by_xpath('//*[@class="grafico"][4]/div/div/div/table/tbody/tr[8]/td[1]').text
                                            valor77 = driver.find_element_by_xpath('//*[@class="grafico"][4]/div/div/div/table/tbody/tr[8]/td[2]').text
                                            valor8 = driver.find_element_by_xpath('//*[@class="grafico"][4]/div/div/div/table/tbody/tr[9]/td[1]').text
                                            valor88 = driver.find_element_by_xpath('//*[@class="grafico"][4]/div/div/div/table/tbody/tr[9]/td[2]').text
                                            grupo = {
                                                            "pesquisador":
                                                                [{
                                                                    "identificacao":[{
                                                                        
                                                                        
                                                                            "pesquisador": nome, "producao":[{
                                                                                "ano": valor_ano,
                                                                                valor1: valor11,
                                                                                valor2: valor22,
                                                                                valor3: valor33,
                                                                                valor4: valor44,
                                                                                valor5: valor55,
                                                                                valor6: valor66,
                                                                                valor7: valor77,
                                                                                valor8: valor88
                                                                                }]
                                                                        }]
                                                                }]
                                                    }
                                        if cont_lin == 8:
                                            valor1 = driver.find_element_by_xpath('//*[@class="grafico"][4]/div/div/div/table/tbody/tr[2]/td[1]').text
                                            valor11 = driver.find_element_by_xpath('//*[@class="grafico"][4]/div/div/div/table/tbody/tr[2]/td[2]').text
                                            valor2 = driver.find_element_by_xpath('//*[@class="grafico"][4]/div/div/div/table/tbody/tr[3]/td[1]').text
                                            valor22 = driver.find_element_by_xpath('//*[@class="grafico"][4]/div/div/div/table/tbody/tr[3]/td[2]').text
                                            valor3 = driver.find_element_by_xpath('//*[@class="grafico"][4]/div/div/div/table/tbody/tr[4]/td[1]').text
                                            valor33 = driver.find_element_by_xpath('//*[@class="grafico"][4]/div/div/div/table/tbody/tr[4]/td[2]').text
                                            valor4 = driver.find_element_by_xpath('//*[@class="grafico"][4]/div/div/div/table/tbody/tr[5]/td[1]').text
                                            valor44 = driver.find_element_by_xpath('//*[@class="grafico"][4]/div/div/div/table/tbody/tr[5]/td[2]').text
                                            valor5 = driver.find_element_by_xpath('//*[@class="grafico"][4]/div/div/div/table/tbody/tr[6]/td[1]').text
                                            valor55 = driver.find_element_by_xpath('//*[@class="grafico"][4]/div/div/div/table/tbody/tr[6]/td[2]').text
                                            valor6 = driver.find_element_by_xpath('//*[@class="grafico"][4]/div/div/div/table/tbody/tr[7]/td[1]').text
                                            valor66 = driver.find_element_by_xpath('//*[@class="grafico"][4]/div/div/div/table/tbody/tr[7]/td[2]').text
                                            valor7 = driver.find_element_by_xpath('//*[@class="grafico"][4]/div/div/div/table/tbody/tr[8]/td[1]').text
                                            valor77 = driver.find_element_by_xpath('//*[@class="grafico"][4]/div/div/div/table/tbody/tr[8]/td[2]').text
                                            grupo = {
                                                            "pesquisador":
                                                                [{
                                                                    "identificacao":[{
                                                                        
                                                                        
                                                                            "pesquisador": nome, "producao":[{
                                                                                "ano": valor_ano,
                                                                                valor1: valor11,
                                                                                valor2: valor22,
                                                                                valor3: valor33,
                                                                                valor4: valor44,
                                                                                valor5: valor55,
                                                                                valor6: valor66,
                                                                                valor7: valor77
                                                                                }]
                                                                        }]
                                                                }]
                                                    }
                                        if cont_lin == 7:
                                            valor1 = driver.find_element_by_xpath('//*[@class="grafico"][4]/div/div/div/table/tbody/tr[2]/td[1]').text
                                            valor11 = driver.find_element_by_xpath('//*[@class="grafico"][4]/div/div/div/table/tbody/tr[2]/td[2]').text
                                            valor2 = driver.find_element_by_xpath('//*[@class="grafico"][4]/div/div/div/table/tbody/tr[3]/td[1]').text
                                            valor22 = driver.find_element_by_xpath('//*[@class="grafico"][4]/div/div/div/table/tbody/tr[3]/td[2]').text
                                            valor3 = driver.find_element_by_xpath('//*[@class="grafico"][4]/div/div/div/table/tbody/tr[4]/td[1]').text
                                            valor33 = driver.find_element_by_xpath('//*[@class="grafico"][4]/div/div/div/table/tbody/tr[4]/td[2]').text
                                            valor4 = driver.find_element_by_xpath('//*[@class="grafico"][4]/div/div/div/table/tbody/tr[5]/td[1]').text
                                            valor44 = driver.find_element_by_xpath('//*[@class="grafico"][4]/div/div/div/table/tbody/tr[5]/td[2]').text
                                            valor5 = driver.find_element_by_xpath('//*[@class="grafico"][4]/div/div/div/table/tbody/tr[6]/td[1]').text
                                            valor55 = driver.find_element_by_xpath('//*[@class="grafico"][4]/div/div/div/table/tbody/tr[6]/td[2]').text
                                            valor6 = driver.find_element_by_xpath('//*[@class="grafico"][4]/div/div/div/table/tbody/tr[7]/td[1]').text
                                            valor66 = driver.find_element_by_xpath('//*[@class="grafico"][4]/div/div/div/table/tbody/tr[7]/td[2]').text
                                            grupo = {
                                                            "pesquisador":
                                                                [{
                                                                    "identificacao":[{
                                                                        
                                                                        
                                                                            "pesquisador": nome, "producao":[{
                                                                                "ano": valor_ano,
                                                                                valor1: valor11,
                                                                                valor2: valor22,
                                                                                valor3: valor33,
                                                                                valor4: valor44,
                                                                                valor5: valor55,
                                                                                valor6: valor66
                                                                                }]
                                                                        }]
                                                                }]
                                                    }
                                        if cont_lin == 6:
                                            valor1 = driver.find_element_by_xpath('//*[@class="grafico"][4]/div/div/div/table/tbody/tr[2]/td[1]').text
                                            valor11 = driver.find_element_by_xpath('//*[@class="grafico"][4]/div/div/div/table/tbody/tr[2]/td[2]').text
                                            valor2 = driver.find_element_by_xpath('//*[@class="grafico"][4]/div/div/div/table/tbody/tr[3]/td[1]').text
                                            valor22 = driver.find_element_by_xpath('//*[@class="grafico"][4]/div/div/div/table/tbody/tr[3]/td[2]').text
                                            valor3 = driver.find_element_by_xpath('//*[@class="grafico"][4]/div/div/div/table/tbody/tr[4]/td[1]').text
                                            valor33 = driver.find_element_by_xpath('//*[@class="grafico"][4]/div/div/div/table/tbody/tr[4]/td[2]').text
                                            valor4 = driver.find_element_by_xpath('//*[@class="grafico"][4]/div/div/div/table/tbody/tr[5]/td[1]').text
                                            valor44 = driver.find_element_by_xpath('//*[@class="grafico"][4]/div/div/div/table/tbody/tr[5]/td[2]').text
                                            valor5 = driver.find_element_by_xpath('//*[@class="grafico"][4]/div/div/div/table/tbody/tr[6]/td[1]').text
                                            valor55 = driver.find_element_by_xpath('//*[@class="grafico"][4]/div/div/div/table/tbody/tr[6]/td[2]').text
                                            grupo = {
                                                            "pesquisador":
                                                                [{
                                                                    "identificacao":[{
                                                                        
                                                                        
                                                                            "pesquisador": nome, "producao":[{
                                                                                "ano": valor_ano,
                                                                                valor1: valor11,
                                                                                valor2: valor22,
                                                                                valor3: valor33,
                                                                                valor4: valor44,
                                                                                valor5: valor55
                                                                                }]
                                                                        }]
                                                                }]
                                                    }
                                        if cont_lin == 5:
                                            valor1 = driver.find_element_by_xpath('//*[@class="grafico"][4]/div/div/div/table/tbody/tr[2]/td[1]').text
                                            valor11 = driver.find_element_by_xpath('//*[@class="grafico"][4]/div/div/div/table/tbody/tr[2]/td[2]').text
                                            valor2 = driver.find_element_by_xpath('//*[@class="grafico"][4]/div/div/div/table/tbody/tr[3]/td[1]').text
                                            valor22 = driver.find_element_by_xpath('//*[@class="grafico"][4]/div/div/div/table/tbody/tr[3]/td[2]').text
                                            valor3 = driver.find_element_by_xpath('//*[@class="grafico"][4]/div/div/div/table/tbody/tr[4]/td[1]').text
                                            valor33 = driver.find_element_by_xpath('//*[@class="grafico"][4]/div/div/div/table/tbody/tr[4]/td[2]').text
                                            valor4 = driver.find_element_by_xpath('//*[@class="grafico"][4]/div/div/div/table/tbody/tr[5]/td[1]').text
                                            valor44 = driver.find_element_by_xpath('//*[@class="grafico"][4]/div/div/div/table/tbody/tr[5]/td[2]').text
                                            grupo = {
                                                            "pesquisador":
                                                                [{
                                                                    "identificacao":[{
                                                                        
                                                                        
                                                                            "pesquisador": nome, "producao":[{
                                                                                "ano": valor_ano,
                                                                                valor1: valor11,
                                                                                valor2: valor22,
                                                                                valor3: valor33,
                                                                                valor4: valor44
                                                                                }]
                                                                        }]
                                                                }]
                                                    }
                                        if cont_lin == 4:
                                            valor1 = driver.find_element_by_xpath('//*[@class="grafico"][4]/div/div/div/table/tbody/tr[2]/td[1]').text
                                            valor11 = driver.find_element_by_xpath('//*[@class="grafico"][4]/div/div/div/table/tbody/tr[2]/td[2]').text
                                            valor2 = driver.find_element_by_xpath('//*[@class="grafico"][4]/div/div/div/table/tbody/tr[3]/td[1]').text
                                            valor22 = driver.find_element_by_xpath('//*[@class="grafico"][4]/div/div/div/table/tbody/tr[3]/td[2]').text
                                            valor3 = driver.find_element_by_xpath('//*[@class="grafico"][4]/div/div/div/table/tbody/tr[4]/td[1]').text
                                            valor33 = driver.find_element_by_xpath('//*[@class="grafico"][4]/div/div/div/table/tbody/tr[4]/td[2]').text
                                            grupo = {
                                                            "pesquisador":
                                                                [{
                                                                    "identificacao":[{
                                                                        
                                                                        
                                                                            "pesquisador": nome, "producao":[{
                                                                                "ano": valor_ano,
                                                                                valor1: valor11,
                                                                                valor2: valor22,
                                                                                valor3: valor33
                                                                                }]
                                                                        }]
                                                                }]
                                                    }
                                        if cont_lin == 3:
                                            valor1 = driver.find_element_by_xpath('//*[@class="grafico"][4]/div/div/div/table/tbody/tr[2]/td[1]').text
                                            valor11 = driver.find_element_by_xpath('//*[@class="grafico"][4]/div/div/div/table/tbody/tr[2]/td[2]').text
                                            valor2 = driver.find_element_by_xpath('//*[@class="grafico"][4]/div/div/div/table/tbody/tr[3]/td[1]').text
                                            valor22 = driver.find_element_by_xpath('//*[@class="grafico"][4]/div/div/div/table/tbody/tr[3]/td[2]').text
                                            grupo = {
                                                            "pesquisador":
                                                                [{
                                                                    "identificacao":[{
                                                                        
                                                                        
                                                                            "pesquisador": nome, "producao":[{
                                                                                "ano": valor_ano,
                                                                                valor1: valor11,
                                                                                valor2: valor22
                                                                                }]
                                                                        }]
                                                                }]
                                                    }
                                        if cont_lin == 2:
                                            valor1 = driver.find_element_by_xpath('//*[@class="grafico"][4]/div/div/div/table/tbody/tr[2]/td[1]').text
                                            valor11 = driver.find_element_by_xpath('//*[@class="grafico"][4]/div/div/div/table/tbody/tr[2]/td[2]').text
                                            grupo = {
                                                            "pesquisador":
                                                                [{
                                                                    "identificacao":[{
                                                                        
                                                                        
                                                                            "pesquisador": nome, "producao":[{
                                                                                "ano": valor_ano,
                                                                                valor1: valor11
                                                                                }]
                                                                        }]
                                                                }]
                                                    }
                                    elif cont_tabs == 3:
                                        cont_lin = len(driver.find_elements_by_xpath('//*[@class="grafico"][3]/div/div/div/table/tbody/tr'))
                                        nome = nomes[s]
                                        if cont_lin == 11:
                                            valor1 = driver.find_element_by_xpath('//*[@class="grafico"][3]/div/div/div/table/tbody/tr[2]/td[1]').text
                                            valor11 = driver.find_element_by_xpath('//*[@class="grafico"][3]/div/div/div/table/tbody/tr[2]/td[2]').text
                                            valor2 = driver.find_element_by_xpath('//*[@class="grafico"][3]/div/div/div/table/tbody/tr[3]/td[1]').text
                                            valor22 = driver.find_element_by_xpath('//*[@class="grafico"][3]/div/div/div/table/tbody/tr[3]/td[2]').text
                                            valor3 = driver.find_element_by_xpath('//*[@class="grafico"][3]/div/div/div/table/tbody/tr[4]/td[1]').text
                                            valor33 = driver.find_element_by_xpath('//*[@class="grafico"][3]/div/div/div/table/tbody/tr[4]/td[2]').text
                                            valor4 = driver.find_element_by_xpath('//*[@class="grafico"][3]/div/div/div/table/tbody/tr[5]/td[1]').text
                                            valor44 = driver.find_element_by_xpath('//*[@class="grafico"][3]/div/div/div/table/tbody/tr[5]/td[2]').text
                                            valor5 = driver.find_element_by_xpath('//*[@class="grafico"][3]/div/div/div/table/tbody/tr[6]/td[1]').text
                                            valor55 = driver.find_element_by_xpath('//*[@class="grafico"][3]/div/div/div/table/tbody/tr[6]/td[2]').text
                                            valor6 = driver.find_element_by_xpath('//*[@class="grafico"][3]/div/div/div/table/tbody/tr[7]/td[1]').text
                                            valor66 = driver.find_element_by_xpath('//*[@class="grafico"][3]/div/div/div/table/tbody/tr[7]/td[2]').text
                                            valor7 = driver.find_element_by_xpath('//*[@class="grafico"][3]/div/div/div/table/tbody/tr[8]/td[1]').text
                                            valor77 = driver.find_element_by_xpath('//*[@class="grafico"][3]/div/div/div/table/tbody/tr[8]/td[2]').text
                                            valor8 = driver.find_element_by_xpath('//*[@class="grafico"][3]/div/div/div/table/tbody/tr[9]/td[1]').text
                                            valor88 = driver.find_element_by_xpath('//*[@class="grafico"][3]/div/div/div/table/tbody/tr[9]/td[2]').text
                                            valor9 = driver.find_element_by_xpath('//*[@class="grafico"][3]/div/div/div/table/tbody/tr[10]/td[1]').text
                                            valor99 = driver.find_element_by_xpath('//*[@class="grafico"][3]/div/div/div/table/tbody/tr[10]/td[2]').text
                                            valor10 = driver.find_element_by_xpath('//*[@class="grafico"][3]/div/div/div/table/tbody/tr[11]/td[1]').text
                                            valor1010 = driver.find_element_by_xpath('//*[@class="grafico"][3]/div/div/div/table/tbody/tr[11]/td[2]').text
                                            grupo = {
                                                            "pesquisador":
                                                                [{
                                                                    "identificacao":[{
                                                                        
                                                                        
                                                                            "pesquisador": nome, "producao":[{
                                                                                "ano": valor_ano,
                                                                                valor1: valor11,
                                                                                valor2: valor22,
                                                                                valor3: valor33,
                                                                                valor4: valor44,
                                                                                valor5: valor55,
                                                                                valor6: valor66,
                                                                                valor7: valor77,
                                                                                valor8: valor88,
                                                                                valor9: valor99,
                                                                                valor10: valor1010
                                                                                }]
                                                                        }]
                                                                }]
                                                    }
                                        if cont_lin == 10:
                                            valor1 = driver.find_element_by_xpath('//*[@class="grafico"][3]/div/div/div/table/tbody/tr[2]/td[1]').text
                                            valor11 = driver.find_element_by_xpath('//*[@class="grafico"][3]/div/div/div/table/tbody/tr[2]/td[2]').text
                                            valor2 = driver.find_element_by_xpath('//*[@class="grafico"][3]/div/div/div/table/tbody/tr[3]/td[1]').text
                                            valor22 = driver.find_element_by_xpath('//*[@class="grafico"][3]/div/div/div/table/tbody/tr[3]/td[2]').text
                                            valor3 = driver.find_element_by_xpath('//*[@class="grafico"][3]/div/div/div/table/tbody/tr[4]/td[1]').text
                                            valor33 = driver.find_element_by_xpath('//*[@class="grafico"][3]/div/div/div/table/tbody/tr[4]/td[2]').text
                                            valor4 = driver.find_element_by_xpath('//*[@class="grafico"][3]/div/div/div/table/tbody/tr[5]/td[1]').text
                                            valor44 = driver.find_element_by_xpath('//*[@class="grafico"][3]/div/div/div/table/tbody/tr[5]/td[2]').text
                                            valor5 = driver.find_element_by_xpath('//*[@class="grafico"][3]/div/div/div/table/tbody/tr[6]/td[1]').text
                                            valor55 = driver.find_element_by_xpath('//*[@class="grafico"][3]/div/div/div/table/tbody/tr[6]/td[2]').text
                                            valor6 = driver.find_element_by_xpath('//*[@class="grafico"][3]/div/div/div/table/tbody/tr[7]/td[1]').text
                                            valor66 = driver.find_element_by_xpath('//*[@class="grafico"][3]/div/div/div/table/tbody/tr[7]/td[2]').text
                                            valor7 = driver.find_element_by_xpath('//*[@class="grafico"][3]/div/div/div/table/tbody/tr[8]/td[1]').text
                                            valor77 = driver.find_element_by_xpath('//*[@class="grafico"][3]/div/div/div/table/tbody/tr[8]/td[2]').text
                                            valor8 = driver.find_element_by_xpath('//*[@class="grafico"][3]/div/div/div/table/tbody/tr[9]/td[1]').text
                                            valor88 = driver.find_element_by_xpath('//*[@class="grafico"][3]/div/div/div/table/tbody/tr[9]/td[2]').text
                                            valor9 = driver.find_element_by_xpath('//*[@class="grafico"][3]/div/div/div/table/tbody/tr[10]/td[1]').text
                                            valor99 = driver.find_element_by_xpath('//*[@class="grafico"][3]/div/div/div/table/tbody/tr[10]/td[2]').text
                                            grupo = {
                                                            "pesquisador":
                                                                [{
                                                                    "identificacao":[{
                                                                        
                                                                        
                                                                            "pesquisador": nome, "producao":[{
                                                                                "ano": valor_ano,
                                                                                valor1: valor11,
                                                                                valor2: valor22,
                                                                                valor3: valor33,
                                                                                valor4: valor44,
                                                                                valor5: valor55,
                                                                                valor6: valor66,
                                                                                valor7: valor77,
                                                                                valor8: valor88,
                                                                                valor9: valor99
                                                                                }]
                                                                        }]
                                                                }]
                                                    }
                                        if cont_lin == 9:
                                            valor1 = driver.find_element_by_xpath('//*[@class="grafico"][3]/div/div/div/table/tbody/tr[2]/td[1]').text
                                            valor11 = driver.find_element_by_xpath('//*[@class="grafico"][3]/div/div/div/table/tbody/tr[2]/td[2]').text
                                            valor2 = driver.find_element_by_xpath('//*[@class="grafico"][3]/div/div/div/table/tbody/tr[3]/td[1]').text
                                            valor22 = driver.find_element_by_xpath('//*[@class="grafico"][3]/div/div/div/table/tbody/tr[3]/td[2]').text
                                            valor3 = driver.find_element_by_xpath('//*[@class="grafico"][3]/div/div/div/table/tbody/tr[4]/td[1]').text
                                            valor33 = driver.find_element_by_xpath('//*[@class="grafico"][3]/div/div/div/table/tbody/tr[4]/td[2]').text
                                            valor4 = driver.find_element_by_xpath('//*[@class="grafico"][3]/div/div/div/table/tbody/tr[5]/td[1]').text
                                            valor44 = driver.find_element_by_xpath('//*[@class="grafico"][3]/div/div/div/table/tbody/tr[5]/td[2]').text
                                            valor5 = driver.find_element_by_xpath('//*[@class="grafico"][3]/div/div/div/table/tbody/tr[6]/td[1]').text
                                            valor55 = driver.find_element_by_xpath('//*[@class="grafico"][3]/div/div/div/table/tbody/tr[6]/td[2]').text
                                            valor6 = driver.find_element_by_xpath('//*[@class="grafico"][3]/div/div/div/table/tbody/tr[7]/td[1]').text
                                            valor66 = driver.find_element_by_xpath('//*[@class="grafico"][3]/div/div/div/table/tbody/tr[7]/td[2]').text
                                            valor7 = driver.find_element_by_xpath('//*[@class="grafico"][3]/div/div/div/table/tbody/tr[8]/td[1]').text
                                            valor77 = driver.find_element_by_xpath('//*[@class="grafico"][3]/div/div/div/table/tbody/tr[8]/td[2]').text
                                            valor8 = driver.find_element_by_xpath('//*[@class="grafico"][3]/div/div/div/table/tbody/tr[9]/td[1]').text
                                            valor88 = driver.find_element_by_xpath('//*[@class="grafico"][3]/div/div/div/table/tbody/tr[9]/td[2]').text
                                            grupo = {
                                                            "pesquisador":
                                                                [{
                                                                    "identificacao":[{
                                                                        
                                                                        
                                                                            "pesquisador": nome, "producao":[{
                                                                                "ano": valor_ano,
                                                                                valor1: valor11,
                                                                                valor2: valor22,
                                                                                valor3: valor33,
                                                                                valor4: valor44,
                                                                                valor5: valor55,
                                                                                valor6: valor66,
                                                                                valor7: valor77,
                                                                                valor8: valor88
                                                                                }]
                                                                        }]
                                                                }]
                                                    }
                                        if cont_lin == 8:
                                            valor1 = driver.find_element_by_xpath('//*[@class="grafico"][3]/div/div/div/table/tbody/tr[2]/td[1]').text
                                            valor11 = driver.find_element_by_xpath('//*[@class="grafico"][3]/div/div/div/table/tbody/tr[2]/td[2]').text
                                            valor2 = driver.find_element_by_xpath('//*[@class="grafico"][3]/div/div/div/table/tbody/tr[3]/td[1]').text
                                            valor22 = driver.find_element_by_xpath('//*[@class="grafico"][3]/div/div/div/table/tbody/tr[3]/td[2]').text
                                            valor3 = driver.find_element_by_xpath('//*[@class="grafico"][3]/div/div/div/table/tbody/tr[4]/td[1]').text
                                            valor33 = driver.find_element_by_xpath('//*[@class="grafico"][3]/div/div/div/table/tbody/tr[4]/td[2]').text
                                            valor4 = driver.find_element_by_xpath('//*[@class="grafico"][3]/div/div/div/table/tbody/tr[5]/td[1]').text
                                            valor44 = driver.find_element_by_xpath('//*[@class="grafico"][3]/div/div/div/table/tbody/tr[5]/td[2]').text
                                            valor5 = driver.find_element_by_xpath('//*[@class="grafico"][3]/div/div/div/table/tbody/tr[6]/td[1]').text
                                            valor55 = driver.find_element_by_xpath('//*[@class="grafico"][3]/div/div/div/table/tbody/tr[6]/td[2]').text
                                            valor6 = driver.find_element_by_xpath('//*[@class="grafico"][3]/div/div/div/table/tbody/tr[7]/td[1]').text
                                            valor66 = driver.find_element_by_xpath('//*[@class="grafico"][3]/div/div/div/table/tbody/tr[7]/td[2]').text
                                            valor7 = driver.find_element_by_xpath('//*[@class="grafico"][3]/div/div/div/table/tbody/tr[8]/td[1]').text
                                            valor77 = driver.find_element_by_xpath('//*[@class="grafico"][3]/div/div/div/table/tbody/tr[8]/td[2]').text
                                            grupo = {
                                                            "pesquisador":
                                                                [{
                                                                    "identificacao":[{
                                                                        
                                                                        
                                                                            "pesquisador": nome, "producao":[{
                                                                                "ano": valor_ano,
                                                                                valor1: valor11,
                                                                                valor2: valor22,
                                                                                valor3: valor33,
                                                                                valor4: valor44,
                                                                                valor5: valor55,
                                                                                valor6: valor66,
                                                                                valor7: valor77
                                                                                }]
                                                                        }]
                                                                }]
                                                    }
                                        if cont_lin == 7:
                                            valor1 = driver.find_element_by_xpath('//*[@class="grafico"][3]/div/div/div/table/tbody/tr[2]/td[1]').text
                                            valor11 = driver.find_element_by_xpath('//*[@class="grafico"][3]/div/div/div/table/tbody/tr[2]/td[2]').text
                                            valor2 = driver.find_element_by_xpath('//*[@class="grafico"][3]/div/div/div/table/tbody/tr[3]/td[1]').text
                                            valor22 = driver.find_element_by_xpath('//*[@class="grafico"][3]/div/div/div/table/tbody/tr[3]/td[2]').text
                                            valor3 = driver.find_element_by_xpath('//*[@class="grafico"][3]/div/div/div/table/tbody/tr[4]/td[1]').text
                                            valor33 = driver.find_element_by_xpath('//*[@class="grafico"][3]/div/div/div/table/tbody/tr[4]/td[2]').text
                                            valor4 = driver.find_element_by_xpath('//*[@class="grafico"][3]/div/div/div/table/tbody/tr[5]/td[1]').text
                                            valor44 = driver.find_element_by_xpath('//*[@class="grafico"][3]/div/div/div/table/tbody/tr[5]/td[2]').text
                                            valor5 = driver.find_element_by_xpath('//*[@class="grafico"][3]/div/div/div/table/tbody/tr[6]/td[1]').text
                                            valor55 = driver.find_element_by_xpath('//*[@class="grafico"][3]/div/div/div/table/tbody/tr[6]/td[2]').text
                                            valor6 = driver.find_element_by_xpath('//*[@class="grafico"][3]/div/div/div/table/tbody/tr[7]/td[1]').text
                                            valor66 = driver.find_element_by_xpath('//*[@class="grafico"][3]/div/div/div/table/tbody/tr[7]/td[2]').text
                                            grupo = {
                                                            "pesquisador":
                                                                [{
                                                                    "identificacao":[{
                                                                        
                                                                        
                                                                            "pesquisador": nome, "producao":[{
                                                                                "ano": valor_ano,
                                                                                valor1: valor11,
                                                                                valor2: valor22,
                                                                                valor3: valor33,
                                                                                valor4: valor44,
                                                                                valor5: valor55,
                                                                                valor6: valor66
                                                                                }]
                                                                        }]
                                                                }]
                                                    }
                                        if cont_lin == 6:
                                            valor1 = driver.find_element_by_xpath('//*[@class="grafico"][3]/div/div/div/table/tbody/tr[2]/td[1]').text
                                            valor11 = driver.find_element_by_xpath('//*[@class="grafico"][3]/div/div/div/table/tbody/tr[2]/td[2]').text
                                            valor2 = driver.find_element_by_xpath('//*[@class="grafico"][3]/div/div/div/table/tbody/tr[3]/td[1]').text
                                            valor22 = driver.find_element_by_xpath('//*[@class="grafico"][3]/div/div/div/table/tbody/tr[3]/td[2]').text
                                            valor3 = driver.find_element_by_xpath('//*[@class="grafico"][3]/div/div/div/table/tbody/tr[4]/td[1]').text
                                            valor33 = driver.find_element_by_xpath('//*[@class="grafico"][3]/div/div/div/table/tbody/tr[4]/td[2]').text
                                            valor4 = driver.find_element_by_xpath('//*[@class="grafico"][3]/div/div/div/table/tbody/tr[5]/td[1]').text
                                            valor44 = driver.find_element_by_xpath('//*[@class="grafico"][3]/div/div/div/table/tbody/tr[5]/td[2]').text
                                            valor5 = driver.find_element_by_xpath('//*[@class="grafico"][3]/div/div/div/table/tbody/tr[6]/td[1]').text
                                            valor55 = driver.find_element_by_xpath('//*[@class="grafico"][3]/div/div/div/table/tbody/tr[6]/td[2]').text
                                            grupo = {
                                                            "pesquisador":
                                                                [{
                                                                    "identificacao":[{
                                                                        
                                                                        
                                                                            "pesquisador": nome, "producao":[{
                                                                                "ano": valor_ano,
                                                                                valor1: valor11,
                                                                                valor2: valor22,
                                                                                valor3: valor33,
                                                                                valor4: valor44,
                                                                                valor5: valor55
                                                                                }]
                                                                        }]
                                                                }]
                                                    }
                                        if cont_lin == 5:
                                            valor1 = driver.find_element_by_xpath('//*[@class="grafico"][3]/div/div/div/table/tbody/tr[2]/td[1]').text
                                            valor11 = driver.find_element_by_xpath('//*[@class="grafico"][3]/div/div/div/table/tbody/tr[2]/td[2]').text
                                            valor2 = driver.find_element_by_xpath('//*[@class="grafico"][3]/div/div/div/table/tbody/tr[3]/td[1]').text
                                            valor22 = driver.find_element_by_xpath('//*[@class="grafico"][3]/div/div/div/table/tbody/tr[3]/td[2]').text
                                            valor3 = driver.find_element_by_xpath('//*[@class="grafico"][3]/div/div/div/table/tbody/tr[4]/td[1]').text
                                            valor33 = driver.find_element_by_xpath('//*[@class="grafico"][3]/div/div/div/table/tbody/tr[4]/td[2]').text
                                            valor4 = driver.find_element_by_xpath('//*[@class="grafico"][3]/div/div/div/table/tbody/tr[5]/td[1]').text
                                            valor44 = driver.find_element_by_xpath('//*[@class="grafico"][3]/div/div/div/table/tbody/tr[5]/td[2]').text
                                            grupo = {
                                                            "pesquisador":
                                                                [{
                                                                    "identificacao":[{
                                                                        
                                                                        
                                                                            "pesquisador": nome, "producao":[{
                                                                                "ano": valor_ano,
                                                                                valor1: valor11,
                                                                                valor2: valor22,
                                                                                valor3: valor33,
                                                                                valor4: valor44
                                                                                }]
                                                                        }]
                                                                }]
                                                    }
                                        if cont_lin == 4:
                                            valor1 = driver.find_element_by_xpath('//*[@class="grafico"][3]/div/div/div/table/tbody/tr[2]/td[1]').text
                                            valor11 = driver.find_element_by_xpath('//*[@class="grafico"][3]/div/div/div/table/tbody/tr[2]/td[2]').text
                                            valor2 = driver.find_element_by_xpath('//*[@class="grafico"][3]/div/div/div/table/tbody/tr[3]/td[1]').text
                                            valor22 = driver.find_element_by_xpath('//*[@class="grafico"][3]/div/div/div/table/tbody/tr[3]/td[2]').text
                                            valor3 = driver.find_element_by_xpath('//*[@class="grafico"][3]/div/div/div/table/tbody/tr[4]/td[1]').text
                                            valor33 = driver.find_element_by_xpath('//*[@class="grafico"][3]/div/div/div/table/tbody/tr[4]/td[2]').text
                                            grupo = {
                                                            "pesquisador":
                                                                [{
                                                                    "identificacao":[{
                                                                        
                                                                        
                                                                            "pesquisador": nome, "producao":[{
                                                                                "ano": valor_ano,
                                                                                valor1: valor11,
                                                                                valor2: valor22,
                                                                                valor3: valor33
                                                                                }]
                                                                        }]
                                                                }]
                                                    }
                                        if cont_lin == 3:
                                            valor1 = driver.find_element_by_xpath('//*[@class="grafico"][3]/div/div/div/table/tbody/tr[2]/td[1]').text
                                            valor11 = driver.find_element_by_xpath('//*[@class="grafico"][3]/div/div/div/table/tbody/tr[2]/td[2]').text
                                            valor2 = driver.find_element_by_xpath('//*[@class="grafico"][3]/div/div/div/table/tbody/tr[3]/td[1]').text
                                            valor22 = driver.find_element_by_xpath('//*[@class="grafico"][3]/div/div/div/table/tbody/tr[3]/td[2]').text
                                            grupo = {
                                                            "pesquisador":
                                                                [{
                                                                    "identificacao":[{
                                                                        
                                                                        
                                                                            "pesquisador": nome, "producao":[{
                                                                                "ano": valor_ano,
                                                                                valor1: valor11,
                                                                                valor2: valor22
                                                                                }]
                                                                        }]
                                                                }]
                                                    }
                                        if cont_lin == 2:
                                            valor1 = driver.find_element_by_xpath('//*[@class="grafico"][3]/div/div/div/table/tbody/tr[2]/td[1]').text
                                            valor11 = driver.find_element_by_xpath('//*[@class="grafico"][3]/div/div/div/table/tbody/tr[2]/td[2]').text
                                            grupo = {
                                                            "pesquisador":
                                                                [{
                                                                    "identificacao":[{
                                                                        
                                                                        
                                                                            "pesquisador": nome, "producao":[{
                                                                                "ano": valor_ano,
                                                                                valor1: valor11
                                                                                }]
                                                                        }]
                                                                }]
                                                    }
                                    elif cont_tabs == 2:
                                        cont_lin = len(driver.find_elements_by_xpath('//*[@class="grafico"][2]/div/div/div/table/tbody/tr'))
                                        nome = nomes[s]
                                        if cont_lin == 11:
                                            valor1 = driver.find_element_by_xpath('//*[@class="grafico"][2]/div/div/div/table/tbody/tr[2]/td[1]').text
                                            valor11 = driver.find_element_by_xpath('//*[@class="grafico"][2]/div/div/div/table/tbody/tr[2]/td[2]').text
                                            valor2 = driver.find_element_by_xpath('//*[@class="grafico"][2]/div/div/div/table/tbody/tr[3]/td[1]').text
                                            valor22 = driver.find_element_by_xpath('//*[@class="grafico"][2]/div/div/div/table/tbody/tr[3]/td[2]').text
                                            valor3 = driver.find_element_by_xpath('//*[@class="grafico"][2]/div/div/div/table/tbody/tr[4]/td[1]').text
                                            valor33 = driver.find_element_by_xpath('//*[@class="grafico"][2]/div/div/div/table/tbody/tr[4]/td[2]').text
                                            valor4 = driver.find_element_by_xpath('//*[@class="grafico"][2]/div/div/div/table/tbody/tr[5]/td[1]').text
                                            valor44 = driver.find_element_by_xpath('//*[@class="grafico"][2]/div/div/div/table/tbody/tr[5]/td[2]').text
                                            valor5 = driver.find_element_by_xpath('//*[@class="grafico"][2]/div/div/div/table/tbody/tr[6]/td[1]').text
                                            valor55 = driver.find_element_by_xpath('//*[@class="grafico"][2]/div/div/div/table/tbody/tr[6]/td[2]').text
                                            valor6 = driver.find_element_by_xpath('//*[@class="grafico"][2]/div/div/div/table/tbody/tr[7]/td[1]').text
                                            valor66 = driver.find_element_by_xpath('//*[@class="grafico"][2]/div/div/div/table/tbody/tr[7]/td[2]').text
                                            valor7 = driver.find_element_by_xpath('//*[@class="grafico"][2]/div/div/div/table/tbody/tr[8]/td[1]').text
                                            valor77 = driver.find_element_by_xpath('//*[@class="grafico"][2]/div/div/div/table/tbody/tr[8]/td[2]').text
                                            valor8 = driver.find_element_by_xpath('//*[@class="grafico"][2]/div/div/div/table/tbody/tr[9]/td[1]').text
                                            valor88 = driver.find_element_by_xpath('//*[@class="grafico"][2]/div/div/div/table/tbody/tr[9]/td[2]').text
                                            valor9 = driver.find_element_by_xpath('//*[@class="grafico"][2]/div/div/div/table/tbody/tr[10]/td[1]').text
                                            valor99 = driver.find_element_by_xpath('//*[@class="grafico"][2]/div/div/div/table/tbody/tr[10]/td[2]').text
                                            valor10 = driver.find_element_by_xpath('//*[@class="grafico"][2]/div/div/div/table/tbody/tr[11]/td[1]').text
                                            valor1010 = driver.find_element_by_xpath('//*[@class="grafico"][2]/div/div/div/table/tbody/tr[11]/td[2]').text
                                            grupo = {
                                                            "pesquisador":
                                                                [{
                                                                    "identificacao":[{
                                                                        
                                                                        
                                                                            "pesquisador": nome, "producao":[{
                                                                                "ano": valor_ano,
                                                                                valor1: valor11,
                                                                                valor2: valor22,
                                                                                valor3: valor33,
                                                                                valor4: valor44,
                                                                                valor5: valor55,
                                                                                valor6: valor66,
                                                                                valor7: valor77,
                                                                                valor8: valor88,
                                                                                valor9: valor99,
                                                                                valor10: valor1010
                                                                                }]
                                                                        }]
                                                                }]
                                                    }
                                        if cont_lin == 10:
                                            valor1 = driver.find_element_by_xpath('//*[@class="grafico"][2]/div/div/div/table/tbody/tr[2]/td[1]').text
                                            valor11 = driver.find_element_by_xpath('//*[@class="grafico"][2]/div/div/div/table/tbody/tr[2]/td[2]').text
                                            valor2 = driver.find_element_by_xpath('//*[@class="grafico"][2]/div/div/div/table/tbody/tr[3]/td[1]').text
                                            valor22 = driver.find_element_by_xpath('//*[@class="grafico"][2]/div/div/div/table/tbody/tr[3]/td[2]').text
                                            valor3 = driver.find_element_by_xpath('//*[@class="grafico"][2]/div/div/div/table/tbody/tr[4]/td[1]').text
                                            valor33 = driver.find_element_by_xpath('//*[@class="grafico"][2]/div/div/div/table/tbody/tr[4]/td[2]').text
                                            valor4 = driver.find_element_by_xpath('//*[@class="grafico"][2]/div/div/div/table/tbody/tr[5]/td[1]').text
                                            valor44 = driver.find_element_by_xpath('//*[@class="grafico"][2]/div/div/div/table/tbody/tr[5]/td[2]').text
                                            valor5 = driver.find_element_by_xpath('//*[@class="grafico"][2]/div/div/div/table/tbody/tr[6]/td[1]').text
                                            valor55 = driver.find_element_by_xpath('//*[@class="grafico"][2]/div/div/div/table/tbody/tr[6]/td[2]').text
                                            valor6 = driver.find_element_by_xpath('//*[@class="grafico"][2]/div/div/div/table/tbody/tr[7]/td[1]').text
                                            valor66 = driver.find_element_by_xpath('//*[@class="grafico"][2]/div/div/div/table/tbody/tr[7]/td[2]').text
                                            valor7 = driver.find_element_by_xpath('//*[@class="grafico"][2]/div/div/div/table/tbody/tr[8]/td[1]').text
                                            valor77 = driver.find_element_by_xpath('//*[@class="grafico"][2]/div/div/div/table/tbody/tr[8]/td[2]').text
                                            valor8 = driver.find_element_by_xpath('//*[@class="grafico"][2]/div/div/div/table/tbody/tr[9]/td[1]').text
                                            valor88 = driver.find_element_by_xpath('//*[@class="grafico"][2]/div/div/div/table/tbody/tr[9]/td[2]').text
                                            valor9 = driver.find_element_by_xpath('//*[@class="grafico"][2]/div/div/div/table/tbody/tr[10]/td[1]').text
                                            valor99 = driver.find_element_by_xpath('//*[@class="grafico"][2]/div/div/div/table/tbody/tr[10]/td[2]').text
                                            grupo = {
                                                            "pesquisador":
                                                                [{
                                                                    "identificacao":[{
                                                                        
                                                                        
                                                                            "pesquisador": nome, "producao":[{
                                                                                "ano": valor_ano,
                                                                                valor1: valor11,
                                                                                valor2: valor22,
                                                                                valor3: valor33,
                                                                                valor4: valor44,
                                                                                valor5: valor55,
                                                                                valor6: valor66,
                                                                                valor7: valor77,
                                                                                valor8: valor88,
                                                                                valor9: valor99
                                                                                }]
                                                                        }]
                                                                }]
                                                    }
                                        if cont_lin == 9:
                                            valor1 = driver.find_element_by_xpath('//*[@class="grafico"][2]/div/div/div/table/tbody/tr[2]/td[1]').text
                                            valor11 = driver.find_element_by_xpath('//*[@class="grafico"][2]/div/div/div/table/tbody/tr[2]/td[2]').text
                                            valor2 = driver.find_element_by_xpath('//*[@class="grafico"][2]/div/div/div/table/tbody/tr[3]/td[1]').text
                                            valor22 = driver.find_element_by_xpath('//*[@class="grafico"][2]/div/div/div/table/tbody/tr[3]/td[2]').text
                                            valor3 = driver.find_element_by_xpath('//*[@class="grafico"][2]/div/div/div/table/tbody/tr[4]/td[1]').text
                                            valor33 = driver.find_element_by_xpath('//*[@class="grafico"][2]/div/div/div/table/tbody/tr[4]/td[2]').text
                                            valor4 = driver.find_element_by_xpath('//*[@class="grafico"][2]/div/div/div/table/tbody/tr[5]/td[1]').text
                                            valor44 = driver.find_element_by_xpath('//*[@class="grafico"][2]/div/div/div/table/tbody/tr[5]/td[2]').text
                                            valor5 = driver.find_element_by_xpath('//*[@class="grafico"][2]/div/div/div/table/tbody/tr[6]/td[1]').text
                                            valor55 = driver.find_element_by_xpath('//*[@class="grafico"][2]/div/div/div/table/tbody/tr[6]/td[2]').text
                                            valor6 = driver.find_element_by_xpath('//*[@class="grafico"][2]/div/div/div/table/tbody/tr[7]/td[1]').text
                                            valor66 = driver.find_element_by_xpath('//*[@class="grafico"][2]/div/div/div/table/tbody/tr[7]/td[2]').text
                                            valor7 = driver.find_element_by_xpath('//*[@class="grafico"][2]/div/div/div/table/tbody/tr[8]/td[1]').text
                                            valor77 = driver.find_element_by_xpath('//*[@class="grafico"][2]/div/div/div/table/tbody/tr[8]/td[2]').text
                                            valor8 = driver.find_element_by_xpath('//*[@class="grafico"][2]/div/div/div/table/tbody/tr[9]/td[1]').text
                                            valor88 = driver.find_element_by_xpath('//*[@class="grafico"][2]/div/div/div/table/tbody/tr[9]/td[2]').text
                                            grupo = {
                                                            "pesquisador":
                                                                [{
                                                                    "identificacao":[{
                                                                            "pesquisador": nome, 
                                                                            "producao":[{
                                                                                "ano": valor_ano,
                                                                                valor1: valor11,
                                                                                valor2: valor22,
                                                                                valor3: valor33,
                                                                                valor4: valor44,
                                                                                valor5: valor55,
                                                                                valor6: valor66,
                                                                                valor7: valor77,
                                                                                valor8: valor88
                                                                                }]
                                                                        }]
                                                                }]
                                                    }
                                        if cont_lin == 8:
                                            valor1 = driver.find_element_by_xpath('//*[@class="grafico"][2]/div/div/div/table/tbody/tr[2]/td[1]').text
                                            valor11 = driver.find_element_by_xpath('//*[@class="grafico"][2]/div/div/div/table/tbody/tr[2]/td[2]').text
                                            valor2 = driver.find_element_by_xpath('//*[@class="grafico"][2]/div/div/div/table/tbody/tr[3]/td[1]').text
                                            valor22 = driver.find_element_by_xpath('//*[@class="grafico"][2]/div/div/div/table/tbody/tr[3]/td[2]').text
                                            valor3 = driver.find_element_by_xpath('//*[@class="grafico"][2]/div/div/div/table/tbody/tr[4]/td[1]').text
                                            valor33 = driver.find_element_by_xpath('//*[@class="grafico"][2]/div/div/div/table/tbody/tr[4]/td[2]').text
                                            valor4 = driver.find_element_by_xpath('//*[@class="grafico"][2]/div/div/div/table/tbody/tr[5]/td[1]').text
                                            valor44 = driver.find_element_by_xpath('//*[@class="grafico"][2]/div/div/div/table/tbody/tr[5]/td[2]').text
                                            valor5 = driver.find_element_by_xpath('//*[@class="grafico"][2]/div/div/div/table/tbody/tr[6]/td[1]').text
                                            valor55 = driver.find_element_by_xpath('//*[@class="grafico"][2]/div/div/div/table/tbody/tr[6]/td[2]').text
                                            valor6 = driver.find_element_by_xpath('//*[@class="grafico"][2]/div/div/div/table/tbody/tr[7]/td[1]').text
                                            valor66 = driver.find_element_by_xpath('//*[@class="grafico"][2]/div/div/div/table/tbody/tr[7]/td[2]').text
                                            valor7 = driver.find_element_by_xpath('//*[@class="grafico"][2]/div/div/div/table/tbody/tr[8]/td[1]').text
                                            valor77 = driver.find_element_by_xpath('//*[@class="grafico"][2]/div/div/div/table/tbody/tr[8]/td[2]').text
                                            grupo = {
                                                            "pesquisador":
                                                                [{
                                                                    "identificacao":[{
                                                                            "pesquisador": nome, 
                                                                            "producao":[{
                                                                                "ano": valor_ano,
                                                                                valor1: valor11,
                                                                                valor2: valor22,
                                                                                valor3: valor33,
                                                                                valor4: valor44,
                                                                                valor5: valor55,
                                                                                valor6: valor66,
                                                                                valor7: valor77
                                                                                }]
                                                                        }]
                                                                }]
                                                    }
                                        if cont_lin == 7:
                                            valor1 = driver.find_element_by_xpath('//*[@class="grafico"][2]/div/div/div/table/tbody/tr[2]/td[1]').text
                                            valor11 = driver.find_element_by_xpath('//*[@class="grafico"][2]/div/div/div/table/tbody/tr[2]/td[2]').text
                                            valor2 = driver.find_element_by_xpath('//*[@class="grafico"][2]/div/div/div/table/tbody/tr[3]/td[1]').text
                                            valor22 = driver.find_element_by_xpath('//*[@class="grafico"][2]/div/div/div/table/tbody/tr[3]/td[2]').text
                                            valor3 = driver.find_element_by_xpath('//*[@class="grafico"][2]/div/div/div/table/tbody/tr[4]/td[1]').text
                                            valor33 = driver.find_element_by_xpath('//*[@class="grafico"][2]/div/div/div/table/tbody/tr[4]/td[2]').text
                                            valor4 = driver.find_element_by_xpath('//*[@class="grafico"][2]/div/div/div/table/tbody/tr[5]/td[1]').text
                                            valor44 = driver.find_element_by_xpath('//*[@class="grafico"][2]/div/div/div/table/tbody/tr[5]/td[2]').text
                                            valor5 = driver.find_element_by_xpath('//*[@class="grafico"][2]/div/div/div/table/tbody/tr[6]/td[1]').text
                                            valor55 = driver.find_element_by_xpath('//*[@class="grafico"][2]/div/div/div/table/tbody/tr[6]/td[2]').text
                                            valor6 = driver.find_element_by_xpath('//*[@class="grafico"][2]/div/div/div/table/tbody/tr[7]/td[1]').text
                                            valor66 = driver.find_element_by_xpath('//*[@class="grafico"][2]/div/div/div/table/tbody/tr[7]/td[2]').text
                                            grupo = {
                                                            "pesquisador":
                                                                [{
                                                                    "identificacao":[{
                                                                            "pesquisador": nome, 
                                                                            "producao":[{
                                                                                "ano": valor_ano,
                                                                                valor1: valor11,
                                                                                valor2: valor22,
                                                                                valor3: valor33,
                                                                                valor4: valor44,
                                                                                valor5: valor55,
                                                                                valor6: valor66
                                                                                }]
                                                                        }]
                                                                }]
                                                    }
                                        if cont_lin == 6:
                                            valor1 = driver.find_element_by_xpath('//*[@class="grafico"][2]/div/div/div/table/tbody/tr[2]/td[1]').text
                                            valor11 = driver.find_element_by_xpath('//*[@class="grafico"][2]/div/div/div/table/tbody/tr[2]/td[2]').text
                                            valor2 = driver.find_element_by_xpath('//*[@class="grafico"][2]/div/div/div/table/tbody/tr[3]/td[1]').text
                                            valor22 = driver.find_element_by_xpath('//*[@class="grafico"][2]/div/div/div/table/tbody/tr[3]/td[2]').text
                                            valor3 = driver.find_element_by_xpath('//*[@class="grafico"][2]/div/div/div/table/tbody/tr[4]/td[1]').text
                                            valor33 = driver.find_element_by_xpath('//*[@class="grafico"][2]/div/div/div/table/tbody/tr[4]/td[2]').text
                                            valor4 = driver.find_element_by_xpath('//*[@class="grafico"][2]/div/div/div/table/tbody/tr[5]/td[1]').text
                                            valor44 = driver.find_element_by_xpath('//*[@class="grafico"][2]/div/div/div/table/tbody/tr[5]/td[2]').text
                                            valor5 = driver.find_element_by_xpath('//*[@class="grafico"][2]/div/div/div/table/tbody/tr[6]/td[1]').text
                                            valor55 = driver.find_element_by_xpath('//*[@class="grafico"][2]/div/div/div/table/tbody/tr[6]/td[2]').text
                                            grupo = {
                                                            "pesquisador":
                                                                [{
                                                                    "identificacao":{
                                                                            "pesquisador": nome, 
                                                                            "producao":[{
                                                                                "ano": valor_ano,
                                                                                valor1: valor11,
                                                                                valor2: valor22,
                                                                                valor3: valor33,
                                                                                valor4: valor44,
                                                                                valor5: valor55
                                                                                }]
                                                                        }
                                                                }]
                                                    }
                                        if cont_lin == 5:
                                            valor1 = driver.find_element_by_xpath('//*[@class="grafico"][2]/div/div/div/table/tbody/tr[2]/td[1]').text
                                            valor11 = driver.find_element_by_xpath('//*[@class="grafico"][2]/div/div/div/table/tbody/tr[2]/td[2]').text
                                            valor2 = driver.find_element_by_xpath('//*[@class="grafico"][2]/div/div/div/table/tbody/tr[3]/td[1]').text
                                            valor22 = driver.find_element_by_xpath('//*[@class="grafico"][2]/div/div/div/table/tbody/tr[3]/td[2]').text
                                            valor3 = driver.find_element_by_xpath('//*[@class="grafico"][2]/div/div/div/table/tbody/tr[4]/td[1]').text
                                            valor33 = driver.find_element_by_xpath('//*[@class="grafico"][2]/div/div/div/table/tbody/tr[4]/td[2]').text
                                            valor4 = driver.find_element_by_xpath('//*[@class="grafico"][2]/div/div/div/table/tbody/tr[5]/td[1]').text
                                            valor44 = driver.find_element_by_xpath('//*[@class="grafico"][2]/div/div/div/table/tbody/tr[5]/td[2]').text
                                            grupo = {
                                                            "pesquisador":
                                                                [{
                                                                    "identificacao":[{
                                                                            "pesquisador": nome, 
                                                                            "producao":[{
                                                                                "ano": valor_ano,
                                                                                valor1: valor11,
                                                                                valor2: valor22,
                                                                                valor3: valor33,
                                                                                valor4: valor44
                                                                                }]
                                                                        }]
                                                                }]
                                                    }
                                        if cont_lin == 4:
                                            valor1 = driver.find_element_by_xpath('//*[@class="grafico"][2]/div/div/div/table/tbody/tr[2]/td[1]').text
                                            valor11 = driver.find_element_by_xpath('//*[@class="grafico"][2]/div/div/div/table/tbody/tr[2]/td[2]').text
                                            valor2 = driver.find_element_by_xpath('//*[@class="grafico"][2]/div/div/div/table/tbody/tr[3]/td[1]').text
                                            valor22 = driver.find_element_by_xpath('//*[@class="grafico"][2]/div/div/div/table/tbody/tr[3]/td[2]').text
                                            valor3 = driver.find_element_by_xpath('//*[@class="grafico"][2]/div/div/div/table/tbody/tr[4]/td[1]').text
                                            valor33 = driver.find_element_by_xpath('//*[@class="grafico"][2]/div/div/div/table/tbody/tr[4]/td[2]').text
                                            grupo = {
                                                            "pesquisador":
                                                                [{
                                                                    "identificacao":[{
                                                                        
                                                                        
                                                                            "pesquisador": nome, 
                                                                            "producao":[{
                                                                                "ano": valor_ano,
                                                                                valor1: valor11,
                                                                                valor2: valor22,
                                                                                valor3: valor33
                                                                                }]
                                                                        }]
                                                                }]
                                                    }
                                        if cont_lin == 3:
                                            valor1 = driver.find_element_by_xpath('//*[@class="grafico"][2]/div/div/div/table/tbody/tr[2]/td[1]').text
                                            valor11 = driver.find_element_by_xpath('//*[@class="grafico"][2]/div/div/div/table/tbody/tr[2]/td[2]').text
                                            valor2 = driver.find_element_by_xpath('//*[@class="grafico"][2]/div/div/div/table/tbody/tr[3]/td[1]').text
                                            valor22 = driver.find_element_by_xpath('//*[@class="grafico"][2]/div/div/div/table/tbody/tr[3]/td[2]').text
                                            grupo = {
                                                            "pesquisador":[
                                                                {
                                                                    "identificacao":[{
                                                                        
                                                                        
                                                                            "pesquisador": nome, 
                                                                            "producao":[{
                                                                                "ano": valor_ano,
                                                                                valor1: valor11,
                                                                                valor2: valor22
                                                                                }]
                                                                        }]
                                                                }]
                                                    }
                                        if cont_lin == 2:
                                            valor1 = driver.find_element_by_xpath('//*[@class="grafico"][2]/div/div/div/table/tbody/tr[2]/td[1]').text
                                            valor11 = driver.find_element_by_xpath('//*[@class="grafico"][2]/div/div/div/table/tbody/tr[2]/td[2]').text
                                            grupo = {
                                                        "pesquisador":
                                                        [
                                                            {
                                                                "identificacao":
                                                                [
                                                                    {
                                                                        "pesquisador": nome, 
                                                                        "producao":
                                                                        [
                                                                            {
                                                                                "ano": valor_ano,
                                                                                valor1: valor11
                                                                            }
                                                                        ]
                                                                    }
                                                                ]
                                                            }
                                                        ]
                                                    }
                                    elif cont_tabs == 0:
                                        nome = nomes[s]
                                        nao_prod = driver.find_element_by_xpath('//*[@class="sub_tit_form"]/b').text
                                        grupo = {
                                                    "pesquisador":
                                                    [
                                                        {
                                                            "identificacao":
                                                            [
                                                                {
                                                                    "pesquisador": nome, 
                                                                    "producao":
                                                                    [
                                                                        {
                                                                            "ano": valor_ano,
                                                                            "Situacao": nao_prod
                                                                        }   
                                                                    ]
                                                                }
                                                            ]
                                                        }
                                                    ]
                                                }
                                    producaoPesquisadores.append(grupo)
                                    j = j - 1
                                s = s + 1     
                            else:
                                s = s + 1    
                        else:
                            s = s + 1
                dataGrupo = {
                    "grupo": [
                        {
                            "identificacao":{
                                "nome": grupo_nome,
                                "situacao": situacao_grupo,
                                "anoformacao": ano_formacao,
                                "lider_es": [ lid_grupo ],
                                "area_predominante": area_predom,
                                "istituicao": instituicao,
                                "espelho_grup": espelho_link,
                            },
                            "endereco": {
                                "UF": uf
                            },
                            "recursos_humanos": {
                                "pesquisadores_titulacao": [ pesquisadores ],
                                "dados_producao": [ producaoPesquisadores ]
                            },
                            "estudantes": [ estudantes ],
                            "total": {
                                "pesquisadores": {
                                    "ativos": cont_pesq,
                                    "egressos": cont_pesq_egress
                                },
                                "alunos": {
                                    "ativos": cont_alun,
                                    "egressos": cont_alun_egress
                                }
                            }
                        }
                    ]
                }
                ##dadossss.append(dataGrupo)
                print('Gravando dados nos arquivos')
                # Enviando os dados ao arquivo "data.json"(ATUALIZANDO O ARQUIVO COM NOVOS DADOS)
                with open('grupos.json', 'a', encoding='utf-8') as f:
                    json.dump(dataGrupo, f, ensure_ascii=False, indent=4)
                print('Dados gravados com sucesso!!')
                    
                print("Total de abas :", len(driver.window_handles))
                m = len(driver.window_handles)
                while m > 2:
                    driver.switch_to.window(driver.window_handles[m-1])
                    driver.close()
                    m = m - 1
                driver.switch_to.window(driver.window_handles[1])
                driver.close()
                driver.switch_to.window(driver.window_handles[0])
                print("Dados do grupo coletados...")
                driver.execute_script("window.scrollTo(2,document.body.scrollHeight)")
                dadosContato = []
                pesquisadores = []
                estudantes = []
                y = y + 1
        i = i + 1
    
buscaGrupo()


