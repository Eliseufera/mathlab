# Tarefas de Implementação — Banco de Questões de Matemática (MathLab)

- **Feature**: `001-question-bank`
- **Documento**: `specs/001-question-bank/tasks.md`
- **Base**: [`spec.md`](./spec.md) (RF-001…RF-010, RNF-001…RNF-009, RN-001…RN-008, CA-01…CA-14), [`plan.md`](./plan.md) (alinhado; seções 1–14) e [Constitution v1.0.0](../../.specify/memory/constitution.md) (Princípios I–VI, §3–§8)
- **Stack (Constitution §3)**: Python + Flask + SQLite + HTML + CSS + JavaScript + **Pytest** + **Git/GitHub**
- **Repositório**: `C:\Users\Eliseu\mathlab` (Git — Princípio VI); scaffold real `app/` (pacote) + `tests/` na raiz; `instance/` com `*.sqlite` gitignored (dados não versionados)
- **Status**: Rascunho para revisão humana (Princípios IV/V — supervisão humana obrigatória)

> **Sem código**: este documento **não implementa código**; apenas divide a implementação em tarefas pequenas e ordenadas por dependência. Nomes de arquivos são indicativos (alinhados ao scaffold real e ao `plan.md`).
>
> **Nenhuma tarefa concluída antecipadamente**: todas estão **[ ] Pendente**. Uma tarefa só é marcada **[x] Concluída** quando seu **critério de conclusão** for realmente atendido **e** os testes relevantes passarem (Constitution §4: "completo = CA satisfeitos E testes passando"; Princípio V — supervisão humana). Nenhum `[x]` foi pré-marcado.
>
> **Constitution presente e prevalente (§8)**: `.specify/memory/constitution.md` (v1.0.0) **foi localizada e lida**. A decisão **D-01 está RESOLVIDA** (a Constitution existe). `T001` deixa de ser "portão para criar a Constitution" e passa a **validar a conformidade** spec/plan/tasks contra ela. Em conflito, **a Constitution prevalece** até emenda formal.
>
> **Paths reais (`app/` + `tests/`)**: as tarefas usam o scaffold real do repo (`app/…`, `tests/…`), **não** os paths antigos `mathlab/…`. Isso resolve a lacuna **G6 / risco R-13** reportada no `plan.md` §12.2. O `spec.md` **não foi alterado**.
>
> **Não alteração silenciosa do spec**: lacunas de conformidade que afetam o **spec** (**G2** — RNF-001 omite Pytest/Git; **G3** — RNF-006 omite mobile/acessibilidade; **G1c-spec** — nota obsoleta "Constitution não existe") permanecem **reportadas no `plan.md` §12.2 e aguardam decisão humana item a item** ("só reportar, eu decido"). Este `tasks.md` já incorpora as emendas do lado das tarefas (G1b/G4/G6/G1c-tasks/cabeçalho da stack) como consequência do pedido explícito de regeneração, **sem** tocar o spec. A sincronização do `plan.md` §12.2/§13/§14 (que ainda descreve este arquivo como "não alterado") é tarefa **T050**, sujeita a aprovação.
>
> **Ordem por dependência**: a numeração `T001…T050` já é uma **ordem topológica válida** (toda dependência aparece antes da tarefa). As fases são agrupamentos temáticos; dependências cruzam fases quando necessário.
>
> **Rastreabilidade Git (Princípio VI)**: commits significativos por fase; artefatos SDD versionados (**T003**); evidência de testes versionada (**T045**); fecho/parecer de conformidade (**T050**). **Nenhum commit é feito sem aprovação explícita do usuário.**

**Legenda de campos** — cada tarefa tem: **Descrição**; **Arquivos** (envolvidos); **Requisitos** (RF/RNF/RN/CA do spec; D/G/R/§ do plan; princípio/§ da Constitution); **Conclusão** (critério verificável / Definition of Done); **Dependências** (IDs); **Status**.

**Portões de aprovação humana**: `T001` (validar conformidade com a Constitution) e `T002` (decidir D-02…D-17 + emendas G1–G6). Sem eles, schema e regras ficam indeterminados e **nenhuma tarefa de implementação deve iniciar**.

---

## Fase 1 — Configuração

### T001 — Validar conformidade spec/plan/tasks contra a Constitution
- **Descrição**: Ler a Constitution v1.0.0 e auditar `spec.md`, `plan.md` e este `tasks.md` contra os Princípios I–VI e §3–§8. Confirmar que D-01 está resolvida (Constitution presente) e consolidar a lista de lacunas de conformidade (G1–G6) para decisão humana. Não alterar a Constitution nem o spec.
- **Arquivos**: `.specify/memory/constitution.md` (leitura), `specs/001-question-bank/spec.md` (leitura), `specs/001-question-bank/plan.md` (leitura), `specs/001-question-bank/tasks.md` (leitura).
- **Requisitos**: Constitution §8 (governança/prevalência), Princípio IV (SDD), Princípio V (supervisão); plan §12.2 (G1–G6), §14 (mapa de conformidade); D-01 (RESOLVIDA).
- **Conclusão**: Parecer de conformidade registrado (lista G1–G6 confirmada/atualizada); D-01 marcada resolvida; nenhuma alteração silenciosa em Constitution/spec. Aprovado pelo usuário antes de T002.
- **Dependências**: — (primeira tarefa).
- **Status**: [x] Concluída — auditoria de conformidade confirmada (plan §14; D-01 resolvida; lacunas G1–G6 reportadas, não aplicadas ao spec).

