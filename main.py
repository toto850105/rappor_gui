# coding=utf-8
from Tkinter import *
import tkFileDialog
import os

class App_gui(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.grid()
        self.master.title("rappor")
        self.master.geometry("960x480")
        # let the windows can't resize
        self.master.resizable(0, 0)
        self.pack()
        self.createWidgets()
        # tkFileDialog options
        self.open_file_opt = open_options = {}
        open_options["title"] = "開啟檔案"
        open_options["filetypes"] = [("csv files", "*.csv"), ("all files", "*.*")]
        open_options["initialdir"] = os.getcwd()

        self.save_file_opt = save_options = {}
        save_options["title"] = "儲存檔案"
        save_options["filetypes"] = [("csv files", "*.csv"), ("all files", "*.*")]
        save_options["initialdir"] = os.getcwd()

    def createWidgets(self):
        self.data = Label(self)
        self.data["text"] = "資料名稱："
        self.data["font"] = 24
        self.data["pady"] = 35
        self.data.grid(row=0, column=0)

        self.parameter = Label(self)
        self.parameter["text"] = "參數名稱："
        self.parameter["font"] = 24
        self.parameter["pady"] = 35
        self.parameter.grid(row=1, column=0)

        self.type = Label(self)
        self.type["text"] = "參數名稱："
        self.type["font"] = 24
        self.type["pady"] = 35
        self.type.grid(row=2, column=0)

        self.data_path = Label(self)
        self.data_path["text"] = "-----"
        self.data_path["font"] = 24
        self.data_path["width"] = 20
        self.data_path.grid(row=0, column=1)

        self.parameter_path = Label(self)
        self.parameter_path["text"] = "-----"
        self.parameter_path["font"] = 24
        self.parameter_path["width"] = 20
        self.parameter_path.grid(row=1, column=1)

        self.type_path = Label(self)
        self.type_path["text"] = "-----"
        self.type_path["font"] = 24
        self.type_path["width"] = 20
        self.type_path.grid(row=2, column=1)

        self.data_setting = Button(self)
        self.data_setting["text"] = "設定"
        self.data_setting["font"] = 24
        self.data_setting["command"] = self.set_data
        self.data_setting.grid(row=0, column=2)

        self.parameter_setting = Button(self)
        self.parameter_setting["text"] = "設定"
        self.parameter_setting["font"] = 24
        self.parameter_setting["command"] = self.set_parameter
        self.parameter_setting.grid(row=1, column=2)

        self.type_setting = Button(self)
        self.type_setting["text"] = "設定"
        self.type_setting["font"] = 24
        self.type_setting["command"] = self.set_type
        self.type_setting.grid(row=2, column=2)

        self.start = Button(self)
        self.start["text"] = "開始"
        self.start["width"] = 5
        self.start["height"] = 3
        self.start["font"] = 26
        self.start["padx"] = 50
        self.start.grid(row=1, column=3, padx = 70)

        self.output = Label(self)
        self.output["text"] = "輸出位置"
        self.output["font"] = 24
        self.output.grid(row=0, column=4)

        self.output_setting = Button(self)
        self.output_setting["text"] = "設定"
        self.output_setting["font"] = 24
        self.output_setting["command"] = self.set_output
        self.output_setting.grid(row=0, column=5)

        self.outpu_path_label = Label(self)
        self.outpu_path_label["text"] = "輸出檔案:"
        self.outpu_path_label["font"] = 24
        self.outpu_path_label.grid(row=1, column=4)

        self.output_path = Label(self)
        self.output_path["text"] = "-----"
        self.output_path["font"] = 24
        self.output_path["width"] = 20
        self.output_path.grid(row=1, column=5)

    def set_data(self):
        file_data = tkFileDialog.askopenfile("r", **self.open_file_opt)
        name = file_data.name.split("/")
        self.data_path["text"] = name[-1]

    def set_parameter(self):
        file_parameter = tkFileDialog.askopenfile("r", **self.open_file_opt)
        name = file_parameter.name.split("/")
        self.parameter_path["text"] = name[-1]

    def set_type(self):
        file_type = tkFileDialog.askopenfile("r", **self.open_file_opt)
        name = file_type.name.split("/")
        self.type_path["text"] = name[-1]

    def set_output(self):
        file_ouput = tkFileDialog.asksaveasfile("w", **self.save_file_opt)
        name = file_ouput.name.split("/")
        self.output_path["text"] = name[-1]

if __name__ == "__main__":
    root = Tk()
    app = App_gui(master=root)
    app.mainloop()