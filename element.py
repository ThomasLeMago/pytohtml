class Element():
    def __init__(self, base: str, args: dict, child: any, sametag=False):
        self.base = base
        self.args = args
        self.child = child
        self.sameTag = sametag

        self.rendered = self.render()

    def render(self):
        f = open("./tmp.html", "w")
        e = "<" + self.base

        if self.args != {}:
            for arg in self.args:
                e += " " + str(arg) + "=\"" + str(self.args[arg]) + "\""

        if (self.sameTag):
            e += " />"
            f.write(e)
        else:
            e += ">"
            if type(self.child) != type(self):
                e += self.child
            else:
                e += self.child.rendered + "</" + self.child.base + ">" +"</" + self.base + ">"
            
            
            f.write(e)

        f.close()
        return e

class FullHTML():
    def __init__(self, title = "", sheet = ""):
        self.title = title
        
        self.sheet = ""

        if sheet != None:
            self.sheet = "<link rel=\"stylesheet\" href=\"" + sheet +"\">\n\t"



        f = open("./tmp.html", "r")
        tmp = f.read()
        f.close()

        f = open("./render.html", "w")

        f.write("<!DOCTYPE html>\n<html lang=\"en\">\n<head>\n\t<meta charset=\"UTF-8\">\n\t<meta http-equiv=\"X-UA-Compatible\" content=\"IE=edge\">\n\t<meta name=\"viewport\" content=\"width=device-width, initial-scale=1.0\">\n\t" + self.sheet + "<title>" + self.title + "</title>\n</head>\n<body>\n" + tmp + "\n</body>")
        f.close()