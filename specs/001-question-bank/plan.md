# Plano de Implementação — Banco de Questões de Matemática (MathLab)

- **Feature**: `001-question-bank`
- **Documento**: `specs/001-question-bank/plan.md`
- **Base**: [`spec.md`](./spec.md) (RF-001…RF-010, RNF-001…RNF-009, RN-001…RN-008) e [Constitution v1.0.0](../../.specify/memory/constitution.md) (Princípios I–VI, §3–§8)
- **Stack (Constitution §3)**: Python + Flask + SQLite + HTML + CSS + JavaScript + **Pytest** + **Git/GitHub**
- **Diretrizes**: simplicidade e modularidade (Princípio III)
- **Repositório**: `C:\Users\Eliseu\mathlab` (Git — Princípio VI); scaffold real `app/` + `tests/` na raiz
- **Status**: Rascunho para revisão humana (Princípios IV/V — supervisão humana obrigatória)

> **Sem código**: este plano **não implementa código**. Modelo de dados, rotas e estrutura são descritos como documentação (tabelas/árvores), não como SQL/Python/JS executável.
>
> **Constitution presente e prevalente (§8)**: `.specify/memory/constitution.md` (v1.0.0) **foi localizada e lida**. Este plano foi alinhado a ela. Em conflito entre decisão de implementação e a Constitution, **a Constitution prevalece** até emenda formal. A conformidade é mapeada na seção 14.
>
> **Não alteração silenciosa do spec/tasks**: este plano **não muda** `spec.md` nem `tasks.md`. Lacunas de conformidade e de design que afetam esses documentos estão **reportadas** nas seções 12–13 (itens `G-xx` e `D-xx`) e **aguardam decisão humana item a item** ("só reportar, eu decido"). Onde o desenho precisa de um valor concreto, usa-se a **proposta de MVP do spec**, sempre rotulada com o identificador `D-xx` correspondente e **sujeita a aprovação**.

---

## 1. Arquitetura da aplicação

Aplicação **web monolítica modular** em Flask, renderizada no servidor (Jinja2) com **aprimoramento progressivo** em JavaScript puro. Persistência em **SQLite** local. Sem SPA, sem serviços externos (RNF-003).

Camadas (separação de responsabilidades — RNF-002):

```
Navegador (HTML + CSS + JS)
        │  HTTP (forms / fetch opcional)
        ▼
[Blueprints / Rotas]  → controllers finos: entrada/saída, HTTP, render
        ▼
[Services]            → regras de negócio: correção, validação, política de exclusão, agregação de histórico
        ▼
[Repositories]        → acesso a dados: SQL parametrizado, transações
        ▼
[SQLite]              → arquivo local, chaves estrangeiras habilitadas
```

- **App factory** (`create_app` no pacote `app/`) para configurar, registrar blueprints e inicializar o banco — facilita testes (RNF-008; Constitution §4).
- **Regra de ouro**: rotas não contêm regra de negócio nem SQL; services não conhecem HTTP; repositories não conhecem regra de negócio (Princípio III).
- **Acesso a dados**: proposto `sqlite3` da biblioteca padrão (simplicidade), sem ORM. *(Decisão D-13.)*
- **Estilo de interface**: formulários server-rendered com padrão **POST→Redirect→GET** (evita reenvio). JS apenas como conveniência. *(Decisão D-12.)*
- **UX (Constitution §5)**: interface responsiva **desktop + mobile**, acessível e consistente, com **feedback** em toda ação importante (submeter resposta, receber correção). Detalhado na seção 8.
- **Rastreabilidade (Princípio VI)**: specs, plano, tasks, implementação e evidência de testes versionados no Git/GitHub; commits significativos por mudança.

## 2. Organização dos módulos

