while True:

    msg = (input('What is your message? '))

    dig = int((input('What is your shift integer? ')))
    def cCipher(a, b):
        enc = ""
        for i in a:
            ltr = ord(i)
            xltr = (ltr + b)
            cltr = chr(xltr)
            enc = enc + cltr
        print(enc)
        return

    cCipher(msg, dig)

    while True:
        answer = str(input('Run again? (y/n): '))
        if answer in ('y', 'n'):
            exit()
        print("invalid input.")
    if answer == 'y':
        continue
    else:
        print("Goodbye")
        exit()
