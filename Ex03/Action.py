def fromStringToAction(transaction):
    listOfChar = list(transaction)

    indexOfOpenParenthesis = str.index(transaction, '(')

    return Action(listOfChar[0], int(transaction[1:indexOfOpenParenthesis]), listOfChar[indexOfOpenParenthesis + 1])

def eraseAllSpaces(string):
    return string.replace(" ", "")

class Action:
    def __init__(self, actionName, transactionNumber, tableName):
        self.actionName = actionName
        self.transactionNumber = transactionNumber
        self.tableName = tableName

    def getActionName(self):
        return self.actionName

    def getTableName(self):
        return self.tableName

    def getTransactionNumber(self):
        return self.transactionNumber

    def makeListOfActions(stringTransaction):
        result = []

        for t in stringTransaction:
            result.append(fromStringToAction(eraseAllSpaces(t)))

        return result

    def __str__(self):
        return self.actionName + str(self.transactionNumber) + "(" + self.tableName + ")"