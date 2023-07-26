from tkinter import *
from tkinter.filedialog import asksaveasfilename,askopenfilename
import subprocess

root=Tk()
root.title("Python IDE by HIT")
# root.attributes('-fullscreen',True)
file_path=''

def set_file_path(path):
    global file_path
    file_path=path

def run():
    code=editor.get('1.0',END)
    exec(code)

def execute():
    save_file()
    command=f'python {file_path}'
    process=subprocess.Popen(command,stdout=subprocess.PIPE,stderr=subprocess.PIPE,shell=True)
    output,error=process.communicate()
    code_op.insert('1.0',output)
    code_op.insert('1.0',error)

def new_file():
    global file_path
    file_path=''
    editor.delete('1.0', END)
    code_op.delete('1.0', END)


def save_as():
    path=asksaveasfilename(filetypes=[('Python File','*.py')])
    with open(path,'w') as file:
        code=editor.get('1.0',END)
        file.write(code)
        set_file_path(path)

def save_file():
    if file_path == '':
        path=asksaveasfilename(filetypes=[('Python File','*.py')])
    else:
        path=file_path
    with open(path,'w') as file:
        code=editor.get('1.0',END)
        file.write(code)
        set_file_path(path)

def open_file():
    path=askopenfilename(filetypes=[('Python File','*.py')])
    with open(path, 'r') as file:
        code=file.read()
        editor.delete('1.0',END)
        editor.insert('1.0',code)
        set_file_path(path)

menu_bar=Menu(root)

file_menu=Menu(menu_bar,tearoff=0)
file_menu.add_command(label='New',command=new_file)
file_menu.add_command(label='Open',command=open_file)
file_menu.add_command(label='Save',command=save_file)
file_menu.add_command(label='Save As',command=save_as)
file_menu.add_command(label='Exit',command=exit)
menu_bar.add_cascade(label='File',menu=file_menu)

run_bar=Menu(menu_bar,tearoff=0)
run_bar.add_command(label='Execute',command=execute)
run_bar.add_command(label='Run in Terminal',command=run)
menu_bar.add_cascade(label='Run',menu=run_bar)

root.config(menu=menu_bar)

editor=Text()
editor.config(bg='lavender')
editor.pack()

code_op=Text(height=10)
code_op.config(bg='black',fg='green2')
code_op.pack()

root.mainloop()