### T002 — Aprovar decisões pendentes (D-02…D-17) e emendas (G1–G6)
- **Descrição**: Submeter ao usuário, item a item, as decisões de design D-02…D-17 (identidade, dificuldade, assunto, nº de alternativas, notação, política de exclusão, métricas, append-only, metas, implantação, PRG/fetch, sqlite3 vs ORM, snapshot de gabarito, edição de alternativa referenciada, CSRF, migração) e as emendas de conformidade G1–G6. Registrar as respostas; **não aplicar** emendas no spec sem aprovação explícita.
- **Arquivos**: `specs/001-question-bank/plan.md` (§12–§13), `specs/001-question-bank/spec.md` (§13 — somente leitura até aprovação), registro de decisões (a versionar em T048).
- **Requisitos**: Constitution Princípio V, §6 (escopo), §8; spec D-02…D-11; plan D-12…D-17, G1–G6; RN-001/002/005/006/008.
- **Conclusão**: Cada D-02…D-17 e cada G1–G6 tem decisão humana registrada (aprovar/rejeitar/alterar). Parâmetros de schema/validação deixam de ser indeterminados. Emendas no spec só ocorrem se explicitamente aprovadas.
- **Dependências**: T001.
- **Status**: [ ] Pendente — baseline D-02…D-17 (propostas de MVP) adotada por instrução do usuário ("implemente o MVP / siga os requisitos aprovados"); emendas G1–G6 ao spec seguem pendentes de decisão item a item (não aplicadas).

### T003 — Versionar artefatos SDD no Git e estabelecer commit por fase
- **Descrição**: Garantir que `specs/`, `.specify/` e demais artefatos SDD estejam rastreados no Git (resolve G1). Definir a política de commits significativos por fase (Princípio VI). **Executar commits somente com aprovação explícita do usuário.**
- **Arquivos**: repositório Git (`C:\Users\Eliseu\mathlab`), `specs/001-question-bank/{spec,plan,tasks}.md`, `.specify/memory/constitution.md`, `.gitignore`.
- **Requisitos**: Constitution Princípio VI (Git/GitHub, rastreabilidade), §3; plan G1, R-13; RNF-001.
- **Conclusão**: Artefatos SDD rastreados (não mais untracked); política de commit por fase documentada; histórico Git reflete specs→plan→tasks. Nenhum commit feito sem aprovação.
- **Dependências**: T001, T002.
- **Status**: [ ] Pendente.

### T004 — Preparar ambiente e dependências com justificativa técnica
- **Descrição**: Definir ambiente Python local (Windows), `requirements.txt` com Flask e Pytest; incluir Flask-WTF **somente se D-16 aprovar**. Justificar tecnicamente cada dependência (Constitution §3 — novas deps precisam de propósito). Confirmar execução offline (RNF-003).
- **Arquivos**: `requirements.txt`, `.gitignore` (já ignora `.venv/`, `__pycache__/`, `*.sqlite`, `.pytest_cache/`), `README.md` (esboço de instalação — completo em T047).
- **Requisitos**: Constitution §3 (stack/justificativa de deps), Princípio III (simplicidade); RNF-001/003/009; plan G5, D-16.
- **Conclusão**: Ambiente instalável e executável localmente sem rede; cada dependência tem justificativa; nenhuma dep supérflua. Aprovado pelo usuário.
- **Dependências**: T002.
- **Status**: [x] Concluída — .venv com Flask 3.1.3 + Pytest 9.2.0; requirements.txt justificado (CSRF manual, sem Flask-WTF); validado por 7 testes Pytest.

### T005 — Criar esqueleto de pacotes `app/` e `tests/`
- **Descrição**: Estruturar o pacote `app/` (com subpacotes `blueprints/`, `services/`, `repositories/`, `templates/`, `static/css`, `static/js`) e `tests/` (com `unit/`, `integration/`, `routes/`) conforme plan §3, sobre o scaffold real. Sem lógica de negócio ainda.
- **Arquivos**: `app/__init__.py` (placeholder), `app/blueprints/`, `app/services/`, `app/repositories/`, `app/templates/`, `app/static/css/`, `app/static/js/`, `tests/unit/`, `tests/integration/`, `tests/routes/`.
- **Requisitos**: RNF-002 (modularidade); Constitution Princípio III; plan §2–§3; G6/R-13 (paths reais).
- **Conclusão**: Árvore de diretórios/pacotes criada e importável; separação de camadas refletida na estrutura; nenhum código de regra de negócio implementado.
- **Dependências**: T004.
- **Status**: [x] Concluída — pacotes app/{blueprints,services,repositories} + tests/{unit,integration,routes} criados e importáveis.

### T006 — Módulo de configuração `app/config.py`
- **Descrição**: Definir configurações (caminho do DB em `instance/`, secret key, ambiente dev/test/prod) de forma simples. Prever config de teste com DB temporário/em memória. Sem valores sensíveis versionados.
- **Arquivos**: `app/config.py`, `instance/` (gitignored via `*.sqlite`).
- **Requisitos**: RNF-003/009; Constitution §4 (integridade), Princípio III; plan §2 (config), D-11.
- **Conclusão**: Config carregável por ambiente; caminho do DB e secret key definidos; config de teste isola dados; nenhum segredo no Git.
- **Dependências**: T005.
- **Status**: [x] Concluída — app/config.py validado (defaults, overrides, DATABASE em instance/, constantes D-03/D-05); SECRET_KEY via env (placeholder dev, sem segredo real).

---

## Fase 2 — Backend Flask

### T007 — App factory `create_app()`
- **Descrição**: Implementar a fábrica `create_app` em `app/__init__.py`: carregar config, registrar blueprints, inicializar DB e tratamento de erros. Base para testabilidade (Flask test client).
- **Arquivos**: `app/__init__.py`, `app/config.py`.
- **Requisitos**: RNF-002/008; Constitution §4, Princípio III; plan §1–§2 (app factory).
- **Conclusão**: `create_app()` retorna app Flask configurado; blueprints registrados; app de teste criável com DB isolado; sem regra de negócio nas rotas.
- **Dependências**: T006.
- **Status**: [ ] Pendente — fundação create_app() criada e testada (config + instance path); registro de DB/erros/CSRF/blueprints completa a tarefa em T008–T011.

### T008 — Conexão SQLite e `PRAGMA foreign_keys=ON`
- **Descrição**: Implementar `app/db.py`: conexão por request/app, `PRAGMA foreign_keys=ON`, helpers de transação e fechamento adequado. Sem SQL de negócio aqui.
- **Arquivos**: `app/db.py`.
- **Requisitos**: RNF-004 (integridade/FK); Constitution §4, Princípio II; plan §1/§7 (db), D-13.
- **Conclusão**: Conexão reutilizável; FK habilitadas em toda conexão; transações e fechamento corretos; verificável por teste de integridade.
- **Dependências**: T007.
- **Status**: [ ] Pendente.

