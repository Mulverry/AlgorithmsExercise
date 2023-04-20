ppap = input()

stack = []
for char in ppap:
    stack.append(char)
    if len(stack) >= 4 and stack[-4:] == ['P', 'P', 'A', 'P']:
        stack[-4:] = ['P']
if stack == ['P']:
    print('PPAP')
else:
    print('NP')