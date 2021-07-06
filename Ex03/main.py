from Action import Action
from Graph import Graph

def findMaxInTransaction(allTransaction):
    max_transaction_number = allTransaction[0].transactionNumber

    for t in allTransaction:
        if max_transaction_number < t.transactionNumber:
            max_transaction_number = t.transactionNumber

    return max_transaction_number

def isOneOfThemWriteAction(firstTransaction, secondTransaction):
    return firstTransaction.actionName == "W" or secondTransaction.actionName == "W"

def isActionOnSameTable(firstTransaction, secondTransaction):
    return firstTransaction.tableName == secondTransaction.tableName

# decrease by 1 for Graph
def isDifferentTransactionNumber(firstTransaction, secondTransaction):
    return firstTransaction.transactionNumber != secondTransaction.transactionNumber

def makeGraphOfTransaction(allTransaction):
    g = Graph(findMaxInTransaction(allTransaction))
    addEdges(g, allTransaction)
    return g

# R2(A);R1(B);W2(A);R2(B);R3(A);W1(B);W3(A);W2(B)
def addEdges(g, allTransaction):
    curr = 0

    while curr != allTransaction.__len__():
        innerCurr = curr+1

        while innerCurr != allTransaction.__len__():
            if isActionOnSameTable(allTransaction[curr], allTransaction[innerCurr]):
                if isDifferentTransactionNumber(allTransaction[curr], allTransaction[innerCurr]):
                    if isOneOfThemWriteAction(allTransaction[curr], allTransaction[innerCurr]):
                        g.addEdge(allTransaction[curr].transactionNumber - 1, allTransaction[innerCurr].transactionNumber - 1)

            innerCurr += 1

        curr += 1


if __name__ == '__main__':
    query = input("Please enter the transaction: ")
    allTransaction = query.split(";")
    allTransaction = Action.makeListOfActions(allTransaction)

    g = makeGraphOfTransaction(allTransaction)

    if g.isCyclic():
        print("NO")
    else:
        g.topologicalSort()