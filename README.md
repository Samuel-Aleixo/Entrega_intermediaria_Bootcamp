# TaskTracker

Aplicação de linha de comando (CLI) em Python para gerenciamento de tarefas, desenvolvida no **Bootcamp II – Fase 2 (Entrega Intermediária)**.

## Problema resolvido
Pessoas e equipes perdem o controle de prazos e prioridades quando as tarefas ficam espalhadas em anotações e mensagens. O TaskTracker centraliza o cadastro e a visualização das tarefas, organizando-as por prioridade.

## Funcionalidades
- Cadastrar tarefas com título, descrição, prioridade e data limite
- Visualizar tarefas ordenadas da prioridade mais urgente para a menos urgente
- Marcar tarefas como concluídas e ver o total de concluídas

## Regras de negócio
1. O título é obrigatório (vazio ou só espaços é rejeitado).
2. A prioridade deve ser `Alta`, `Média` (ou `Media`) ou `Baixa`.
3. A data limite deve estar no formato `DD/MM/AAAA` e não pode ser anterior à data atual.
4. Só é possível concluir tarefas que existam na lista.
5. Toda tarefa nasce com status `Pendente`.

## Tecnologias
- Python 3
- Git e GitHub

## Estrutura do projeto
```
tasktracker-projeto/
├── README.md
├── .gitignore
├── docs/
│   └── planejamento_logico.pdf
└── src/
    └── main.py
```

## Como executar
```bash
git clone https://github.com/<seu-usuario>/tasktracker-projeto.git
cd tasktracker-projeto
python3 src/main.py
```
Não há dependências externas (apenas a biblioteca padrão do Python).

## Autor
Samuel Aleixo Amantéa – Ciência de Dados, UniCEUB
