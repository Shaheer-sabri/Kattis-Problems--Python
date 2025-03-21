import math

# Read the number of messages
number = int(input())
messages = []

# Read all input messages
for _ in range(number):
    message = input()
    messages.append(message)

# Process each message
for x in messages:
    L = len(x)  # Length of the original message
    K = math.ceil(math.sqrt(L))  # Find the smallest K such that K^2 >= L
    M = K * K  # The padded length

    # Pad the message with '*' to fit K x K
    x = x.ljust(M, '*')

    # Convert the message into a KxK matrix (row-major order)
    matrix = [list(x[i * K:(i + 1) * K]) for i in range(K)]

    # Rotate the matrix 90 degrees clockwise
    rotated_matrix = [[matrix[K - 1 - j][i] for j in range(K)] for i in range(K)]

    # Read the encrypted message row-wise and remove asterisks
    encrypted_message = ''.join(''.join(row) for row in rotated_matrix).replace('*', '')

    # Print the final encoded message
    print(encrypted_message)
