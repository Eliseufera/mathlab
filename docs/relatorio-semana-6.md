# Semana 6 — Validação e README

- **Projeto:** MathLab — banco de questões de matemática
- **Repositório:** <https://github.com/Eliseufera/mathlab>
- **Dupla:** Dupla 11 — Eliseu Anacleto
- **Data da validação:** 21/11/2026
- **Commit testado no clone limpo:** `6509f91`
- **Ambiente:** Windows 10.0.22621, Git Bash, Python 3.14.6, Flask 3.1.3, Pytest 9.2.0

## 1. Evidência de validação

### 1.1 Escopo validado — e o que não foi

O recorte definido na semana 3 (cadastrar, filtrar, responder, corrigir e consultar histórico) **ainda não está implementado**. A validação abaixo cobre a fundação entregue até aqui e **não** afirma que o recorte está pronto. O bloqueio está documentado na seção 3. Esta é a leitura honesta do estado: validar a fundação é possível; declarar o recorte validado, não.

| Critério de aceitação | Estado | Evidência / motivo |
|---|---|---|
| CA-01 — cadastrar questão e recuperar com alternativa correta | **Não implementado** | Rotas de CRUD e schema ainda não existem (`T012` em diante). |
| CA-02 — rejeitar cadastro inválido sem persistir | **Não implementado** | Depende do formulário e do schema. |
| CA-03 — editar questão e refletir os novos valores | **Não implementado** | Rota de edição ausente. |
| CA-04 — rejeitar edição inválida mantendo a original | **Não implementado** | Depende da edição. |
| CA-05 — excluir questão e removê-la da listagem | **Não implementado** | Rota de exclusão e listagem ausentes. |
| CA-06 — filtrar por assunto/dificuldade | **Não implementado** | Listagem/filtros ausentes. |
| CA-07 — resposta correta resulta em “correta” | **Não implementado** | Correção automática ausente. |
| CA-08 — resposta incorreta indica a correta | **Não implementado** | Correção automática ausente. |
| CA-09 — uma tentativa registrada por resposta | **Não implementado** | Persistência de tentativas ausente. |
| CA-10 — N respostas geram N registros | **Não implementado** | Persistência de tentativas ausente. |
| CA-11 — métricas do histórico | **Não implementado** | Serviço e rota de histórico ausentes. |
| CA-12 — filtros do histórico | **Não implementado** | Serviço e rota de histórico ausentes. |
| CA-13 — id inexistente retorna “não encontrado” | **Parcial** | O handler genérico de 404 funciona (`test_unknown_route_returns_404`), mas ainda não há rotas de questão para validar id inexistente. |
| CA-14 — entrada especial é renderizada escapada e sem alterar consultas | **Parcial** | Autoescape configurado (`test_autoescape_enabled_for_html`) e CSRF rejeita POST sem token (`test_post_without_csrf_is_rejected`); não há persistência/exibição de payload para testar XSS armazenado, e ainda não há SQL de negócio para testar injeção. |

### 1.2 Testes automatizados — 15 testes, 15 verdes

Comando (na raiz do repositório, com o ambiente virtual ativo):

```bash
python -m pytest -q
```

Saída observada em 21/11/2026 na execução local (no clone limpo, `15 passed in 2.10s`):

```text
...............                                                          [100%]
15 passed in 0.31s
```

| Arquivo / teste | O que verifica |
|---|---|
| `test_app.py::test_create_app_returns_flask_instance` | A fábrica retorna uma instância Flask. |
| `test_app.py::test_default_config_is_not_testing` | Configuração padrão não está em modo de teste. |
| `test_app.py::test_test_config_overrides_defaults` | Configuração de teste sobrepõe os padrões. |
| `test_app.py::test_database_defaults_to_instance_path` | Banco padrão aponta para `instance/`. |
| `test_app.py::test_instance_directory_exists` | Diretório `instance/` é criado. |
| `test_app.py::test_difficulty_and_alternative_limits` | Constantes de dificuldade e limites de alternativas (proposta D-05, ainda sujeita a aprovação). |
| `test_app.py::test_client_fixture_is_usable` | O client de teste responde. |
| `test_backend.py::test_home_returns_200` | `GET /` retorna 200. |
| `test_backend.py::test_unknown_route_returns_404` | Rota inexistente retorna a página de erro 404. |
| `test_backend.py::test_foreign_keys_enabled` | Toda conexão abre com `PRAGMA foreign_keys = ON`. |
| `test_backend.py::test_db_connection_reused_within_context` | A conexão é reutilizada dentro do mesmo request/contexto. |
| `test_backend.py::test_autoescape_enabled_for_html` | O autoescape do Jinja2 está ligado para HTML. |
| `test_backend.py::test_post_without_csrf_is_rejected` | POST sem token CSRF retorna 400. |
| `test_backend.py::test_post_with_valid_csrf_passes` | POST com token de sessão válido passa. |
| `test_backend.py::test_409_handler_renders_error_page` | Erro de regra de negócio (409) renderiza a página de erro. |

