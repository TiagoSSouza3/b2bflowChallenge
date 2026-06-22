# Desafio Técnico - Estágio Python | b2bflow

Projeto desenvolvido como parte do processo seletivo para a vaga de Estágio em Desenvolvimento Python da b2bflow.

## Objetivo

Ler contatos armazenados no Supabase e enviar uma mensagem personalizada via Z-API para até 3 números.

Mensagem enviada:

```text
Ola, <nome_contato> tudo bem com você?
```

---

## Estrutura do banco

Tabela: `contacts`

| Campo | Tipo |
|-------|------|
| id | int8 |
| name | text |
| number | number |

---

## Variáveis de ambiente

Crie um arquivo `.env` na raiz do projeto com as seguintes variáveis:

```env
SUPABASE_URL=
SUPABASE_KEY=
ZAPI_INSTANCE_ID=
ZAPI_INSTANCE_TOKEN=
```

Há também um arquivo `.env.example` como modelo.

---

## Instalação

Clone o repositório:

```bash
git clone <url-do-repositorio>
```

Instale as dependências:

```bash
pip install -r requirements.txt
```

---

## Execução

Execute o projeto com:

```bash
python main.py
```

---

## Estrutura do projeto

```
.
├── services/
│   ├── supabase.py
│   └── whatsapp.py
├── .env.example
├── .gitignore
├── main.py
├── requirements.txt
└── README.md
```