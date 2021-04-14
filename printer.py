from prettytable import PrettyTable


def Grammar_Printer(grammar):
    print('--------------------------- GRAMMAR -----------------------------')
    print(grammar)

    print('+------------------------------- FIRST --------------------------------+')
    tableFirst = PrettyTable(["Methods", "Assignment", "Set"])
    tableFirst.align["Methods"] = "l"
    tableFirst.align["Assignment"] = "c"
    tableFirst.align["Set"] = "l"
    for terminal in grammar.Terms:
        tableRow = terminal.funcFirst()
        tableFirst.add_row([tableRow['methods'], tableRow['assignment'], tableRow['set']])

    print(tableFirst)

    print('+------------------------------------- FOLLOW -----------------------------------------+')
    tableFollow = PrettyTable(["Methods", "Assignment", "Set"])
    tableFollow.align["Methods"] = "l"
    tableFollow.align["Assignment"] = "c"
    tableFollow.align["Set"] = "l"
    for terminal in grammar.Terms:
        tableRow = terminal.funcFollow()
        tableFollow.add_row([tableRow['methods'], tableRow['assignment'], tableRow['set']])

    print(tableFollow)

def Grammar_Table_Printer(s):
    ljust = 15
    print('\n-------------------------TABLE-------------------------')
    print(s.table)
    print()

    # header
    for non_terminal in s.table:
        line = "".ljust(ljust + len(non_terminal) - 1)

        for terminal in s.table[non_terminal]:
            line += terminal.ljust(ljust)

        centerWord = "TABLE"

        lineLen = len(line)
        halfLineLen = int(lineLen / 2)
        centerWordLen = len(centerWord)
        halfCenterWordLen = int(centerWordLen / 2)

        headerLines = "".ljust((halfLineLen - halfCenterWordLen), '-')
        print(headerLines + centerWord + headerLines)
        print("|" + line + "|")

        break

    # body
    for non_terminal in s.table:
        line = non_terminal.ljust(ljust)

        for terminal in s.table[non_terminal]:
            value = s.table[non_terminal][terminal]
            if (type(value) is tuple):
                line += str(value[1]).ljust(ljust)
            else:
                line += str(value).ljust(ljust)

        print("|" + line + "|")


def LexicPrint(tokens):
    print('\n-------------------------LEXIC-------------------------')

    for token in tokens:
        print(token)


def CompileHistoric(historic):
    print('\n-----------------------HISTORIC-----------------------')
    print(historic)
