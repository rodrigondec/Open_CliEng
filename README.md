 # Open Clineng

Software para gerenciamento de engenharia clínica.

Veja nossa [wiki](https://github.com/rodrigondec/Open_Clineng/wiki). E se você pretende ajudar no desenvolvimento, leia e siga nosso [arquivo de contribuição](./CONTRIBUTING.md).

# Instruções

> **Atenção***: as configurações de desenvolvimento são instáveis e se atualizando constantemente, não sendo adequadas para produção

## Configurando ambiente de desenvolvimento

- Instale os seguintes programas e certifique-se de que as **versões** usadas estão sempre corretas e os serviços estão **ativos**:
    - [Python 3.6.3](https://www.python.org/downloads/release/python-363) (mas provavelmente qualquer versão acima de 3.3 irá servir)
        - Tenha certeza de que seu Python3 tem o ```pip``` adequado a ele (no Linux, às vezes é pip3), com módulo ```virtualenv``` instalado
    - [PostgreSQL](https://www.postgresql.org/download/) recente
- Prepare o ambiente virtual:
    - Crie banco de dados chamado Open_Clineng
    - Edite as variáveis de prefixo ```DB_``` no arquivo [config.py](./Open_Clineng/config.py) com os dados de instalação do seu PostgreSQL
    - Crie um arquivo vazio ```logs/error.log```
    - Crie o ambiente virtual via console usando ```python -m venv env```
- Ative o ambiente virtual (e você irá **precisar refazer este único passo sempre que executar usar o sistema**):
    - No Windows, execute no prompt (cmd): ```env\Scripts\activate.bat```
    - No Unix ou MacOS, execute no terminal (bash): ```source env/bin/activate```
- Rode o ```pip``` para instalar as dependências do sistema com ```pip install -r requirements.txt```.
- Termine de configurar o banco de dados adicionando as tabelas dele através do console do seu SO:
    - Rode ```python manage.py makemigrations```: Cria uma migração com nase nas alterações feitas dos models
    - Rode ```python manage.py migrate```: Altera o banco de dados com base nas migrações criadas
    
## Rodando o servidor

Considerando que todo o ambiente foi corretamente instalado e configurado, sempre que for executar o sistema:

- Execute novamente o passo de ativação do ambiente virtual
- Inicie o servidor com ```python manage.py runserver``` e leia o output que lhe dirá em qual endereço IP e porta a aplicação está rodando
    - Se for "0.0.0.0" significa que está aberto para toda sua rede interna, e você deve encontrar seu IP público (no Linux, use ```ifconfig```)
