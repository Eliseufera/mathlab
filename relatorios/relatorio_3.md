# Relatório — MathLab — semana 3

## Viabilidade

- Grupo: Dupla 11
- Integrante: Eliseu Anacleto
- Specify: https://github.com/Eliseufera/mathlab/blob/main/specs/001-question-bank/spec.md
- Plan: https://github.com/Eliseufera/mathlab/blob/main/specs/001-question-bank/plan.md
- Tasks: https://github.com/Eliseufera/mathlab/blob/main/specs/001-question-bank/tasks.md
- Commit dos três: `23d0263` (11/11/2026)
- Veredito: Atende o recorte, com decisões ainda abertas

Os três arquivos estão na `main`. O recorte é um banco local de múltipla escolha: cadastrar, filtrar por assunto e dificuldade, corrigir na hora e ver histórico. Ficam fora conta, outros tipos de questão, LaTeX, importação, ranking, nuvem e API pública. As decisões D-02 a D-17 estão marcadas como proposta, não como fato. A identidade do respondente segue sem autenticação até alguém aprovar o contrário.

## SWOT

### Forças

O que entra e o que fica fora está em lista. Cada requisito tem caminho para tarefa. O status das tarefas separa o que já foi marcado como feito (T003 a T011, a fundação) do CRUD, da correção e do histórico, que continuam pendentes. A spec não trata silêncio como aceite.

### Fraquezas

A spec ainda lista D-01 como “constitution ausente”, e o arquivo `.specify/memory/constitution.md` já está no repositório desde 07/11. As tarefas dizem que D-01 foi resolvida. Os dois textos não contam a mesma coisa. Várias regras de negócio dependem de decisão que o próprio quadro deixa em aberto, entre elas o número de alternativas e se a tentativa pode ser apagada.

### Oportunidades

Fechar D-02 como usuário único local destrava o modelo: questão, alternativa, tentativa, sem tabela de conta. A tarefa seguinte pode ser o schema, que a lista ainda mostra pendente.

### Ameaças

Implementar CRUD enquanto D-05 e D-07 seguem “a confirmar” faz o código escolher o que a spec não fechou. Autenticação, hoje fora do MVP, volta se o papel de professor for tratado como outro usuário.

## Stack técnica

**Parecer: Adequada para o recorte.** Python, Flask, SQLite sem ORM e Pytest seguem. A spec não pede serviço externo. Texto simples no lugar de MathJax está na proposta D-06, ainda por confirmar.

## Recomendação

**Fechem as decisões do quadro, a começar por usuário único, uma alternativa correta e tentativa que não se apaga, e alinhem a spec ao fato de que a constitution já existe.**

O recorte do banco local permanece. Conta, LaTeX e ranking continuam fora. Tarefa de domínio só começa depois que a decisão correspondente deixar de ser proposta.
