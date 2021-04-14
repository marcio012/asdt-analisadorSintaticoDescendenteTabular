from Entidades.Grammar.Grammar import Grammar
from Entidades.Term import TermUnit


class Token:
    def __init__(self, value, unit: TermUnit):
        self.value = value
        self.unit = unit

    def __str__(self):
        return str(self.unit) + " = (" + self.value + ")"

    def __repr__(self):
        return self.__str__()


class LexicAnalyzer:

    def __init__(self, text, grammar: Grammar):
        self.NSigma = grammar.Alphabet
        self.STREAM_END_UNIT = grammar.STREAM_END_UNIT

        self.text = " ".join(text.split('\n')) + " " + TermUnit.STREAM_END
        # print(self.text)

        self.cursor = 0

        self.tokens = []

    def getUnit(self, item):
        return next((x for x in self.NSigma if x.text == item), None)

    def getUnits(self, item):
        return [x for x in self.NSigma if (x.text.find(item, 0) + 1)]

    def isNotDone(self):
        return self.cursor < len(self.text)

    def isNotLast(self):
        return (self.cursor + 1) < len(self.text)

    def peekNext(self):
        return self.text[self.cursor + 1]

    def next(self):
        self.cursor += 1
        return self.current()

    def progress(self):
        self.cursor += 1

    def current(self):
        return self.text[self.cursor]

    @staticmethod
    def isWhiteSpace(string):
        string = string.strip()
        return string == "" or string == " " or string == "\n"  # or TermUnit.STREAM_END == string

    def isaBreak(self, string):
        return LexicAnalyzer.isWhiteSpace(string) or not self.isNotLast() or TermUnit.STREAM_END == string

    def isaDigitBreak(self, string):
        return self.isaBreak(string) or (not string.isdigit() and not string.isalpha())

    def isaOperandBreak(self, string):
        return self.isaBreak(string) or string.isdigit() or string.isalpha() or string == ';'

    @property
    def getToken(self):
        retorno = None
        state = 0
        accum = ""
        match = None

        while self.isNotDone():
            current = self.current()
            # print("current: "+current)
            if state == 0:
                if LexicAnalyzer.isWhiteSpace(current):
                    self.progress()
                    continue

                else:
                    accum += current
                    state = 1
                    continue

            elif state == 1:
                match = self.getUnit(accum)

                if self.isNotLast():
                    # print('notlast')

                    next = accum + self.peekNext()
                    nextUnits = self.getUnits(next)

                    nextUnitsLen = len(nextUnits)
                    matchNext = nextUnitsLen

                    if matchNext:
                        # print('matchnext')
                        accum += self.next()
                        continue

                    if match:
                        # if(self.isaOperandBreak(self.peekNext()) or self.isaDigitBreak(self.peekNext())):
                        if not (match.text == "ide") or not (match.text == "num"):
                            state = 2
                            continue

                state = 3

            elif state == 2:
                self.progress()
                retorno = match
                break

            elif state == 3:
                if self.isNotLast() and not self.isaDigitBreak(self.peekNext()):
                    accum += self.next()
                    # self.progress()
                    continue

                self.progress()

                if accum[0].isdigit():
                    retorno = self.getUnit("num")
                    if not accum.isnumeric():
                        raise Exception('variables can\'t start with numbers ON:' + accum)
                    if not retorno:
                        raise Exception('this grammar don\'t accept numbers ON:' + accum)

                elif accum == TermUnit.STREAM_END:
                    retorno = self.STREAM_END_UNIT

                else:
                    retorno = self.getUnit("ide")
                    if not retorno:
                        raise Exception('this grammar don\'t accept variables ON:' + accum)

                break

        retorno = Token(accum, retorno)
        self.tokens.append(retorno)

        return retorno
