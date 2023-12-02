def load_inp(s):
    with open("../" + s + ".txt", mode="r") as h:
        data = [x.strip() for x in h.readlines()]
    return data


GAME_CONF = {
    "red": 12,
    "green": 13,
    "blue": 14
}

class GameSet:
    def __init__(self, data:str):
        self.red = 0
        self.green = 0
        self.blue = 0
        for r in data.split(","):
            r = r.strip()
            d = int(r.split(" ")[0])
            c = r.split(" ")[-1]
            self.red = d if c == "red" else self.red
            self.green = d if c == "green" else self.green
            self.blue = d if c == "blue" else self.blue

class Game:
    def __init__(self, data:str):
        self.id = int(data.split(":")[0].split(" ")[-1].strip())
        self.data = [x.strip() for x in data.split(":")[-1].split(';')]
        self.sets = [GameSet(x) for x in self.data]
        self.red_max = 0
        self.green_max = 0
        self.blue_max = 0
        self._set_max()

    def _set_max(self):
        for s in self.sets:
            self.red_max = s.red if s.red > self.red_max else self.red_max
            self.green_max = s.green if s.green > self.green_max else self.green_max
            self.blue_max = s.blue if s.blue > self.blue_max else self.blue_max

    def check(self, conf):
        r = conf.get('red')
        g = conf.get('green')
        b = conf.get('blue')
        return r >= self.red_max and g >= self.green_max and b >= self.blue_max

    def pow(self):
        r = self.red_max if self.red_max > 0 else 1
        g = self.green_max if self.green_max > 0 else 1
        b = self.blue_max if self.blue_max > 0 else 1
        return r * g * b

def p1(inp):
    res = [g.id if g.check(GAME_CONF) else 0 for g in inp]
    print(sum(res))

def p2(inp):
    pows = [x.pow() for x in inp]
    print(sum(pows))

def main(inp_ref):
    inp = load_inp(inp_ref)
    games = [Game(l) for l in inp]
    p1(games)
    p2(games)

if __name__ == '__main__':
    main("input")