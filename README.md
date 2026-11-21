# MathLab

Aplicação web local para cadastrar, organizar e responder questões de matemática de múltipla escolha, com correção automática e histórico de desempenho.

> **Estado atual:** a fundação da aplicação está pronta e validada (configuração, app factory, SQLite com chaves estrangeiras, tratamento de erros, CSRF, autoescape e rota inicial). O fluxo principal do recorte — cadastrar questões, responder, corrigir e consultar histórico — **ainda não está implementado**. As limitações e o bloqueio estão detalhados em [docs/relatorio-semana-6.md](docs/relatorio-semana-6.md#4-limitações-e-bloqueios).

## Requisitos

- Python 3.10 ou superior (testado em **Python 3.14.6**)
- Git
- Nenhum serviço externo, banco de dados servidor ou credencial

## Como executar

Os comandos abaixo assumem que você está na raiz do repositório.

### 1. Clonar

```bash
git clone https://github.com/Eliseufera/mathlab.git
cd mathlab
```

### 2. Criar e ativar o ambiente virtual

Windows (PowerShell):

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
```

Windows (cmd):

```bat
python -m venv .venv
.venv\Scripts\activate.bat
```

Git Bash:

```bash
python -m venv .venv
source .venv/Scripts/activate
```

macOS/Linux:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

> Se a ativação for bloqueada no PowerShell, use `Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass` na sessão atual ou execute os comandos com o caminho completo (`.venv\Scripts\python`), sem ativar.

### 3. Instalar as dependências

```bash
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
```

Dependências: **Flask 3.1** e **Pytest 9.2** (versões testadas). Não há Flask-WTF; o CSRF usa a biblioteca padrão, conforme a decisão D-16 e o Princípio III da Constitution.

### 4. Configurar variáveis de ambiente

Nenhuma variável é obrigatória para rodar em desenvolvimento, mas recomenda-se definir uma chave própria:

Windows (PowerShell):

```powershell
$env:SECRET_KEY = "troque-por-um-valor-secreto"
```

Windows (cmd):

```bat
set SECRET_KEY=troque-por-um-valor-secreto
```

Git Bash / macOS / Linux:

```bash
export SECRET_KEY="troque-por-um-valor-secreto"
```

| Variável | Obrigatória | Padrão | Uso |
|---|---|---|---|
| `SECRET_KEY` | Não em dev | Valor de desenvolvimento embutido | Assinatura da sessão e token CSRF. Defina uma chave própria fora de desenvolvimento. |
| `MATHLAB_DATABASE` | Não | `instance/mathlab.sqlite` | Caminho do arquivo SQLite. Aceita caminho absoluto ou relativo ao diretório de execução. |

> O projeto **não carrega `.env` automaticamente**. Defina as variáveis no shell antes de iniciar a aplicação. O arquivo `.env` está no `.gitignore`; nenhuma chave ou credencial é versionada.

### 5. Executar a aplicação

```bash
python -m flask --app app run
```

Abra <http://127.0.0.1:5000> no navegador. Para encerrar, use `Ctrl+C`.

O servidor embutido do Flask é apenas para desenvolvimento. O modo `--debug` é opcional:

```bash
python -m flask --app app run --debug
```

### 6. Executar os testes

```bash
python -m pytest -q
```

Resultado esperado nesta etapa:

```text
...............                                                          [100%]
15 passed
```

## Banco de dados

- O banco é **SQLite em arquivo**, usando `sqlite3` da biblioteca padrão; não há servidor, usuário ou senha.
- O caminho padrão é `instance/mathlab.sqlite`. O diretório `instance/` é criado automaticamente e os arquivos `*.sqlite` são ignorados pelo Git.
- **Ainda não há schema nem migrações nesta etapa.** As tabelas (`subject`, `question`, `alternative`, `attempt`) serão criadas na Fase 3 (`T012`–`T018`) do [plano de tarefas](specs/001-question-bank/tasks.md). Até lá, a conexão é aberta com `PRAGMA foreign_keys = ON`, mas sem tabelas de negócio.
- Os testes usam um arquivo SQLite temporário por execução, criado pelas fixtures de `tests/conftest.py`.

## O que funciona hoje

- `GET /` responde **200** com a página inicial e navegação.
- Fábrica `create_app()` com configuração por ambiente e configuração de teste.
- Conexão SQLite por request, com `PRAGMA foreign_keys = ON` e fechamento no fim do contexto.
- Páginas de erro para **400, 404, 409 e 500**, com mensagem ao usuário e sem expor stack trace ou SQL.
- **CSRF** em todos os métodos não seguros (POST, PUT, PATCH, DELETE), com token de sessão.
- **Autoescape** do Jinja2 habilitado para HTML.
- 15 testes automatizados cobrindo a fundação.

## Limitações e bloqueios

- Cadastro, edição, exclusão, listagem e filtro de questões: **não implementados**.
- Resposta, correção automática e histórico: **não implementados**.
- Os links “Questões” e “Histórico” do menu apontam para rotas que ainda respondem **404**.
- Schema, seed de assuntos e repositórios: **não implementados** (Fase 3 em diante).
- Decisão **D-16** (CSRF manual × Flask-WTF) ainda aguarda ratificação formal da dupla; o comportamento está validado, mas a decisão de design segue aberta.
- Não há autenticação, contas ou múltiplos usuários (fora do MVP, conforme a especificação).

## Estrutura do projeto

```text
app/
  __init__.py          # create_app()
  config.py            # configuração por ambiente
  db.py                # conexão SQLite + PRAGMA foreign_keys
  errors.py            # handlers 400/404/409/500
  security.py          # CSRF manual (sessão + hmac)
  blueprints/          # main, questions, attempts, history
  templates/           # base, home e página de erro
  static/css/          # estilo responsivo
tests/
  conftest.py          # app e client de teste, banco temporário
  test_app.py          # 7 testes de fábrica/configuração
  test_backend.py      # 8 testes de rota, banco, CSRF e autoescape
specs/001-question-bank/  # spec, plan e tasks (SDD)
.specify/memory/          # Constitution v1.0.0
docs/                     # relatórios semanais e validação
```

## A ideia

O MathLab é uma aplicação web local para cadastrar, organizar e responder questões de matemática de múltipla escolha, com correção automática e registro do desempenho. Hoje, quem estuda por conta própria costuma espalhar exercícios entre papel, planilhas e anotações: é difícil revisar por assunto ou dificuldade, não há feedback imediato e não dá para saber se está havendo evolução. O usuário afetado é o estudante que se prepara para provas, e também o professor ou monitor que monta listas de exercícios. A aplicação centraliza o banco de questões, permite filtrar por assunto e dificuldade, corrigir a resposta na hora e consultar o histórico de acertos e erros. O resultado esperado é um ciclo de estudo simples e offline — cadastrar, praticar, receber feedback e enxergar o progresso — sem depender de contas, servidores externos ou conexão com a internet.

## Problema, usuário e resultado esperado

- **Problema:** questões espalhadas em papel e planilhas são difíceis de organizar e filtrar, não oferecem correção automática nem acompanhamento da evolução.
- **Usuário:** estudante que pratica para provas e professor ou monitor que mantém o banco de questões.
- **Resultado esperado:** um ciclo único de cadastro, prática com feedback imediato e consulta de desempenho, funcionando localmente e sem infraestrutura externa.

## Stack tecnológica

| Camada | Tecnologia | Papel no projeto |
|---|---|---|
| IDE | Qoder Desktop (baseada em VS Code) | Edição, execução e depuração |
| Linguagem | Python 3.14 | Back-end e scripts de apoio |
| Framework web | Flask 3.1 | Rotas, blueprints, configuração da aplicação |
| Templates | Jinja2 + HTML5 | Interface renderizada no servidor |
| Estilo e interação | CSS próprio + JavaScript puro | Layout responsivo e aprimoramento progressivo |
| Banco de dados | SQLite (biblioteca padrão `sqlite3`) | Persistência local com chaves estrangeiras |
| Testes | Pytest | Testes unitários, de integração e de rotas |
| Versionamento | Git + GitHub | Histórico e rastreabilidade das mudanças |

## Justificativa técnica

Python com Flask foi escolhido por ser a stack da disciplina e por permitir uma aplicação web completa com poucas dependências: o Flask oferece roteamento, templates Jinja2 e servidor de desenvolvimento sem exigir build de front-end. A separação em blueprints, services e repositories mantém as regras de negócio isoladas das rotas, o que torna correção, validação e histórico testáveis com Pytest e atende ao requisito de modularidade.

O SQLite é o banco embutido da biblioteca padrão do Python: não exige servidor nem configuração, guarda os dados em um único arquivo e suporta chaves estrangeiras e transações — suficiente para um MVP local e monousuário, além de sustentar o uso offline. HTML, CSS e JavaScript puro, renderizados no servidor, evitam a complexidade de uma SPA e mantêm o fluxo funcional mesmo sem JavaScript, com interface responsiva e acessível.

Git e GitHub completam a combinação porque o projeto é conduzido com Spec-Driven Development: Constitution, especificação, plano e tarefas são versionados, e cada mudança permanece rastreável de requisito a commit. Pytest entra como rede de segurança desde o início. O custo de infraestrutura é praticamente zero: a aplicação roda na máquina do usuário, sem serviços externos.

## Validação

- Evidência detalhada, critérios de aceitação cobertos e checklist reproduzível: [docs/relatorio-semana-6.md](docs/relatorio-semana-6.md).
- Teste do terceiro (clone limpo, venv nova, instalação pelo `requirements.txt`, testes e execução): registrado no mesmo relatório.

## Documentação SDD

- [Constitution](.specify/memory/constitution.md)
- [Especificação](specs/001-question-bank/spec.md)
- [Plano](specs/001-question-bank/plan.md)
- [Tarefas](specs/001-question-bank/tasks.md)
