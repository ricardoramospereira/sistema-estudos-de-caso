# Sistema de Gestão de Estudos de Caso

## Visão Geral
O **Sistema de Gestão de Estudos de Caso** é uma aplicação desktop desenvolvida em Python utilizando a biblioteca PyQt5 para criar interfaces gráficas. O sistema permite gerenciar estudos de caso, adicionando, visualizando, editando e excluindo passos e opções associados. Ele também oferece funcionalidades de busca e filtros para facilitar a navegação entre os estudos.

## Funcionalidades Principais
- **Adicionar Estudo de Caso:** Permite criar um novo estudo de caso com um título único e incluir o primeiro passo e opções associadas.
- **Visualizar Estudos de Caso:** Exibe a lista de estudos de caso existentes, permitindo visualizar todos os passos e opções associados.
- **Excluir Estudos de Caso:** Oferece a opção de excluir um estudo de caso inteiro, incluindo todos os passos e opções relacionados.
- **Excluir Passos:** Permite excluir passos específicos ou todos os passos de um estudo de caso.
- **Busca de Estudos de Caso:** Buscar estudos de caso pelo título, ignorando maiúsculas e minúsculas, e limpar a busca para listar todos os estudos novamente.
- **Destaque de Informações:** Os títulos dos passos e opções são formatados com cores diferenciadas para facilitar a leitura e organização.

## Requisitos
- **Python 3.x**
- **PyQt5:** `pip install PyQt5`
- **SQLite3** (já incluído na maioria das instalações Python)

## Instalação e Configuração

### 1. Clonar o Repositório
```bash
git clone https://github.com/seu-usuario/sistema-estudos-de-caso.git
cd sistema-estudos-de-caso

2. Instalar Dependências

pip install -r requirements.txt

3. Configurar Banco de Dados

Verifique se o arquivo db_setup.py está configurado para inicializar o banco de dados corretamente. Execute-o para criar as tabelas necessárias.

4. Executar a Aplicação

python main.py

Estrutura do Projeto

sistema-estudos-de-caso/
│
├── database/
│   ├── db_setup.py
│   ├── db_operations.py
│
├── interface.py
├── main.py
├── requirements.txt
└── README.md

-database/: Diretório que contém os scripts relacionados ao banco de dados SQLite.
-interface.py: Contém a lógica da interface gráfica utilizando PyQt5.
-main.py: Script principal para iniciar a aplicação.
-requirements.txt: Arquivo que lista todas as dependências necessárias para o projeto.
-README.md: Documentação e instruções do projeto.

Criaçao de Executável

Para Windows:

1. Instalar PyInstaller:

pip install pyinstaller

2. Criar o Executável:

pyinstaller --onefile --windowed main.py


Personalização do Ícone
Para personalizar o ícone da aplicação, use o parâmetro --icon ao criar o executável com o PyInstaller:

Windows: Utilize ícones no formato .ico.
Linux: Utilize ícones no formato .png ou .xpm.

pyinstaller --onefile --windowed --icon=icone.ico main.py

(O executável será gerado na pasta dist/.)

Para Linux:

1. Instalar PyInstaller:

pip install pyinstaller

2. Criar o Executável:


pyinstaller --onefile main.py

Personalização do Ícone
Para personalizar o ícone da aplicação, use o parâmetro --icon ao criar o executável com o PyInstaller:

pyinstaller --onefile --icon=icone.png main.py

Configurar Ícone na Interface PyQt5

Adicione a seguinte linha no seu código, antes de iniciar a aplicação:

app.setWindowIcon(QIcon('icone.png'))  # Substitua por 'icone.ico' no Windows

Considerações Finais

Este projeto foi criado para facilitar a gestão de estudos de caso, permitindo uma organização eficiente e visualmente clara das informações. O código foi modularizado para facilitar futuras expansões e manutenções.





