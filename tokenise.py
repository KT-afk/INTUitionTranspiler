from gettext import install
from util import isDigit, isAlpha, isAlphaNumeric, isKeyword, isOp

class Scanner :
    tokens = []
    def _init_(self) :
        self.inst = 0
        self.tokens = []
  

    def tokenize(self, strCode): 
        s = ""; 

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
    

            if isAlphaNumeric(s.strip()) and not isAlphaNumeric(peek) :
                if isKeyword(s.strip()) :
                    self.tokens.append({ "type": "KEYWORD", "value": s })
                else :
                    self.tokens.append({ "type": "IDENTIFIER", "value": s })
                s = ""
                continue

            if isOp(s.strip()) and not isOp(peek) :
                self.tokens.append({ "type": "OP", "value": s.strip() })
                s = ""
                continue
            

            if s == ";" or s == "\n" :
                self.tokens.append({ "type": "EOL" })
                s = ""
                continue
            
        self.tokens.append({ "type": "EOF" })
        return self.tokens


testStr = "class Book { addBook() {} removeBook() {} static getOneBook() {} }"
print(len(testStr))
testFunc = Scanner()
print(testFunc.tokenize(testStr))