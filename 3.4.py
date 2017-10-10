
class Hanoi():
    def __init__(self, size = 5):
        self.towers = [[], [], []]
        self.size = size
        self.towers[0] = [x for x in range(size, 0, -1)]
    
    def __str__(self):
        string = []
        string.append("Hanoi [ ")
        for j in range(3):
            string.append("Tower " + str(j) + " [ ")
            if len(self.towers[j]) == 0:
                string.append("None")
            else:
                for i in range(0, len(self.towers[j])):
                    string.append(str(self.towers[j][i]))
                    string.append(",")
                del(string[-1])
            string.append(" ] ")
        string.append("]")
        string = "".join(string)
        return string

    def play(self):
        print(str(self))
        self.moveDisk(self.size, 0, 2, 1)
        print(str(self))
        return

    def moveDisk(self, disk, origin, destination, helper):
        if disk == 1:
            item = self.towers[origin].pop()
            self.towers[destination].append(item)
            print("Disk " + str(item) + ": Tower " + str(origin) + " -> " + str(destination))
        else:
            self.moveDisk(disk-1, origin, helper, destination)
            self.moveDisk(1, origin, destination, helper)
            self.moveDisk(disk-1, helper, destination, origin)
        return


    

if __name__ == "__main__":
    h = Hanoi(5)
    h.play()