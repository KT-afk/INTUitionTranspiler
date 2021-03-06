from gettext import install
from util import isDataType, isDigit, isLoop, isAlphaNumeric, isKeyword, isOp

class Scanner :
    tokens = []
    def _init_(self) :
        self.inst = 0
        self.tokens = []
  

    def tokenize(self, strCode): 
        s = ""
        newString = True

        for index in range(len(strCode)) :
            s += strCode[index]

            s = s.strip()

            if index + 1 >= len(strCode) :
                peek = ''
            else :
                peek = strCode[index + 1]

            if isDigit(s.strip()) and not isDigit(peek) :
                self.tokens.append({ "type": "NUM", "value": s.strip() })
                s = ""
                continue

            if s.strip() == "(" or s.strip() == ")" :
                if s.strip() == "(" :
                    self.tokens.append({ "type": "LPAREN" }) 
                else:
                    self.tokens.append({ "type": "RPAREN" })
                s = ""
                continue

            if s.strip() == "{" :
                self.tokens.append({ "type": "LBRACE" })
                s = ""
                continue


            if s.strip() == "}" :
                self.tokens.append({ "type": "RBRACE" })
                s = ""
                continue

            if s.strip() == "[" :
                self.tokens.append({ "type": "LSQUARE" })
                s = ""
                continue


            if s.strip() == "]" :
                self.tokens.append({ "type": "RSQUARE" })
                s = ""
                continue

            if s.strip() == '"' :
                if newString == True:
                    self.tokens.append({ "type": "LQUOTE" })
                    newString = False
                else :
                    self.tokens.append({ "type": "RQUOTE" })
                    newString = True
                s = ""
                continue

            if isAlphaNumeric(s.strip()) and not isAlphaNumeric(peek) :
                if isKeyword(s.strip()) :
                    self.tokens.append({ "type": "KEYWORD", "value": s })
                elif isDataType(s.strip()) :
                    self.tokens.append({ "type": "DATATYPE", "value": s })
                elif isLoop(s.strip()) :
                    self.tokens.append({ "type": "LOOPKEYWORD", "value": s})
                else :
                    self.tokens.append({ "type": "IDENTIFIER", "value": s })
                s = ""
                continue

            if isOp(s.strip()) and (not isOp(peek)) :
                self.tokens.append({ "type": "OP", "value": s.strip() })
                s = ""
                continue
            

            if s == ";" or s == "\n" :
                self.tokens.append({ "type": "EOL" })
                s = ""
                continue

            if s == "," :
                self.tokens.append({ "type": "COMMA" })
                s = ""
                continue

            if s == "." :
                self.tokens.append({ "type": "CALL" })
                s = ""
                continue
            
        self.tokens.append({ "type": "EOF" })
        return self.tokens

# Read test java code
with open('javaCodeTest.txt', 'r') as file:
    data = file.read().replace('\n', '')

# # Example java code
# testStr = "class Book { addBook() {}    removeBook() {} static getOneBook() {} } for (int i = 0; i < 10; i++) {}"

# # Tokenise java code string
# testFunc = Scanner()
# print(testFunc.tokenize(data))
