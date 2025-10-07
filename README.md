# Sistema de gestão de produtos 🍶

Sistema insperado em um cadastro de itens de supermercado para gestão de itens/produtos cadastrados, servindo como base para um sistema de inventário de itens.
Nesse cenário o gerente tem controle total sobre tudo que é cadastrado, atualizado, listado e deletado.

O projeto tem como base 2 dos principios do solid:
* **Princípio da Responsabilidade Única**

* **Princípio da Inversão de Dependência**


### Descrição de funcionamento do sistema de gestão:

Feito para usar de forma fácil as funções básicas do **CRUD** do Django Rest Framework e aliado a isso a segurança que o próprio DRF nos proporciona.

* Cadastrar produtos com persistência vinculados a um usuário que o cadastrou
* Listar produtos que foram cadastrados pelo usuário
* Atualizar de forma parcial('PATCH') ou total('PUT') o cadastro vinculado ao usuário
* Deletar um item especifico do usuário que o cadastrou no sistema.

Usando o próprio sistema de autenticação e token's do Django que garante uma camada de segurança a nossa aplicação, somente um usuário validado e logado pode ter acesso ao sistema.

### Regra de Negócios:

* O preço do produto: Não pode ser negativo ou igual a zero, validação feita na service.

* Data de validade: Não podendo ser retroativa a data de cadastro, também no service.

*  Disponibilidade de estoque: Feito com base na criação do produto, quando o estoque é lançado, a disponibilidade é alterada de forma que se o item estiver positivo no estoque a flag é True, casa não é False, e o item fica indisponível.

### Desafios

As regras de negócio elevam para outro nível a robustez e complexidade do projeto, percebi que a base em si é bem simples, mas as regras de negócios são os responsáveis criar as leis do sistema, a forma como os dados são processados e a forma como são disponibilizados para **view** após a requisição.