### T009 — Tratamento centralizado de erros HTTP
- **Descrição**: Mapear erros para os códigos do spec §11 (400 validação, 404 não encontrado, 409 regra de negócio, 500 genérico). Mensagem genérica ao usuário + log técnico, sem vazar SQL/stack.
- **Arquivos**: `app/__init__.py` (handlers) ou `app/errors.py`, `app/templates/` (páginas de erro).
- **Requisitos**: spec §11; CA-13; RNF-005; Constitution §4 (erros sem crash); plan §7/§9.
- **Conclusão**: Erros retornam códigos corretos e mensagem clara; nenhum stack/SQL exposto; falha silenciosa proibida (toda ação responde).
- **Dependências**: T007.
- **Status**: [ ] Pendente.

### T010 — CSRF e autoescape (segurança web básica)
- **Descrição**: Habilitar proteção CSRF em todos os POST (Flask-WTF se D-16, ou token manual) e confirmar Jinja2 autoescape ligado. Base para CA-14/RNF-005.
- **Arquivos**: `app/__init__.py`, `app/templates/base.html`, `app/config.py` (secret key).
- **Requisitos**: RNF-005; CA-14; Constitution §4 (proteger integridade), Princípio II; plan §8, D-16.
- **Conclusão**: POST sem token CSRF válido é rejeitado; saída HTML escapada por padrão; decisão D-16 aplicada conforme aprovação.
- **Dependências**: T007, T002.
- **Status**: [ ] Pendente.

### T011 — Blueprints (esqueleto) e rota inicial `GET /`
- **Descrição**: Registrar blueprints `questions`, `attempts` (ou agrupado em questions), `history` e a rota inicial de navegação. Controllers finos, sem SQL/regra de negócio.
- **Arquivos**: `app/blueprints/questions.py`, `app/blueprints/attempts.py`, `app/blueprints/history.py`, `app/templates/base.html`.
- **Requisitos**: RF-010; RNF-002; Constitution Princípio III; plan §2/§6 (rotas), D-12.
- **Conclusão**: Blueprints registrados; `GET /` responde 200 com navegação; estrutura de rotas pronta para receber handlers nas fases seguintes.
- **Dependências**: T007, T009.
- **Status**: [ ] Pendente.

---

## Fase 3 — Banco de dados

### T012 — Schema DDL `app/schema.sql`
- **Descrição**: Escrever o DDL das tabelas `subject`, `question`, `alternative`, `attempt` conforme plan §4 (tipos, FK, CHECKs, `ON DELETE CASCADE/RESTRICT`, índice único parcial para "exatamente uma correta"). `student` só se D-02 aprovar. Parâmetros seguem D-02…D-07/D-14/D-15 aprovados.
- **Arquivos**: `app/schema.sql`.
- **Requisitos**: RNF-004; RN-001/005/007; CA-01/09/10; Constitution §4, Princípio II; plan §4–§5, D-02…D-07/D-14/D-15.
- **Conclusão**: DDL cria todas as tabelas/restrições; FK e CHECKs corretos; índice único parcial garante ≤1 correta; schema coerente com decisões aprovadas.
- **Dependências**: T002, T008.
- **Status**: [ ] Pendente.

### T013 — Inicialização idempotente do banco (`init_db`)
- **Descrição**: Implementar init de schema a partir de `schema.sql`, idempotente, criando `instance/` se necessário. Integrar ao app factory e ao setup de testes.
- **Arquivos**: `app/db.py`, `app/schema.sql`, `app/__init__.py`.
- **Requisitos**: RNF-004/008; Constitution §4; plan §1/§7, D-17 (migração simples no MVP).
- **Conclusão**: `init_db` cria o schema uma vez e pode ser reexecutado sem erro; DB de teste inicializável; dados em `instance/` (gitignored).
- **Dependências**: T012.
- **Status**: [ ] Pendente.

### T014 — Catálogo de assuntos (seed)
- **Descrição**: Popular o catálogo simples de `subject` conforme D-04 (lista pré-definida/curta, sem CRUD no MVP). Seed idempotente.
- **Arquivos**: `app/db.py` ou `app/repositories/subject_repo.py` (seed), `app/schema.sql`.
- **Requisitos**: RF-004; RN-007; Constitution §6 (escopo MVP); plan §4 (subject), D-04.
- **Conclusão**: Catálogo de assuntos disponível para classificação/filtro; seed não duplica; nenhum CRUD público de assuntos (salvo aprovação).
- **Dependências**: T013.
- **Status**: [ ] Pendente.

### T015 — Repositório de questões `question_repo.py`
- **Descrição**: Acesso a dados de `question` (criar, ler, atualizar, listar/filtrar, excluir) com SQL **parametrizado** e transações. Sem regra de negócio.
- **Arquivos**: `app/repositories/question_repo.py`.
- **Requisitos**: RF-001/002/003/004/005/010; RNF-004/005; Constitution §4, Princípio II/III; plan §2/§7.
- **Conclusão**: CRUD de questão persiste/recupera corretamente; consultas parametrizadas (sem injection); filtros por assunto/dificuldade funcionam; mapeamento linha↔objeto correto.
- **Dependências**: T013.
- **Status**: [ ] Pendente.

### T016 — Repositório de alternativas + invariante "1 correta"
- **Descrição**: Acesso a `alternative` (CRUD vinculado à questão, ordenação), reforçando a invariante "exatamente uma correta" via índice único parcial + contagem mínima (≥2) em conjunto com a service. Edição no lugar / bloqueio de remoção referenciada conforme D-15.
- **Arquivos**: `app/repositories/question_repo.py` (ou `alternative_repo.py`), `app/schema.sql`.
- **Requisitos**: RF-006; RN-001; RNF-004; CA-01/02/04; Constitution §4, Princípio II; plan §4–§5, D-05/D-15, R-04/R-05.
- **Conclusão**: Persistência de alternativas atômica com a questão; impossible ter 0 ou >1 correta; remoção de alternativa referenciada por tentativa é bloqueada (RESTRICT) ou tratada conforme D-15.
- **Dependências**: T015, T012.
- **Status**: [ ] Pendente.

