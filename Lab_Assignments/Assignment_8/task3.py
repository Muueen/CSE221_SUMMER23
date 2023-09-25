# -*- coding: utf-8 -*-
"""task3.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1LZNmCPqm8b6Fsqkpu85JTbe-Kk833F3A
"""

def minimum_coin_change(coins, target_amount):
    dp_table = [float('inf')] * (target_amount + 1)
    dp_table[0] = 0

    for coin in coins:
        for i in range(coin, target_amount + 1):
            dp_table[i] = min(dp_table[i], dp_table[i - coin] + 1)

    return dp_table[target_amount] if dp_table[target_amount] != float('inf') else -1

input_file = open("/content/drive/MyDrive/cse221_ass08/input3_1.txt", "r")
output_file = open("/content/drive/MyDrive/cse221_ass08/output3_1.txt", "w")

N, target_amount = map(int, input_file.readline().strip().split())
coins = list(map(int, input_file.readline().strip().split()))

result = minimum_coin_change(coins, target_amount)
output_file.write(str(result))

input_file.close()
output_file.close()