def figure(num):

    if num <= 0:
        return

    print('*' * num)
    figure(num - 1)
    print('#' * num)



num = int(input())
figure(num)
