class Property():
    def __init__(self, name, value):
        self.prop = "\t" + name + ": " + value + ";\n"

class Style():
    def __init__(self, target: str, props: list):
        tmp = ""
        for prop in props:
            tmp += prop.prop

        self.style = target + "{\n" + tmp + "}\n"

    def __repr__(self) -> str:
        return self.style

class Stylesheet():
    def __init__(self, rules, file):
        f = open("./" + file, "w")

        tmp = ""
        for i in range(len(rules)):
            tmp += rules[i].style
        
        f.write(tmp)
        f.close()