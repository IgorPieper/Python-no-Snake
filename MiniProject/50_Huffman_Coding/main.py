
def huffman(tableQ):
    left, right = [], []
    tableSites = {}

    for n in tableQ:
        tableSites[n] = ""

    while len(tableQ) > 1:
        extractedValue = {}
        tableQ, extractedValue, left = extract(tableQ, extractedValue, left)
        tableQ, extractedValue, right = extract(tableQ, extractedValue, right)
        tableQ = tableQ | insert(extractedValue)
        #print(tableQ)

    for n in range(0, len(left)):
        for m in left[n]:
            tableSites[m] = "0" + tableSites[m]
        for m in right[n]:
            tableSites[m] = "1" + tableSites[m]

    return tableSites


def extract(tableQ, extractedValue, site):
    minValue = min(tableQ.values())
    for n in tableQ:
        if tableQ[n] == minValue:
            minValueIndex = n
            break
    extractedValue[minValueIndex] = minValue
    del tableQ[minValueIndex]
    site.append(minValueIndex)
    return tableQ, extractedValue, site


def insert(extractedValue):
    keysList = []
    mergeTable = {}
    for n in extractedValue:
        keysList.append(n)
    mergeTable[f"{keysList[0] + keysList[1]}"] = extractedValue[keysList[0]]+extractedValue[keysList[1]]
    return mergeTable


def to_byte_array(bin_text):
    bonus_one = 8 - len(bin_text) % 8
    for i in range(bonus_one):
        bin_text += "0"

    bonus_two = "{0:08b}".format(bonus_one)
    full_text = bonus_two + bin_text

    if len(full_text) % 8 != 0:
        print("Encoded text not padded properly")
        exit(0)

    answer = bytearray()
    for i in range(0, len(full_text), 8):
        byte = full_text[i:i+8]
        answer.append(int(byte, 2))
    return answer


try:
    with open("start.txt", "r") as file:
        lines = file.readlines()
except FileNotFoundError:
    with open("start.txt", "w") as file:
        file.write("Sample Text")
    with open("start.txt", "r") as file:
        lines = file.readlines()

tableLetters = []
tableNumber = []
wholeText = ""

for i in lines:
    wholeText += i
    for n in range(0, len(i)):
        if i[n] in tableLetters:
            tableNumber[tableLetters.index(i[n])] += 1
        else:
            tableLetters.append(i[n])
            tableNumber.append(1)


#print(wholeText)
tableC = {}

with open("formula.txt", "w") as file:
    for i in range(0, len(tableLetters)):
        if tableLetters[i] == "\n":
            file.write(f"Enter: {tableNumber[i]}\n")
        else:
            file.write(f"{tableLetters[i]}: {tableNumber[i]}\n")
        tableC[tableLetters[i]] = tableNumber[i]

    fullFormula = huffman(tableC)

    file.write("\n\n\n")
    for n in fullFormula:
        if n == "\n":
            file.write(f"Enter: {fullFormula[n]}\n")
        else:
            file.write(f"{n}: {fullFormula[n]}\n")

bin_answer = ""

for n in wholeText:
    for m in fullFormula:
        if n == m:
            bin_answer += fullFormula[m]

result = to_byte_array(bin_answer)

#print(result)

with open("end.bin", "wb") as file:
    file.write(bytes(result))