| Módulo (caminho no repo) | Responsabilidade | RFs atendidos |
|--------|------------------|---------------|
| `app/` (factory `create_app`) | Criar app, config, registrar blueprints, inicializar DB. | Todos (infra) |
| `app/config.py` | Configurações (caminho do DB, secret key, ambiente). | RNF-003/009 |
| `app/db.py` | Conexão SQLite, `PRAGMA foreign_keys=ON`, init de schema, helpers de transação. | RNF-004 |
| `app/blueprints/questions.py` | Rotas de CRUD, listagem/filtro, resposta. | RF-001,002,003,004,005,006,010 |
| `app/blueprints/attempts.py` | Rota de submissão de resposta → correção + registro (ou agrupada em `questions`). | RF-007,008 |
| `app/blueprints/history.py` | Rotas de histórico/desempenho e filtros. | RF-009 |
| `app/services/question_service.py` | Regras de criação/edição/exclusão, "exatamente uma correta", política RN-005. | RF-001,002,003,006 |
| `app/services/grading_service.py` | Correção automática (comparação escolhida × correta). | RF-007 |
| `app/services/attempt_service.py` | Registrar tentativa de forma atômica e append-only. | RF-008 |
| `app/services/history_service.py` | Agregação de métricas e filtros. | RF-009 |
| `app/repositories/question_repo.py` | Persistência de questão + alternativas + assuntos. | RF-001…006,010 |
| `app/repositories/attempt_repo.py` | Persistência/consulta de tentativas. | RF-008,009 |
| `app/repositories/subject_repo.py` | Leitura do catálogo de assuntos (sem CRUD no MVP, D-04). | RF-004 |
| `app/validators.py` | Regras de validação de entrada (servidor). | RNF-005, RN-001/002/007 |
| `app/templates/` | HTML Jinja2 (autoescape ligado). | RNF-006, CA-14 |
| `app/static/css`, `app/static/js` | Estilo e JS de conveniência/validação client-side. | RNF-006 |
| `tests/` (raiz do repo) | Unit, integração, rotas, segurança (Pytest — §3/§4). | RNF-008 |

## 3. Estrutura de diretórios

> Estrutura alinhada ao scaffold real do repo (`app/` + `tests/` na raiz). Documentação, não código; nomes de arquivos são indicativos. `instance/` é gitignored (dados não versionados). A divergência com os paths `mathlab/...` do `tasks.md` está reportada em G6/R-13 (spec/tasks **não** alterados).

```
mathlab/                            # raiz do repo Git (C:\Users\Eliseu\mathlab)
├─ .gitignore                       # ignora instance/, __pycache__, .venv, etc.
├─ README.md                        # §7: propósito, stack, instalação, execução, testes
├─ requirements.txt                 # Flask (+ Flask-WTF se D-16); Pytest (§3)
├─ .specify/
│  └─ memory/
│     └─ constitution.md            # v1.0.0 — PRESENTE e prevalente (§8)
├─ specs/
│  └─ 001-question-bank/
│     ├─ spec.md                    # base deste plano (não alterado)
│     ├─ plan.md                    # este documento
│     └─ tasks.md                   # tarefas (não alterado; paths divergem — G6/R-13)
├─ app/                             # pacote da aplicação (scaffold existente)
│  ├─ __init__.py                   # create_app()
│  ├─ config.py
│  ├─ db.py                         # conexão + init + PRAGMA FK
│  ├─ schema.sql                    # DDL de inicialização (conteúdo na implementação)
│  ├─ blueprints/
│  │  ├─ questions.py
│  │  ├─ attempts.py
│  │  └─ history.py
│  ├─ services/
│  │  ├─ question_service.py
│  │  ├─ grading_service.py
│  │  ├─ attempt_service.py
│  │  └─ history_service.py
│  ├─ repositories/
│  │  ├─ question_repo.py
│  │  ├─ attempt_repo.py
│  │  └─ subject_repo.py
│  ├─ validators.py
│  ├─ templates/
│  │  ├─ base.html
│  │  ├─ questions/ (list, form, view, answer, result)
│  │  └─ history/ (index)
│  └─ static/
│     ├─ css/
│     └─ js/
├─ instance/
│  └─ mathlab.sqlite                # dados em runtime — GITIGNORED (não versionar)
└─ tests/                           # scaffold existente (raiz do repo)
   ├─ unit/
   ├─ integration/
   ├─ routes/
   └─ conftest.py                   # fixtures, DB temporário/em memória
```

## 4. Modelo relacional do SQLite

> Descrito como documentação. Tipos e restrições refletem as propostas do spec (D-02…D-07). `PRAGMA foreign_keys=ON` obrigatório (RNF-004). Sem entidade `student` no MVP proposto (single-usuário, D-02).

