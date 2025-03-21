while True:
    key = input("").strip()
    n_values = list(map(int, key.split()))
    n = n_values[0]
    n_values.pop(0)
    if n == 0:
        break
    message = input("")
    padding_needed = (n - len(message) % n) % n
    message = message + " " * padding_needed
    index = 0
    encrypted = ""
    while index < len(message):
        block = message[index:index + n]
        for x in n_values:
            encrypted = encrypted + block[x - 1]
        index = index + n    
    print(f"'{encrypted}'")
    