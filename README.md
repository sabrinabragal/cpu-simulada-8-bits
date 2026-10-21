CPU Simulada — 8 Bits Nome: Sabrina Braga Lima 582060

Projeto desenvolvido para a disciplina de Arquitetura e Organização de Computadores (AOC 2026.2).
O objetivo é simular o funcionamento básico de uma CPU de 8 bits, implementando registradores, memória, 
contador de programa, Unidade Lógica e Aritmética (ULA) e execução de instruções.

1.Arquitetura
A CPU simulada possui:
Dados de 8 bits.
Quatro registradores: R0, R1, R2 e R3.
Memória com 16 posições.
Contador de programa (PC).
Unidade Lógica e Aritmética (ULA).
Ciclo de execução Fetch, Decode e Execute.
 FETCH - obter da memória a instrução indicada pelo PC.
 DECODE - identificar qual instrução foi obtida e quais são seus operandos.
 EXECUTE - realizar a operação e atualizar registradores, memória ou PC.
   
2.Instruções implementadas
LOAD: carrega um valor em um registrador.
STORE: armazena um valor na memória.
ADD: realiza uma soma.
SUB: realiza uma subtração.
AND: realiza uma operação lógica AND.
OR: realiza uma operação lógica OR.
XOR: realiza uma operação lógica XOR.
JMP: altera o endereço do programa.
HALT: encerra a execução.

3.Arquivos do projeto
cpu.py: estrutura principal da CPU.
ula.py: operações aritméticas e lógicas.
main.py: programa de demonstração.
testes.py: testes das instruções implementadas.

4.Como executar
É necessário ter Python 3 instalado.
Para executar a demonstração:
python main.py
Para executar os testes:
python testes.py

5. Exemplo de funcionamento
Um programa pode carregar os valores 5 e 8 em registradores, somá-los e armazenar o resultado na posição 15 da memória.
O resultado esperado é:
R0 = 13 após a soma.
Memória na posição 15 = 13 após a instrução STORE.
