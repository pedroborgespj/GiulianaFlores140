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