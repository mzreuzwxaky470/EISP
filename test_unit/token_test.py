import tiktoken




def num_tokens_from_string(string: str) -> int:
    """Returns the number of tokens in a text string."""
    encoding = tiktoken.get_encoding("cl100k_base")
    num_tokens = len(encoding.encode(string))
    return num_tokens

code = """
X, K, D = map(int, input().split())

X = abs(X)  # Consider the absolute value of X

# Calculate the number of moves needed to reach X
moves_needed = X // D

if K >= moves_needed:
        # If K is greater than or equal to moves_needed, go to 0
        K -= moves_needed
        X -= moves_needed * D
else:
        # If K is less than moves_needed, distribute moves to minimize absolute value
        X -= K * D
        K = 0

    # The remaining moves should be used to get as close to 0 as possible
if K % 2 == 1:
        X = abs(X - D)

print(X)

"""

print(num_tokens_from_string(code))
