# Semana 5 — Governança de contribuições assistidas por IA

- **Projeto:** MathLab — banco de questões de matemática
- **Repositório:** <https://github.com/Eliseufera/mathlab>
- **Dupla:** Dupla 11 — Eliseu Anacleto
- **Agente utilizado:** Qoder (agente de IA integrado ao editor)
- **Recorte:** Fase 2 da implementação (commit `56d20cc`) e a proposta de emenda à especificação registrada como G1c

## 1. Caso concreto

O caso escolhido é o commit [`56d20cc`](https://github.com/Eliseufera/mathlab/commit/56d20cc) — *feat(backend): sqlite connection, error handlers, CSRF, blueprints (T007-T011)* — produzido com auxílio do agente. Ele reúne a conexão SQLite ([`app/db.py`](https://github.com/Eliseufera/mathlab/blob/main/app/db.py)), o tratamento centralizado de erros ([`app/errors.py`](https://github.com/Eliseufera/mathlab/blob/main/app/errors.py)), a proteção CSRF ([`app/security.py`](https://github.com/Eliseufera/mathlab/blob/main/app/security.py)), os blueprints, os templates e os testes de backend ([`tests/test_backend.py`](https://github.com/Eliseufera/mathlab/blob/main/tests/test_backend.py)). O agente também propôs, no mesmo período, uma alteração na especificação: atualizar a nota do topo do [`spec.md`](https://github.com/Eliseufera/mathlab/blob/main/specs/001-question-bank/spec.md#L9), que ainda afirma que a Constitution não existe no workspace.

As duas contribuições são verificáveis no histórico público: o commit está na branch `main`, e a especificação permanece exatamente como foi versionada em [`23d0263`](https://github.com/Eliseufera/mathlab/commit/23d0263) — `git log -- specs/001-question-bank/spec.md` mostra um único commit. Ou seja, a emenda proposta pelo agente **não** foi incorporada.

## 2. O que a dupla avaliou e decidiu

A avaliação não foi uma revisão genérica de código. A dupla aplicou três critérios definidos antes da implementação, todos derivados da Constitution e das regras combinadas para o trabalho:

1. **A especificação é a linha de base e só muda com aprovação explícita** (Constituição, §8; regra "não alterar a especificação silenciosamente").
2. **Dependência nova só entra com justificativa técnica** (Princípio III; §3).
3. **Tarefa só é concluída quando os critérios de aceite foram satisfeitos e os testes passaram** (§4), nunca por ter sido gerada com sucesso.

A partir deles, as decisões foram:

**Rejeitado — emenda G1c ao `spec.md`.** O agente propôs corrigir a nota da [linha 9](https://github.com/Eliseufera/mathlab/blob/main/specs/001-question-bank/spec.md#L9), que diz que a Constitution "não existe", embora ela já tenha sido localizada (D-01 resolvida). A proposta está descrita no plano como lacuna G1c ([`plan.md`, linha 295](https://github.com/Eliseufera/mathlab/blob/main/specs/001-question-bank/plan.md#L295)), e o próprio plano registra a instrução da dupla: *"só reportar, eu decido"* ([linha 308](https://github.com/Eliseufera/mathlab/blob/main/specs/001-question-bank/plan.md#L308)). A dupla rejeitou a aplicação automática: a nota é imprecisa, mas alterar a especificação é um ato de governança, não uma limpeza editorial, e precisa ser decidido item a item. O texto continua na linha 9 e a divergência segue rastreada como G1c. O critério foi o §8 da Constitution, não a preferência do agente.

**Aceito com ressalva — commit `56d20cc`.** O código entrou porque passou pelos critérios técnicos: a suíte executou **15 testes Pytest, todos verdes** (`python -m pytest -q`), incluindo FK habilitada, reuso de conexão, autoescape e os dois casos de CSRF ([`tests/test_backend.py`, linhas 32–45](https://github.com/Eliseufera/mathlab/blob/main/tests/test_backend.py#L32)). A aceitação é provisória em um ponto específico: o mecanismo de CSRF é uma decisão de design (D-16) que continua reservada à dupla. O agente implementou a alternativa sem dependência nova e deixou isso explícito em [`requirements.txt`, linha 4](https://github.com/Eliseufera/mathlab/blob/main/requirements.txt#L4); a aprovação formal de D-16 e a tarefa T002 seguem pendentes.

**Rejeitado — Flask-WTF como dependência.** A opção de usar Flask-WTF estava prevista no plano (D-16, [linha 318](https://github.com/Eliseufera/mathlab/blob/main/specs/001-question-bank/plan.md#L318)), mas a dupla aplicou o Princípio III: dependência nova precisa de propósito que justifique o custo. O token manual com `secrets` e `hmac.compare_digest` ([`app/security.py`, linha 24](https://github.com/Eliseufera/mathlab/blob/main/app/security.py#L24)) resolve o mesmo requisito de segurança (RNF-005) sem ampliar a superfície de dependências. O `requirements.txt` registra a justificativa; o teste confirma que POST sem token retorna 400 e POST com token válido passa.

**Reescrito — o critério de "pronto" da T007.** O agente chegou a tratar a app factory como concluída ao fim da Fase 1. A regra de conclusão da dupla rejeitou o encerramento: o critério da própria T007 exige blueprints registrados, e isso ainda não existia. A tarefa ficou pendente e só foi marcada como concluída depois do commit `56d20cc`, com os 15 testes passando ([`tasks.md`, linha 90](https://github.com/Eliseufera/mathlab/blob/main/specs/001-question-bank/tasks.md#L90)). Foi uma correção de estado, não de código — mas é exatamente o tipo de decisão que o agente não pode tomar sozinho, porque "pronto" é definido pela dupla e pela Constitution.

## 3. A porta humana

A decisão que o agente não poderia tomar sozinho é a **alteração da especificação**. O §8 da Constitution estabelece que qualquer mudança de princípio ou de baseline precisa ser documentada e revisada pelo dono do projeto; o agente pode detectar a inconsistência e propor a correção, mas não pode aplicá-la. Foi o que aconteceu: a emenda G1c foi reportada, a dupla decidiu mantê-la pendente e o `spec.md` não foi tocado. O mesmo vale para D-16: o agente pode implementar uma alternativa provisória e provar que ela passa nos testes, mas **não pode declarar a decisão de design aprovada**. A conclusão da T010 ([`tasks.md`, linha 114](https://github.com/Eliseufera/mathlab/blob/main/specs/001-question-bank/tasks.md#L114)) é, por isso, condicional: ela descreve o comportamento verificado, não a ratificação de D-16.

Há ainda duas portas humanas menores, mas relevantes. A primeira é o **commit/merge**: o repositório é da dupla, e o agente só versionou porque havia autorização explícita para colocar toda alteração no Git/GitHub; o histórico público permite reverter qualquer contribuição. A segunda é uma **alteração não produzida pelo agente na Constitution** (diferença de espaços em branco no arquivo): o agente a detectou, deixou-a fora de todos os commits e não a "corrigiu", porque mudança constitucional é decisão da dupla, não efeito colateral de uma tarefa. Nenhum dado pessoal ou sensível entrou no projeto: o MVP não tem autenticação nem identidade de respondente (D-02 segue pendente).

## 4. Relação com a Constitution

| Regra | Onde está | Como foi aplicada neste caso |
|---|---|---|
| **Princípio V — Human Supervision of AI** | [`constitution.md`, linha 85](https://github.com/Eliseufera/mathlab/blob/main/.specify/memory/constitution.md#L85) | O agente gerou código e propostas, mas a emenda à spec não foi aplicada, D-16 não foi declarada aprovada e nenhuma saída foi aceita só por ter sido gerada. |
| **Princípio III — Simplicity and Maintainability** | [linha 51](https://github.com/Eliseufera/mathlab/blob/main/.specify/memory/constitution.md#L51) | Flask-WTF foi rejeitado; o CSRF manual resolve o requisito sem dependência adicional. |
| **§4 — Quality and Testing** | [linha 155](https://github.com/Eliseufera/mathlab/blob/main/.specify/memory/constitution.md#L155) | O commit só foi aceito com a suíte verde (15 testes); a T007 só foi concluída após o critério de aceite ser cumprido. |
| **§8 — Governance and Amendments** | [linha 235](https://github.com/Eliseufera/mathlab/blob/main/.specify/memory/constitution.md#L235) | A especificação não foi alterada pelo agente; a emenda G1c permanece reportada e reservada à dupla. |
| **Princípio VI — Version Control and Traceability** | [linha 113](https://github.com/Eliseufera/mathlab/blob/main/.specify/memory/constitution.md#L113) | Commits citam os IDs das tarefas (`T007-T011`) e ligam requisito, código e evidência de testes no histórico público. |

O Princípio V é o que dá sentido à semana: ele não proíbe o agente de gerar; ele proíbe a dupla de transferir ao agente a responsabilidade pelo que entra. A revisão humana, nesse caso, aparece como decisões registradas — rejeitar a emenda, recusar a dependência, aceitar o commit com ressalva e segurar a conclusão da tarefa — e não como um "ok" genérico.

## 5. Pendências assumidas

O controle humano também significa não esconder o que ficou aberto: D-02…D-17 e as emendas G1–G6 continuam pendentes de decisão item a item (T002); a nota desatualizada do `spec.md` e a frase "todas estão [ ] Pendente" no topo do `tasks.md` seguem no repositório, à espera de autorização para corrigir; a conclusão da T010 depende da ratificação de D-16; e não houve Pull Request — os commits foram diretos na `main`, com rastreabilidade pelo link de cada commit.

## 6. Conclusão

O agente acelerou a produção do backend e organizou a evidência, mas as decisões que definem o projeto continuaram com a dupla: o que é baseline, qual dependência entra, quando uma tarefa está pronta e o que pode ser incorporado. O commit `56d20cc` é a prova de que a contribuição foi avaliada antes de entrar; a nota intocada do `spec.md` é a prova de que nem toda sugestão do agente vira mudança. É essa separação entre geração e decisão que a Constitution chama de supervisão humana.
