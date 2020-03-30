def maior(*num):
    print("-="*30)
    for i in num:
        print(f"{i} ", end="")
    print(f"foram passados {len(num)} parâmetros.")
    print(f"O maior valor passado foi {max(num)}")


#Programa Principal
maior(2,9,4,5,7,1)
maior(4,7,0)
#maior()
