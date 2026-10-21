"""
MAIN — Demonstração do código-base
AOC 2026.2

Este programa utiliza somente LOAD, JMP e HALT,
que já estão implementados no código-base.

Depois de implementar as demais instruções, substitua
o programa de teste por um programa mais completo.
"""

from cpu import CPU

cpu = CPU()


cpu.memoria[0] = "LOAD R0, 10"
cpu.memoria[1] = "LOAD R1, 3"
cpu.memoria[2] = "ADD R0, R1"
cpu.memoria[3] = "STORE R0, 15"
cpu.memoria[4] = "SUB R0, R1"
cpu.memoria[5] = "LOAD R2, 12"
cpu.memoria[6] = "LOAD R3, 10"
cpu.memoria[7] = "AND R2, R3"
cpu.memoria[8] = "OR R2, R3"
cpu.memoria[9] = "XOR R2, R3"
cpu.memoria[10] = "HALT"

print("======================================")
print("       CPU SIMULADA — 8 BITS")
print("======================================")

cpu.executar()

print()
print("======================================")
print("RESULTADO FINAL")
print("======================================")

cpu.mostrar_estado()
print("Memória na posição 15:", cpu.memoria[15])



