import sys

fil = sys.argv[0]
cheie = sys.argv[1]
inp = sys.argv[2]
ou = sys.argv[3]
f = open(ou, "w")
g = open(inp, "rb")
i = 0
sir_intrare = g.read(1)
while sir_intrare:
    f.write(chr(sir_intrare[0] ^ ord(cheie[i % len(cheie)])))
    sir_intrare = g.read(1)

g.close()

f.close()
