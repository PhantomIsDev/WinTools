import tkinter as tk
import tkinter.font as tkFont
from tkinter import *
from tkinter import filedialog
import subprocess
import os


class App:
    def __init__(self, root):
        window = tk.Tk()
        window.withdraw()
        filename = filedialog.askopenfilename()
        #setting title
        root.title("WinTools 0.11.2")
        #setting window size
        width=600
        height=500
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)

        GButton_906=tk.Button(root)
        GButton_906["bg"] = "#f0f0f0"
        GButton_906["cursor"] = "arrow"
        GButton_906["fg"] = "#000000"
        GButton_906["justify"] = "center"
        GButton_906["text"] = "Перезагрузить обновления"
        GButton_906.place(x=10,y=190,width=163,height=30)
        GButton_906["relief"] = "groove"
        GButton_906["command"] = self.GButton_906_command

        GButton_493=tk.Button(root)
        GButton_493["bg"] = "#f0f0f0"
        GButton_493["fg"] = "#000000"
        GButton_493["justify"] = "center"
        GButton_493["text"] = "Установить/удалить патч ISO"
        GButton_493.place(x=190,y=190,width=229,height=30)
        GButton_493["relief"] = "groove"
        GButton_493["command"] = self.GButton_493_command

        GButton_485=tk.Button(root)
        GButton_485["bg"] = "#f0f0f0"
        GButton_485["fg"] = "#000000"
        GButton_485["justify"] = "center"
        GButton_485["text"] = "Открыть UMCT"
        GButton_485.place(x=10,y=240,width=96,height=30)
        GButton_485["relief"] = "groove"
        GButton_485["command"] = self.GButton_485_command

        GButton_527=tk.Button(root)
        GButton_527["bg"] = "#f0f0f0"
        GButton_527["fg"] = "#000000"
        GButton_527["justify"] = "center"
        GButton_527["text"] = "Убрать проверку TPM при обновленнии из системы"
        GButton_527.place(x=120,y=240,width=300,height=30)
        GButton_527["relief"] = "groove"
        GButton_527["command"] = self.GButton_527_command

        GLabel_881=tk.Label(root)
        ft = tkFont.Font(size=88)
        GLabel_881["font"] = ft
        GLabel_881["fg"] = "#001aff"
        GLabel_881["justify"] = "center"
        GLabel_881["text"] = "WinTools"
        GLabel_881.place(x=10,y=10,width=492,height=160)

        GLabel_154=tk.Label(root)
        ft = tkFont.Font(size=13)
        GLabel_154["font"] = ft
        GLabel_154["fg"] = "#47d908"
        GLabel_154["justify"] = "center"
        GLabel_154["text"] = "Alpha"
        GLabel_154.place(x=450,y=30,width=49,height=30)


    def GButton_906_command(self):
        subprocess.call(["bypass11\windows_update_refresh.bat"])

    def GButton_493_command():
        GGButton_493_commandd(filename)

    def GButton_493_commandd(text):
        subprocess.call(["bypass11\Quick_11_iso_esd_wim_TPM_toggle.bat", text])


    def GButton_485_command(self):
        subprocess.call(["MediaCreationTool.bat"])


    def GButton_527_command(self):
        subprocess.call(["bypass11\Skip_TPM_Check_on_Dynamic_Update.cmd"])


if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