**Tabela `subject`** *(catálogo simples — D-04)*
| Coluna | Tipo | Restrições |
|--------|------|------------|
| id | INTEGER | PK, autoincrement |
| name | TEXT | NOT NULL, UNIQUE |

**Tabela `question`**
| Coluna | Tipo | Restrições |
|--------|------|------------|
| id | INTEGER | PK, autoincrement |
| statement | TEXT | NOT NULL (enunciado) |
| subject_id | INTEGER | NOT NULL, FK → subject(id) |
| difficulty | TEXT | NOT NULL, CHECK ∈ {Fácil, Médio, Difícil} *(D-03)* |
| created_at | TIMESTAMP | NOT NULL, default now |
| updated_at | TIMESTAMP | NOT NULL, default now |

**Tabela `alternative`**
| Coluna | Tipo | Restrições |
|--------|------|------------|
| id | INTEGER | PK, autoincrement |
| question_id | INTEGER | NOT NULL, FK → question(id) ON DELETE CASCADE |
| text | TEXT | NOT NULL |
| is_correct | INTEGER | NOT NULL, CHECK ∈ {0,1} |
| position | INTEGER | ordenação de exibição (opcional) |

- **Invariante "exatamente uma correta"** (RN-001): garantida na **service** (dentro de transação) e reforçada por **índice único parcial** em `alternative(question_id)` onde `is_correct=1`, além de checagem de contagem mínima (≥2) na service. *(Estratégia descrita; DDL na implementação.)*

**Tabela `attempt`**
| Coluna | Tipo | Restrições |
|--------|------|------------|
| id | INTEGER | PK, autoincrement |
| question_id | INTEGER | NOT NULL, FK → question(id) ON DELETE RESTRICT *(RN-005/D-07: bloquear exclusão)* |
| alternative_id | INTEGER | NOT NULL, FK → alternative(id) ON DELETE RESTRICT |
| is_correct | INTEGER | NOT NULL, CHECK ∈ {0,1} — **resultado congelado no momento da resposta** *(D-14)* |
| created_at | TIMESTAMP | NOT NULL, default now |
| student_id | INTEGER | **omitido no MVP** ; só existe se D-02 aprovar identidade |

- `attempt.is_correct` é **snapshot** do resultado no instante da resposta, para que editar o gabarito depois **não reescreva** o histórico (coerente com RN-004 append-only). Ver D-14 e seção 12.

## 5. Entidades e relacionamentos

| Relacionamento | Cardinalidade | Regra de integridade |
|----------------|---------------|----------------------|
| `subject` — `question` | 1 : N | `question.subject_id` obrigatório (RN-007). |
| `question` — `alternative` | 1 : N (≥2) | Composição; exclusão de questão remove alternativas (CASCADE), **mas** exclusão de questão com tentativas é bloqueada (RESTRICT em `attempt`). |
| `question` — `attempt` | 1 : N | ON DELETE RESTRICT (RN-005/D-07 proposto). |
| `alternative` — `attempt` (escolhida) | 1 : N | ON DELETE RESTRICT — não remover alternativa já referenciada por tentativa (ver D-15). |
| `student` — `attempt` | 1 : N | **Somente** se D-02 aprovar identidade; ausente no MVP proposto. |

**Observação de integridade**: como `attempt` referencia `alternative`, editar uma questão **não pode** excluir alternativas que já possuem tentativas. Estratégia proposta: edição atualiza textos/ordem no lugar e bloqueia remoção de alternativas referenciadas (RESTRICT), ou congela o texto escolhido na tentativa. Decisão D-15 / seção 12.

## 6. Rotas HTTP

> Proposta server-rendered + POST→Redirect→GET (D-12). `application/x-www-form-urlencoded` nos POST. CSRF em todos os POST (RNF-005). Códigos de erro conforme spec §11.

