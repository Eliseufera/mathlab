# Especificação — Banco de Questões de Matemática (MathLab)

- **Feature**: `001-question-bank`
- **Documento**: `specs/001-question-bank/spec.md`
- **Stack obrigatória**: Python + Flask + SQLite + HTML + CSS + JavaScript
- **Status**: Rascunho para revisão humana
- **Idioma**: PT-BR

> **Dependência de governança pendente**: o arquivo obrigatório `.specify/memory/constitution.md` **não existe** no workspace. Esta especificação **não pôde ser verificada contra a Constitution**. Nenhum princípio de governança foi inventado. A conformidade constitucional permanece **pendente de aprovação** assim que a Constitution for fornecida.

> **Origem**: este documento foi derivado exclusivamente do briefing da solicitação inicial e das 8 funcionalidades previstas. **Não implementa código** e **não inventa funcionalidades**. Tudo que não está explicitamente definido nas funcionalidades previstas está marcado como **[DECISÃO PENDENTE]** e consolidado na seção 13.

---

## 1. Visão geral e propósito

O MathLab é uma aplicação web local para **cadastrar, organizar e responder questões de matemática de múltipla escolha**, com **correção automática** e **registro do desempenho** ao longo do tempo.

O propósito do MVP é oferecer um ciclo completo e simples:

1. Um autor cadastra questões (enunciado, assunto, dificuldade, alternativas e resposta correta).
2. As questões podem ser editadas, excluídas e filtradas por assunto e dificuldade.
3. Um respondente responde às questões de múltipla escolha.
4. A aplicação corrige automaticamente a resposta.
5. Cada tentativa é registrada.
6. O histórico de desempenho pode ser consultado.

A aplicação prioriza **simplicidade, modularidade e uso offline/local**, coerente com a stack obrigatória (Flask + SQLite).

## 2. Problema que a aplicação resolve

- Organização manual de questões (papel, planilhas soltas) é trabalhosa, difícil de filtrar e não oferece correção nem acompanhamento.
- Sem correção automática, o respondente não obtém feedback imediato.
- Sem registro de tentativas, não há como medir evolução ou identificar assuntos/dificuldades com mais erros.

O MathLab centraliza o banco de questões, padroniza a classificação (assunto/dificuldade), corrige objetivamente (múltipla escolha) e mantém um histórico consultável de tentativas e desempenho.

## 3. Público-alvo

- **Autor de questões**: pessoa que cadastra e mantém o banco (ex.: professor, monitor ou o próprio estudante montando material de estudo).
- **Respondente**: pessoa que responde às questões para praticar (ex.: estudante).

> **[DECISÃO PENDENTE — Papéis/identidade]**: não está definido se autor e respondente são a mesma pessoa, se há papéis distintos, ou se as tentativas/histórico são vinculados a uma identidade (conta/nome) ou são de um único usuário local sem autenticação. Ver seções 9, 12 e 13. O MVP **não assume autenticação** até aprovação.

## 4. Objetivos do MVP

- **O-1**: Permitir o ciclo CRUD de questões de múltipla escolha (cadastrar, listar/visualizar, editar, excluir).
- **O-2**: Classificar questões por **assunto** e por **dificuldade** e permitir filtragem por esses critérios.
- **O-3**: Corrigir automaticamente a alternativa escolhida e informar o resultado.
- **O-4**: Registrar cada tentativa de resposta de forma persistida.
- **O-5**: Exibir histórico de desempenho consultável (com filtros mínimos).
- **O-6**: Rodar localmente/offline sobre Flask + SQLite, com interface web simples em PT-BR.

> Objetivos derivam diretamente das 8 funcionalidades previstas. Nenhuma funcionalidade adicional foi incluída como objetivo.

## 5. Requisitos funcionais

Cada RF indica a funcionalidade prevista de origem. RFs marcados como *implícito* são sub-capacidades necessárias para realizar uma funcionalidade prevista (ex.: listar para poder editar/excluir/responder), não funcionalidades novas.

