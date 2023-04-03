def fact_sum(num):
    if num == 0:
        return 1
    return num * fact_sum(num - 1)

num = int(input())
print(fact_sum(num))