### T017 — Repositório de tentativas `attempt_repo.py`
- **Descrição**: Acesso a `attempt` (inserir append-only, consultar por questão/filtros). `is_correct` como snapshot (D-14). Sem edição/exclusão pelo usuário (D-09). SQL parametrizado.
- **Arquivos**: `app/repositories/attempt_repo.py`.
- **Requisitos**: RF-008/009; RN-004/005; RNF-004; CA-09/10; Constitution §4, Princípio II; plan §4/§7, D-07/D-09/D-14.
- **Conclusão**: Tentativas inseridas e consultáveis; append-only (sem update/delete exposto); FK RESTRICT impede órfãs; snapshot de resultado preservado.
- **Dependências**: T013.
- **Status**: [ ] Pendente.

### T018 — Repositório de assuntos (leitura) `subject_repo.py`
- **Descrição**: Leitura do catálogo de `subject` para preencher selects de cadastro e filtros. Sem CRUD no MVP (D-04).
- **Arquivos**: `app/repositories/subject_repo.py`.
- **Requisitos**: RF-004; RN-007; Constitution §6; plan §2/§6, D-04.
- **Conclusão**: Catálogo recuperável para templates/filtros; somente leitura; coerente com o seed de T014.
- **Dependências**: T014.
- **Status**: [ ] Pendente.

---

## Fase 4 — CRUD de questões

### T019 — Validação de entrada no servidor `app/validators.py`
- **Descrição**: Regras de validação (autoridade = servidor): enunciado obrigatório; assunto existente (FK); dificuldade ∈ conjunto fechado (D-03); ≥2 e ≤máx alternativas (D-05); exatamente uma correta; textos não vazios; comprimentos conforme D-05. Mensagens por campo (spec §11).
- **Arquivos**: `app/validators.py`.
- **Requisitos**: RN-001/002/007; RNF-005; CA-02/04; Constitution §4 (validar inputs), Princípio II; plan §9, D-03/D-05.
- **Conclusão**: Entradas inválidas rejeitadas antes de persistir, com mensagens por campo; nenhuma operação inválida altera o banco; validação client-side é apenas conveniência.
- **Dependências**: T002.
- **Status**: [ ] Pendente.

### T020 — Service de criação/edição `question_service.py`
- **Descrição**: Orquestrar validação + persistência atômica de questão e alternativas em **transação**; garantir "exatamente uma correta"; aplicar regras de edição (D-15). Sem conhecimento de HTTP.
- **Arquivos**: `app/services/question_service.py`.
- **Requisitos**: RF-001/002/006; RN-001; CA-01/02/03/04; RNF-004; Constitution §4, Princípio II/III; plan §7, D-15, R-05.
- **Conclusão**: Criar/editar persiste questão+alternativas atomicamente; edição inválida mantém a original inalterada; invariante "1 correta" preservada; testável isoladamente.
- **Dependências**: T015, T016, T019.
- **Status**: [ ] Pendente.

### T021 — Service de exclusão + política de tentativas
- **Descrição**: Excluir questão aplicando RN-005/D-07 (proposta: **bloquear** se houver tentativas → 409). Sem tentativas, remove questão+alternativas (CASCADE). Checagem na service + RESTRICT no banco.
- **Arquivos**: `app/services/question_service.py`, `app/repositories/question_repo.py`, `app/repositories/attempt_repo.py`.
- **Requisitos**: RF-003; RN-005; CA-05; RNF-004; Constitution §4, Princípio II; plan §5/§7, D-07, R-06.
- **Conclusão**: Questão sem tentativas é excluída e some da listagem; questão com tentativas tem exclusão bloqueada com motivo claro (409); histórico preservado; nenhuma órfã.
- **Dependências**: T017, T020.
- **Status**: [ ] Pendente.

### T022 — Rotas CRUD de questões `questions.py`
- **Descrição**: Handlers finos: `GET /questions/new`, `POST /questions`, `GET /questions/<id>`, `GET /questions/<id>/edit`, `POST /questions/<id>`, `POST /questions/<id>/delete`. PRG (D-12); CSRF (T010); mapear erros para HTTP; reexibir formulário com valores + erros.
- **Arquivos**: `app/blueprints/questions.py`, `app/templates/questions/{form,view}.html`.
- **Requisitos**: RF-001/002/003/010; CA-01…05/13; RNF-005/006; Constitution §4/§5; plan §6/§8, D-12.
- **Conclusão**: Fluxo CRUD via test client retorna 200/302/400/404/409 corretos; PRG evita reenvio; formulário reexibido com dados e mensagens por campo; id inexistente → 404 sem órfãs.
- **Dependências**: T010, T011, T020, T021.
- **Status**: [ ] Pendente.

### T023 — Listagem e filtros por assunto/dificuldade
- **Descrição**: `GET /questions?subject=&difficulty=` listando questões com filtros combináveis; catálogo de assuntos no contexto do template. Sem JS obrigatório.
- **Arquivos**: `app/blueprints/questions.py`, `app/repositories/question_repo.py`, `app/repositories/subject_repo.py`, `app/templates/questions/list.html`.
- **Requisitos**: RF-004/005/010; CA-06; RNF-006/007; Constitution §5; plan §6, D-04/D-10.
- **Conclusão**: Filtro por assunto e/ou dificuldade retorna apenas as questões correspondentes; listagem funciona sem JS; desempenho adequado à base local (D-10).
- **Dependências**: T015, T018, T022.
- **Status**: [ ] Pendente.

---

## Fase 5 — Sistema de resolução

### T024 — Exibição da questão para resposta `answer.html`
- **Descrição**: `GET /questions/<id>/answer` mostrando enunciado e alternativas (sem revelar a correta) como formulário de escolha. Acessível e responsivo (base de T031).
- **Arquivos**: `app/blueprints/questions.py` (ou `attempts.py`), `app/templates/questions/answer.html`.
- **Requisitos**: RF-006; CA-07/08; RNF-006; Constitution §5 (UX/feedback); plan §6/§8.
- **Conclusão**: Tela de resposta exibe alternativas selecionáveis sem expor o gabarito; id inexistente → 404; formulário pronto para submissão (T027).
- **Dependências**: T022, T016.
- **Status**: [ ] Pendente.

