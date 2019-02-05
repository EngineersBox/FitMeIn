import tkinter
from tkinter import *
import DBManage

root = Tk()
text = Text(root)
retData = DBManage.db_main.main_init('Hair Co', 'hairdresser', 'kincumber')
text.insert(INSERT, retData.get('name') + '\n')
text.insert(INSERT, retData.get('type') + '\n')
text.insert(INSERT, retData.get('location') + '\n')
text.insert(INSERT, retData.get('services'))
text.insert(INSERT, '\n')
text.insert(INSERT, retData.get('timetable'))
text.config(state=DISABLED)
text.pack()

root.mainloop()
