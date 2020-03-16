class Shop():
    shopname = 'Roga i kopita'
    total = 0

    def __init__(self, branch, count):
        self.branch = branch
        self.count = count
        Shop.total += count

    def addcount(self):
        self.count += 1
        Shop.total += 1

    def totalinfo(self):
        print("Shop:", self.shopname, "\tBranch:", self.branch, "\tTotal per branch:", self.count)

test1 = Shop("ul Test1", 10)
test2 = Shop("ul Test2", 10)
test1.addcount()
test1.addcount()
test2.addcount()

print("Today all branch of:", Shop.shopname, "\nSell:", Shop.total, "goods\n")
test1.totalinfo()
test2.totalinfo()
