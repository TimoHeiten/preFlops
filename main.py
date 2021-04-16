import tkinter as ui
import img_locator as flop


root = ui.Tk()
btn_frame = ui.Frame(root, width=250, height=250)
btn_frame.grid(row=0, column=0)
img_frame = ui.Frame(root)
img_frame.grid(row=0, column=1)

cnt_label = None

def insert_img(img_path):
    global cnt_label
    if cnt_label:
        cnt_label.destroy()

    photo = ui.PhotoImage(file=img_path)
    panel = ui.Label(img_frame, image=photo)
    panel.image = photo
    panel.pack()
    cnt_label = panel

def _add_btns(row, preFlop):
    cnt_column = 1
    r = row +1
    for img_name, img_path in preFlop:
        tmp_v = img_path
        btn1 = ui.Button(btn_frame, text=img_name, width=25, height=5, command=lambda i=tmp_v: insert_img(i))
        btn1.grid(row=r, column=cnt_column)
        cnt_column+=1
        if cnt_column > 5:
            r+=1
            cnt_column=0
    
    next_row = r+1
    return next_row


next_row = 0
column = 2
for preFlop in flop.all_flops:
    lbl = ui.Label(btn_frame, height=2, relief=ui.RIDGE, text=preFlop.name)
    lbl.grid(row=next_row, column=2)
    next_row = _add_btns(next_row, preFlop)

root.mainloop()