| Método | Caminho | Propósito | RF | Sucesso | Erros |
|--------|---------|-----------|----|---------|-------|
| GET | `/` | Página inicial / navegação. | RF-010 | 200 | — |
| GET | `/questions` | Listar + filtros (`?subject=&difficulty=`). | RF-004,005,010 | 200 | — |
| GET | `/questions/new` | Formulário de cadastro. | RF-001 | 200 | — |
| POST | `/questions` | Criar questão + alternativas. | RF-001,006 | 302 → `/questions/<id>` | 400 validação |
| GET | `/questions/<id>` | Visualizar questão. | RF-010 | 200 | 404 |
| GET | `/questions/<id>/edit` | Formulário de edição. | RF-002 | 200 | 404 |
| POST | `/questions/<id>` | Atualizar questão. | RF-002 | 302 → `/questions/<id>` | 400 / 404 / 409 (D-15) |
| POST | `/questions/<id>/delete` | Excluir questão. | RF-003 | 302 → `/questions` | 404 / 409 (RN-005) |
| GET | `/questions/<id>/answer` | Formulário de resposta (alternativas). | RF-006 | 200 | 404 |
| POST | `/questions/<id>/answer` | Corrigir + registrar tentativa. | RF-007,008 | 302 → resultado (ou 200 render) | 400 / 404 |
| GET | `/questions/<id>/result` | Exibir correção (PRG). | RF-007 | 200 | 404 |
| GET | `/history` | Histórico + filtros (`?subject=&difficulty=&from=&to=`). | RF-009 | 200 | — |

- **Assuntos para filtro**: catálogo enviado ao template via contexto (sem rota CRUD pública no MVP, D-04). Endpoint JSON opcional apenas se o aprimoramento JS exigir (D-12).
- **Idempotência/PRG**: POST de resposta redireciona ao resultado para evitar registro duplicado em refresh (consistência RF-007↔RF-008, CA-09).

## 7. Responsabilidades do backend

- **Rotas (controllers)**: parsear entrada, chamar service, escolher resposta (render/redirect), mapear erros para HTTP (spec §11). Sem SQL/regra de negócio.
- **Services**:
  - `question_service`: validar (RN-001/002/007), garantir "exatamente uma correta", criar/editar em **transação** (questão + alternativas atômicas), aplicar política de exclusão (RN-005).
  - `grading_service`: comparar alternativa escolhida × correta → resultado binário (RF-007, RN-003).
  - `attempt_service`: registrar tentativa **na mesma transação** da correção (RF-008), append-only (RN-004), com `is_correct` snapshot (D-14).
  - `history_service`: agregar métricas (total/acertos/erros/% acerto) e aplicar filtros (RF-009, RN-006/D-08).
- **Repositories**: SQL **parametrizado**, transações, mapeamento linha↔objeto. Sem regra de negócio.
- **db**: conexão por request/app, `foreign_keys=ON`, init de schema, fechamento adequado.
- **Transações obrigatórias**: (a) criar/editar questão+alternativas; (b) corrigir+registrar tentativa. Garante RNF-004 e CA-09.
- **Erros/log**: mensagem genérica ao usuário + log técnico (spec §11), sem vazar SQL/stack.

## 8. Comunicação frontend/backend

- **Renderização**: Jinja2 no servidor; **autoescape ligado** (mitiga XSS — CA-14/RNF-005).
- **Envio**: formulários HTML `POST` (`application/x-www-form-urlencoded`); **POST→Redirect→GET**.
- **CSRF**: token em todos os formulários POST (Flask-WTF ou token manual — D-16). Requisito de segurança (RNF-005).
- **JavaScript (vanilla)**: conveniência — validação client-side espelhando a do servidor, auto-submit de filtros, feedback inline. **Aprimoramento progressivo**: o fluxo completo funciona **sem JS** (RNF-003/006).
- **Fetch/JSON (opcional)**: apenas se aprovado (D-12) para correção sem reload; caso contrário, navegação clássica. MVP proposto: **sem dependência de fetch**.
- **Estilo**: CSS próprio, interface simples em PT-BR (RNF-006).
- **UX (Constitution §5)**: layout **responsivo desktop + mobile** (CSS próprio, sem framework externo — Princípio III); **acessibilidade** (labels associados aos campos, contraste, navegação por teclado); **consistência** visual entre telas. *Origem §5; o spec RNF-006 ainda não cita mobile/acessibilidade — lacuna reportada em G3 (spec não alterado).*
- **Feedback (§5)**: toda ação importante retorna confirmação/erro visível — submeter resposta → correção imediata; cadastrar/editar/excluir → mensagem de sucesso ou erro por campo (spec §11; falha silenciosa proibida).
- **Contrato de erro**: servidor reexibe o formulário com valores preenchidos + mensagens por campo (spec §11).

## 9. Validação de dados

