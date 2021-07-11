

class TikiTarget:
    def __init__(self, pattenStr = "", categoryStr = ""):
        self.patternString = pattenStr
        self.patterns = self.__splitPattern()
        self.categoryUrl = categoryStr

    def info(self):
        return "Pattern: " + str(self.patterns) + " | Category: " + self.categoryUrl

    def __splitPattern(self):
        newList = self.patternString.split(",")
        i = 0
        while i < len(newList):
            newList[i] =  newList[i].strip()
            i += 1
        return newList

    def getKeyWord(self):
        keyworld = ""
        for key in self.patterns:
            keyworld = keyworld + " " + key
        return keyworld

    def getSearchLink(self,pageNum):
        return(self.categoryUrl +"?q="+ self.getKeyWord() +"&ref=categorySearch&page=" + str(pageNum))