### T025 — Service de registro de tentativa `attempt_service.py`
- **Descrição**: Registrar tentativa de forma **atômica e append-only**, com `is_correct` snapshot (D-14), na mesma transação da correção. Sem HTTP.
- **Arquivos**: `app/services/attempt_service.py`, `app/repositories/attempt_repo.py`.
- **Requisitos**: RF-008; RN-004; CA-09/10; RNF-004; Constitution §4, Princípio II; plan §7, D-09/D-14, R-03.
- **Conclusão**: Cada resposta gera exatamente uma tentativa (questão, alternativa, resultado, data/hora); N respostas → N registros distintos; resultado congelado mesmo se o gabarito mudar depois.
- **Dependências**: T017.
- **Status**: [ ] Pendente.

---

## Fase 6 — Correção automática

### T026 — Service de correção `grading_service.py`
- **Descrição**: Comparar alternativa escolhida × alternativa correta da questão → resultado binário (correta/incorreta); quando incorreta, identificar a correta. Sem crédito parcial (RN-003). Sem HTTP.
- **Arquivos**: `app/services/grading_service.py`, `app/repositories/question_repo.py`.
- **Requisitos**: RF-007; RN-003; CA-07/08; Constitution §4, Princípio II (correção matemática confiável); plan §7.
- **Conclusão**: Escolha correta → "correta"; escolha incorreta → "incorreta" + indicação da correta; alternativa que não pertence à questão é rejeitada; lógica coberta por testes unitários.
- **Dependências**: T016.
- **Status**: [ ] Pendente.

### T027 — Submissão de resposta (correção + tentativa atômica, PRG)
- **Descrição**: `POST /questions/<id>/answer`: validar alternativa, corrigir (T026) e registrar tentativa (T025) **na mesma transação**; redirecionar ao resultado (PRG) para evitar duplicação em refresh. CSRF.
- **Arquivos**: `app/blueprints/attempts.py` (ou `questions.py`), `app/services/grading_service.py`, `app/services/attempt_service.py`.
- **Requisitos**: RF-007/008; RN-003/004; CA-07/08/09; RNF-004/005; Constitution §4/§5 (feedback), Princípio II; plan §6–§7, D-12/D-14, R-03.
- **Conclusão**: Correção e tentativa ocorrem juntas (nunca uma sem a outra); exatamente uma tentativa por submissão; refresh não duplica (PRG); alternativa inválida → 400; id inexistente → 404.
- **Dependências**: T024, T025, T026.
- **Status**: [ ] Pendente.

### T028 — Exibição do resultado da correção `result.html`
- **Descrição**: `GET /questions/<id>/result` (pós-PRG) mostrando resultado (correta/incorreta) e, se errou, a alternativa correta. Feedback claro ao usuário.
- **Arquivos**: `app/blueprints/attempts.py` (ou `questions.py`), `app/templates/questions/result.html`.
- **Requisitos**: RF-007; CA-07/08; RNF-006; Constitution §5 (feedback em ação importante); plan §6/§8.
- **Conclusão**: Tela de resultado exibe o desfecho e a correta quando incorreta; feedback visível; id/resultado inexistente → 404; coerente com a tentativa registrada.
- **Dependências**: T027.
- **Status**: [ ] Pendente.

---

## Fase 7 — Histórico

### T029 — Service de histórico `history_service.py`
- **Descrição**: Agregar métricas a partir das tentativas (total, acertos, erros, % de acerto — D-08/RN-006) e aplicar filtros (assunto/dificuldade; período se aprovado). Métricas derivam **apenas** dos registros. Sem HTTP.
- **Arquivos**: `app/services/history_service.py`, `app/repositories/attempt_repo.py`.
- **Requisitos**: RF-009; RN-006; CA-11/12; Constitution §4, Princípio II (cálculos corretos); plan §7, D-08.
- **Conclusão**: Métricas calculadas corretamente a partir das tentativas; filtros refletem apenas o subconjunto; % de acerto correto (incl. base zero); coberto por testes unitários.
- **Dependências**: T017, T002.
- **Status**: [ ] Pendente.

### T030 — Rota e visão de histórico `history.py`
- **Descrição**: `GET /history?subject=&difficulty=&from=&to=` exibindo métricas e filtros. Controller fino chamando a service; template acessível.
- **Arquivos**: `app/blueprints/history.py`, `app/templates/history/index.html`.
- **Requisitos**: RF-009; CA-11/12; RNF-006; Constitution §5; plan §6, D-08.
- **Conclusão**: Histórico consultável com métricas corretas; filtros por assunto/dificuldade (e período se aprovado) funcionam; funciona sem JS; base vazia tratada sem erro.
- **Dependências**: T029, T011.
- **Status**: [ ] Pendente.

---

## Fase 8 — Interface

### T031 — Layout base, CSS responsivo e acessibilidade
- **Descrição**: `base.html` + CSS próprio: layout responsivo **desktop + mobile**, navegação consistente, labels associados aos campos, contraste, navegação por teclado, e área de **feedback** (mensagens de sucesso/erro). Sem framework externo (Princípio III). Origem Constitution §5; lacuna G3 reportada no spec.
- **Arquivos**: `app/templates/base.html`, `app/static/css/`.
- **Requisitos**: RNF-006; Constitution §5 (clareza/acessibilidade/consistência/desktop+mobile/feedback), Princípio III; plan §8, G3.
- **Conclusão**: Layout responsivo e acessível; consistente entre telas; toda ação importante tem feedback visível; verificável por checklist manual (T046) desktop+mobile.
- **Dependências**: T011.
- **Status**: [ ] Pendente.

### T032 — Telas de questões (listar/formulário/visualizar/editar)
- **Descrição**: Templates de listagem com filtros, formulário de cadastro/edição (alternativas dinâmicas, marcação de correta), visualização. Autoescape; reexibição com erros por campo.
- **Arquivos**: `app/templates/questions/{list,form,view}.html`, `app/static/css/`.
- **Requisitos**: RF-001/002/004/005/010; CA-01…06; RNF-005/006; Constitution §5; plan §8.
- **Conclusão**: Telas renderizam dados escapados; formulário permite ≥2 alternativas e exatamente uma correta; erros aparecem junto ao campo; filtros visíveis e funcionais sem JS.
- **Dependências**: T022, T023, T031.
- **Status**: [ ] Pendente.

