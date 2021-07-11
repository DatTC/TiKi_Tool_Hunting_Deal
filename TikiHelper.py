


from TikiTarget import TikiTarget 

def getTargetFromFile(fileName):
    targetFile = open(fileName,'r',encoding="utf-8") 
    # Normal: fileName = open(fileName,"r") but in TARGET_FILE have some word witer in vietnamese
    lines = targetFile.readlines()
    targetFile.close()
    targets = []
    i = 0
    while i < len(lines):
        newTarget = TikiTarget(lines[i].strip(),lines[i+1].strip())
        # print(newTarget.info())
        i += 2
        targets.append(newTarget)

    return targets

def convertToNum(strPrice):
    strPrice = strPrice.replace('.',"")
    strPrice = strPrice.replace('₫',"")
    return int(strPrice)