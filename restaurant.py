def process(operations):
    pileA = 0 # Pile 1
    pileB = 0 # Pile 2
    for i in range(0, len(operations)):
        operation = operations[i].split(' ')[0]
        amount = int(operations[i].split(' ')[1])
        if operation == 'DROP': # This just drops, no other logic
            pileB += amount
            print(f"DROP 2 {amount}")
        
        elif operation == 'TAKE':
            if pileA == 0:    
                print(f"MOVE 2->1 {pileB}")
                print(f"TAKE 1 {amount}")
                pileA = pileB - amount
                pileB = 0
            else:
                
                if pileA >= amount:
                    print(f"TAKE 1 {amount}")
                    pileA = pileA - amount
                else:
                    print(f"TAKE 1 {pileA}")
                    remainingAmount = amount - pileA
                    pileA = 0
                    pileA = pileB - remainingAmount
                    print(f"MOVE 2->1 {pileB}")
                    print(f"TAKE 1 {remainingAmount}")
                    pileB = 0




while True:
    n = int(input())
    if n == 0:
        break
    inputs = []
    for i in range(0, n):
        inputs.append(input())

    process(inputs)
    print()