Os testes usam banco SQLite temporário por execução, definido em [`tests/conftest.py`](https://github.com/Eliseufera/mathlab/blob/main/tests/conftest.py), e a configuração de teste (`TESTING=True`).

### 1.3 Checklist manual reproduzível

Pré-requisito: aplicação em execução com `python -m flask --app app run` (porta 5000). Em Windows, use `curl.exe` se o `curl` não estiver disponível no shell.

| Passo | Ação | Resultado esperado | Resultado observado |
|---|---|---|---|
| 1 | `curl -s -o /dev/null -w "%{http_code}\n" http://127.0.0.1:5000/` | `200` | `200` |
| 2 | Abrir <http://127.0.0.1:5000/> no navegador | Página inicial com o título “MathLab” | Página exibida com `<h1>MathLab</h1>` |
| 3 | `curl -s -o /dev/null -w "%{http_code}\n" http://127.0.0.1:5000/rota-inexistente` | `404` com página de erro, sem stack trace | `404` e página “Erro 404” |
| 4 | Acessar “Questões” no menu | **404** nesta etapa (limitação conhecida) | `404` — rota ainda não implementada |
| 5 | Acessar “Histórico” no menu | **404** nesta etapa (limitação conhecida) | `404` — rota ainda não implementada |
| 6 | Enviar POST sem token CSRF | Não é possível pela interface atual; coberto pelo teste automatizado | `test_post_without_csrf_is_rejected` → 400 |

O checklist não usa os fluxos de cadastro/resposta porque eles ainda não existem. Ele valida o que é reproduzível hoje e registra explicitamente os 404 conhecidos, em vez de tratá-los como sucesso.

### 1.4 Teste do terceiro — clone limpo

O teste foi feito a partir da URL pública, sem usar o diretório de desenvolvimento. Passos executados:

```bash
CLEAN=$(mktemp -d)
git clone --depth 1 https://github.com/Eliseufera/mathlab.git "$CLEAN/mathlab"
cd "$CLEAN/mathlab"
python -m venv .venv
source .venv/Scripts/activate
python -m pip install --quiet --disable-pip-version-check -r requirements.txt
python -m pytest -q
```

Resultados:

| Verificação | Resultado |
|---|---|
| Clone do repositório público | OK |
| Criação da venv | OK — Python 3.14.6 |
| `pip install -r requirements.txt` | OK — exit code 0 |
| Versões instaladas | Flask 3.1.3, Jinja2 3.1.6, Werkzeug 3.1.9, Pytest 9.2.0 |
| `python -m pytest -q` | `15 passed in 2.10s` |
| `python -m flask --app app run` (porta 5057) | Servidor iniciou |
| `curl http://127.0.0.1:5057/` | `200`, com `<h1>MathLab</h1>` |
| Commit do clone | `6509f91` |
| Diretório temporário | Removido ao final do teste |

O teste final foi repetido **depois** da publicação deste README e do relatório, no commit `6509f91`, seguindo a ativação descrita no README (`source .venv/Scripts/activate` no Git Bash) e apenas a URL pública do repositório. O resultado foi o mesmo: instalação concluída, 15 testes verdes e `GET /` respondendo 200.

Esse é o teste do terceiro em ambiente limpo: outra pessoa, com apenas a URL, consegue clonar, instalar, executar a aplicação e rodar os testes seguindo o README. O que ela **não** consegue é validar o recorte completo, porque o recorte não está implementado.

## 2. README

Link: <https://github.com/Eliseufera/mathlab/blob/main/README.md>

O README cobre, na ordem em que uma pessoa de fora precisa:

1. **Clonar** o repositório.
2. **Criar e ativar** o ambiente virtual em Windows (PowerShell e cmd), Git Bash e macOS/Linux, com alternativa sem ativação.
3. **Instalar** as dependências com `pip install -r requirements.txt`.
4. **Configurar** `SECRET_KEY` (opcional em dev) e `MATHLAB_DATABASE` (opcional), com exemplos por shell; explica que `.env` não é carregado automaticamente e que nenhuma credencial é versionada.
5. **Configurar o banco**: SQLite em arquivo, sem serviço externo; caminho padrão `instance/mathlab.sqlite`; informa que o schema ainda não existe nesta fase.
6. **Executar** com `python -m flask --app app run` e abrir `http://127.0.0.1:5000`.
7. **Testar** com `python -m pytest -q` e o resultado esperado (`15 passed`).
8. **Limitações**: o que funciona, o que falta e o que responde 404.

O README foi validado pelo teste do terceiro da seção 1.4. As instruções são suficientes para reproduzir a execução da fundação; não são suficientes para demonstrar o fluxo principal porque ele não existe ainda.

## 3. Estado atual e limitações

### O que funciona de ponta a ponta hoje

- Clonar, instalar e executar a aplicação em ambiente limpo.
- Abrir a página inicial (`GET /` → 200).
- Receber páginas de erro 400/404/409/500 sem stack trace.
- Abrir conexões SQLite com chaves estrangeiras ligadas.
- Rejeitar POST sem CSRF e aceitar POST com token válido.
- Rodar 15 testes automatizados verdes.

### O que impede o recorte de funcionar de ponta a ponta

1. **Schema e repositórios ausentes** (Fase 3, `T012`–`T018`): não há tabelas `subject`, `question`, `alternative` ou `attempt`.
2. **CRUD de questões ausente** (Fase 4): não há rotas de cadastro, listagem, edição, exclusão ou filtro.
3. **Resposta e correção ausentes** (Fases 5–6): não há formulário de resposta, comparação com o gabarito nem registro de tentativa.
4. **Histórico ausente** (Fase 7): não há agregação de métricas nem filtros.
5. **Links de navegação quebrados**: “Questões” e “Histórico” retornam 404; é a lacuna visível para quem abre a aplicação.
6. **Decisões de design abertas**: D-16 (mecanismo de CSRF) continua sem ratificação formal; D-02, D-05 e D-07 também seguem pendentes. O código atual adota a proposta de MVP, mas não substitui a aprovação da dupla.
7. **T010 condicional**: a tarefa está marcada como concluída pelo comportamento verificado, não pela ratificação de D-16.

### O que o README não promete

O README não afirma que o banco de questões está funcional, não lista cadastro/correção/histórico como disponíveis e não esconde os 404. Quem clonar o projeto encontrará exatamente o estado descrito: uma fundação executável e testada, com o fluxo principal pendente.

## 4. Próximos passos para fechar o recorte

1. Implementar `app/schema.sql`, `init_db` e seed de assuntos (`T012`–`T018`).
2. Implementar repositórios e serviços de questão, com validação de “exatamente uma correta”.
3. Implementar rotas de CRUD e filtros (Fase 4).
4. Implementar resposta, correção e registro atômico de tentativa (Fases 5–6).
5. Implementar histórico e métricas (Fase 7).
6. Ampliar a suíte para cobrir CA-01…CA-14 e repetir o teste do terceiro.
7. Ratificar D-16 e as demais decisões pendentes antes de tratar as tarefas condicionais como definitivas.

## 5. Evidências

- Commit do código testado: <https://github.com/Eliseufera/mathlab/commit/6509f91>
- README: <https://github.com/Eliseufera/mathlab/blob/main/README.md>
- Testes: [tests/test_app.py](https://github.com/Eliseufera/mathlab/blob/main/tests/test_app.py) e [tests/test_backend.py](https://github.com/Eliseufera/mathlab/blob/main/tests/test_backend.py)
- Fixtures: [tests/conftest.py](https://github.com/Eliseufera/mathlab/blob/main/tests/conftest.py)
- Tarefas pendentes: [tasks.md](https://github.com/Eliseufera/mathlab/blob/main/specs/001-question-bank/tasks.md)
- Critérios de aceitação: [spec.md, seção 8](https://github.com/Eliseufera/mathlab/blob/main/specs/001-question-bank/spec.md)
