import re

def decode_matrix_script(rows, columns, matrix):
    decoded_script = ''
    
    for col in range(columns):
        column_chars = [matrix[row][col] for row in range(rows)]
        decoded_script += ''.join(column_chars)
    
    # Replace symbols and spaces between alphanumeric characters with a single space
    decoded_script = re.sub(r'(?<=[a-zA-Z0-9])[^a-zA-Z0-9]+(?=[a-zA-Z0-9])', ' ', decoded_script)
    
    return decoded_script

# Input
rows, columns = map(int, input().split())
matrix = [input() for _ in range(rows)]

# Decode matrix script
decoded_script = decode_matrix_script(rows, columns, matrix)

# Output
print(decoded_script)
