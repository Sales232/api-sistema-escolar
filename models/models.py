from sqlalchemy import create_engine, Column, String, Integer, Float, ForeignKey
from sqlalchemy.orm import declarative_base, relationship

# Cria a conexão com o bd
db = create_engine("sqlite:///banco.db")
# Cria o modelo do bd
Base = declarative_base()

class Aluno(Base):
    __tablename__ = "alunos"
    id_aluno = Column("id_aluno", Integer, primary_key=True, autoincrement=True)
    email = Column("Email", String, nullable=False)
    nome = Column("nome", String)
    data_nascimento = Column("data_nascimento", String) 
    cpf = Column("CPF", Float)
    endereco = Column("Endereço", String)
    turma_id = Column("Turma", Integer, ForeignKey("turmas.id_turma"), nullable=True )

    def __init__(self, id_aluno, email, nome, data_nascimento, cpf, endereco):
        self.nome = nome
        self.id_aluno = id_aluno
        self.email = email
        self.data_nascimento = data_nascimento
        self.cpf = cpf
        self.endereco = endereco

    turmas = relationship("Turma", back_populates="alunos")

class Turma(Base):
    __tablename__ = "turmas"
    id_turma = Column("id_turma", Integer, primary_key=True, autoincrement=True)
    ano = Column("ano", String)
    turno = Column("turno", String)
    professor_id = Column(Integer, ForeignKey("professores.id_professor"), nullable=True)
    
    def __init__(self, id_turma, alunos, ano, turno):
        self.id_turma = id_turma
        self.alunos = alunos
        self.ano = ano
        self.turno = turno
    
    alunos = relationship("Aluno", back_populates="turmas")
    professor = relationship("Professor", back_populates="turmas")

    # id: int nome: str ano: int turno: str

class Professor(Base):
    __tablename__ = "professores"
    id_professor = Column("id_professor", Integer, primary_key=True, autoincrement=True)
    nome = Column("nome", String, nullable=False)
    
    def __init__(self, id_professor, nome):
        self.id_professor = id_professor
        self.nome = nome
    
    turmas = relationship("Turma", back_populates="professor")

#class ProfessorAdmin(Base):
 #   email: EmailStr
  #  password: constr(min_length=6)