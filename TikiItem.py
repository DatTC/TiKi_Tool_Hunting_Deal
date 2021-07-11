


class TikiItem:
    def __init__(self):
        self.title = ""
        self.price = 0
        self.url = ""

    def info(self):
        return self.title + " | " + str(self.price) + " | " + str(self.url) 

    def isValidItem(self, parttens):
        for p in parttens:
            if self.title.lower().find(p.lower()) < 0:
                return False
        return True