### T033 — Telas de resposta e resultado
- **Descrição**: Templates de resposta (escolha de alternativa) e resultado (correta/incorreta + gabarito quando errou), com feedback imediato e acessível.
- **Arquivos**: `app/templates/questions/{answer,result}.html`, `app/static/css/`.
- **Requisitos**: RF-006/007; CA-07/08; RNF-006; Constitution §5 (feedback); plan §8.
- **Conclusão**: Fluxo de resposta→resultado claro e acessível; gabarito não exposto antes da submissão; resultado destaca a correta quando incorreta; funciona sem JS.
- **Dependências**: T024, T028, T031.
- **Status**: [ ] Pendente.

### T034 — Tela de histórico
- **Descrição**: Template de histórico com métricas (total/acertos/erros/%) e filtros, legível em desktop+mobile.
- **Arquivos**: `app/templates/history/index.html`, `app/static/css/`.
- **Requisitos**: RF-009; CA-11/12; RNF-006; Constitution §5; plan §8, D-08.
- **Conclusão**: Métricas e filtros exibidos de forma clara; base vazia com mensagem adequada; responsivo e acessível; coerente com a service (T029).
- **Dependências**: T030, T031.
- **Status**: [ ] Pendente.

### T035 — JavaScript de conveniência (aprimoramento progressivo)
- **Descrição**: JS vanilla opcional: validação client-side espelhando a do servidor, auto-submit de filtros, adicionar/remover alternativas no formulário, feedback inline. **O fluxo completo funciona sem JS.**
- **Arquivos**: `app/static/js/`.
- **Requisitos**: RNF-003/006; Constitution §5, Princípio III; plan §8, D-12.
- **Conclusão**: Com JS, conveniências funcionam; sem JS, todos os fluxos (CRUD, resposta, histórico) permanecem operacionais; nenhuma dependência de fetch não aprovada.
- **Dependências**: T032, T033, T034.
- **Status**: [ ] Pendente.

### T036 — Notação matemática nas questões (D-06)
- **Descrição**: Aplicar a decisão D-06 de notação (proposta MVP: **texto simples/Unicode**, sem MathJax). Garantir renderização escapada e legível de enunciados/alternativas com símbolos matemáticos.
- **Arquivos**: `app/templates/questions/{view,answer,form,result}.html`, `app/static/css/`.
- **Requisitos**: RF-001; RNF-006; Constitution §6 (escopo), §5; plan D-06, R-10.
- **Conclusão**: Notação conforme D-06 aprovada; símbolos Unicode exibidos corretamente e escapados; nenhuma dependência externa de renderização não aprovada.
- **Dependências**: T002, T032.
- **Status**: [ ] Pendente.

---

## Fase 9 — Testes

### T037 — Fixtures e banco de teste (Pytest)
- **Descrição**: `tests/conftest.py` com fixtures: app de teste, DB temporário/em memória por teste, seed de assuntos/questões, test client. Base para toda a suíte (RNF-008).
- **Arquivos**: `tests/conftest.py`, `tests/unit/`, `tests/integration/`, `tests/routes/`.
- **Requisitos**: RNF-008; Constitution §3 (Pytest), §4, Princípio II; plan §10.
- **Conclusão**: Fixtures isolam dados por teste; suíte Pytest executável; app de teste criável sem tocar `instance/` real.
- **Dependências**: T007, T013.
- **Status**: [ ] Pendente.

### T038 — Testes unitários de validação e questões
- **Descrição**: Testar validação (RN-001/002/007: ≥2 alternativas, exatamente 1 correta, dificuldade enum, campos obrigatórios) e services de criação/edição/exclusão.
- **Arquivos**: `tests/unit/` (validação, question_service).
- **Requisitos**: CA-02/04/05; RN-001/002/005/007; Constitution §4, Princípio II; plan §10.
- **Conclusão**: Casos válidos e inválidos cobertos; edição inválida mantém original; exclusão com tentativas bloqueada; testes passando.
- **Dependências**: T019, T020, T037.
- **Status**: [ ] Pendente.

### T039 — Testes unitários de correção
- **Descrição**: Testar `grading_service`: escolha correta → "correta"; incorreta → "incorreta" + correta indicada; alternativa inválida rejeitada; snapshot não reescrito ao editar gabarito.
- **Arquivos**: `tests/unit/` (grading_service).
- **Requisitos**: CA-07/08; RN-003; RF-007; Constitution §4, Princípio II; plan §10, D-14.
- **Conclusão**: Correção binária correta em todos os casos; indicação da correta quando errou; testes passando.
- **Dependências**: T026, T037.
- **Status**: [ ] Pendente.

### T040 — Testes unitários de histórico
- **Descrição**: Testar agregação de métricas (total/acertos/erros/%) e filtros (assunto/dificuldade/período), incluindo base vazia e cálculo correto de %.
- **Arquivos**: `tests/unit/` (history_service).
- **Requisitos**: CA-11/12; RN-006; RF-009; Constitution §4, Princípio II; plan §10, D-08.
- **Conclusão**: Métricas derivadas apenas das tentativas; filtros refletem subconjunto; % correto (incl. zero); testes passando.
- **Dependências**: T029, T037.
- **Status**: [ ] Pendente.

### T041 — Testes de integração de repositórios e integridade
- **Descrição**: Testar persistência CRUD, FK/integridade, invariante "1 correta" (índice único parcial), atomicidade criar questão+alternativas e corrigir+tentativa, append-only, RESTRICT/CASCADE.
- **Arquivos**: `tests/integration/` (question_repo, attempt_repo, db).
- **Requisitos**: CA-01/03/09/10; RNF-004; RN-001/004/005; Constitution §4, Princípio II; plan §10, R-04/R-05/R-06.
- **Conclusão**: Integridade referencial garantida; transações atômicas (falha não deixa estado parcial); invariantes respeitadas; testes passando.
- **Dependências**: T015, T016, T017, T021, T037.
- **Status**: [ ] Pendente.

