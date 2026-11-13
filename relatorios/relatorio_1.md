# Relatório — MathLab

## Viabilidade

- Grupo: Dupla 11
- Integrante: Eliseu Anacleto. Não há segundo integrante.
- Repositório: https://github.com/Eliseufera/mathlab
- Ideia: https://github.com/Eliseufera/mathlab/blob/main/docs/relatorio-semana-1.md
- Stack: Python 3.14, Flask 3.1, Jinja2, HTML, CSS, JavaScript, SQLite, Pytest e Qoder Desktop.
- Veredito: Viável, com o convite ainda pendente no texto

O problema cabe na disciplina: um banco local de questões de múltipla escolha, com filtro por assunto e dificuldade, correção na hora e histórico de acertos. Não depende de conta nem de servidor externo. O próprio relatório da semana 1 deixa o colega em branco e diz que o convite de leitura para @MarcoMinozzo ainda não foi feito.

## SWOT

### Forças

Usuário, problema e resultado estão no mesmo texto. A stack é uma só linguagem, com banco em arquivo e teste desde o início. O README repete a ideia e aponta constitution, spec, plano e tarefas.

### Fraquezas

Quem cadastra a questão e quem responde ainda não está separado. O texto admite estudante e professor no mesmo uso, sem dizer se é uma pessoa só na máquina. O convite ao instrutor está escrito como passo futuro, não como evidência.

### Oportunidades

Um usuário local, sem login, já permite cadastrar, responder e ver o próprio histórico. LaTeX, ranking e nuvem ficam para depois, como a spec também deixa fora.

### Ameaças

Tratar professor e aluno como papéis diferentes puxa conta e permissão antes de existir uma questão corrigida. Python 3.14 precisa estar na máquina de quem for rodar; a spec fala em Windows, e isso tem de constar no README de execução.

## Stack técnica

**Parecer: Adequada.** Flask, SQLite e Pytest bastam para um banco local de questões. Não há frontend separado para construir.

Jinja2 entrega a tela. JavaScript fica como complemento. A chave de nenhum serviço entra nesta ideia, porque não há API externa. Qoder, em cima do editor do curso, serve para editar e rodar.

## Recomendação

**Mantenham o banco local de múltipla escolha e concluam o convite de leitura para @MarcoMinozzo.**

O ciclo é cadastrar, filtrar, responder e ver o acerto. Conta, LaTeX e nuvem não entram nesta etapa. O lugar do segundo integrante permanece vazio, porque não há outra pessoa.
