# IFPE - Instituto Federal de Pernambuco
# Curso: Análise e Desenvolvimento de Sistemas
# Disciplina: Introdução à Programação
# Docente: Rodrigo Cesar Lira da Silva
# Discente: Thiago da Mota Vilela (20211ADSPL0140)
# E-mail: tmv@discente.ifpe.edu.br
# Avaliação da 2ª Unidade - Data: 28 de julho de 2021

# Projeto: Calculadora do Custo Unitário Básico de Construção (CUB).
# Funcionalidades Extras: Graphical User Interface; Arquivo Executável.
# Módulo: PyQt5 - Programa: Qt Designer

# Imports: 
from PyQt5 import uic,QtWidgets
from PyQt5 import QtCore
from PyQt5.QtWidgets import QMessageBox

import modulefinder

import webbrowser   # importa a função para abrir o link em uma página do navegador.
import sys          # importa definições de sistema para finalizar a aplicação.
import Resource_rc  # Importa as imagens da Aplicação.

# Funções:
def funcao_tipo():  # Verifica e define o Tipo de Projeto selecionado pelo usuário.
    opcao = ""
    if formulario.rb_residencial_baixo.isChecked():
        opcao = "Residencial - Padrão Baixo\nCUB/m²: R$ 1865.81"
    elif formulario.rb_residencial_normal.isChecked():
        opcao = "Residencial - Padrão Normal\nCUB/m²: R$ 2206.60"
    elif formulario.rb_residencial_alto.isChecked():
        opcao = "Residencial - Padrão Alto\nCUB/m²: R$ 2837.63"
    elif formulario.rb_cal_normal.isChecked():
        opcao = "Comercial Andares Livres\nPadrão Normal\nCUB/m²: R$ 2092.01"
    elif formulario.rb_cal_alto.isChecked():
        opcao = "Comercial Andares Livres\nPadrão Alto\nCUB/m²: R$ 2236.02"
    elif formulario.rb_csl_normal.isChecked():
        opcao = "Comercial Salas e Lojas\nPadrão Normal\nCUB/m²: R$ 1807.94"
    elif formulario.rb_csl_alto.isChecked():
        opcao = "Comercial Salas e Lojas\nPadrão Alto\nCUB/m²: R$ 1980.54"
    elif formulario.rb_galpao_industrial.isChecked():
        opcao = "Galpão Industrial\nCUB/m²: R$ 1016.76"
    elif formulario.rb_residencia_popular.isChecked():
        opcao = "Residencia Popular\nCUB/m²: R$ 1703.34"
    formulario.lbl_projeto_selecionado.setText(opcao)  # Exibe o Tipo de Projeto selecionado pelo usuário.

def funcao_calcular():  # Verifica qual Tipo de Projeto foi selecionado e Calcula o Custo Unitário Básico de Construção (Custo Global da Obra).
    valor_m2 = 0        # Variável para definir o valor do m² de acordo com o tipo de projeto selecionado pelo usuário.
    if formulario.rb_residencial_baixo.isChecked():
        valor_m2 = 1865.81
    elif formulario.rb_residencial_normal.isChecked():
        valor_m2 = 2206.60
    elif formulario.rb_residencial_alto.isChecked():
        valor_m2 = 2837.63
    elif formulario.rb_cal_normal.isChecked():
        valor_m2 = 2092.01
    elif formulario.rb_cal_alto.isChecked():
        valor_m2 = 2236.02
    elif formulario.rb_csl_normal.isChecked():
        valor_m2 = 1807.94
    elif formulario.rb_csl_alto.isChecked():
        valor_m2 = 1980.54
    elif formulario.rb_galpao_industrial.isChecked():
        valor_m2 = 1016.76
    elif formulario.rb_residencia_popular.isChecked():
        valor_m2 = 1703.34
    
    # Conversões e Cálculo Final:
    ledt_valor_area_m2 = formulario.txt_valor_area_m2.text()  # Atribui o QLineEdit para uma variável.
    ledt_valor_area_m2 = ledt_valor_area_m2.replace(',','.')  # Substitui a virgula por ponto para efeito de cálculo.
    area_m2 = float(ledt_valor_area_m2)     # Cria-se uma nova variável e atribui o type float a variável anterior.
    cub_m2 = area_m2 * valor_m2             # Calcula o Custo Unitário Básico de Construção (Custo Global da Obra).
    cub = str(f"R$:{cub_m2:,.2f}").replace(',','.')           # Cria-se uma variável, tranformando-a em type String e executa formatação.
    formulario.lbl_custo_final.setText(cub) # Coloca o resultado final na Label 'lbl_custo_final'.
    
