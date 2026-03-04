# Sistema de upload de arquivos (SisUpa)

Aplicação desktop desenvolvida com Tkinter para upload, listagem e visualização de arquivos compactados.

Projeto focado em organização arquitetural e aplicação de conceitos de POO.


## Objetivo

Projeto desenvolvido para fins de aprendizado e portfólio profissional, com foco em:

- Separação de responsabilidades
- Estrutura em camadas
- Evolução para aplicação de Design Patterns
- Explorar modelagem orientada a objetos em aplicações desktop

---

## Tecnologias Utilizadas

- Python 3.8+
- Tkinter (GUI nativa)
- SQLite
- Programação Orientada a Objetos

---

## Funcionalidades

- Gerenciar upload de arquivos
- Listar registros dinamicamente em uma Treeview
- Visualizar imagens extraídas de arquivos compactados
- Permitir navegação entre imagens

---

## Estrutura

```python
app/
│
├── views/
│ ├── form_view.py
│ ├── render_preview_view.py
│
├── services/
│ ├── search_file_service.py
│ ├── decompressed_service.py
│
├── repository/
│ └── repository.py
└── main.py
```


- **Views** → Interface gráfica e eventos
- **Services** → Regras de negócio  
- **Repository** → Persistência e acesso a dados  
- **App** → Orquestração da aplicação  

Essa separação permite:

- Redução de acoplamento
- Possível evolução para padrões mais avançados

---

## Screenshots

### Principal
![Interface Principal](docs/screenshots/main.png)

### Visualização de Arquivo
![Visualização](docs/screenshots/preview.png)

## Demonstração

![Demonstração do Sistema](docs/demo2.gif)

---

![License](https://img.shields.io/badge/license-MIT-green)

## Como exercutar?

### 1) Clone o repositório
```bash

git clone https://github.com/CodePhsp/projeto-tkinter.git
cd projeto-tkinter

```

### 2) Crie ambiente virtual
Para o sistema operacional windows

> Dica: você pode escolher qualquer nome para seu ambiente virtual 
```bash
python -m venv .venv
venv\Scripts\activate  
```

Para o sistema operacional Linux
```bash
python3 -m venv venv
source venv/bin/activate
```

### 3) Instale as dependências

```bash
python -m pip install -r requirements.txt
```

### 4) Execute
```bash
cd app
python main.py
```