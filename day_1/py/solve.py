import re
def load_inp(s):
    with open("../" + s + ".txt", mode="r") as h:
        data = [x.strip() for x in h.readlines()]
    return data

def p1(inp):
    r = []
    for l in inp:
        d = re.findall(r'[0-9]', l)
        r.append(int(d[0] + d[-1]))
    print(sum(r))

def p2(inp):
    r = []
    for l in inp:
        l = l.replace("one", "o1e").replace("two", "t2o").replace("three", "t3e").replace("four", "f4r").replace("five", "f5e").replace("six", "s6x").replace("seven", "s7n").replace("eight", "e8t").replace("nine", "n9e")
        d = re.findall(r'[0-9]', l)
        r.append(int(d[0] + d[-1]))
    print(sum(r))
def main(inp_ref):
    inp = load_inp(inp_ref)
    # p1(inp)
    p2(inp)

if __name__ == '__main__':
    main("test2")