# Calculadora Financeira

Este repositório faz parte do projeto para a disciplina de Matemática Discreta do curso de Engenharia de Computação do IPRJ - UERJ.

Mais detalhes sobre o projeto podem ser vistos [aqui]().

![Calculadora Financeira em funcionamento]()

# Sobre o Projeto

Optou-se pela utilização do framework [Qt](https://www.qt.io/) para a criação da interface gráfica.

O arquivo "calculadora-financeira-gui.ui", criado visualmente através da ferramenta [Qt Creator](https://www.qt.io/download-qt-installer), contém todas as informações visuais para a instanciação dos elementos gráficos (tipo de elemento, posicionamento, propriedades, etc).

O arquivo "calculadora-financeira.py" contém a lógica principal do programa, bem como o código responsável por carregar o arquivo de informações dos elementos visuais "calculadora-financeira-gui.ui" e também a associação da lógica do programa com os elementos gráficos.

# Como Utilizar Este Repositório

Para utilizar este repositório é necessário que se tenha instalado python >= 3.6. Os comandos abaixo farão o necessário para a instalação das dependências e execução do programa.

```
pip install -r requirements.txt
python calculadora-financeira.py
```

Caso esteja com pressa...

```
make
```
