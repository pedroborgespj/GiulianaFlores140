Feature: Comprar Produto

    Scenario: Criacao de usuario
        Given que acesso o site Giuliana Flores
        When acesso a pagina de cadastro
        And preencho os campos de cadastro com nome completo Levi Jorge Hugo Ribeiro e cpf 842.457.325-04 e email levi.jorge.ribeiro@iblojas.com.br e senha 2QOEZxRQPX e cep 84052-420 e numero do endereco 370 e numero de telefone 42984729027
        Then o cadastro é realizado com sucesso para o usuario Levi
    
    Scenario: Login positivo
        Given que acesso o site Giuliana Flores
        When acesso a pagina de login
        And preencho os campos de email levi.jorge.ribeiro@iblojas.com.br e senha 2QOEZxRQPX
        Then o login do usuário Levi é realizado com sucesso

    Scenario Outline: Login negativo
        Given que acesso o site Giuliana Flores
        When acesso a pagina de login
        And preencho os campos de email <email> e senha <senha>
        Then exibe a <mensagem> de erro no login

        Examples:
        | id | email                             | senha         | mensagem                               |
        | 01 | levi.jorge.ribeiro@iblojas.com.br | laranja123    | e-mail ou senha inválidos!             |
        | 02 |                                   | 2QOEZxRQPX    | Verifique o E-mail ou CPF digitado!    |
        | 03 | juca@email.com                    | 2QOEZxRQPX    | e-mail ou senha inválidos!             |
    
    Scenario: Compra de produto pelo banner
        Given que acesso o site Giuliana Flores
        When coloco o primeiro item do banner no carrinho
        And finalizo a compra na página do carrinho
        Then sou direcionado para a página de login