# Semana 1 — Da ideia ao repositório (DSAIA)

- **Projeto:** MathLab — banco de questões de matemática
- **Repositório:** <https://github.com/Eliseufera/mathlab>
- **Integrantes:** Eliseu e [colega — preencher]
- **Status do convite ao instrutor:** pendente (ação manual no GitHub)

## 1. Descrição da ideia

O MathLab é uma aplicação web local para cadastrar, organizar e responder questões de matemática de múltipla escolha, com correção automática e registro do desempenho. Hoje, quem estuda por conta própria costuma espalhar exercícios entre papel, planilhas e anotações: é difícil revisar por assunto ou dificuldade, não há feedback imediato e não dá para saber se está havendo evolução. O usuário afetado é o estudante que se prepara para provas, e também o professor ou monitor que monta listas de exercícios. A aplicação centraliza o banco de questões, permite filtrar por assunto e dificuldade, corrigir a resposta na hora e consultar o histórico de acertos e erros. O resultado esperado é um ciclo de estudo simples e offline — cadastrar, praticar, receber feedback e enxergar o progresso — sem depender de contas, servidores externos ou conexão com a internet.

## 2. Stack tecnológica inicial

- **IDE:** Qoder Desktop (baseada em VS Code)
- **Linguagem:** Python 3.14
- **Framework web:** Flask 3.1
- **Templates:** Jinja2 + HTML5
- **Estilo e interação:** CSS próprio + JavaScript puro
- **Banco de dados:** SQLite (biblioteca padrão `sqlite3`)
- **Testes:** Pytest
- **Versionamento:** Git + GitHub

## 3. Justificativa técnica

Python com Flask foi escolhido por ser a stack da disciplina e por permitir uma aplicação web completa com poucas dependências: o Flask oferece roteamento, templates Jinja2 e servidor de desenvolvimento sem exigir build de front-end. A separação em blueprints, services e repositories mantém as regras de negócio isoladas das rotas, o que torna correção, validação e histórico testáveis com Pytest e atende ao requisito de modularidade.

O SQLite é o banco embutido da biblioteca padrão do Python: não exige servidor nem configuração, guarda os dados em um único arquivo e suporta chaves estrangeiras e transações — suficiente para um MVP local e monousuário, além de sustentar o uso offline. HTML, CSS e JavaScript puro, renderizados no servidor, evitam a complexidade de uma SPA e mantêm o fluxo funcional mesmo sem JavaScript, com interface responsiva e acessível.

Git e GitHub completam a combinação porque o projeto é conduzido com Spec-Driven Development: Constitution, especificação, plano e tarefas são versionados, e cada mudança permanece rastreável de requisito a commit. Pytest entra como rede de segurança desde o início. O custo de infraestrutura é praticamente zero: a aplicação roda na máquina do usuário, sem serviços externos.

## 4. Convite ao instrutor

O instrutor **@MarcoMinozzo** deve ser adicionado ao repositório <https://github.com/Eliseufera/mathlab> com permissão de **leitura (Read)**.

Como fazer (somente o proprietário do repositório pode):

1. Abrir <https://github.com/Eliseufera/mathlab/settings/access>.
2. Em **Collaborators**, clicar em **Add people**.
3. Buscar `MarcoMinozzo`, selecionar a permissão **Read** e confirmar.
4. Guardar o convite aceito como evidência da entrega.

Frase para o formulário depois de concluir: "O instrutor @MarcoMinozzo foi adicionado ao repositório com permissão de leitura."