| ID | Requisito | Origem |
|----|-----------|--------|
| **RF-001** | Cadastrar questão de matemática contendo: enunciado, assunto, dificuldade, alternativas e exatamente uma alternativa correta. | Cadastro de questões; Múltipla escolha |
| **RF-002** | Editar uma questão existente (enunciado, assunto, dificuldade, alternativas e resposta correta). | Edição de questões |
| **RF-003** | Excluir uma questão existente. | Exclusão de questões |
| **RF-004** | Classificar questão por **assunto** e filtrar/listar questões por assunto. | Classificação por assunto |
| **RF-005** | Classificar questão por **dificuldade** e filtrar/listar questões por dificuldade. | Classificação por dificuldade |
| **RF-006** | Estruturar a questão como **múltipla escolha**: conjunto de alternativas, das quais exatamente uma é a correta. | Questões de múltipla escolha |
| **RF-007** | **Corrigir automaticamente** a alternativa escolhida, retornando resultado (correta/incorreta) e, quando incorreta, qual era a alternativa correta. | Correção automática |
| **RF-008** | **Registrar cada tentativa** de resposta (questão, alternativa escolhida, resultado, data/hora). | Registro de tentativas |
| **RF-009** | Consultar **histórico de desempenho** a partir das tentativas registradas (métricas e filtros mínimos). | Histórico de desempenho |
| **RF-010** | Listar e visualizar questões cadastradas (com filtros por assunto/dificuldade), para suportar edição, exclusão e resposta. | *Implícito* (CRUD + correção) |

> **[DECISÃO PENDENTE]** detalhes que afetam RF-001/RF-006 (nº de alternativas), RF-004 (modelo de assunto), RF-005 (escala de dificuldade), RF-008/RF-009 (identidade do respondente e métricas) estão na seção 13. Os RFs acima permanecem válidos independentemente dessas decisões; apenas seus parâmetros mudam.

## 6. Requisitos não funcionais

| ID | Requisito | Verificação |
|----|-----------|-------------|
| **RNF-001** | Usar exclusivamente a stack: Python + Flask + SQLite + HTML + CSS + JavaScript. | Inspeção de dependências/estrutura. |
| **RNF-002** | Simplicidade e modularidade: camadas separadas (rotas, regras de negócio, acesso a dados, apresentação). | Revisão de arquitetura (ver `plan.md`). |
| **RNF-003** | Execução local/offline, sem dependência de serviços externos para o fluxo principal. | Executar sem rede; fluxo completo funciona. |
| **RNF-004** | Integridade dos dados: chaves/relacionamentos consistentes; nenhuma tentativa órfã; exatamente uma alternativa correta por questão. | Testes de integridade + restrições no banco. |
| **RNF-005** | Segurança web básica: consultas parametrizadas (contra SQL injection) e saída escapada (contra XSS); validação no servidor. | Testes com entradas maliciosas. |
| **RNF-006** | Usabilidade: interface simples em PT-BR; mensagens de erro claras junto ao campo/ação. | Checklist manual de UI. |
| **RNF-007** | Desempenho adequado a base local pequena/média (meta proposta: listar até 1.000 questões em tempo percebido como instantâneo). | Medição com base de teste. **[DECISÃO PENDENTE — metas numéricas]** |
| **RNF-008** | Testabilidade: lógica de correção, validação e agregação de histórico cobertas por testes automatizados. | Suíte de testes executável. |
| **RNF-009** | Portabilidade: executar no ambiente do usuário (Windows) com Python e dependências mínimas. | Execução local no ambiente alvo. |

> RNF-003 (offline) e RNF-007 (metas) são **propostas** alinhadas à stack e ao contexto; confirmar na aprovação.

## 7. Histórias de usuário

