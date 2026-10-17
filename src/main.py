
from datetime import datetime, date

PRIORIDADES_VALIDAS = {
    "alta":"Alta",
    "média":"Média",
    "media":"Média",
    "baixa":"Baixa",
}
ORDEM_PRIORIDADE={"Alta":0,"Média":1,"Baixa":2}

tarefas=[]


def ler_titulo():
    """Regra 1: título obrigatório (não aceita vazio nem só espaços)."""
    while True:
        titulo = input("Título da tarefa: ").strip()
        if titulo:
            return titulo
        print("Erro: o título não pode ser vazio. Tente novamente.")


def ler_prioridade():
    """Regra 2: aceita apenas Alta, Média (ou Media) e Baixa."""
    while True:
        entrada = input("Prioridade (Alta, Média ou Baixa): ").strip().lower()
        if entrada in PRIORIDADES_VALIDAS:
            return PRIORIDADES_VALIDAS[entrada]
        print("Erro: prioridade inválida. Use apenas Alta, Média ou Baixa.")


def ler_data_limite():
    """Regra 3: data no formato DD/MM/AAAA e não retroativa."""
    while True:
        entrada = input("Data limite (DD/MM/AAAA): ").strip()
        try:
            data = datetime.strptime(entrada, "%d/%m/%Y").date()
        except ValueError:
            print("Erro: data inválida. Use o formato DD/MM/AAAA.")
            continue
        if data < date.today():
            print("Erro: a data limite não pode ser anterior à data atual.")
            continue
        return entrada

def cadastrar_tarefa():
    print("cadastrar nova tarefa")
    titulo=ler_titulo()
    descricao=input("descrição da tarefa:").strip()
    prioridade=ler_prioridade()
    data_limite=ler_data_limite()

    tarefas.append({
        "titulo":titulo,
        "descricao":descricao,
        "prioridade":prioridade,
        "data_limite":data_limite,
        "status":"Pendente",
    })
    print(f"Tarefa'{titulo}'cadastrada com sucesso")


def ordenar_tarefas():
    """Ordena da prioridade mais urgente para a menos urgente, depois por data."""
    return sorted(
        tarefas,
        key=lambda t: (
            ORDEM_PRIORIDADE[t["prioridade"]],
            datetime.strptime(t["data_limite"], "%d/%m/%Y"),
        ),
    )


def exibir_tarefas(lista):
    for i, t in enumerate(lista, start=1):
        print(f"\n[{i}] {t['titulo']}")
        print(f"Descrição:{t['descricao'] or '(sem descrição)'}")
        print(f"Prioridade:{t['prioridade']}")
        print(f"Data limite:{t['data_limite']}")
        print(f"Status:{t['status']}")


def marcar_concluida(lista):
    """Regra 4: só conclui tarefas que existem na lista."""
    while True:
        entrada = input("Número da tarefa a concluir: ").strip()
        if entrada.isdigit() and 1 <= int(entrada) <= len(lista):
            tarefa = lista[int(entrada) - 1]
            if tarefa["status"] == "Concluída":
                print("Essa tarefa já está concluída.")
            else:
                tarefa["status"] = "Concluída"
                print(f"Tarefa '{tarefa['titulo']}' marcada como concluída!")
            return
        print(f"Erro: tarefa inexistente. Digite um número entre 1 e {len(lista)}.")


def visualizar_tarefas():
    print("Tarefas cadastradas")
    if not tarefas:
        print("Não há tarefas cadastradas no momento.")
        return

    lista = ordenar_tarefas()
    exibir_tarefas(lista)

    concluidas = sum(1 for t in tarefas if t["status"]=="Concluída")
    print(f"\nTotal: {len(tarefas)} tarefa(s) | Concluídas: {concluidas}")

    resposta = input("\nDeseja marcar alg   uma tarefa como concluída? (s/n): ").strip().lower()
    if resposta in ("s", "sim"):
        marcar_concluida(lista)


def menu():
    while True:
        print("\n TASKTRACKER ")
        print("1. Cadastrar nova tarefa")
        print("2. Visualizar tarefas cadastradas")
        print("3. Sair da aplicação")
        opcao = input("Escolha uma opção: ").strip()

        if opcao=="1":
            cadastrar_tarefa()
        elif opcao=="2":
            visualizar_tarefas()
        elif opcao=="3":
            print("Encerrando o TaskTracker.")
            break
        else:
            print("Opção inválida. Escolha 1, 2 ou 3.")


if __name__ == "__main__":
    menu()