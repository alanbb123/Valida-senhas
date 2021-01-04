<h1 align="center">
    Verificador de senha
</h1>

# Índice
- [Sobre](#sobre)
- [Tecnologias Utilizadas](#-tecnologias-utilizadas)
- [Clonando o projeto](#-clonando-o-projeto)
- [Instalando Dependências](#instalando-dependências)
    - [Instalando Python 3](#instalando-python-3)
    - [Instalando Pip](#insalando-pip)
    - [Instalando Virtualenv](#instalando-virtualenv)
    - [Instalando Flask](#instalando-flask)
- [Executando Projeto](#executando-projeto)



## 🧾Sobre

O projeto **Verificador de senha** é uma **API** simples que verifica a senha digitada.

O requisito da API é realizar uma validação na senha, atendendo os seguintes requisitos:

 - Nove ou mais caracteres
 - Ao menos 1 dígito
 - Ao menos 1 letra minúscula
 - Ao menos 1 letra maiúscula
 - Ao menos 1 caractere especial
    - Considere como especial os seguintes caracteres: !@#$%^&*()-+
 - Não possuir caracteres repetidos dentro do conjunto

### Obs: Embora eu tenha utilizado o CSS3.0, o foco deste projeto é na execução, deixando um pouco de lado a estilização e focando no escopo do projeto.
---

## 🛠 Tecnologias utilizadas

- [Python 3.9.1](https://www.python.org/)
- [Flask](https://palletsprojects.com/)
- [Pip](https://pypi.org/project/pip/)
- [VirtualEnv](https://pypi.org/project/virtualenv/)
- HTML 5
- CSS 3

---

## 📁 Clonando o projeto

```bash
# Clonar o repositório

    $ git clone https://github.com/alanbb123/verificador_senha.git

```
---

# Instalando dependências
## Instalando Python 3
```bash
    # Para Windows

    https://www.python.org/downloads/

    # Para Linux

        # Verifica se está instalado o Python 3
        $ which python3

        # Verifica a versão do python, caso esteja instalado
        $ python --version

        # Realiza o download via apt-get
        $ sudo apt-get install python3

        # Realiza o download via Yum
        $ sudo yum install python3
```

## Instalando Pip
```bash
 Caso sua versão não possua o pip

    # Para Windows
    https://pypi.org/project/pip

    # Para Linux  via apt-get
    $ sudo apt-get install python3-pip

    # Para Linux via Yum
    $ yum -y install python3-pip
 ```
 ## Instalando Virtualenv
```bash
# Via pip
    pip install virtualenv
```
    

 ## Instalando Flask
```bash
# Instalando via Pip

    $ pip install flask
```
---
<br>

# Executando Projeto

```bash
# No prompt de comando
    cd /backend-challenge\Valida-senhas\venv\Scripts

# Agora execute o arquivo activate
    C:\Users\backend-challenge\Valida-senhas\venv\Scripts>activate

# Com o (venv) ativado, vá até a pasta onde o arquivo python está
    (venv) C:\Users\Desktop\backend-challenge\Valida-senhas\venv\api>

# Execute o arquivo
    (venv) C:\Users\Desktop\backend-challenge\Valida-senhas\venv\api>python verificador_senha.py
```

<h1 align="center">
    <img src="https://ik.imagekit.io/alanbertoldo/cmd_8IsRwHHfjR.png">
</h1>

<h1 align="center">
    <img src="https://ik.imagekit.io/alanbertoldo/run2_00_00_00-00_00_30_1_fJCQAJ3fn.gif">
</h1>

<h1 align="center">
    <img src="https://ik.imagekit.io/alanbertoldo/Run1_00_00_00-00_00_30_2_IzYk8I_BCm.gif">
</h1>