- **US-01 (Autor)** — Como autor, quero **cadastrar** uma questão de múltipla escolha com assunto e dificuldade, para montar meu banco. *(RF-001, RF-004, RF-005, RF-006)*
- **US-02 (Autor)** — Como autor, quero **editar** e **excluir** questões, para manter o banco correto e atualizado. *(RF-002, RF-003)*
- **US-03 (Autor/Respondente)** — Como usuário, quero **filtrar por assunto e dificuldade**, para encontrar questões relevantes. *(RF-004, RF-005, RF-010)*
- **US-04 (Respondente)** — Como respondente, quero **escolher uma alternativa e receber a correção automática**, para ter feedback imediato. *(RF-007)*
- **US-05 (Respondente)** — Como respondente, quero que **minhas tentativas sejam registradas**, para não perder meu progresso. *(RF-008)*
- **US-06 (Respondente/Autor)** — Como usuário, quero **consultar o histórico de desempenho**, para acompanhar evolução e identificar pontos fracos. *(RF-009)*

## 8. Critérios de aceitação verificáveis

Formato Given/When/Then (Dado/Quando/Então). Cada CA é testável e referencia RFs. Parâmetros marcados **[DECISÃO PENDENTE]** assumem o valor proposto apenas até aprovação.

- **CA-01 (RF-001, RF-006)** — Dado um formulário com enunciado, assunto, dificuldade, ≥2 alternativas e exatamente 1 correta, quando o cadastro é submetido, então a questão é persistida e pode ser recuperada com todos os campos e a alternativa correta identificada.
- **CA-02 (RF-001, RF-006)** — Dado um cadastro sem enunciado, ou com <2 alternativas, ou com zero/mais de uma alternativa correta, quando submetido, então o sistema **rejeita**, não persiste e exibe mensagem de validação.
- **CA-03 (RF-002)** — Dada uma questão existente, quando edito campos válidos e salvo, então a recuperação reflete os novos valores.
- **CA-04 (RF-002)** — Dada uma edição inválida (mesmas regras de CA-02), quando submetida, então é rejeitada e a questão original permanece inalterada.
- **CA-05 (RF-003)** — Dada uma questão existente, quando confirmo a exclusão, então ela deixa de aparecer na listagem. *(O destino das tentativas vinculadas segue RN-005 / [DECISÃO PENDENTE].)*
- **CA-06 (RF-004, RF-005, RF-010)** — Dadas questões com assuntos/dificuldades variados, quando filtro por um assunto e/ou dificuldade, então apenas as questões correspondentes são listadas.
- **CA-07 (RF-007)** — Dada uma questão, quando escolho a alternativa correta, então o resultado é "correta".
- **CA-08 (RF-007)** — Dada uma questão, quando escolho uma alternativa incorreta, então o resultado é "incorreta" **e** a alternativa correta é indicada.
- **CA-09 (RF-008)** — Dada uma resposta submetida, quando a correção ocorre, então exatamente **uma** tentativa é registrada contendo questão, alternativa escolhida, resultado e data/hora.
- **CA-10 (RF-008)** — Dada a mesma questão respondida N vezes, quando consulto as tentativas, então existem N registros distintos (histórico é acumulativo, não sobrescrito).
- **CA-11 (RF-009)** — Dadas tentativas registradas, quando consulto o histórico, então vejo as métricas acordadas (ex.: total de tentativas, acertos, % de acerto) calculadas corretamente a partir dos registros.
- **CA-12 (RF-009)** — Dado o histórico, quando filtro por assunto/dificuldade (e período, se aprovado), então as métricas refletem apenas o subconjunto filtrado.
- **CA-13 (RF-002, RF-003, RF-007)** — Dado um id de questão inexistente, quando tento editar/excluir/responder, então o sistema retorna "não encontrado" sem criar dados órfãos.
- **CA-14 (RNF-005)** — Dada entrada com caracteres especiais/SQL/HTML no enunciado ou alternativas, quando persistida e exibida, então é armazenada com segurança e renderizada escapada (sem executar scripts nem alterar consultas).

## 9. Regras de negócio

