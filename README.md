# Agenda Project

## Descrição
O **Agenda Project** é uma aplicação web desenvolvida com o framework Django. Seu objetivo é oferecer funcionalidades para gerenciar contatos de maneira eficiente. A aplicação inclui uma interface intuitiva e recursos como gerenciamento de usuários e organização de dados em uma agenda.

## Funcionalidades
- **Gerenciamento de Contatos:** Criação, edição e exclusão de contatos.
- **Integração com Mídias:** Suporte ao uso de imagens (via Pillow).

## Tecnologias Utilizadas
- **Python**: Linguagem de programação principal.
- **Django 5.1.4**: Framework principal para desenvolvimento web.
- **HTML e CSS**: Linguagens para estruturação e estilização da interface do usuário.
- **Pillow 11.0.0**: Biblioteca para manipulação de imagens.
- **Faker 33.1.0**: Ferramenta para gerar dados fictícios (ex.: contatos).).

## Configuração do Projeto
1. Clone este repositório:

   ```bash
   git clone https://github.com/vitorgsantoss/agenda-project.git
   cd agenda-project
   ```

2. Instale as dependências listadas no arquivo `requirements.txt`.
   
Certifique-se de que você tem o Python 3.10 ou superior instalado. Em seguida, instale as dependências com o comando:

```bash
pip install -r requirements.txt
```

Arquivo `requirements.txt`:
```
asgiref==3.8.1
Django==5.1.4
Faker==33.1.0
pillow==11.0.0
python-dateutil==2.9.0.post0
six==1.17.0
typing_extensions==4.12.2
```


4. Execute as migrações para configurar o banco de dados:


   ```bash
   python manage.py migrate
   ```

5. Criar contatos fictícios:
   ```bash
   python utils/data_faker.py
   ```

7. Inicie o servidor de desenvolvimento:

   ```bash
   python manage.py runserver
   ```

8. Acesse a aplicação no navegador:

   ```
   http://127.0.0.1:8000
   ```

## Estrutura do Projeto
- **base_static/**: Arquivos estáticos globais (CSS, JS, etc.).
- **base_templates/**: Templates reutilizáveis para renderização das páginas.
- **contact/**: Gerenciamento de funcionalidades relacionadas a contatos.
- **project/**: Configurações principais do Django.
- **utils/**: Funções auxiliares usadas em toda a aplicação.

## Contato
Criado por [Vitor Santos](https://github.com/vitorgsantoss). 
E-mail: vg452004@gmail.com. 
Sinta-se à vontade para entrar em contato em caso de dúvidas ou sugestões.
