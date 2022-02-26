import tokenise
import Parser

# args = process.argv[2]
# buffer = fs.readFileSync(args).toString()
testStr = "class Book { addBook() {} removeBook() {} static getOneBook() {} }"
# str1 = ["if", "(",  "!", "sayHello", "==", "True", ")"]
scanner = tokenise.Scanner()
tokens = scanner.tokenize(testStr)
parser = Parser.Parser()
asts = parser.parse(tokens)
print(asts)
# result = new Visitor().visitStatements(asts)

# fs.writeFileSync("test/cls-transpiled.js", result);
# log(args, " successfully transpiled!!");