**Autoridade = servidor** (RNF-005); cliente apenas conveniência. Matriz (regras do spec RN-001/002/007, CA-02/CA-04):

| Campo / Ação | Regra | Erro (spec §11) |
|--------------|-------|-----------------|
| `statement` | obrigatório, não vazio; comprimento máx. proposto *(D-05/RNF)* | 400 "enunciado obrigatório" |
| `subject` | obrigatório; deve existir no catálogo (FK) | 400 "assunto inválido" |
| `difficulty` | ∈ {Fácil, Médio, Difícil} *(D-03)* | 400 "dificuldade inválida" |
| `alternatives` | ≥2 e ≤ máx. proposto (6) *(D-05)*; textos não vazios | 400 "mínimo de 2 alternativas" |
| `is_correct` | **exatamente uma** alternativa correta | 400 "selecione exatamente uma correta" |
| resposta (`alternative_id`) | pertence à questão respondida | 400 "alternativa inválida" / 404 |
| `<id>` inexistente | questão não encontrada | 404 (CA-13) |
| exclusão com tentativas | bloqueada (RN-005/D-07) | 409 (CA-05) |
| entrada maliciosa | SQL parametrizado + autoescape | CA-14 |

- Validação ocorre **antes** de persistir; operação inválida **não** altera o banco (CA-02/CA-04).
- Comprimento/tipos sanitizados no servidor; nenhuma confiança em validação client-side.

## 10. Estratégia de testes

**Ferramentas**: **Pytest** (Constitution §3) + Flask test client; SQLite **em memória/arquivo temporário** por teste; fixtures/seed em `tests/conftest.py` (RNF-008). Sem código neste plano.

| Camada | O que testa | CAs / RFs |
|--------|-------------|-----------|
| **Unit — services** | correção (correta/incorreta + gabarito), validação (RN-001/002/007), política de exclusão (RN-005), agregação de histórico (RN-006). | CA-02,04,07,08,11,12 |
| **Unit — validação** | ≥2 alternativas, exatamente 1 correta, dificuldade enum, campos obrigatórios. | CA-02,04 |
| **Integração — repositories** | persistência CRUD, FK/integridade, invariante "1 correta", atomicidade criar questão+alternativas e corrigir+tentativa. | CA-01,03,09,10; RNF-004 |
| **Rotas/funcional** | Fluxos A e B via test client: status 200/302/400/404/409, PRG, filtros, reexibição com erros. | CA-01…13 |
| **Segurança** | payloads SQL injection e XSS/HTML armazenados e renderizados escapados; CSRF ausente/ inválido rejeitado. | CA-14; RNF-005 |
| **Regressão** | cada CA do spec mapeado a ≥1 teste automatizado. | todos |
| **Manual — UI** | checklist em navegador **desktop + mobile** (§5): golden path + bordas (sem JS, com JS, filtros, mensagens, feedback, acessibilidade). | RNF-006; §5 |

- **Critério de "completo" (Constitution §4)**: uma funcionalidade só é considerada concluída quando **seus CA forem satisfeitos E os testes relevantes passarem**. Nenhuma tarefa é marcada como concluída antecipadamente (Princípio V; regra do usuário).
- **Evidência de testes rastreável (Princípio VI)**: resultados da suíte Pytest associados aos commits; cada CA mapeado a ≥1 teste (tabela acima) para auditoria spec↔implementação (§4).
- **Meta de cobertura (proposta)**: alta cobertura da lógica de negócio (correção/validação/histórico); sem percentual obrigatório até aprovação.
- **Limitação do ambiente**: teste de UI em navegador **não é automatizável aqui**; deve ser executado por humano/dev (desktop + mobile) antes de considerar concluído (ver risco R-11).
- **Pirâmide**: muitas unit (services) > integração (repos/rotas) > manual (UI).

## 11. Riscos técnicos

