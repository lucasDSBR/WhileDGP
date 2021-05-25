<h1 align="center">
  <img alt="logowhiledgp" src="logo.png" />
</h1>
<p align="justify">O WhileDGP foi um projeto desenvolvido visando a necessidade da Universidade da Integração internacional da Lusofonia Afro-brasileira em avaliar a produção científica tranto dos grupos de pesquisas como de seus pesquisadores. Mediante tal necessidade, a aplicação foi desenvolvida principalmente para coletar informações(de produção) de cada grupo de pesquisa da instituição registrados no <a href="http://lattes.cnpq.br/web/dgp">Diretório Geral dos Grupos de Pesquisa no Brasil/CNPq</a>. Tal aplicação faz a coleta de informações básicas de cada grupo como por exemplo: Nome do grupo, Situacao, Ano de formação, seus lideres, Área predominante, Unidade Federativa, Instituição e Total de pesquisadores e alunos ativos ou egressos do grupo. E também informações de cada pesquisador do grupo, como por exemplo: Trabalhos Publicados em Anais de Evento, Resumos Publicados em Anais de Eventos, Artigos Completos Publicados em Periódicos, Livro ou Capítulo, Apresentações de trabalho e entre outras informações. Além disso, o WhileDGP lhe dá a possibilidade de coletar informações de todos os anos e de anos específicos(em relação aos pesquisadores dos grupos).</p>
<p align="justify">Algumas das informações coletadas já foram estudadas e publicadas em uma página específica no site da <a href="http://proppg.unilab.edu.br/">PRÓ-REITORIA DE PESQUISA E PÓS-GRADUAÇÃO</a> da UNILAB entitulada com <a href="http://proppg.unilab.edu.br/index.php/painel-indicadores/">PAINEL DE INDICADORES</a>
<h2 align="center">Desenvolvedores:</h2>
<table align="center">
  <tr>
    <td align="center">
      Lucas da Silva Maciel<br><img src="https://img.shields.io/static/v1?label=Discente&message=UNILAB&color=blue&style=<STYLE>&logo=<LOGO>">
    </td>
    <td align="center">
      Allberson Bruno de Oliveira Dantas<img src="https://img.shields.io/static/v1?label=Docente&message=UNILAB&color=blue&style=<STYLE>&logo=<LOGO>">
    </td>
     <td align="center">
       Renato Farias de Paiva<br><img src="https://img.shields.io/static/v1?label=TAE&message=UNILAB&color=blue&style=<STYLE>&logo=<LOGO>">
    </td>
     <td align="center">
       Pedro Bruno Silva Lemos<br><img src="https://img.shields.io/static/v1?label=TAE&message=UNILAB&color=blue&style=<STYLE>&logo=<LOGO>"></a>
    </td align="center">
    <td align="center">
       Antonio Paulo Uamba<br><img src="https://img.shields.io/static/v1?label=Discente&message=UNILAB&color=blue&style=<STYLE>&logo=<LOGO>">
    </td>
  </tr>
</table>
<hr>
<h1>Sobre a Aplicação(DEV):</h1>
<p align="justify">A aplicação foi desenvolvida totalmente na linguagem de programação Python. Ou seja, para que tal funcione de uma forma automatizada, optamos desenvolve-la nessa linguagem. Além disso, foi utilizada a biblioteca PySimpleGUI, para que fosse possível se desenvolvida uma aplicação possível de ser utilizada por qualquer tipo de usuário(sem que precisasse realizar comandos no prompt). Outas bibliotecas também foram usadas, mas não irei comenta-las aqui. Ainda, para que tal aplicação funcionasse, foi necessário utilizar um WEBDRIVER da google, para que fosse possível que o WhileDGP funcionasse no Google Chrome.</p>
<hr>
<h1>Como a aplicação funciona(DEV):</h1>
# 1) WhileDGP Entra no site da DGP/CNPq;<br>
# 2) Realiza a busca dos grupos de pesquisa;<br>
# 3) Após encontrar os grupos, ele conta o total de grupos;<br>
# 4) Após isso, ele começa a realizar a coleta das informações dos grupos e de seus pesquisadores;<br>
# 5) Após realizar a coleta de todas as informações, o WhileDGP salva todos os dados em seus arquivos específicos. Ou seja, os dados dos grupos são salvos em uma arquivos .JSON e o dos pesquisadores também são salvos em outro arquivos .JSON.
