# 🚀 Formação Django REST Framework: crie APIs com Python

API RESTful completa para gerenciamento de plataforma educacional, desenvolvida durante a formação **Django REST Framework: crie APIs com Python** da Alura. O projeto implementa CRUD de estudantes, cursos e matrículas, com foco em **validações customizadas, autenticação, permissões, throttling, documentação automática e integração CORS**.

---

## 📂 Estrutura do Projeto
```
raiz/
├── backend/          # API Django REST Framework
├── frontend/         # Interface React + Vite (fornecida no curso)
├── Certificados/     # Certificados de conclusão (.png)
└── README.md
```

---

## 🛠️ Tecnologias Utilizadas

Nesta formação, as principais tecnologias e ferramentas utilizadas para construir a API RESTful e a aplicação de front-end foram:

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Django](https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=white)
![DRF](https://img.shields.io/badge/Django_REST-ff1709?style=for-the-badge&logo=django&logoColor=white)
![SQLite](https://img.shields.io/badge/SQLite-07405E?style=for-the-badge&logo=sqlite&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white)
![React](https://img.shields.io/badge/React-20232A?style=for-the-badge&logo=react&logoColor=61DAFB)
![Vite](https://img.shields.io/badge/Vite-646CFF?style=for-the-badge&logo=vite&logoColor=white)
![Nginx](https://img.shields.io/badge/Nginx-009639?style=for-the-badge&logo=nginx&logoColor=white)

**Backend:**  
Python • Django 5.2 • Django REST Framework 3.16 • SQLite • django-cors-headers • django-filter • drf-yasg • validate-docbr

**Frontend:**  
React 18 • Vite • styled-components • Docker • Nginx

---

## 🚀 Como Executar

### Backend
```bash
cd backend
python -m venv venv
source venv/bin/activate  # Windows: .\venv\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

**Documentação Swagger:** `http://127.0.0.1:8000/swagger/`

### Frontend (Docker)
```bash
cd frontend
docker-compose up --build
```

**Aplicação:** `http://localhost:8042`

> **Nota:** O frontend consome a API em `http://localhost:8000/cursos` (configurado via variável de ambiente `VITE_URL`)

---

## 📖 Conteúdo Técnico

### **Curso 1: Construindo APIs RESTful**
- Models com relacionamentos (Estudante, Curso, Matricula)
- Serializers e ViewSets com rotas automáticas
- Validações customizadas (CPF, nome, celular)

### **Curso 2: Validação e Filtros Avançados**
- Serializers especializados para diferentes contextos
- Filtros, busca e ordenação com django-filter
- Paginação e geração de dados com Faker

### **Curso 3: Permissões, Documentação, Throttling e CORS**
- Sistema de autenticação e permissões baseado em grupos Django
- **Throttling**: Limitação de 5 requisições/dia para anônimos no endpoint de matrículas
- **Documentação automática**: Swagger/OpenAPI com drf-yasg
- **CORS**: Integração segura com front-end React
- **Validações avançadas**: CPF (validate-docbr), formato de celular, unicidade de códigos

---

## 🔑 Recursos Principais

**Endpoints:**
- `/estudantes/` - CRUD completo com filtros por nome/CPF e ordenação
- `/cursos/` - Gerenciamento de cursos com níveis (Básico, Intermediário, Avançado)
- `/matriculas/` - Controle de matrículas por período (Matutino, Vespertino, Noturno)
- `/estudantes/{id}/matriculas/` - Listagem de matrículas por estudante
- `/curso/{id}/matriculas/` - Listagem de matrículas por curso

**Diferenciais:**
- ✅ Validação completa de CPF brasileiro
- ✅ Throttling customizado para proteção da API
- ✅ Permissões granulares (leitura livre em cursos, escrita protegida em estudantes)
- ✅ Documentação interativa via Swagger
- ✅ CORS configurado para ambiente de desenvolvimento
- ✅ Frontend containerizado com Docker e Nginx

---

## 🎓 Certificações

Certificados de conclusão dos 3 cursos disponíveis na pasta **`Certificados/`**.

---

## 📝 Licença

O conteúdo deste repositório está licenciado sob a **Licença MIT**.

Sinta-se à vontade para explorar o código para fins de aprendizado, mas lembre-se de dar o devido crédito se utilizá-lo como base para seus próprios projetos.

---

## 🤝 Créditos

- **Backend (API)**: [Ana Karolina Niclevicz](https://www.linkedin.com/in/ana-karolina-niclevicz-364017218/)
- **Frontend (React)**: Fornecido pela [Alura](https://www.alura.com.br/)

---

⭐ **Se este projeto foi útil, considere dar uma estrela!**