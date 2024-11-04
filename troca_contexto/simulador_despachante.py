import threading
import time
import random
from collections import deque


class Processo:
    def __init__(self, pid, nome):
        self.pid = pid  # ID do processo
        self.nome = nome  # Nome do processo
        # Tempo total de execução do processo
        self.tempo_execucao = random.randint(3, 7)
        self.tempo_restante = self.tempo_execucao  # Tempo restante para execução
        self.lock = threading.Lock()  # Para gerenciar acesso ao tempo restante

    def executar(self, quantum):
        with self.lock:  # Garante acesso seguro à variável compartilhada
            tempo_a_executar = min(self.tempo_restante, quantum)
            print(f"Executando processo {self.nome} (PID: {self.pid}) por {tempo_a_executar} segundos.")
            time.sleep(tempo_a_executar)  # Simula o tempo de execução
            self.tempo_restante -= tempo_a_executar  # Reduz o tempo restante
            if self.tempo_restante == 0:
                print(f"Processo {self.nome} (PID: {self.pid}) finalizado.")
            else:
                print(f"Processo {self.nome} (PID: {self.pid}) ainda tem {self.tempo_restante} segundos restantes.")


class Despachante:
    def __init__(self, processos, quantum):
        self.processos = processos
        self.quantum = quantum
        self.fila = deque(processos)  # Fila de processos para escalonamento

    def executar(self):
        while self.fila:
            processo_atual = self.fila.popleft()  # Retira o processo do início da fila
            thread = threading.Thread(
                target=processo_atual.executar, args=(self.quantum,))
            print(f"\n[Despachante] Trocando para: {processo_atual.nome}")
            thread.start()  # Inicia a thread
            thread.join()  # Aguarda a thread finalizar
            if processo_atual.tempo_restante > 0:
                # Se não terminou, coloca de volta na fila
                self.fila.append(processo_atual)

# Simulação


def simular_sistema_operacional():
    # Criando processos
    processos = [
        Processo(1, "Processo_A"),
        Processo(2, "Processo_B"),
        Processo(3, "Processo_C"),
        Processo(4, "Processo_D"),
        Processo(5, "Processo_E"),
        Processo(6, "Processo_F"),
        Processo(7, "Processo_G")
    ]

    quantum = 2  # Iniciar o despachante com um tempo de troca de 2 segundos
    print("Iniciando a simulação do despachante com troca de contexto entre threads...")
    despachante = Despachante(processos, quantum)
    despachante.executar()
    print("\nTodos os processos foram executados.")


# Executar a simulação
simular_sistema_operacional()
