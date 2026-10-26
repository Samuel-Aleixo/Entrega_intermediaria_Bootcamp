# TaskTracker

Aplicação de linha de comando (CLI) em Python para gerenciamento de tarefas, desenvolvida no **Bootcamp II**. Na Fase 3 a aplicação foi **containerizada com Docker**.

Problema resolvido
Pessoas e equipes perdem o controle de prazos e prioridades quando as tarefas ficam espalhadas em anotações e mensagens. O TaskTracker centraliza o cadastro e a visualização das tarefas, organizando-as por prioridade.

Funcionalidades
- Cadastrar tarefas com título, descrição, prioridade e data limite
- Visualizar tarefas ordenadas da prioridade mais urgente para a menos urgente
- Marcar tarefas como concluídas e ver o total de concluídas

Regras de negócio
1. O título é obrigatório (vazio ou só espaços é rejeitado).
2. A prioridade deve ser `Alta`, `Média` (ou `Media`) ou `Baixa`.
3. A data limite deve estar no formato `DD/MM/AAAA` e não pode ser anterior à data atual.
4. Só é possível concluir tarefas que existam na lista.
5. Toda tarefa nasce com status `Pendente`.

Tecnologias
- Python 3.11
- Git e GitHub
- Docker e Docker Compose

Estrutura do projeto
```
tasktracker-projeto/
 .gitignore
 docs/
 planejamento_logico.pdf
 src/
 main.py
 Dockerfile
 docker-compose.yml
 README.md
```

Executando com Docker

Pré-requisito: [Docker](https://www.docker.com/) instalado e em execução.

**Como construir a imagem:**
```bash
docker build -t tasktracker .
```

**Como rodar o container em modo isolado:**
```bash
docker run -it tasktracker
```

**Como rodar via orquestração (Recomendado):**
```bash
docker compose run --rm tasktracker
```

> O `-it` (e, no Compose, `stdin_open` e `tty`) é necessário porque a aplicação usa `input()` e precisa de um terminal interativo.

## Executando sem Docker
```bash
python src/main.py
```

## Autor
Samuel Aleixo Amantéa – Ciência de Dados, UniCEUB
