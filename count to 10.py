cases = int(input().rstrip())



for i in range(cases):
    bits = int(input())
    
    for i in range (2**bits):
        print(bin(i)[2:].zfill(bits))
