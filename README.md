# 📚 API Sistema Escolar

Projeto criado para a disciplina de SEMINÁRIO INTEGRADOR do CENTRO UNIVERSITÁRIO DE DESENVOLVIMENTO DO CENTRO-OESTE. Uma API REST desenvolvida em Python com FastAPI para gerenciamento completo de sistemas escolares. O projeto fornece endpoints para gerenciar alunos, turmas, disciplinas, matrículas e atribuições de professores.

## 🎯 Funcionalidades

- **Gerenciamento de Alunos**: Criar, ler, atualizar e deletar registros de alunos
- **Gestão de Turmas**: Organizar turmas e vincular alunos
- **Disciplinas**: Cadastro e associação de disciplinas aos professores
- **Matrículas**: Sistema de matrícula de alunos em turmas
- **Atribuições**: Atribuição de disciplinas aos professores
- **Banco de Dados**: SQLAlchemy ORM com migrations automáticas via Alembic

## 🚀 Tecnologias

- **FastAPI**: Framework web moderno e de alta performance
- **SQLAlchemy**: ORM para manipulação de dados
- **Alembic**: Migrations de banco de dados
- **SQLite**: Banco de dados padrão
- **Python 3.9+**: Linguagem de desenvolvimento

## 📋 Pré-requisitos

- Python 3.9 ou superior
- pip (gerenciador de pacotes Python)
- Git

## 💾 Instalação

1. Clone o repositório:
```bash
git clone https://github.com/Sales232/api-sistema-escolar.git
cd api-sistema-escolar
```

2. Crie um ambiente virtual:
```bash
python -m venv venv
```

3. Ative o ambiente virtual:

**No Windows:**
```bash
venv\Scripts\activate
```

**No macOS/Linux:**
```bash
source venv/bin/activate
```

4. Instale as dependências:
```bash
pip install -r requirements.txt
```

5. Execute as migrations do banco de dados:
```bash
alembic upgrade head
```

## ▶️ Como Usar

1. Inicie o servidor:
```bash
python main.py
```

O servidor estará disponível em `http://localhost:8000`

2. Acesse a documentação interativa:
- Swagger UI: `http://localhost:8000/docs`
- ReDoc: `http://localhost:8000/redoc`

## 📁 Estrutura do Projeto

```
api-sistema-escolar/
├── alembic/                 # Migrations do banco de dados
├── database/                # Configuração do banco de dados
├── models/                  # Modelos de dados
├── router/                  # Rotas e endpoints da API
├── main.py                  # Arquivo principal da aplicação
├── models.py                # Definição de modelos SQLAlchemy
├── matriculas.py            # Lógica de matrículas
├── atribuicoes.py           # Lógica de atribuições
├── banco.db                 # Arquivo do banco de dados SQLite
├── requirements.txt         # Dependências Python
└── alembic.ini             # Configuração do Alembic
```

## 🔌 Endpoints Principais

### Alunos
- `GET /alunos` - Listar todos os alunos
- `POST /alunos` - Criar novo aluno
- `GET /alunos/{id}` - Obter detalhes de um aluno
- `PUT /alunos/{id}` - Atualizar aluno
- `DELETE /alunos/{id}` - Deletar aluno

### Turmas
- `GET /turmas` - Listar turmas
- `POST /turmas` - Criar turma
- `GET /turmas/{id}` - Obter turma específica

### Matrículas
- `POST /matriculas` - Criar matrícula
- `GET /matriculas` - Listar matrículas

### Atribuições
- `POST /atribuicoes` - Atribuir disciplina a professor
- `GET /atribuicoes` - Listar atribuições

## 🛠️ Desenvolvimento

### Criar uma nova migration:
```bash
alembic revision --autogenerate -m "Descrição da alteração"
alembic upgrade head
```

### Executar testes:
```bash
pytest
```

## 📝 Variáveis de Ambiente

Crie um arquivo `.env` na raiz do projeto (opcional):
```
DATABASE_URL=sqlite:///./banco.db
DEBUG=True
```

## Contribuições:

Contribuições são bem-vindas! Para contribuir:

1. Faça um fork do projeto
2. Crie uma branch para sua feature (`git checkout -b feature/AmazingFeature`)
3. Commit suas mudanças (`git commit -m 'Add some AmazingFeature'`)
4. Push para a branch (`git push origin feature/AmazingFeature`)
5. Abra um Pull Request

## Contato

Para dúvidas ou sugestões, abra uma [issue](https://github.com/Sales232/api-sistema-escolar/issues) no repositório.

---

**Status**: Em Desenvolvimento 🚧