| ID | Risco | Prob. | Impacto | Mitigação |
|----|-------|-------|---------|-----------|
| **R-01** | Lacunas de conformidade spec/tasks × Constitution (G1–G6) ainda não emendadas. | Média | Alto | Constitution localizada (D-01 resolvida); reportar G-xx e aguardar decisão humana item a item antes de implementar (§8). |
| **R-02** | Identidade/autenticação indefinida (D-02) → retrabalho de schema (`student`, FK em `attempt`). | Média | Alto | Decidir D-02 antes do DDL; isolar repositórios para minimizar impacto. |
| **R-03** | Editar gabarito após tentativas → histórico inconsistente. | Média | Alto | `is_correct` snapshot (D-14); definir semântica e aprovar (seção 12). |
| **R-04** | Editar/remover alternativa referenciada por tentativa → FK órfã. | Média | Alto | RESTRICT + edição no lugar ou snapshot de texto (D-15). |
| **R-05** | Invariante "exatamente uma correta" violada em create/edit concorrente. | Média | Médio | Transação + índice único parcial + validação na service. |
| **R-06** | Política de exclusão (RN-005) divergente entre FK e service. | Baixa | Médio | RESTRICT no banco + checagem na service; teste de 409. |
| **R-07** | Concorrência de escrita do SQLite se houver rede/múltiplos usuários (D-11/D-02). | Baixa | Médio | MVP local single-usuário; WAL/timeout se rede for aprovada. |
| **R-08** | SQL injection / XSS. | Média | Alto | SQL parametrizado + autoescape + CSRF (RNF-005, CA-14). |
| **R-09** | Evolução de schema sem ferramenta de migração. | Média | Médio | `schema.sql` versionado; migração simples/manual no MVP (D-17); adotar Alembic só se necessário. |
| **R-10** | Notação matemática indefinida (D-06) → retrabalho de frontend. | Média | Médio | Texto/Unicode no MVP; MathJax só se aprovado. |
| **R-11** | Correção de UI não verificada em navegador neste ambiente. | Alta | Médio | Checklist manual obrigatório antes de concluir; não declarar sucesso sem teste real. |
| **R-12** | Scope creep além das 8 funcionalidades. | Média | Médio | Seção "fora do escopo" do spec é vinculante; novas ideias exigem aprovação (§6). |
| **R-13** | Divergência de paths: plano usa `app/` (scaffold real) × `tasks.md` usa `mathlab/...`. | Alta | Médio | Reportado em G6; alinhar `tasks.md` ao repo só após aprovação (não alterado silenciosamente). |
| **R-14** | Artefatos `specs/` ainda **untracked** no Git; sem commits → rastreabilidade incompleta (Princípio VI). | Alta | Médio | Commit dos artefatos só com aprovação explícita do usuário; evidência de testes versionada junto à implementação. |

## 12. Pontos que afetam spec/tasks (NÃO alterados silenciosamente)

**`spec.md` e `tasks.md` não foram modificados.** Conforme a decisão humana "só reportar, eu decido", as lacunas abaixo ficam **reportadas** e aguardam aprovação **item a item** antes de qualquer emenda. A Constitution (§8) prevalece enquanto não emendados.

### 12.1 Lacunas de design (afetam o spec)

1. **Semântica do histórico após editar gabarito** (R-03/D-14): o spec define tentativas como append-only (RN-004), mas não diz se `is_correct` histórico é **snapshot** (proposto) ou **recomputado**. Impacta RN-004/RN-006 e CA-11.
2. **Edição de alternativas com tentativas** (R-04/D-15): o spec (RF-002) permite editar alternativas, mas não define o que ocorre se a alternativa já foi respondida. Impacta RF-002/RF-008 e integridade (RNF-004).
3. **Comprimento máximo de enunciado/alternativas** (D-05): não definido no spec; necessário para validação determinística.

### 12.2 Lacunas de conformidade com a Constitution (afetam spec/tasks/repo)

