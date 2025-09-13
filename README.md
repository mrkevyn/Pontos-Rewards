# 🎯 Automação para Pontos Microsoft Rewards  

Este projeto é um script em **Python** que automatiza pesquisas no **Bing** utilizando o **Selenium WebDriver** com o navegador **Microsoft Edge**, ajudando a acumular **pontos Microsoft Rewards** de forma prática e automática.  

## 🚀 Funcionalidades
- Abre o **Microsoft Edge** via WebDriver.  
- Realiza pesquisas automáticas no **Bing**.  
- Aguarda entre pesquisas para simular comportamento humano.  
- Fecha o navegador ao final do processo.  

## 🛠️ Tecnologias
- [Python 3](https://www.python.org/)  
- [Selenium](https://www.selenium.dev/)  
- [Microsoft Edge WebDriver](https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/)  

## 📋 Como usar
Instale as dependências:

pip install selenium


Baixe o msedgedriver.exe compatível com a versão do seu Edge e ajuste o caminho no script:

EDGE_DRIVER_PATH = r"C:\Users\SeuUsuario\Documents\msedgedriver.exe"

Execute o script:
python pesquisa.py