### T042 — Testes de rota/funcionais (Fluxos A e B)
- **Descrição**: Via test client: Fluxo A (autor: cadastrar/filtrar/editar/excluir) e Fluxo B (respondente: responder→corrigir→tentativa→histórico). Status 200/302/400/404/409, PRG, filtros, reexibição com erros.
- **Arquivos**: `tests/routes/` (questions, attempts, history).
- **Requisitos**: CA-01…13; RF-001…010; Constitution §4/§5; plan §10.
- **Conclusão**: Ambos os fluxos cobertos de ponta a ponta; códigos HTTP corretos; PRG sem duplicação; cada CA de rota mapeado a ≥1 teste; testes passando.
- **Dependências**: T022, T023, T027, T028, T030, T037.
- **Status**: [ ] Pendente.

### T043 — Testes de segurança (SQL injection, XSS, CSRF)
- **Descrição**: Payloads SQL/HTML armazenados e renderizados escapados; consultas parametrizadas resistem a injection; POST sem/ com CSRF inválido rejeitado.
- **Arquivos**: `tests/routes/` ou `tests/integration/` (segurança).
- **Requisitos**: CA-14; RNF-005; Constitution §4 (proteger integridade), Princípio II; plan §10, R-08.
- **Conclusão**: Entradas maliciosas armazenadas com segurança e exibidas escapadas (sem executar scripts nem alterar consultas); CSRF ausente/inválido rejeitado; testes passando.
- **Dependências**: T010, T022, T037.
- **Status**: [ ] Pendente.

### T044 — Regressão: matriz CA→teste e suíte verde
- **Descrição**: Garantir que **cada CA do spec (CA-01…CA-14)** está mapeado a ≥1 teste automatizado; executar a suíte completa e confirmar que passa. Critério de "completo" da Constitution §4.
- **Arquivos**: `tests/` (toda a suíte), matriz CA→teste (registro em T045/T048).
- **Requisitos**: Todos os CA; RNF-008; Constitution §4 (completo = CA + testes), Princípio II/V; plan §10.
- **Conclusão**: Matriz CA→teste completa (nenhum CA órfão); suíte Pytest integralmente verde; nenhuma tarefa de funcionalidade marcada concluída antes disto.
- **Dependências**: T038, T039, T040, T041, T042, T043.
- **Status**: [ ] Pendente.

### T045 — Evidência de testes versionada no Git
- **Descrição**: Registrar a evidência de execução da suíte (resultado/relatório) e a matriz CA→teste de forma rastreável no repositório, associada aos commits (Princípio VI). **Commit somente com aprovação explícita.**
- **Arquivos**: registro de evidência (ex.: `specs/001-question-bank/` ou `tests/` — a definir), histórico Git.
- **Requisitos**: Constitution Princípio VI (evidência de testes rastreável), §4; plan §10, G1b; RNF-008.
- **Conclusão**: Evidência de testes e matriz CA→teste versionadas e associadas aos commits; auditoria spec↔implementação↔testes possível. Nenhum commit sem aprovação.
- **Dependências**: T044, T003.
- **Status**: [ ] Pendente.

### T046 — Checklist manual de UI (desktop + mobile)
- **Descrição**: Checklist em navegador real: golden path + bordas (sem JS, com JS, filtros, mensagens, feedback, acessibilidade, responsividade desktop+mobile). **Não automatizável neste ambiente** — executar por humano/dev (risco R-11).
- **Arquivos**: checklist de UI (registro), `app/templates/`, `app/static/`.
- **Requisitos**: RNF-006; Constitution §5 (desktop+mobile/acessibilidade/feedback); plan §10, R-11, G3.
- **Conclusão**: Checklist desktop+mobile executado e aprovado por humano; fluxos funcionam sem JS; feedback e acessibilidade verificados; evidência registrada.
- **Dependências**: T032, T033, T034, T035.
- **Status**: [ ] Pendente.

---

## Fase 10 — Documentação

### T047 — README completo (Constitution §7)
- **Descrição**: README com **propósito do projeto**, **stack tecnológica**, **instalação e configuração**, **instruções de execução** e **instruções de testes** (todos os itens exigidos por §7). Resolve G4 (T045 antigo incompleto).
- **Arquivos**: `README.md`, `requirements.txt`.
- **Requisitos**: Constitution §7 (documentação), §3; plan G4; RNF-009.
- **Conclusão**: README permite a outro desenvolvedor entender, configurar, executar e testar a aplicação; todos os 5 itens de §7 presentes; coerente com o ambiente real.
- **Dependências**: T004, T013, T007, T044.
- **Status**: [ ] Pendente.

### T048 — Registrar decisões aprovadas (D-01…D-17) e emendas (G)
- **Descrição**: Consolidar em documento versionado as decisões humanas de T002 (D-01 resolvida; D-02…D-17) e o destino de cada emenda G1–G6 (aplicada/pendente/rejeitada). Rastreabilidade spec↔decisões.
- **Arquivos**: registro de decisões (ex.: `specs/001-question-bank/decisions.md` — a criar somente se aprovado), `specs/001-question-bank/plan.md` (§13).
- **Requisitos**: Constitution Princípio IV/V/VI, §8; plan §13, D-01…D-17, G1–G6.
- **Conclusão**: Cada decisão tem status e justificativa registrados; emendas no spec só constam como aplicadas se aprovadas; histórico Git rastreável (commit com aprovação).
- **Dependências**: T001, T002.
- **Status**: [ ] Pendente.

### T049 — Documentação de referência (schema, rotas, arquitetura)
- **Descrição**: Documentar o schema final, a tabela de rotas e a arquitetura em camadas como referência para manutenção, coerente com a implementação real e o plan.
- **Arquivos**: `README.md` ou doc de referência (a definir), `app/schema.sql`, `app/blueprints/`.
- **Requisitos**: Constitution §7, Princípio III/VI; RNF-002; plan §4/§6.
- **Conclusão**: Referência de schema/rotas/arquitetura bate com o código implementado; um desenvolvedor consegue navegar e manter o sistema.
- **Dependências**: T012, T022, T027, T030.
- **Status**: [ ] Pendente.

