class Adatok:
    def __init__(self, list):
        self.year = list[0]
        self.races = list[1]
        self.wins = list[2]
        self.podiums = list[3]
        self.poles = list[4]
        self.fastests = list[5]

def ImportFromTxt():
    f = open("jackie.txt", "r", encoding="UTF-8").read()
    lines = f.split("\n")
    temp = []
    for i in range(1, len(lines)):
        temp.append(Adatok(lines[i].split("\t")))
    return temp

def feladat4(list):
    temp = list[0]
    for i in range(1, len(list)):
        if list[i].races > temp.races:
            temp = list[i]
    return temp.year

def feladat5(list):
    yMap = dict()
    for i in range(len(list)):
        temp = list[i].year[2]
        if temp not in yMap:
            yMap[temp] = 0
        yMap[temp] += int(list[i].wins)
    formatYMap(yMap)

def formatYMap(map):
    for key in map:
        print(f"\t{key}0 - es évek: {map[key]} megnyer verseny")

def feladat6(list):
    lines = "<!DOCTYPE html>\n<html>\n<head></head>\n<style>td { border:1px solid black; }</style>\n<body>\n<h1>Jackie Stewart</h1>\n<table>\n"
    for i in list:
        lines += f"<tr><td>{i.year}</td><td>{i.races}</td><td>{i.wins}</td>\n"
    lines += f"</table>\n</body>\n</html>"

    writeToFile("jackie2.html", lines)


def writeToFile(filename, lines):    
    f = open(filename, "w", encoding="UTF-8")
    for i in lines:
        f.write(i)

def main():
    list = ImportFromTxt()
    print(f"3. feladat: {len(list)}")
    print(f"4. feladat: {feladat4(list)}")
    print("5. feladat: ")
    feladat5(list)
    print("6. feladat: jackie.html")
    feladat6(list)
main()