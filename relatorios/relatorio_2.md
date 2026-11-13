# Relatório — MathLab — semana 2

## Viabilidade

- Grupo: Dupla 11
- Integrante: Eliseu Anacleto
- Constitution: https://github.com/Eliseufera/mathlab/blob/main/.specify/memory/constitution.md
- Commit: `2c2db45` (07/11/2026), “docs: establish project constitution”
- Veredito: Parcial

O arquivo abre na `main`. Ele fixa spec antes de código, revisão humana do que a IA gerar, stack Python/Flask/SQLite/Pytest e “pronto” só com critério e teste. Não diz quem aprova o merge, o que o agente pode versionar sozinho e três regras do banco de questões. O texto está em inglês e o dono aparece como “MathLab Project Owner”, sem nome.

## SWOT

### Forças

Princípio IV impede funcionalidade grande sem spec e plano. Princípio V diz que código gerado não vale só porque a IA o produziu: o dono revisa, confere a spec, roda o teste e recusa o que estiver errado. Dependência nova precisa de motivo. A constitution prevalece se o código divergir.

### Fraquezas

A semana pede papéis concretos. Aqui não há a frase de quem aprova a spec, quem faz o merge e o que entra na branch sem revisão prévia. “Toda contribuição gerada passa por revisão humana” é a regra genérica que a etapa pede para evitar como única regra. Não há regra de gabarito, de alternativa correta única nem de histórico que não se apaga.

### Oportunidades

Três regras cabem neste banco: uma questão só entra com uma alternativa correta; a correção usa o gabarito gravado, sem a IA inventar a resposta; tentativa registrada não é editada nem apagada. O merge fica com o Eliseu, porque não há o outro integrante.

### Ameaças

Sem a faixa do agente, um commit pode mudar o gabarito ou a spec e ainda parecer “documentação”. O arquivo em `.specify/memory/` também fica fácil de não achar a partir da raiz, embora o README o cite.

## Stack técnica

**Parecer: Sem mudança.** A constitution repete Python, Flask, SQLite, HTML, CSS, JavaScript, Pytest e Git. Não troca o banco nem acrescenta serviço externo.

## Recomendação

**Reescrevam a constitution com o nome do Eliseu, o merge feito por ele e três regras do banco de questões.**

Spec aprovada por ele antes do código. O agente escreve teste e código na branch, sem alterar gabarito nem spec. Uma alternativa correta, correção pelo gabarito gravado e tentativa que não se apaga são as regras que este projeto usa.