| ID | Regra | Observação |
|----|-------|-----------|
| **RN-001** | Toda questão possui: enunciado, assunto, dificuldade, ≥2 alternativas e **exatamente uma** correta. | Base de RF-001/RF-006; validada no servidor. |
| **RN-002** | A dificuldade pertence a um conjunto fechado. | **[DECISÃO PENDENTE]** escala proposta: `Fácil / Médio / Difícil`. |
| **RN-003** | A correção compara a alternativa escolhida com a alternativa correta da questão; resultado é binário (correta/incorreta). | Sem crédito parcial no MVP. |
| **RN-004** | Cada resposta submetida gera exatamente uma tentativa; tentativas são **append-only** (não editáveis). | Proposta; confirmar imutabilidade do histórico. |
| **RN-005** | Exclusão de questão que possui tentativas segue política definida. | **[DECISÃO PENDENTE]** opções: (a) bloquear exclusão; (b) excluir em cascata; (c) manter tentativa anonimizada. Proposta MVP: **(a) bloquear** para preservar histórico, sujeito a aprovação. |
| **RN-006** | Métricas do histórico derivam apenas das tentativas registradas. | **[DECISÃO PENDENTE]** conjunto exato: total, acertos, erros, % acerto; opcional por assunto/dificuldade/período. |
| **RN-007** | Assunto e dificuldade são obrigatórios para permitir classificação e filtragem. | Modelo de assunto em [DECISÃO PENDENTE]. |
| **RN-008** | Tentativas/histórico podem ou não ser vinculados a uma identidade de respondente. | **[DECISÃO PENDENTE]** MVP proposto: single-usuário local, sem autenticação. |

## 10. Fluxos principais

**Fluxo A — Autor (manter banco)**
1. Acessa listagem de questões (RF-010).
2. Cadastra nova questão (RF-001/RF-006) → valida (RN-001) → persiste.
3. Filtra por assunto/dificuldade (RF-004/RF-005).
4. Edita (RF-002) ou exclui (RF-003, sujeito a RN-005).

**Fluxo B — Respondente (praticar)**
1. Filtra/lista questões por assunto/dificuldade (RF-004/RF-005/RF-010).
2. Abre uma questão e escolhe uma alternativa (RF-006).
3. Submete → correção automática (RF-007) → exibe resultado e, se errou, a correta.
4. Tentativa registrada (RF-008).
5. Consulta histórico de desempenho (RF-009), com filtros.

## 11. Tratamento de erros

- **Validação (entrada inválida)**: rejeitar a operação, **não persistir**, e exibir mensagens por campo (ex.: "enunciado obrigatório", "selecione exatamente uma alternativa correta", "mínimo de 2 alternativas"). Mapeia CA-02/CA-04.
- **Não encontrado**: editar/excluir/responder questão inexistente → informar "questão não encontrada", sem efeitos colaterais. Mapeia CA-13.
- **Regra de negócio violada**: excluir questão com tentativas (se RN-005 = bloquear) → informar o motivo e não excluir.
- **Erro de servidor/banco**: exibir mensagem genérica ao usuário ("não foi possível concluir a operação") e registrar detalhes técnicos em log, sem expor stack/SQL ao usuário.
- **Falha silenciosa proibida**: toda ação deve retornar confirmação ou erro visível; nenhuma tentativa deve ser registrada sem correção, e nenhuma correção sem tentativa (consistência RF-007↔RF-008).
- **Frontend**: validação client-side é conveniência; a **autoridade é o servidor** (RNF-005). Reexibir o formulário com os dados já preenchidos e as mensagens de erro.

## 12. Funcionalidades fora do escopo

Explicitamente **fora do MVP** (não inventar nem implementar sem nova aprovação):

