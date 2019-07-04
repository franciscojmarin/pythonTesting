word = "días"
for num in range(10, 0, -1):
    if num == 1:
        word = "día"
        print(num, word, "para año nuevo.")
        print("Mañana será año nuevo.")
    else:
        print(num, word, "para año nuevo.")
        new_num = num - 1
        if new_num == 1:
            word = "dia"
            print("Mañana quedará ", new_num, word, " para año nuevo.")
        else:
            print("Mañana quedarán ", new_num, word, " para año nuevo.")

    print()

    
