# MathLab

Aplicação web local para cadastrar, organizar e responder questões de matemática de múltipla escolha, com correção automática e histórico de desempenho.

## A ideia

O MathLab é uma aplicação web local para cadastrar, organizar e responder questões de matemática de múltipla escolha, com correção automática e registro do desempenho. Hoje, quem estuda por conta própria costuma espalhar exercícios entre papel, planilhas e anotações: é difícil revisar por assunto ou dificuldade, não há feedback imediato e não dá para saber se está havendo evolução. O usuário afetado é o estudante que se prepara para provas, e também o professor ou monitor que monta listas de exercícios. A aplicação centraliza o banco de questões, permite filtrar por assunto e dificuldade, corrigir a resposta na hora e consultar o histórico de acertos e erros. O resultado esperado é um ciclo de estudo simples e offline — cadastrar, praticar, receber feedback e enxergar o progresso — sem depender de contas, servidores externos ou conexão com a internet.

## Problema, usuário e resultado esperado

- **Problema:** questões espalhadas em papel e planilhas são difíceis de organizar e filtrar, não oferecem correção automática nem acompanhamento da evolução.
- **Usuário:** estudante que pratica para provas e professor ou monitor que mantém o banco de questões.
- **Resultado esperado:** um ciclo único de cadastro, prática com feedback imediato e consulta de desempenho, funcionando localmente e sem infraestrutura externa.

## Stack tecnológica inicial

| Camada | Tecnologia | Papel no projeto |
|---|---|---|
| IDE | Qoder Desktop (baseada em VS Code) | Edição, execução e depuração |
| Linguagem | Python 3.14 | Back-end e scripts de apoio |
| Framework web | Flask 3.1 | Rotas, blueprints, configuração da aplicação |
| Templates | Jinja2 + HTML5 | Interface renderizada no servidor |
| Estilo e interação | CSS próprio + JavaScript puro | Layout responsivo e aprimoramento progressivo |
| Banco de dados | SQLite (biblioteca padrão `sqlite3`) | Persistência local com chaves estrangeiras |
| Testes | Pytest | Testes unitários, de integração e de rotas |
| Versionamento | Git + GitHub | Histórico e rastreabilidade das mudanças |

## Justificativa técnica

Python com Flask foi escolhido por ser a stack da disciplina e por permitir uma aplicação web completa com poucas dependências: o Flask oferece roteamento, templates Jinja2 e servidor de desenvolvimento sem exigir build de front-end. A separação em blueprints, services e repositories mantém as regras de negócio isoladas das rotas, o que torna correção, validação e histórico testáveis com Pytest e atende ao requisito de modularidade.

O SQLite é o banco embutido da biblioteca padrão do Python: não exige servidor nem configuração, guarda os dados em um único arquivo e suporta chaves estrangeiras e transações — suficiente para um MVP local e monousuário, além de sustentar o uso offline. HTML, CSS e JavaScript puro, renderizados no servidor, evitam a complexidade de uma SPA e mantêm o fluxo funcional mesmo sem JavaScript, com interface responsiva e acessível.

Git e GitHub completam a combinação porque o projeto é conduzido com Spec-Driven Development: Constitution, especificação, plano e tarefas são versionados, e cada mudança permanece rastreável de requisito a commit. Pytest entra como rede de segurança desde o início. O custo de infraestrutura é praticamente zero: a aplicação roda na máquina do usuário, sem serviços externos.

## Documentação SDD

- [Constitution](.specify/memory/constitution.md)
- [Especificação](specs/001-question-bank/spec.md)
- [Plano](specs/001-question-bank/plan.md)
- [Tarefas](specs/001-question-bank/tasks.md)

## Situação do projeto

A proposta e o repositório estão estabelecidos. O desenvolvimento da aplicação está em andamento (configuração, app factory, conexão SQLite, tratamento de erros, CSRF e blueprints já implementados e cobertos por testes); as demais fases seguem o plano em `specs/001-question-bank/tasks.md`.
