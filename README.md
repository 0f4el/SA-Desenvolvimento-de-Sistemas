# RACK+ - Sistema de Gerenciamento de Racks Inteligentes

Repositorio:
https://github.com/0f4el/SA-Desenvolvimento-de-Sistemas.git

---

## Sobre o Projeto

O RACK+ e uma aplicação web desenvolvida em Django para auxiliar no gerenciamento de racks inteligentes utilizados em instituicões educacionais.

A proposta do sistema e facilitar o monitoramento de salas, racks e notebooks, permitindo visualizar quais equipamentos estão disponiveis, em uso, ausentes ou em manutenção.

O projeto foi desenvolvido para a SA (Situação de Aprendizagem) de Desenvolvimento de Sistemas Web e foi se utilizado e adaptado do modelo da SA anterior do Rack+.

---

## Funcionalidades Implementadas

* Cadastro e login de usuários
* Protecão de páginas por login
* Homepage com listagem de salas cadastradas
* CRUD completo de salas
* CRUD completo de racks inteligentes
* CRUD completo de notebooks
* Visualização dos racks por sala
* Interface visual dos slots do rack
* Indicadores por cor para o status dos notebooks
* Mensagens de feedback para cadastro, edição e exclusão
* API REST com Django REST Framework
* Rotas da API protegidas por autenticação
* Serializers usando ModelSerializer
* Validações de campos obrigatórios, tags únicas e slots ocupados

---

## Tecnologias Utilizadas

* Python 3
* Django 6
* Django REST Framework
* SQLite
* HTML
* CSS
* JS
* Bootstrap

---

## Models Principais

### Cadastro

Model de usuário do sistema, baseado no `AbstractUser` do Django.

Campos principais:

| Campo | Descricão |
| ----- | --------- |
| username | Nome de usuário para login |
| email | E-mail do usuário |
| nome | Nome completo |
| cpf | CPF único |
| instituição | Instituição do usuário |
| cargo | Professor, tutor, gestor ou aluno |

### Sala

Representa uma sala da instituição onde podem existir racks inteligentes.

Campos principais:

| Campo | Descrição |
| ----- | --------- |
| nome | Nome da sala |
| bloco | Bloco da instituição |
| número | Número da sala |
| andar | Andar da sala |

### Rack

Representa um rack inteligente localizado em uma sala.

Campos principais:

| Campo | Descrição |
| ----- | --------- |
| identificador | Codigo único do rack |
| sala | Sala onde o rack esta localizado |
| status | Ativo, manutenção ou inativo |
| quantidade_slots | Quantidade de slots disponiveis |
| temperatura | Temperatura registrada no rack |

### Notebook

Representa um notebook conectado a um slot de um rack.

Campos principais:

| Campo | Descrição |
| ----- | --------- |
| tag | Identificação única do notebook |
| modelo | Modelo do notebook |
| rack | Rack onde o notebook está conectado |
| numero_slot | Slot ocupado no rack |
| status | Disponivel, em uso, manutenção ou ausente |
| ultima_atualização | Data da ultima atualização |

---

## Configuracão do Ambiente

### 1. Clonar o repositorio

```bash
git clone https://github.com/0f4el/SA-Desenvolvimento-de-Sistemas.git
cd SA-Desenvolvimento-de-Sistemas
```

---

### 2. Criar o ambiente virtual

```bash
python -m venv venv
```

---

### 3. Ativar o ambiente virtual

#### Windows - CMD

```bash
venv\Scripts\activate
```

#### Windows - PowerShell

```bash
venv\Scripts\Activate.ps1
```

#### Linux / Mac

```bash
source venv/bin/activate
```

---

### 4. Instalar as dependencias

```bash
pip install -r requirements.txt
```

---

### 5. Aplicar as migrations

```bash
python manage.py migrate
```

---

### 6. Criar um superusuario

```bash
python manage.py createsuperuser
```

---

## Executando o Projeto

```bash
python manage.py runserver
```

A aplicacão estara disponivel em:

```text
http://127.0.0.1:8000/
```

---

## Rotas Web

