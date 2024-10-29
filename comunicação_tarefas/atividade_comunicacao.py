import multiprocessing
import time

# Função para o processo Produtor
def produtor(queue):
    actions = ["Clique no botão Reload", "Clique no botão Stop", "Arrastar Texto"]
    for action in actions:
        print(f"Produtor: enviando ação - {action}")
        queue.put(action)  # Envia a ação para o Consumidor
        time.sleep(1)  # Simula o tempo de espera entre ações
    queue.put("FIM")  # Indica ao Consumidor que terminou

# Função para o processo Consumidor
def consumidor(queue):
    while True:
        action = queue.get()  # Recebe a ação do Produtor
        if action == "FIM":
            print("Consumidor: finalizando")
            break
        print(f"Consumidor: recebida ação - {action}")
        # Aqui, poderíamos adicionar uma lógica para reagir a cada ação recebida

# Função principal
if __name__ == "__main__":
    # Cria uma fila para comunicação entre os processos
    queue = multiprocessing.Queue()

    # Cria os processos de Produtor e Consumidor
    produtor_process = multiprocessing.Process(target=produtor, args=(queue,))
    consumidor_process = multiprocessing.Process(target=consumidor, args=(queue,))

    # Inicia os processos
    produtor_process.start()
    consumidor_process.start()

    # Aguarda a finalização dos processos
    produtor_process.join()
    consumidor_process.join()

    print("Processo de comunicação entre tarefas finalizado.")
