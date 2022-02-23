import random

slova=["slovo", "vorona", "lev", "pravo"]
s=random.choice(slova)
g=random.randint(1, len(s))
e=s[g]
h=s[0:g]+'?'+s[g+1:len(s)]

print(h)
f=input('guess the letter ')
if f==e:
    print("You win")
else:
    print("you lose(")