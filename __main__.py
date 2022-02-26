import tokenise
import Parser

# args = process.argv[2]
# buffer = fs.readFileSync(args).toString()
# str1 = ["if", "(",  "!", "sayHello", "==", "True", ")"]
with open('javaCodeTest.txt', 'r') as file:
    data = file.read().replace('\n', '')

scanner = tokenise.Scanner()
tokens = scanner.tokenize(data)
parser = Parser.Parser()
asts = parser.parse(tokens)
print(asts)
# result = new Visitor().visitStatements(asts)

# fs.writeFileSync("test/cls-transpiled.js", result);
# log(args, " successfully transpiled!!");
