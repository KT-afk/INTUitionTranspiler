import tokenise
import Parser

# 'Text' class is used to display the input-field

t1 = tk.Text(window,width=50,height=25,borderwidth=5,relief='groove')
t1.grid(row=5,column=3, sticky = 'nsew', padx= 10, pady= 3)

title1 = tk.Text(window,width=43,height=1,borderwidth=5,relief='groove')
title1.grid(row=1,column=3, sticky = 'w', padx= 10, pady= 1)

t2 = tk.Text(window,width=50,height=25,borderwidth=5,relief='groove')
t2.grid(row = 5, column = 7, sticky = 'nsew', padx= 4, pady= 4)

def translate():
    filePath = title1.get('1.0','end-1c')
    with open(filePath, 'r') as file:
        data = file.read().replace('\n', '')
    t1.insert('1.0', data)
    scanner = tokenise.Scanner()
    tokens = scanner.tokenize(data)
    parser = Parser.Parser()
    asts = parser.parse(tokens)

    t2.insert('1.0', data)

# press button to upload file
def upload_action(event=None):
    # filename = filedialog.askopenfilename()
    ftype = [('Text File','*.txt')]
    filename = filedialog.askopenfilename(filetypes = ftype)

    title1.insert('1.0', filename)


# press button > verify uploaded file

def verify_script():
    text_t = title1.get('1.0','end-1c')

    if text_t == '':
        tk.Label(window, text="Please upload a file.", fg='red').grid(row=8, column=3)
    else:
        tk.Label(window, text="Script is verified.", fg='green').grid(row=8, column=3)


# upload button
btn_upload = tk.Button(window, text = "Upload", fg = "black", command = upload_action)
btn_upload.grid(row = 1, column = 3, sticky = 'e', padx= 12, pady= 4)

# verify button
btn_verify = tk.Button(window, text = "Verify", fg = "black", command = verify_script)
btn_verify.grid(row = 8, column = 3, sticky = 'e', padx= 75, pady= 0)

# enter button, command to translate script add later
btn_enter = tk.Button(window, text = "Translate", fg = "black", command = translate)
btn_enter.grid(row = 8, column = 3, sticky = 'e', padx=13, pady= 0)


window.mainloop()
# args = process.argv[2]
# buffer = fs.readFileSync(args).toString()
# str1 = ["if", "(",  "!", "sayHello", "==", "True", ")"]
# with open('javaCodeTest.txt', 'r') as file:
#     data = file.read().replace('\n', '')
# scanner = tokenise.Scanner()
# tokens = scanner.tokenize(data)
# parser = Parser.Parser()
# asts = parser.parse(tokens)
# print(asts)

# result = new Visitor().visitStatements(asts)

# fs.writeFileSync("test/cls-transpiled.js", result);
# log(args, " successfully transpiled!!");