| ID | Lacuna (verificada) | Onde | Constitution | Emenda proposta (a aprovar) |
|----|---------------------|------|--------------|------------------------------|
| **G1** | `specs/` está **untracked** no Git; nenhum commit dos artefatos → rastreabilidade incompleta. | repo (`git status`) | Princípio VI | Commitar spec/plan/tasks com aprovação explícita; commits significativos por fase. |
| **G1b** | `tasks.md` (T001–T048) **não tem** tarefa de commit/versionamento nem de registrar evidência de testes no histórico Git. | `tasks.md` | Princípio VI; §4 | Acrescentar tarefas de Git (commit por fase) e de evidência Pytest associada aos commits. |
| **G1c** | Nota "Constitution **não existe**/pendente (D-01)" ainda presente, mas o arquivo **já foi localizado**. | `spec.md` (topo) e `tasks.md` (linha 10) | §8 | Atualizar a nota para "Constitution v1.0.0 presente"; marcar D-01 como resolvida. |
| **G2** | Stack obrigatória lista só Python/Flask/SQLite/HTML/CSS/JS; omite **Pytest** e **Git/GitHub**. | `spec.md` RNF-001 (e cabeçalho de `tasks.md`) | §3 | Acrescentar Pytest + Git/GitHub à stack obrigatória. |
| **G3** | RNF-006 diz só "interface simples em PT-BR"; não cita **mobile** nem **acessibilidade**. | `spec.md` RNF-006 | §5 | Ampliar RNF-006: responsivo desktop+mobile, acessível, feedback em ações importantes. |
| **G4** | T045 (README) cobre instalar/init/run/test, mas **omite propósito do projeto e stack**. | `tasks.md` T045 | §7 | README deve explicar: propósito, stack, instalação/config, execução e testes. |
| **G5** | Justificativa técnica de nova dependência (ex.: **Flask-WTF** em D-16) não registrada formalmente. | `plan.md` D-16 / `tasks.md` T003 | §3 | Documentar o propósito técnico de cada dependência antes de adicioná-la. |
| **G6** | `tasks.md` usa paths `mathlab/...` e `mathlab/tests/`; o scaffold real (e este plano) é `app/` + `tests/` na raiz. | `tasks.md` (T004–T045) | §4 (consistência); III | Alinhar os paths das tarefas ao repo (`app/`, `tests/`) — ver R-13. |

> Nenhuma emenda G-xx foi aplicada. Este plano já **observa** a Constitution (§8) em suas próprias seções (stack §3, UX §5, testes §4, rastreabilidade VI); as divergências remanescentes em `spec.md`/`tasks.md`/repo estão **somente reportadas** aqui para decisão humana.

## 13. Decisões que necessitam de aprovação humana

**D-01 (Constitution ausente) — RESOLVIDA**: o arquivo `.specify/memory/constitution.md` (v1.0.0) foi localizado em `C:\Users\Eliseu\mathlab` e lido. Este plano foi alinhado a ela (seção 14). Restam apenas as notas stale em spec/tasks (G1c), a emendar com aprovação.

**D-02…D-11** (spec §13) e **D-12…D-17** (abaixo) continuam **pendentes** de aprovação humana. As **emendas de conformidade G1–G6** (seção 12.2) também aguardam decisão **item a item** ("só reportar, eu decido") — nenhuma foi aplicada a `spec.md`/`tasks.md`.

Além das decisões do spec, o plano acrescenta decisões de design:

| # | Decisão de design | Proposta (a confirmar) |
|---|-------------------|------------------------|
| **D-12** | Estilo de comunicação: forms server-rendered + PRG vs JSON/fetch. | **Forms + PRG**, JS como aprimoramento progressivo (funciona sem JS). |
| **D-13** | Acesso a dados: `sqlite3` padrão vs ORM (SQLAlchemy). | **`sqlite3` padrão** (simplicidade), SQL parametrizado. |
| **D-14** | `attempt.is_correct`: snapshot vs recomputado ao editar gabarito. | **Snapshot** (histórico estável). |
| **D-15** | Editar/remover alternativa já respondida. | **RESTRICT** (bloquear remoção) + edição de texto no lugar; ou snapshot do texto escolhido. |
| **D-16** | Mecanismo de CSRF/validação de form. | **Flask-WTF** (ou token manual) — decidir para manter dependências mínimas. |
| **D-17** | Migração de schema. | **`schema.sql` + init** no MVP; Alembic apenas se a base evoluir muito. |

### Rastreabilidade RF → módulos / rotas / entidades / testes

