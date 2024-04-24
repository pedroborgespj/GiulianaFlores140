# Projeto de Testes Automatizados com Selenium WebDriver e Pytest

Este projeto consiste na criação de scripts de teste automatizados utilizando o Selenium WebDriver em conjunto com a biblioteca Pytest para interagir com o site www.giulianaflores.com.br. O objetivo é validar diferentes funcionalidades do site, desde a criação de usuário até o fluxo de compra a partir de um banner na página inicial.

## Scripts de Teste

### 1. Criação de Usuário
Este script tem como objetivo automatizar o processo de criação de um novo usuário no site. Serão inseridos dados válidos nos campos obrigatórios do formulário de cadastro e verificado se o usuário é criado com sucesso.

### 2. Login Positivo
Neste script, o objetivo é autenticar um usuário já cadastrado no site com credenciais válidas. Serão inseridos um nome de usuário e senha corretos, e verificado se o login é realizado com sucesso.

### 3. Login Negativo
Este script visa testar o comportamento do sistema ao tentar autenticar um usuário com credenciais inválidas. Serão inseridos um nome de usuário inexistente e/ou uma senha incorreta, e verificado se o sistema exibe a mensagem de erro apropriada.

### 4. Fluxo de Compra a partir de um Banner na Home
O objetivo deste script é simular o processo de compra a partir de um banner na página inicial do site. Será clicado no banner especificado, seguido pela seleção de um produto e finalização da compra, verificando se o processo é concluído com sucesso.

## Pré-requisitos

- Python 3.x
- Selenium WebDriver
- Pytest
- Chrome (ou outro navegador suportado)

## Configuração

1. Instale o Python 3.x em seu ambiente.
2. Instale as dependências do projeto, incluindo o Selenium WebDriver e o Pytest, utilizando o gerenciador de pacotes pip:
```pip install pytest```
```pip install selenium```

## Execução

Para executar os scripts de teste, siga os passos abaixo:

1. Clone este repositório em sua máquina local:
```
git clone https://github.com/pedroborgespj/GiulianaFlores140
```

2. Navegue até o diretório do projeto:
```
cd nome-do-repositorio
```

3. Execute os testes utilizando o Pytest:
```pytest -k "nome_do_arquivo_de_test"```

## Notas

- Certifique-se de que os testes são executados em um ambiente de teste apropriado para evitar impactos no ambiente de produção.
- Este projeto pode ser expandido para incluir mais cenários de teste e funcionalidades do site.
