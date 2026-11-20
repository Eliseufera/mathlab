# Relatório — MathLab — semana 5

## Viabilidade

- Grupo: Dupla 11
- Integrante: Eliseu Anacleto
- Repositório: https://github.com/Eliseufera/mathlab
- Exemplo: https://github.com/Eliseufera/mathlab/commit/56d20cc
- Veredito: Atende

O commit `56d20cc` abre. A mensagem cobre T007 a T011: conexão SQLite, erros, CSRF, blueprints e testes. O texto separa quatro decisões. A emenda G1c ao `spec.md` foi recusada e o arquivo segue no commit `23d0263`. O código do `56d20cc` entrou com ressalva: 15 testes Pytest verdes, e a decisão D-16 do CSRF continua sem aprovação formal. Flask-WTF foi recusado; o token manual com `secrets` e `hmac.compare_digest` cobre o RNF-005 sem pacote novo. A T007 não foi dada como pronta na Fase 1, porque o critério pedia os blueprints, que só chegaram nesse commit.

## SWOT

### Forças

Cada decisão tem critério anterior ao código: a spec só muda com aprovação, dependência nova precisa de justificativa, e tarefa só fecha com aceite e teste. A porta humana é a alteração da especificação, que o agente propôs e não aplicou. A constitution aparece no Princípio V, na supervisão humana, e no Princípio III, na dependência mínima. A semana 4 pedia um trecho aceito, recusado ou reescrito; este relato nomeia os três.

### Fraquezas

Eu não executei o Pytest de novo. O número de 15 testes e as linhas citadas do plano e do `spec.md` estão no relato, não numa saída colada. D-16 segue pendente enquanto o CSRF já está na `main`, o que a semana 4 já tinha marcado.

### Oportunidades

Aprovar ou recusar D-16 num commit curto fecha a ressalva deste caso. A emenda G1c pode continuar pendente, desde que a nota do `spec.md` não seja editada pelo agente.

### Ameaças

Marcar T010 como concluída antes da ratificação de D-16 transforma a ressalva em aceite. O próprio texto deixa essa conclusão condicional; apagar essa condição no `tasks.md` desfaz a porta humana.

## Stack técnica

**Parecer: Sem mudança.** Python, Flask, SQLite da biblioteca padrão e Pytest continuam. CSRF não entrou como Flask-WTF. O agente nomeado é o Qoder, o mesmo da semana 1.

## Recomendação

**Mantenham G1c fora do `spec.md` até uma decisão explícita, e fechem D-16 antes de tratar o CSRF como aceito.**

O caso mostra proposta, avaliação e recusa. O código que entrou continua provisório no ponto que a constitution reserva à dupla.