- Autenticação, autorização, contas e múltiplos usuários/perfis. *(Relacionado à [DECISÃO PENDENTE] de identidade; se aprovado, deixa de ser "fora" e vira requisito.)*
- Tipos de questão além de múltipla escolha (discursiva, verdadeiro/falso, numérica, associação).
- Crédito parcial, pesos por questão, penalidades, prova cronometrada, simulados com nota ponderada.
- Renderização matemática avançada (LaTeX/MathJax), imagens/áudio/vídeo nas questões. *(Ver [DECISÃO PENDENTE] de notação.)*
- Importação/exportação (CSV, PDF, planilhas), cadastro em lote.
- Gestão avançada de taxonomia de assuntos (CRUD de assuntos) — depende da decisão de modelo de assunto.
- Rankings, gamificação, medalhas, metas, notificações, recomendações/IA.
- Sincronização em nuvem, aplicativo mobile, API pública para terceiros.
- Relatórios/analíticos avançados além do histórico de desempenho definido em RF-009.

## 13. Ambiguidades e decisões que necessitam de aprovação humana

> Nada abaixo foi decidido silenciosamente. Cada item traz uma **proposta de MVP** apenas para permitir redação de critérios testáveis; a proposta **não** entra em vigor sem aprovação.

| # | Ambiguidade / Decisão | Proposta de MVP (a confirmar) | Impacto se mudar |
|---|------------------------|-------------------------------|------------------|
| **D-01** | **Constitution ausente** (`.specify/memory/constitution.md`). | Fornecer o arquivo; validar conformidade desta spec e do `plan.md`. | Pode impor princípios que alteram requisitos/RNFs. |
| **D-02** | Identidade do respondente / autenticação / papéis (autor vs respondente). | Single-usuário local, **sem autenticação**; tentativas sem conta. | RN-008, RF-008/RF-009, modelo de dados (entidade estudante), escopo. |
| **D-03** | Escala de dificuldade. | Conjunto fechado `Fácil / Médio / Difícil`. | RN-002, RF-005, validação, filtros. |
| **D-04** | Modelo de **assunto**: texto livre, lista pré-definida ou entidade gerenciável (CRUD). | Lista pré-definida/curta (catálogo simples), sem CRUD de assuntos no MVP. | RF-004, RN-007, modelo de dados, escopo de gestão. |
| **D-05** | Nº de alternativas por questão (fixo ou configurável). | Configurável, **mínimo 2**, sem máximo rígido no MVP (proposta: até 6). | RF-001/RF-006, RN-001, validação, layout. |
| **D-06** | Notação/renderização matemática (texto simples/Unicode vs LaTeX/MathJax). | **Texto simples/Unicode** no MVP; sem MathJax. | RF-001, RNF-006, esforço de frontend, escopo. |
| **D-07** | Política de exclusão de questão com tentativas. | **Bloquear** exclusão para preservar histórico (RN-005). | RF-003, RN-005, integridade, UX. |
| **D-08** | Métricas e filtros do histórico. | Total, acertos, erros, % acerto; filtros por assunto/dificuldade; período **opcional**. | RF-009, RN-006, consultas/agregações. |
| **D-09** | Imutabilidade das tentativas (append-only). | Tentativas **não editáveis/não excluíveis** pelo usuário. | RN-004, RF-008, histórico. |
| **D-10** | Metas numéricas de desempenho (RNF-007) e tamanho-alvo da base. | Listar até 1.000 questões de forma percebida como instantânea. | RNF-007, testes de carga. |
| **D-11** | Implantação: local/offline vs acessível em rede. | **Local/offline** (localhost). | RNF-003, RNF-005, concorrência do SQLite. |

### Rastreabilidade funcionalidade prevista → RF

| Funcionalidade prevista | RFs |
|--------------------------|-----|
| Cadastro de questões matemáticas | RF-001, RF-006 |
| Edição e exclusão de questões | RF-002, RF-003 |
| Classificação por assunto | RF-004 |
| Classificação por dificuldade | RF-005 |
| Questões de múltipla escolha | RF-006 |
| Correção automática | RF-007 |
| Registro de tentativas | RF-008 |
| Histórico de desempenho | RF-009 |
| (Sub-capacidade necessária) Listar/visualizar | RF-010 |