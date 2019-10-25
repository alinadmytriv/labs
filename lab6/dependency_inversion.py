"""Dependency inversion
Rose & Chamomile inherit Flower
function flower_color has Rose & Chamomile"""
class Flower:
    def color(self):
        pass

class Chamomile(Flower):
    def color(self):
        return "white"

class Rose(Flower):
    def color(self):
        return "red"

def flower_color(flower):
    print(flower.color())

def main():
    f1 = Rose()
    f2 = Chamomile()
    flower_color(f1)
    flower_color(f2)

if __name__ == '__main__':
    main()