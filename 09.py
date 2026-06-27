def initial_stream():
    start = 2
    while True:
        yield start
        start += 1

def filter_stream(stream, prime):
    for x in stream:
        if x % prime==0:
            continue
        yield x
def prime_generator(stream):
    prime = next(stream)
    yield prime
    filtered = filter_stream(stream, prime)
    for p in prime_generator(filtered):
        yield p

g = prime_generator(initial_stream())
n = int(input())
print("First", n, "prime number(s):")

for _ in range(n):
    print(next(g), end=' ')
