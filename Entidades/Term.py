from prettytable import PrettyTable

class TermUnit:
    TERMINAL = 'TERMINAL'
    NONTERMINAL = 'NON-TERMINAL'
    EMPTY = 'EMPTY'
    STREAM_END = '$'

    def __init__(self, firstType, firstText):
        self.type = firstType
        self.text = firstText

    def __str__(self):
        return self.text

    def __repr__(self):
        return self.__str__()


class Term:
    RE = r'\s*(.+)\s*->\s*(.+)\s*'

    def __init__(self, left, text):
        self.left = left
        self.right = []
        self.text = text

        self.lFix = 20

        self.first = set()
        self.follow = set()

    def __str__(self):
        return self.left  # + " -> " + str([[j.text for j in tunit] for tunit in self.right])

    def __repr__(self):
        return self.left
    
    def funcFirst(self):
        tableRow = dict()
        tableRow['methods'] = ("first("+self.left + ")").ljust(self.lFix)
        tableRow['assignment'] = " => "
        tableRow['set'] = str(self.first)
        return tableRow

    def funcFollow(self):
        tableRow = dict()
        tableRow['methods'] = ("follow(" + self.left + ")").ljust(self.lFix)
        tableRow['assignment'] = " => "
        tableRow['set'] = str(self.follow)
        return tableRow