def funcao_mensagem(texto):  # Janela com Mensagem de Erro.
    mensagem = QMessageBox()                    # QMessageBox: A execução do código da aplicação é interrompida até que a mensagem seja fechada.
    mensagem.setWindowTitle("Mensagem de Erro") # Coloca o Título da janela de Erro.
    mensagem.setText(texto)                     # Escreve qual mensagem de erro será exibida na caixa.
    
    mensagem.exec_()                            # Executa a janela com a mensagem de erro para o usuário.
    formulario.txt_valor_area_m2.setText("")    # Após o erro limpa o campo de m² digitado pelo usuário.

def funcao_validar():  # Valida as eventos do usuário (Regras da Aplicação)
    # Checa se existe algum Radio Button selecionado pelo usuário:
    if formulario.rb_residencial_baixo.isChecked() or formulario.rb_residencial_normal.isChecked() or formulario.rb_residencial_alto.isChecked() or formulario.rb_cal_alto.isChecked() or formulario.rb_csl_normal.isChecked() or formulario.rb_csl_alto.isChecked() or formulario.rb_galpao_industrial.isChecked() or formulario.rb_residencia_popular.isChecked():
        
        ledt_valor_area_m2 = formulario.txt_valor_area_m2.text()  # Atribui o QLineEdit para uma variável.
        ledt_valor_area_m2 = ledt_valor_area_m2.replace(',','.')  # Substitui a virgula por ponto para efeito de cálculo (Evita uma entrada inválida)
        
        # Try / Except: Tratamento de exceções.
        # Utilizada para validar qualquer valor diferente de float (ponto flutuante) na variável do QLineEdit:
        try: # Teste:
            if ledt_valor_area_m2 == '':                                            # Se o usuário deixar a caixa do QLineEdit em vazia.
                texto = "Por favor digite o valor da área do projeto (m²)."         # Atribui na variável texto o que vai ser projetado na janela de erro.
                funcao_mensagem(texto)                                              # Executa a Função Mensagem e exibe a mensagem de erro.
                
            elif float(ledt_valor_area_m2) <= 0:                                    # Se o usuário digitar um valor menor ou igual a zero.
                texto = "Por favor digite um valor da área do projeto (m²) maior do que zero."
                funcao_mensagem(texto)                                              # Executa a Função Mensagem e exibe a mensagem de erro.
                
            elif float(ledt_valor_area_m2):                                         # Se o usuário digitar um float, executa a Função Calcular.                                      
                funcao_calcular()
                
        except Exception:                                                           # Algo diferente das anteriores, exemplo: Letras, Caracteres Especiais.
            texto = "Você digitou um valor inválido, por favor tente novamente."    # Atribui na variável texto o que vai ser projetado na janela de erro.
            funcao_mensagem(texto)                                                  # Executa a Função Mensagem e exibe a mensagem de erro.

    else:                                                    # Caso o usuário não selecione o Radio Button do Tipo de Projeto.
        texto = "Por favor selecione o Tipo de Projeto."     # Atribui na variável texto o que vai ser projetado na janela de erro.
        funcao_mensagem(texto)                               # Executa a Função Mensagem e exibe a mensagem de erro.
              
def funcao_site():  # Carrega o site do IFPE em uma janela (Navegador Padrão).
    webbrowser.open_new_tab('https://www.ifpe.edu.br/campus/paulista')   # Abre a url em uma nova página ("guia") do navegador padrão do usuário.

