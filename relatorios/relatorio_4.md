# Relatório — MathLab — semana 4

## Viabilidade

- Grupo: Dupla 11
- Integrante: Eliseu Anacleto
- Repositório: https://github.com/Eliseufera/mathlab
- Relato: https://github.com/Eliseufera/mathlab/blob/main/docs/relatorio-semana-4.md
- Commits abertos: `23d0263` (spec), `a813e8e` (T004–T007), `56d20cc` (T007–T011)
- Veredito: Atende o rastro da fundação

Os commits existem e os arquivos batem com o relato. `a813e8e` traz `requirements.txt`, `app/config.py`, a factory e os testes de configuração. `56d20cc` traz `db.py`, `errors.py`, `security.py`, os blueprints e a página inicial. `app/db.py` liga `PRAGMA foreign_keys = ON`. `app/security.py` recusa POST sem token CSRF. O blueprint de questões só declara o prefixo `/questions` e não tem rota. Há 15 funções de teste nos dois arquivos. Eu não executei o Pytest.

## SWOT

### Forças

A trilha tarefa, commit e arquivo está na mensagem e na tabela do relato. O estado atual separa o que responde (`GET /` 200, erro sem vazar SQL, CSRF) do que o menu anuncia e ainda não existe. A troca de Flask-WTF por token manual está justificada pela constitution, que pede dependência mínima. O domínio não foi marcado como pronto.

### Fraquezas

A revisão da IA descreve o procedimento (teste verde, commit por módulo, decisão registrada) e não mostra um trecho aceito, recusado ou reescrito. O relato deixa a IDE em “[preencher]”, enquanto a semana 1 já tinha nomeado o Qoder. As decisões D-05 e D-16 continuam “aguardando confirmação”, e o código de CSRF já está na `main`.

### Oportunidades

A fase seguinte é o schema e o CRUD, nas tarefas que a lista ainda deixa desmarcadas. Um comentário no commit `56d20cc` com uma linha que a IA sugeriu e o Eliseu mudou fecha a revisão que a semana pede.

### Ameaças

O menu com “Questões” e “Histórico” aponta para rota que responde 404. Tratar a fundação como o banco pronto esconde que cadastrar, corrigir e consultar desempenho não estão no código.

## Stack técnica

**Parecer: Sem mudança, com uma escolha registrada.** Python, Flask, SQLite da biblioteca padrão e Pytest continuam. CSRF não entrou como pacote novo. A IDE no relato da semana 4 está em branco; na semana 1 é o Qoder.

Não há ORM nem serviço externo. A frase “sem mudança” vale para a linguagem e o banco.

## Recomendação

**Sigam para o schema e o cadastro da questão, e registrem um exemplo de código da IA que tenha sido alterado.**

T004 a T011 podem permanecer como a fundação. Questão, alternativa, correção e histórico são as tarefas ainda abertas. A IDE no relato deve repetir o Qoder, ou dizer qual editor foi usado nesta etapa.