### T050 — Parecer final de conformidade e sincronização de lacunas
- **Descrição**: Auditar a implementação final contra a Constitution e o spec; **sincronizar** as referências do `plan.md` §12.2/§13/§14 que descreviam este `tasks.md` como "não alterado" (agora regenerado), e o status real de G1–G6. Reportar conformidade final para aprovação humana. **Não alterar spec/Constitution silenciosamente.**
- **Arquivos**: `specs/001-question-bank/plan.md` (§12.2/§13/§14), `specs/001-question-bank/tasks.md`, parecer final (registro).
- **Requisitos**: Constitution §8 (governança), Princípio IV/V/VI, §4; plan §12.2/§14, G1–G6.
- **Conclusão**: Parecer final de conformidade emitido; referências cruzadas plan↔tasks sincronizadas (com aprovação); lacunas remanescentes reportadas; nenhuma alteração silenciosa em spec/Constitution.
- **Dependências**: T001, T048, T045, T047.
- **Status**: [ ] Pendente.

---

## Ordem de execução (topológica)

`T001 → T002 → T003 → T004 → T005 → T006 → T007 → T008 → T009 → T010 → T011 → T012 → T013 → T014 → T015 → T016 → T017 → T018 → T019 → T020 → T021 → T022 → T023 → T024 → T025 → T026 → T027 → T028 → T029 → T030 → T031 → T032 → T033 → T034 → T035 → T036 → T037 → T038 → T039 → T040 → T041 → T042 → T043 → T044 → T045 → T046 → T047 → T048 → T049 → T050`

> A numeração já é topológica: toda dependência de uma tarefa aparece **antes** dela. As fases são temáticas; a execução real pode intercalar fases respeitando as dependências (ex.: T031 pode iniciar logo após T011, em paralelo do backend).

**Portões de aprovação humana**: `T001` (conformidade Constitution) e `T002` (D-02…D-17 + G1–G6). **Nenhuma tarefa de implementação inicia antes deles.**

**Caminho crítico** (cadeia mais longa de dependências): `T001 → T002 → T004 → T005 → T006 → T007 → T008 → T012 → T013 → T015 → T016 → T020 → T021 → T022 → T024 → T026 → T027 → T028 → T033 → T035 → T046`.

**Paralelizáveis** (após seus pré-requisitos): T009/T010/T011 (backend) ∥ T012–T018 (dados) ∥ T019 (validação); T031 (layout) pode correr junto das fases 4–7; T038/T039/T040 (unit) ∥ entre si; T047/T048/T049 (docs) ∥ entre si.

---

## Rastreabilidade requisito → tarefas

| Origem | IDs | Tarefas |
|--------|-----|---------|
| RF-001 (cadastrar) | RF-001 | T012,T015,T016,T019,T020,T022,T032,T036,T038,T041,T042 |
| RF-002 (editar) | RF-002 | T015,T020,T022,T032,T038,T042 |
| RF-003 (excluir) | RF-003 | T021,T022,T038,T041,T042 |
| RF-004 (assunto) | RF-004 | T014,T018,T023,T032,T042 |
| RF-005 (dificuldade) | RF-005 | T012,T019,T023,T032,T042 |
| RF-006 (múltipla escolha) | RF-006 | T016,T019,T020,T024,T033,T038,T041 |
| RF-007 (correção) | RF-007 | T026,T027,T028,T033,T039,T042 |
| RF-008 (tentativa) | RF-008 | T017,T025,T027,T041,T042 |
| RF-009 (histórico) | RF-009 | T029,T030,T034,T040,T042 |
| RF-010 (listar/ver) | RF-010 | T011,T015,T022,T023,T032 |
| RNF-001 (stack) | RNF-001 | T003,T004,T005 |
| RNF-002 (modularidade) | RNF-002 | T005,T007,T011,T049 |
| RNF-003 (offline) | RNF-003 | T004,T035 |
| RNF-004 (integridade) | RNF-004 | T008,T012,T013,T016,T017,T021,T041 |
| RNF-005 (segurança) | RNF-005 | T010,T019,T043 |
| RNF-006 (usabilidade) | RNF-006 | T031,T032,T033,T034,T035,T046 |
| RNF-007 (desempenho) | RNF-007 | T023 |
| RNF-008 (testabilidade) | RNF-008 | T007,T037,T044,T045 |
| RNF-009 (portabilidade) | RNF-009 | T004,T006,T047 |
| CA-01…CA-14 | CA | T038–T044 (matriz completa em T044) |
| RN-001/002/007 | RN | T012,T016,T019,T020,T038 |
| RN-003 (correção binária) | RN-003 | T026,T039 |
| RN-004 (append-only) | RN-004 | T017,T025,T041 |
| RN-005 (exclusão) | RN-005 | T021,T041 |
| RN-006 (métricas) | RN-006 | T029,T040 |
| RN-008 (identidade) | RN-008 | T002,T012 (D-02) |
| Constitution §3 (stack/Pytest/Git) | §3 | T003,T004,T037,T045 |
| Constitution §4 (completo=CA+testes) | §4 | T044,T045,T050 |
| Constitution §5 (UX desktop+mobile/a11y/feedback) | §5 | T031,T032,T033,T034,T046 |
| Constitution §7 (README) | §7 | T047,T049 |
| Constitution Princípio VI (Git/rastreabilidade) | VI | T003,T045,T048,T050 |
| Lacunas G1–G6 | G | T001,T002,T003 (G1), T045 (G1b), T050 (G1c/G2/G3 sync), T047 (G4), T004 (G5), T005 (G6) |
| Decisões D-01…D-17 | D | T001 (D-01), T002/T048 (D-02…D-17) |

---

## Nota final

- **Nenhuma tarefa está concluída**: todas **[ ] Pendente**. Marcar **[x]** somente quando o critério de conclusão for atendido **e** os testes relevantes passarem (Constitution §4; Princípio V), com revisão humana.
- **Nenhum código foi implementado** por este documento; ele apenas planeja a implementação.
- **O `spec.md` e a Constitution não foram alterados.** Lacunas que afetam o spec (G2/G3/G1c-spec) seguem reportadas no `plan.md` §12.2, aguardando decisão humana item a item.
- **Decisões que necessitam de aprovação humana** (portão T002): D-02…D-17 (design) e G1–G6 (emendas de conformidade). Detalhadas no `plan.md` §12–§13. Nenhum commit Git sem aprovação explícita (T003/T045/T050).