import tokenise
import Parser
from visitor import *

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
result = Visitor().visitStatements(asts)
print(result)

# fs.writeFileSync("test/cls-transpiled.js", result);
# log(args, " successfully transpiled!!");
