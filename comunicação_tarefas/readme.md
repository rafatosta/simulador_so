# Comunicação entre Processos com Python

Este projeto demonstra um exemplo prático de comunicação entre processos usando Python e o módulo `multiprocessing`. A atividade ilustra o conceito de **Comunicação entre Tarefas (IPC - Inter-Process Communication)**, simulado com um Produtor e um Consumidor que trocam mensagens através de uma fila compartilhada.

## Descrição

A comunicação entre tarefas é essencial em sistemas complexos onde múltiplos processos precisam cooperar para atingir um objetivo comum. Este exemplo simula:
- Um **Produtor** que envia mensagens simulando ações do usuário (ex.: clicar em botões).
- Um **Consumidor** que recebe e processa essas mensagens.

A comunicação é feita por meio de uma fila (`Queue`), que simula um mecanismo IPC, permitindo que os processos compartilhem informações e coordenem suas ações.

## Estrutura do Código

- **Produtor**: Gera mensagens e coloca-as na fila. Cada mensagem representa uma ação do usuário.
- **Consumidor**: Recebe mensagens da fila e reage a cada ação, simulando uma resposta do sistema a comandos do usuário.
- **Fila (`Queue`)**: O canal de comunicação entre o Produtor e o Consumidor, permitindo a troca de mensagens.

## Pré-requisitos

- Python 3.x

## Como Executar

1. Clone este repositório ou copie o código para seu ambiente de trabalho.
2. Salve o código em um arquivo, como `atividade_comunicacao.py`.
3. No terminal, execute o código com:
   ```bash
   python atividade_comunicacao.py
   ```

## Exemplo de saída

A saída do programa deve exibir o Produtor enviando ações para o Consumidor, e o Consumidor respondendo a cada ação. Um exemplo de saída:

```bash
Produtor: enviando ação - Clique no botão Reload
Consumidor: recebida ação - Clique no botão Reload
Produtor: enviando ação - Clique no botão Stop
Consumidor: recebida ação - Clique no botão Stop
Produtor: enviando ação - Arrastar Texto
Consumidor: recebida ação - Arrastar Texto
Consumidor: finalizando
Processo de comunicação entre tarefas finalizado.
```

## Explicação dos Conceitos
Este exemplo foi desenvolvido para ilustrar os seguintes conceitos:

- **Mecanismo IPC (Inter-Process Communication):** Comunicação entre processos independentes para sincronização e compartilhamento de informações.
- **Produtor e Consumidor:** Padrão de design onde um processo gera informações que outro processo utiliza.

## Personalização
Para expandir este exemplo, você pode:

- Adicionar mais ações no Produtor.
- Implementar respostas específicas no Consumidor para cada tipo de ação.