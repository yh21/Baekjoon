message = list(input())
reverse = message.copy()
reverse.reverse()

for i in range(0, len(message)):
    if message[i] != reverse[i]:
        print('0')
        break
else:
    print('1')