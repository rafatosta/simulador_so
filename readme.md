# Simulador de Despachante de Processos em Python

## Descrição

Este projeto é um simulador simples de um **despachante de processos** em um sistema operacional, implementado em Python usando **threads**. O objetivo do código é simular a execução de processos, alternando entre eles de forma controlada, utilizando o conceito de **quantum de tempo** do escalonamento round-robin.

Cada processo é executado por um tempo limitado (quantum), e se não terminar nesse período, é colocado de volta na fila para ser executado novamente até que todos os processos finalizem.

## Estrutura do Código

O código consiste em duas principais classes: `Processo` e `Despachante`.

### 1. Classe `Processo`
A classe `Processo` simula um processo individual com os seguintes atributos e métodos:
- **Atributos**:
  - `pid`: Identificador único do processo.
  - `nome`: Nome do processo.
  - `tempo_execucao`: Tempo total necessário para o processo ser executado (definido aleatoriamente entre 3 e 7 segundos).
  - `tempo_restante`: Tempo que falta para a execução completa do processo.
  - `lock`: Um bloqueio (threading.Lock) para gerenciar o acesso concorrente ao tempo restante.

- **Método**:
  - `executar(quantum)`: Executa o processo por um tempo limitado (quantum). Se o tempo restante for menor que o quantum, o processo termina. Caso contrário, o processo é pausado e colocado de volta na fila.

### 2. Classe `Despachante`
A classe `Despachante` gerencia a fila de processos e alterna a execução entre eles, simulando o comportamento do escalonador de um sistema operacional.

- **Atributos**:
  - `processos`: Lista de processos a serem executados.
  - `quantum`: Tempo máximo que um processo pode ser executado antes de ser trocado.
  - `fila`: Fila de processos, organizada como uma `deque` (fila de duas extremidades) para eficiência na remoção e adição de processos.

- **Método**:
  - `executar()`: Executa os processos um por um, retirando-os da fila e colocando-os de volta caso não tenham terminado. Ele cria uma nova thread para cada processo, simulando o tempo de execução.

### 3. Função `simular_sistema_operacional()`
Esta função inicializa três processos (`Processo_A`, `Processo_B`, e `Processo_C`), cria um despachante com quantum de 2 segundos, e inicia a simulação.

## Como Funciona

1. O programa cria três processos com tempos de execução aleatórios.
2. O despachante alterna entre os processos, permitindo que cada um seja executado por no máximo 2 segundos (quantum).
3. Se o processo não terminar dentro do quantum, ele é colocado novamente no final da fila.
4. O despachante continua alternando entre os processos até que todos tenham sido executados completamente.

## Execução

### Pré-requisitos
- Python 3.x
- Biblioteca `threading` (inclusa na instalação padrão do Python)
- Biblioteca `collections` (inclusa na instalação padrão do Python)

### Como Executar
Para executar o código, siga os seguintes passos:

1. Salve o código em um arquivo, por exemplo, `simulador_despachante.py`.
2. Abra o terminal ou prompt de comando.
3. Navegue até o diretório onde o arquivo está salvo.
4. Execute o comando:

```bash
python simulador_despachante.py