| RF | Módulos | Rotas | Entidades | Testes (CA) |
|----|---------|-------|-----------|-------------|
| RF-001 | questions, question_service, question_repo | POST `/questions` | question, alternative, subject | CA-01,02 |
| RF-002 | questions, question_service | GET/POST `/questions/<id>/edit`, POST `/questions/<id>` | question, alternative | CA-03,04 |
| RF-003 | questions, question_service | POST `/questions/<id>/delete` | question, attempt | CA-05 |
| RF-004 | questions, subject_repo | GET `/questions?subject=` | subject, question | CA-06 |
| RF-005 | questions, validators | GET `/questions?difficulty=` | question | CA-06 |
| RF-006 | questions, question_service | GET `/questions/new`, `/questions/<id>/answer` | alternative | CA-01,02,07,08 |
| RF-007 | attempts, grading_service | POST `/questions/<id>/answer`, GET result | alternative, attempt | CA-07,08 |
| RF-008 | attempts, attempt_service, attempt_repo | POST `/questions/<id>/answer` | attempt | CA-09,10 |
| RF-009 | history, history_service, attempt_repo | GET `/history` | attempt | CA-11,12 |
| RF-010 | questions, question_repo | GET `/`, `/questions`, `/questions/<id>` | question | CA-06,13 |

## 14. Conformidade com a Constitution (v1.0.0)

Mapeamento explícito de cada princípio/seção para onde **este plano** o atende. "Conforme (plano)" = o documento já observa a exigência; lacunas em `spec.md`/`tasks.md`/repo estão **reportadas** (G-xx, seção 12.2) e **não emendadas** sem aprovação. A Constitution **não foi alterada**.

| Item | Exigência (resumo) | Onde este plano atende | Status |
|------|--------------------|------------------------|--------|
| **Princípio I** — Educational Value | Prática matemática significativa > funcionalidade desnecessária. | Escopo às 8 funcionalidades; spec §12 vinculante; §11 R-12. | Conforme (plano). |
| **Princípio II** — Correctness/Reliability | Comportamento crítico verificável por testes automatizados. | §10 (Pytest; correção/validação/histórico; CA→teste). | Conforme (plano). |
| **Princípio III** — Simplicity/Maintainability | Modular, legível; sem deps/complexidade desnecessárias. | §1 camadas; §2 módulos; `sqlite3` sem ORM (D-13); CSS/JS próprios. | Conforme (plano). |
| **Princípio IV** — SDD | Specify→Plan→Tasks→Implement; sem feature major sem spec+plan aprovados. | Artefatos spec/plan/tasks; portões T001/T002; status "revisão humana". | Conforme (plano); aprovação pendente. |
| **Princípio V** — Human Supervision | Todo output de IA revisado; owner roda testes/rejeita. | Status rascunho; §10 "completo = CA + testes"; D/G pendentes de humano. | Conforme (plano). |
| **Princípio VI** — Version Control/Traceability | Git/GitHub; commits significativos; spec/plan/tasks/impl/evidência rastreáveis. | §1 rastreabilidade; §10 evidência de testes; repo Git. | **Parcial** — G1/G1b/R-14 (`specs/` untracked, sem commits). |
| **§3** — Technical Standards | Python/Flask/SQLite/HTML/CSS/JS/**Pytest**/**Git-GitHub**; nova dep justificada. | Cabeçalho Stack; §10 Pytest; `requirements.txt` (§3). | Conforme (plano); G2 (spec) / G5 (justificativa) pendentes. |
| **§4** — Quality/Testing | Validar entrada; tratar erros; integridade; testar lógica; consistência spec↔impl; completo = CA + testes. | §9 validação; §7 erros/transações; §10 critério de completo. | Conforme (plano). |
| **§5** — User Experience | Clareza/acessibilidade/consistência/navegação; **desktop+mobile**; feedback em ações importantes. | §8 UX + feedback; §10 manual desktop+mobile. | Conforme (plano); G3 (spec RNF-006) pendente. |
| **§6** — Scope Management | MVP primeiro; avaliar novas features; sem fora-do-escopo sem revisar spec/plan. | spec §12 vinculante; §11 R-12. | Conforme (plano). |
| **§7** — Documentation | README: propósito, stack, instalação/config, execução, testes. | §3 árvore (`README.md`); tarefa T045. | **Parcial** — G4 (T045 omite propósito/stack). |
| **§8** — Governance | Constitution governa tudo; em conflito, **prevalece** até emenda formal. | Cabeçalho; §12/§13 reportam sem alterar spec/tasks; esta seção. | Conforme (plano). |

> **Síntese**: o **plano** está alinhado à Constitution v1.0.0. A conformidade de **spec/tasks/repo** tem lacunas **G1–G6** (seção 12.2) apenas **reportadas**, aguardando decisão humana item a item. Nenhuma emenda foi aplicada; a Constitution não foi alterada; nenhum código foi implementado.