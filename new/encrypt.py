import sys

fil = sys.argv[0]
cheie = sys.argv[1]
inp = sys.argv[2]
ou = sys.argv[3]
f = open(ou, "wb")
g = open(inp, "r")
i = 0
sir_intrare = g.read(1)
while sir_intrare:
    f.write((ord(sir_intrare) ^ ord(cheie[i % len(cheie)])).to_bytes(1, 'big'))

    i += 1
g.close()
f.close()
