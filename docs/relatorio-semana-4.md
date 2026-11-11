# Semana 4 — Implementação (Relatório de projeto) — MathLab

- **Curso:** DSAIA
- **Entrega:** Semana 4 — Implementação (1 ponto · trabalho em dupla)
- **Projeto:** MathLab — Banco de Questões de Matemática
- **Dupla:** Eliseu [e colega]
- **Repositório:** <https://github.com/Eliseufera/mathlab>
- **Branch:** `main`
- **Data:** 2026-11-11

## Recorte implementado

Fundação da aplicação web (Flask + SQLite) derivada das tarefas da semana 3 (`specs/001-question-bank/tasks.md`): configuração, *app factory*, conexão de banco com integridade, tratamento de erros, segurança CSRF e estrutura de rotas com página inicial. As funcionalidades de domínio (CRUD de questões, correção automática, histórico) estão **pendentes** (ver *Estado atual*).

> O objetivo desta entrega é demonstrar a transformação de **spec e plano em implementação rastreável**, com controle humano sobre o código gerado por IA — não a aplicação pronta.

## 1. Evidência da implementação (Tasks → Commits → Código)

Commits no GitHub (branch `main`), cada um com os IDs das tarefas no corpo:

| Commit | Mensagem | Tasks | Link |
|---|---|---|---|
| `23d0263` | docs(sdd): spec, plan e tasks | artefatos SDD (G1) | <https://github.com/Eliseufera/mathlab/commit/23d0263> |
| `a813e8e` | feat(setup): ambiente, scaffold e app factory | T004–T007 | <https://github.com/Eliseufera/mathlab/commit/a813e8e> |
| `56d20cc` | feat(backend): db, erros, CSRF, blueprints | T007–T011 | <https://github.com/Eliseufera/mathlab/commit/56d20cc> |

### Mapa tarefa → commit → arquivos

| Task | Entrega | Commit | Arquivos principais | Status |
|---|---|---|---|---|
| T001 | Validar conformidade com a Constitution | auditoria | `tasks.md`, `plan.md` §14 | ✅ |
| T003 | Versionar artefatos SDD no Git | `23d0263` + política por módulo | `specs/`, `.specify/` | ✅ |
| T004 | Ambiente e dependências | `a813e8e` | `requirements.txt` | ✅ |
| T005 | Scaffold `app/` e `tests/` | `a813e8e` | `app/`, `tests/` | ✅ |
| T006 | Configuração | `a813e8e` | `app/config.py` | ✅ |
| T007 | App factory `create_app()` | `a813e8e` + `56d20cc` | `app/__init__.py` | ✅ |
| T008 | Conexão SQLite + `PRAGMA foreign_keys=ON` | `56d20cc` | `app/db.py` | ✅ |
| T009 | Erros 400/404/409/500 | `56d20cc` | `app/errors.py` | ✅ |
| T010 | CSRF + autoescape | `56d20cc` | `app/security.py` | ✅ |
| T011 | Blueprints + `GET /` | `56d20cc` | `app/blueprints/`, `app/templates/` | ✅ |

A rastreabilidade completa (T001–T050) está em [`specs/001-question-bank/tasks.md`](../specs/001-question-bank/tasks.md), com status por tarefa.

## 2. Estado atual da aplicação

**Funciona (na máquina da dupla):**
- `GET /` (página inicial com navegação) → HTTP 200.
- Conexão SQLite por request com `PRAGMA foreign_keys=ON`; teardown fecha a conexão.
- Tratamento centralizado de erros 400/404/409/500 (página de erro, sem expor stack/SQL).
- Proteção **CSRF** em POST (token em sessão; requisição sem token → 400) e **autoescape** HTML.
- Suíte de testes automatizada: **15 testes Pytest verdes**.

**Implementado, porém com limite:**
- Blueprints criados e registrados, mas as rotas de domínio (`/questions`, `/history`) ainda respondem 404 — serão preenchidas nas fases seguintes.
- O menu exibe "Questões" e "Histórico", mas esses destinos ainda não existem.

**Pendente (não implementado):**
- Fase 3 — schema SQLite (`subject`, `question`, `alternative`, `attempt`), inicialização e repositórios.
- Fase 4 — CRUD de questões + filtros por assunto/dificuldade.
- Fases 5–6 — resolução e correção automática + registro de tentativas.
- Fase 7 — histórico de desempenho e métricas.
- Fase 8 — telas completas (CSS responsivo desktop+mobile, JS de aprimoramento).

**Bloqueios:** nenhum bloqueio técnico. Duas decisões de design aguardam confirmação do dono do projeto (limites de validação **D-05** e mecanismo de CSRF **D-16**), e há uma alteração pré-existente da Constitution (apenas espaços em branco) ainda não commitada — por decisão de não alterar a Constitution sem aval.

## 3. Stack efetiva

| Item | Escolha |
|---|---|
| IDE / editor | [preencher: ex. VS Code] |
| Linguagem | Python 3.14.6 |
| Framework web | Flask 3.1.3 |
| Banco de dados | SQLite (módulo `sqlite3` da stdlib, sem ORM) |
| Testes | Pytest 9.2.0 |
| Frontend | HTML + CSS + JavaScript vanilla (Jinja2 server-side) |
| Versionamento | Git + GitHub |
| Ambiente | virtualenv (`.venv`) |

**Mudança em relação à semana 3:** CSRF implementado com **token manual** (stdlib `secrets` + sessão) em vez de Flask-WTF, para manter dependências mínimas (Princípio III da Constitution). Demais escolhas: **sem mudança**.

## 4. Revisão do código gerado por IA

Como a dupla revisou e validou o código produzido com agentes de IA:

- **Gate de testes:** nenhuma tarefa foi marcada como concluída sem a suíte Pytest verde ("completo = critérios atendidos + testes passando").
- **Commits atômicos por módulo**, com o ID das tarefas no corpo, permitindo ao instrutor ligar cada alteração à tarefa correspondente.
- **Decisões explícitas:** toda escolha de design (D-05/D-16) foi registrada e sinalizada para revisão/veto humano.
- **Sem alteração silenciosa:** spec, plan e Constitution não foram alterados sem justificativa; as lacunas identificadas (G1–G6) permanecem reportadas e pendentes de decisão.
- Revisão humana responsável por executar os testes e aceitar/rejeitar cada entrega.

## Como verificar

```bash
git clone https://github.com/Eliseufera/mathlab
cd mathlab
python -m venv .venv
# Windows:
.venv\Scripts\activate
pip install -r requirements.txt
pytest -q                     # 15 testes
flask --app app run           # abrir http://127.0.0.1:5000/
```
