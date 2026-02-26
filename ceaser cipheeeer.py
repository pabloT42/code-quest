cases = int(input().rstrip())

for i in range(cases):

    shift = int(input())

    message = input()

    encrypted_message = ""

    for i in message:
        
        if i == " ":
            encrypted_message+=" "

        elif ord('a') <= ord(i) <= ord('z'):

            shifted = (ord(i) - ord('a') - shift) % 26

            encrypted_message += chr(shifted + ord('a'))


    print(encrypted_message)