| Rota | Descrição |
| ---- | --------- |
| `/` | Tela de login |
| `/cadastro/` | Cadastro de usuário |
| `/home/` | Homepage com as salas |
| `/salas/nova/` | Cadastro de sala |
| `/salas/<id>/editar/` | Edição de sala |
| `/salas/<id>/excluir/` | Exclusão de sala |
| `/salas/<id>/racks/` | Racks de uma sala |
| `/salas/<id>/racks/novo/` | Cadastro de rack em uma sala |
| `/racks/<id>/editar/` | Edição de rack |
| `/racks/<id>/excluir/` | Exclusão de rack |
| `/racks/<id>/notebooks/` | Notebooks e slots de um rack |
| `/racks/<id>/notebooks/novo/` | Cadastro de notebook em um rack |
| `/notebooks/<id>/editar/` | Edição de notebook |
| `/notebooks/<id>/excluir/` | Exclusão de notebook |

---

## Endpoints da API

As rotas da API exigem que o usuario esteja autenticado.

| Metodo | Rota | Descricão |
| ------ | ---- | --------- |
| GET | `/api/salas/` | Lista todas as salas |
| POST | `/api/salas/` | Cria uma nova sala |
| GET | `/api/salas/<id>/` | Retorna uma sala específica |
| PUT | `/api/salas/<id>/` | Atualiza uma sala |
| DELETE | `/api/salas/<id>/` | Remove uma sala |
| GET | `/api/racks/` | Lista todos os racks |
| POST | `/api/racks/` | Cria um novo rack |
| GET | `/api/racks/<id>/` | Retorna um rack específico |
| PUT | `/api/racks/<id>/` | Atualiza um rack |
| DELETE | `/api/racks/<id>/` | Remove um rack |
| GET | `/api/notebooks/` | Lista todos os notebooks |
| POST | `/api/notebooks/` | Cria um novo notebook |
| GET | `/api/notebooks/<id>/` | Retorna um notebook específico |
| PUT | `/api/notebooks/<id>/` | Atualiza um notebook |
| DELETE | `/api/notebooks/<id>/` | Remove um notebook |

---

## Testando a API

Com o servidor rodando, acesse no navegador:

```text
http://127.0.0.1:8000/api/
```

Como a API esta protegida, primeiro faca login no sistema. Depois disso, as rotas da API poderão ser acessadas pelo navegador usando a interface do Django REST Framework.

Exemplos de dados para teste:

### Criar sala

```json
{
  "nome": "Laboratorio 01",
  "bloco": "A",
  "numero": "101",
  "andar": "1"
}
```

### Criar rack

```json
{
  "identificador": "RA-01",
  "sala": 1,
  "status": "ativo",
  "quantidade_slots": 10,
  "temperatura": "24.50"
}
```

### Criar notebook

```json
{
  "tag": "NT-0001",
  "modelo": "Dell Latitude",
  "rack": 1,
  "numero_slot": 1,
  "status": "disponivel"
}
```

---

## Estrutura do Projeto

```text
SA-Desenvolvimento-de-Sistemas/
├── app/
│   ├── migrations/
│   ├── static/
│   ├── templates/
│   ├── admin.py
│   ├── api_views.py
│   ├── forms.py
│   ├── models.py
│   ├── serializers.py
│   ├── urls.py
│   └── views.py
├── Rackplus/
│   ├── settings.py
│   └── urls.py
├── manage.py
├── requirements.txt
└── README.md
```

---

## Boas Praticas Aplicadas

* Separação de responsabilidades entre models, views, forms, serializers e templates
* Uso do sistema de autenticação do Django
* Uso de CRUD web com mensagens de feedback
* Uso de API REST com ViewSets e ModelSerializer
* Proteção das rotas web e da API por login
* Validações para evitar dados duplicados ou inconsistentes
* Uso de migrations para controle do banco de dados
* Interface responsiva com Bootstrap e CSS customizado

---

## Autor

Rafael Eloisio

---

## Observacões

* O banco de dados utilizado no desenvolvimento é o SQLite.
* Para acessar a API, é necessário estar logado.
* Caso use PowerShell e tenha problemas com `curl`, utilize `curl.exe`.
* Os IDs usados nos exemplos podem mudar de acordo com os dados cadastrados no banco.