def funcao_limpar(): # Executa a limpeza para todas as marcações feitas pelo usuário na tela.
    formulario.txt_valor_area_m2.setText("")                 # Substitui o texto do campo área (m²) para vazio.
    formulario.lbl_projeto_selecionado.setText("")           # Substitui o texto do campo Tipo de Projeto selecionado para vazio.
    formulario.lbl_custo_final.setText("")                   # Substitui o texto do campo resultado final para vazio.
    
    # Limpando o Radio Buttons do Tipo de Projeto selecionado pelo usuário:
    formulario.rb_residencial_baixo.setAutoExclusive(False)
    formulario.rb_residencial_baixo.setChecked(False)
    formulario.rb_residencial_baixo.setAutoExclusive(True)
    
    formulario.rb_residencial_normal.setAutoExclusive(False)
    formulario.rb_residencial_normal.setChecked(False)
    formulario.rb_residencial_normal.setAutoExclusive(True)
    
    formulario.rb_residencial_alto.setAutoExclusive(False)
    formulario.rb_residencial_alto.setChecked(False)
    formulario.rb_residencial_alto.setAutoExclusive(True)

    formulario.rb_cal_normal.setAutoExclusive(False)
    formulario.rb_cal_normal.setChecked(False)
    formulario.rb_cal_normal.setAutoExclusive(True)

    formulario.rb_cal_alto.setAutoExclusive(False)
    formulario.rb_cal_alto.setChecked(False)
    formulario.rb_cal_alto.setAutoExclusive(True)

    formulario.rb_csl_normal.setAutoExclusive(False)
    formulario.rb_csl_normal.setChecked(False)
    formulario.rb_csl_normal.setAutoExclusive(True)

    formulario.rb_csl_alto.setAutoExclusive(False)
    formulario.rb_csl_alto.setChecked(False)
    formulario.rb_csl_alto.setAutoExclusive(True)

    formulario.rb_galpao_industrial.setAutoExclusive(False)
    formulario.rb_galpao_industrial.setChecked(False)
    formulario.rb_galpao_industrial.setAutoExclusive(True)

    formulario.rb_residencia_popular.setAutoExclusive(False)
    formulario.rb_residencia_popular.setChecked(False)
    formulario.rb_residencia_popular.setAutoExclusive(True)
    
def funcao_sair(): # Encerra a aplicação:
    formulario.window().close()

# Importa arquivo '.ui' criada na ferramenta de designer do PyQt5 e conecta widgets da GUI aos métodos em Python.
app=QtWidgets.QApplication([])
formulario=uic.loadUi("QtDesigner.ui")

# Radio Buttons:
# Carrega todos os eventos de click do Tipo de Projeto.
formulario.rb_residencial_baixo.clicked.connect(funcao_tipo)
formulario.rb_residencial_normal.clicked.connect(funcao_tipo)
formulario.rb_residencial_alto.clicked.connect(funcao_tipo)
formulario.rb_cal_normal.clicked.connect(funcao_tipo)
formulario.rb_cal_alto.clicked.connect(funcao_tipo)
formulario.rb_csl_normal.clicked.connect(funcao_tipo)
formulario.rb_csl_alto.clicked.connect(funcao_tipo)
formulario.rb_galpao_industrial.clicked.connect(funcao_tipo)
formulario.rb_residencia_popular.clicked.connect(funcao_tipo)

# PushButtons:
formulario.btn_calcular.clicked.connect(funcao_validar) # Evento de Clique do Botão Calcular, em seguida ele validará os dados do usuário.
formulario.btn_ifpe.clicked.connect(funcao_site)   # Evento de Clique no Botão (Logo IFPE), em seguida executa a Função Site.

# MenuBar:
formulario.actionlimpar.triggered.connect(funcao_limpar) # Executa a Função Limpar para todas as marcações feitas pelo usuário na tela.
formulario.actionSair.triggered.connect(funcao_sair) # Executa a Função Sair e encerra o programa.

# Aplicação:
formulario.show() # Exibe a Aplicação.
app.exec() # Executa a Aplicação.