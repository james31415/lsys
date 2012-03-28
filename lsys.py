import sys
import lsysgrammar
import lsysturtle

class LSys:
    def __init__(self, axiom, rules, commands = None, dummy = True, initial_position = (0, -200), initial_angle = 90, angle = 90, length = 100):
        self.turtle = lsysturtle.LTurtle(initial_position, initial_angle, angle, length)

        conv = {
                "F": (self.turtle.draw,),
                "f": (self.turtle.forward,),
                "+": (self.turtle.turnright,),
                "-": (self.turtle.turnleft,),
                "[": (self.turtle.push,),
                "]": (self.turtle.pop,),
                " ": (self.donothing,)}

        if commands:
            self.commands = {k: tuple(conv[q][0] for q in i) for k, i in commands.items()}
        else:
            self.commands = conv
        
        self.length = length
        self.axiom = axiom
        self.rules = rules
        self.dummy = True

    def donothing(self):
        pass

    def interpret(self, axiom, debug = False):
        for c in axiom:
            try:
                for com in self.commands[c]:
                    com()
            except KeyError:
                if self.dummy:
                    continue
                else:
                    raise

    def run(self, depth, debug = False, scale = 0.6):
        self.turtle.set_length(self.length * scale ** depth)
        for axiom in lsysgrammar.full_iterate(depth, self.axiom, self.rules):
            self.interpret(axiom, debug)
        self.turtle.hide()

    def reset(self):
        self.turtle.reset()

    def mainloop(self):
        self.turtle.mainloop()

if __name__ == "__main__":
    axiom = " "
    rules = {" ": "F-[[ ]+ ]+F[+F ]- ", "F": "FF"}

    ls = LSys(axiom, rules, angle = 25)
   
    depth = int(sys.argv[1])

    ls.run(depth)
    ls.mainloop()
