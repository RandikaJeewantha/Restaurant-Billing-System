import tkinter as tk

window = tk.Tk()
window.geometry("1000x500+0+0")
window.title("Student Management System")

var1, var2, var3, var4 = tk.IntVar(),  tk.IntVar(),  tk.IntVar(),  tk.IntVar()
var5, var6, var7, var8, var9 = tk.IntVar(), tk.IntVar(),  tk.IntVar(),  tk.IntVar(),  tk.IntVar()
var10, var11, var12, var13, var14 = tk.IntVar(), tk.IntVar(),  tk.IntVar(),  tk.IntVar(),  tk.IntVar()
var15, var16, var17, var18 = tk.IntVar(),  tk.IntVar(),  tk.IntVar(),  tk.IntVar()

Frame_Top = tk.Frame()
Frame_Top.place(relx=0, rely=0.003, relheight=1, relwidth=1)
Frame_Top.configure(relief='groove')
Frame_Top.configure(borderwidth="8")
Frame_Top.configure(relief="groove")
Frame_Top.configure(background="#d9d9d8")

Label_Name = tk.Label()
Label_Name.place(relx=0.004, rely=0.01, relheight=0.08, width=1353)
Label_Name.configure(background="#000000")
Label_Name.configure(borderwidth="4")
Label_Name.configure(disabledforeground="#a3a3a3")
Label_Name.configure(font="-family {OCR A Std} -size 25 -weight bold")
Label_Name.configure(foreground="#ffffff")
Label_Name.configure(text='''CAMBRIDGE RESTAURANT''')

Frame_left = tk.Frame(Frame_Top)
Frame_left.place(relx=0, rely=0.08, relheight=0.645, relwidth=0.35)
Frame_left.configure(relief='groove')
Frame_left.configure(borderwidth="8")
Frame_left.configure(relief="groove")
Frame_left.configure(background="#d9d9d9")

Frame_middle = tk.Frame(Frame_Top)
Frame_middle.place(relx=0.347, rely=0.08, relheight=0.645, relwidth=0.354)
Frame_middle.configure(relief='groove')
Frame_middle.configure(borderwidth="8")
Frame_middle.configure(relief="groove")
Frame_middle.configure(background="#d9d9d9")

Frame_bottom = tk.Frame(Frame_Top)
Frame_bottom.place(relx=0, rely=0.72, relheight=0.28, relwidth=0.7)
Frame_bottom.configure(relief='groove')
Frame_bottom.configure(borderwidth="8")
Frame_bottom.configure(relief="groove")
Frame_bottom.configure(background="#9198d8")

Frame_right = tk.Frame(Frame_Top)
Frame_right.place(relx=0.697, rely=0.080, relheight=0.38, relwidth=0.31)
Frame_right.configure(relief='groove')
Frame_right.configure(borderwidth="8")
Frame_right.configure(relief="groove")
Frame_right.configure(background="#d9d9d9")

Frame_bottom_right = tk.Frame(Frame_Top)
Frame_bottom_right.place(relx=0.697, rely=0.43, relheight=0.5, relwidth=0.31)
Frame_bottom_right.configure(relief='groove')
Frame_bottom_right.configure(borderwidth="8")
Frame_bottom_right.configure(relief="groove")
Frame_bottom_right.configure(background="#d9d9d9")

listbox_Drinks = tk.Listbox(Frame_bottom)
listbox_Drinks.place(relx=0.3, rely=0.05, relheight=0.2, relwidth=0.2)
listbox_Drinks.configure(background="#d9d9d8")
listbox_Drinks.configure(disabledforeground="#a3a3a3")
listbox_Drinks.configure(font="-family {Segoe UI} -size 14")
listbox_Drinks.configure(foreground="black")
listbox_Drinks.configure(highlightbackground="#d9d9d9")
listbox_Drinks.configure(highlightcolor="black")
listbox_Drinks.configure(borderwidth="5")
listbox_Drinks.configure(justify="right")

listbox_Cakes = tk.Listbox(Frame_bottom)
listbox_Cakes.place(relx=0.3, rely=0.29, relheight=0.2, relwidth=0.2)
listbox_Cakes.configure(background="#d9d9d8")
listbox_Cakes.configure(disabledforeground="#a3a3a3")
listbox_Cakes.configure(font="-family {Segoe UI} -size 14")
listbox_Cakes.configure(foreground="black")
listbox_Cakes.configure(highlightbackground="#d9d9d9")
listbox_Cakes.configure(highlightcolor="black")
listbox_Cakes.configure(borderwidth="5")
listbox_Cakes.configure(justify="right")

listbox_Charge = tk.Listbox(Frame_bottom)
listbox_Charge.place(relx=0.3, rely=0.54, relheight=0.2, relwidth=0.2)
listbox_Charge.configure(background="#d9d9d8")
listbox_Charge.configure(disabledforeground="#a3a3a3")
listbox_Charge.configure(font="-family {Segoe UI} -size 14")
listbox_Charge.configure(foreground="black")
listbox_Charge.configure(highlightbackground="#d9d9d9")
listbox_Charge.configure(highlightcolor="black")
listbox_Charge.configure(borderwidth="5")
listbox_Charge.configure(justify="right")

Cash_Entry = tk.Entry(Frame_bottom)
Cash_Entry.place(relx=0.3, rely=0.78, relheight=0.2, relwidth=0.2)
Cash_Entry.configure(background="#d9d9d8")
Cash_Entry.configure(disabledforeground="#a3a3a3")
Cash_Entry.configure(font="-family {Segoe UI} -size 14")
Cash_Entry.configure(foreground="black")
Cash_Entry.configure(highlightbackground="#d9d9d9")
Cash_Entry.configure(highlightcolor="black")
Cash_Entry.configure(borderwidth="5")
Cash_Entry.configure(justify="right")

Tax_Listbox = tk.Listbox(Frame_bottom)
Tax_Listbox.place(relx=0.75, rely=0.05, relheight=0.2, relwidth=0.2)
Tax_Listbox.configure(background="#d9d9d8")
Tax_Listbox.configure(disabledforeground="#a3a3a3")
Tax_Listbox.configure(font="-family {Segoe UI} -size 14")
Tax_Listbox.configure(foreground="black")
Tax_Listbox.configure(highlightbackground="#d9d9d9")
Tax_Listbox.configure(highlightcolor="black")
Tax_Listbox.configure(borderwidth="5")
Tax_Listbox.configure(justify="right")

Sub_Listbox = tk.Listbox(Frame_bottom)
Sub_Listbox.place(relx=0.75, rely=0.29, relheight=0.2, relwidth=0.2)
Sub_Listbox.configure(background="#d9d9d8")
Sub_Listbox.configure(disabledforeground="#a3a3a3")
Sub_Listbox.configure(font="-family {Segoe UI} -size 14")
Sub_Listbox.configure(foreground="black")
Sub_Listbox.configure(highlightbackground="#d9d9d9")
Sub_Listbox.configure(highlightcolor="black")
Sub_Listbox.configure(borderwidth="5")
Sub_Listbox.configure(justify="right")

Total_Listbox = tk.Listbox(Frame_bottom)
Total_Listbox.place(relx=0.75, rely=0.54, relheight=0.2, relwidth=0.2)
Total_Listbox.configure(background="#d9d9d8")
Total_Listbox.configure(disabledforeground="#a3a3a3")
Total_Listbox.configure(font="-family {Segoe UI} -size 14")
Total_Listbox.configure(foreground="black")
Total_Listbox.configure(highlightbackground="#d9d9d9")
Total_Listbox.configure(highlightcolor="black")
Total_Listbox.configure(borderwidth="5")
Total_Listbox.configure(justify="right")

listbox_Remain = tk.Listbox(Frame_bottom)
listbox_Remain.place(relx=0.75, rely=0.78, relheight=0.2, relwidth=0.2)
listbox_Remain.configure(background="#d9d9d8")
listbox_Remain.configure(disabledforeground="#a3a3a3")
listbox_Remain.configure(font="-family {Segoe UI} -size 14")
listbox_Remain.configure(foreground="black")
listbox_Remain.configure(highlightbackground="#d9d9d9")
listbox_Remain.configure(highlightcolor="black")
listbox_Remain.configure(borderwidth="5")
listbox_Remain.configure(justify="right")

listbox = tk.Listbox(Frame_bottom_right)
listbox.place(relx=0, rely=0, relheight=1, relwidth=1)
listbox.configure(background="black")
listbox.configure(disabledforeground="#a3a3a3")
listbox.configure(font="-family {Segoe UI} -size 8")
listbox.configure(foreground="white")
listbox.configure(highlightbackground="#d9d9d9")
listbox.configure(highlightcolor="black")
listbox.configure(borderwidth="5")

Entry_Cal = tk.Entry(Frame_right)
Entry_Cal.place(relx=0.02, rely=0.03, height=45, relwidth=0.71, bordermode='ignore')
Entry_Cal.configure(background="#9198d8")
Entry_Cal.configure(disabledforeground="#a3a3a3")
Entry_Cal.configure(font="-family {Segoe UI} -size 14")
Entry_Cal.configure(foreground="#000000")
Entry_Cal.configure(insertbackground="black")
Entry_Cal.configure(width=254)
Entry_Cal.configure(borderwidth="5")
Entry_Cal.configure(justify="right")

Latta_Entry = tk.Entry(Frame_left)
Latta_Entry.place(relx=0.7, rely=0.1, height=35, relwidth=0.2, bordermode='ignore')
Latta_Entry.configure(background="white")
Latta_Entry.configure(disabledforeground="#a3a3a3")
Latta_Entry.configure(font="-family {Segoe UI} -size 14")
Latta_Entry.configure(foreground="#000000")
Latta_Entry.configure(insertbackground="black")
Latta_Entry.configure(borderwidth="5")

Espresso_Entry = tk.Entry(Frame_left)
Espresso_Entry.place(relx=0.7, rely=0.2, height=35, relwidth=0.2, bordermode='ignore')
Espresso_Entry.configure(background="white")
Espresso_Entry.configure(disabledforeground="#a3a3a3")
Espresso_Entry.configure(font="-family {Segoe UI} -size 14")
Espresso_Entry.configure(foreground="#000000")
Espresso_Entry.configure(insertbackground="black")
Espresso_Entry.configure(borderwidth="5")

Iced_latte_Entry = tk.Entry(Frame_left)
Iced_latte_Entry.place(relx=0.7, rely=0.3, height=35, relwidth=0.2, bordermode='ignore')
Iced_latte_Entry.configure(background="white")
Iced_latte_Entry.configure(disabledforeground="#a3a3a3")
Iced_latte_Entry.configure(font="-family {Segoe UI} -size 14")
Iced_latte_Entry.configure(foreground="#000000")
Iced_latte_Entry.configure(insertbackground="black")
Iced_latte_Entry.configure(borderwidth="5")

Vale_Entry = tk.Entry(Frame_left)
Vale_Entry.place(relx=0.7, rely=0.4, height=35, relwidth=0.2, bordermode='ignore')
Vale_Entry.configure(background="white")
Vale_Entry.configure(disabledforeground="#a3a3a3")
Vale_Entry.configure(font="-family {Segoe UI} -size 14")
Vale_Entry.configure(foreground="#000000")
Vale_Entry.configure(insertbackground="black")
Vale_Entry.configure(borderwidth="5")

Cappucino_Entry = tk.Entry(Frame_left)
Cappucino_Entry.place(relx=0.7, rely=0.5, height=35, relwidth=0.2, bordermode='ignore')
Cappucino_Entry.configure(background="white")
Cappucino_Entry.configure(disabledforeground="#a3a3a3")
Cappucino_Entry.configure(font="-family {Segoe UI} -size 14")
Cappucino_Entry.configure(foreground="#000000")
Cappucino_Entry.configure(insertbackground="black")
Cappucino_Entry.configure(borderwidth="5")

African_Entry = tk.Entry(Frame_left)
African_Entry.place(relx=0.7, rely=0.6, height=35, relwidth=0.2, bordermode='ignore')
African_Entry.configure(background="white")
African_Entry.configure(disabledforeground="#a3a3a3")
African_Entry.configure(font="-family {Segoe UI} -size 14")
African_Entry.configure(foreground="#000000")
African_Entry.configure(insertbackground="black")
African_Entry.configure(borderwidth="5")

American_Entry = tk.Entry(Frame_left)
American_Entry.place(relx=0.7, rely=0.7, height=35, relwidth=0.2, bordermode='ignore')
American_Entry.configure(background="white")
American_Entry.configure(disabledforeground="#a3a3a3")
American_Entry.configure(font="-family {Segoe UI} -size 14")
American_Entry.configure(foreground="#000000")
American_Entry.configure(insertbackground="black")
American_Entry.configure(borderwidth="5")

Iced_cap_Entry = tk.Entry(Frame_left)
Iced_cap_Entry.place(relx=0.7, rely=0.8, height=35, relwidth=0.2, bordermode='ignore')
Iced_cap_Entry.configure(background="white")
Iced_cap_Entry.configure(disabledforeground="#a3a3a3")
Iced_cap_Entry.configure(font="-family {Segoe UI} -size 14")
Iced_cap_Entry.configure(foreground="#000000")
Iced_cap_Entry.configure(insertbackground="black")
Iced_cap_Entry.configure(borderwidth="5")

Iced_Milk_Entry = tk.Entry(Frame_left)
Iced_Milk_Entry.place(relx=0.7, rely=0.9, height=35, relwidth=0.2, bordermode='ignore')
Iced_Milk_Entry.configure(background="white")
Iced_Milk_Entry.configure(disabledforeground="#a3a3a3")
Iced_Milk_Entry.configure(font="-family {Segoe UI} -size 14")
Iced_Milk_Entry.configure(foreground="#000000")
Iced_Milk_Entry.configure(insertbackground="black")
Iced_Milk_Entry.configure(borderwidth="5")

School_Entry = tk.Entry(Frame_middle)
School_Entry.place(relx=0.7, rely=0.1, height=35, relwidth=0.2, bordermode='ignore')
School_Entry.configure(background="white")
School_Entry.configure(disabledforeground="#a3a3a3")
School_Entry.configure(font="-family {Segoe UI} -size 14")
School_Entry.configure(foreground="#000000")
School_Entry.configure(insertbackground="black")
School_Entry.configure(borderwidth="5")

Sunday_Entry = tk.Entry(Frame_middle)
Sunday_Entry.place(relx=0.7, rely=0.2, height=35, relwidth=0.2, bordermode='ignore')
Sunday_Entry.configure(background="white")
Sunday_Entry.configure(disabledforeground="#a3a3a3")
Sunday_Entry.configure(font="-family {Segoe UI} -size 14")
Sunday_Entry.configure(foreground="#000000")
Sunday_Entry.configure(insertbackground="black")
Sunday_Entry.configure(borderwidth="5")

Jonathan_Entry = tk.Entry(Frame_middle)
Jonathan_Entry.place(relx=0.7, rely=0.3, height=35, relwidth=0.2, bordermode='ignore')
Jonathan_Entry.configure(background="white")
Jonathan_Entry.configure(disabledforeground="#a3a3a3")
Jonathan_Entry.configure(font="-family {Segoe UI} -size 14")
Jonathan_Entry.configure(foreground="#000000")
Jonathan_Entry.configure(insertbackground="black")
Jonathan_Entry.configure(borderwidth="5")

west_Entry = tk.Entry(Frame_middle)
west_Entry.place(relx=0.7, rely=0.4, height=35, relwidth=0.2, bordermode='ignore')
west_Entry.configure(background="white")
west_Entry.configure(disabledforeground="#a3a3a3")
west_Entry.configure(font="-family {Segoe UI} -size 14")
west_Entry.configure(foreground="#000000")
west_Entry.configure(insertbackground="black")
west_Entry.configure(borderwidth="5")

Lagos_Entry = tk.Entry(Frame_middle)
Lagos_Entry.place(relx=0.7, rely=0.5, height=35, relwidth=0.2, bordermode='ignore')
Lagos_Entry.configure(background="white")
Lagos_Entry.configure(disabledforeground="#a3a3a3")
Lagos_Entry.configure(font="-family {Segoe UI} -size 14")
Lagos_Entry.configure(foreground="#000000")
Lagos_Entry.configure(insertbackground="black")
Lagos_Entry.configure(borderwidth="5")

kilburn_Entry = tk.Entry(Frame_middle)
kilburn_Entry.place(relx=0.7, rely=0.6, height=35, relwidth=0.2, bordermode='ignore')
kilburn_Entry.configure(background="white")
kilburn_Entry.configure(disabledforeground="#a3a3a3")
kilburn_Entry.configure(font="-family {Segoe UI} -size 14")
kilburn_Entry.configure(foreground="#000000")
kilburn_Entry.configure(insertbackground="black")
kilburn_Entry.configure(borderwidth="5")

Carlton_Entry = tk.Entry(Frame_middle)
Carlton_Entry.place(relx=0.7, rely=0.7, height=35, relwidth=0.2, bordermode='ignore')
Carlton_Entry.configure(background="white")
Carlton_Entry.configure(disabledforeground="#a3a3a3")
Carlton_Entry.configure(font="-family {Segoe UI} -size 14")
Carlton_Entry.configure(foreground="#000000")
Carlton_Entry.configure(insertbackground="black")
Carlton_Entry.configure(borderwidth="5")

queen_Entry = tk.Entry(Frame_middle)
queen_Entry.place(relx=0.7, rely=0.8, height=35, relwidth=0.2, bordermode='ignore')
queen_Entry.configure(background="white")
queen_Entry.configure(disabledforeground="#a3a3a3")
queen_Entry.configure(font="-family {Segoe UI} -size 14")
queen_Entry.configure(foreground="#000000")
queen_Entry.configure(insertbackground="black")
queen_Entry.configure(borderwidth="5")

Pyramid_Entry = tk.Entry(Frame_middle)
Pyramid_Entry.place(relx=0.7, rely=0.9, height=35, relwidth=0.2, bordermode='ignore')
Pyramid_Entry.configure(background="white")
Pyramid_Entry.configure(disabledforeground="#a3a3a3")
Pyramid_Entry.configure(font="-family {Segoe UI} -size 14")
Pyramid_Entry.configure(foreground="#000000")
Pyramid_Entry.configure(insertbackground="black")
Pyramid_Entry.configure(borderwidth="5")

Button_TOTAL = tk.Button()
Button_TOTAL.place(relx=0.699, rely=0.92, height=45, width=100)
Button_TOTAL.configure(activebackground="#ececec")
Button_TOTAL.configure(activeforeground="#000000")
Button_TOTAL.configure(background="#b423d8")
Button_TOTAL.configure(borderwidth="5")
Button_TOTAL.configure(disabledforeground="#a3a3a3")
Button_TOTAL.configure(font="-family {Segoe UI} -size 14")
Button_TOTAL.configure(foreground="#000000")
Button_TOTAL.configure(highlightbackground="#d9d9d9")
Button_TOTAL.configure(highlightcolor="black")
Button_TOTAL.configure(pady="0")
Button_TOTAL.configure(text='''TOTAL''')

Button_RECEIPT = tk.Button()
Button_RECEIPT.place(relx=0.773, rely=0.92, height=45, width=100)
Button_RECEIPT.configure(activebackground="#ececec")
Button_RECEIPT.configure(activeforeground="#000000")
Button_RECEIPT.configure(background="#b423d8")
Button_RECEIPT.configure(borderwidth="5")
Button_RECEIPT.configure(disabledforeground="#a3a3a3")
Button_RECEIPT.configure(font="-family {Segoe UI} -size 14")
Button_RECEIPT.configure(foreground="#000000")
Button_RECEIPT.configure(highlightbackground="#d9d9d9")
Button_RECEIPT.configure(highlightcolor="black")
Button_RECEIPT.configure(pady="0")
Button_RECEIPT.configure(text='''RECEIPT''')

Button_RESET = tk.Button()
Button_RESET.place(relx=0.848, rely=0.92, height=45, width=100)
Button_RESET.configure(activebackground="#ececec")
Button_RESET.configure(activeforeground="#000000")
Button_RESET.configure(background="#b423d8")
Button_RESET.configure(borderwidth="5")
Button_RESET.configure(disabledforeground="#a3a3a3")
Button_RESET.configure(font="-family {Segoe UI} -size 14")
Button_RESET.configure(foreground="#000000")
Button_RESET.configure(highlightbackground="#d9d9d9")
Button_RESET.configure(highlightcolor="black")
Button_RESET.configure(pady="0")
Button_RESET.configure(text='''RESET''')

Button_EXIT = tk.Button()
Button_EXIT.place(relx=0.92, rely=0.92, height=45, width=100)
Button_EXIT.configure(activebackground="#ececec")
Button_EXIT.configure(activeforeground="#000000")
Button_EXIT.configure(background="#b423d8")
Button_EXIT.configure(borderwidth="5")
Button_EXIT.configure(disabledforeground="#a3a3a3")
Button_EXIT.configure(font="-family {Segoe UI} -size 14")
Button_EXIT.configure(foreground="#000000")
Button_EXIT.configure(highlightbackground="#d9d9d9")
Button_EXIT.configure(highlightcolor="black")
Button_EXIT.configure(pady="0")
Button_EXIT.configure(text='''EXIT''')

Button_7 = tk.Button()
Button_7.place(relx=0.70, rely=0.17, height=45, width=100)
Button_7.configure(activebackground="#ececec")
Button_7.configure(activeforeground="#000000")
Button_7.configure(background="#b423d8")
Button_7.configure(borderwidth="5")
Button_7.configure(disabledforeground="#a3a3a3")
Button_7.configure(font="-family {Segoe UI} -size 18")
Button_7.configure(foreground="#000000")
Button_7.configure(highlightbackground="#d9d9d9")
Button_7.configure(highlightcolor="black")
Button_7.configure(pady="0")
Button_7.configure(text='''7''')

Button_8 = tk.Button()
Button_8.place(relx=0.774, rely=0.17, height=45, width=100)
Button_8.configure(activebackground="#ececec")
Button_8.configure(activeforeground="#000000")
Button_8.configure(background="#b423d8")
Button_8.configure(borderwidth="5")
Button_8.configure(disabledforeground="#a3a3a3")
Button_8.configure(font="-family {Segoe UI} -size 18")
Button_8.configure(foreground="#000000")
Button_8.configure(highlightbackground="#d9d9d9")
Button_8.configure(highlightcolor="black")
Button_8.configure(pady="0")
Button_8.configure(text='''8''')

Button_9 = tk.Button()
Button_9.place(relx=0.847, rely=0.17, height=45, width=100)
Button_9.configure(activebackground="#ececec")
Button_9.configure(activeforeground="#000000")
Button_9.configure(background="#b423d8")
Button_9.configure(borderwidth="5")
Button_9.configure(disabledforeground="#a3a3a3")
Button_9.configure(font="-family {Segoe UI} -size 18")
Button_9.configure(foreground="#000000")
Button_9.configure(highlightbackground="#d9d9d9")
Button_9.configure(highlightcolor="black")
Button_9.configure(pady="0")
Button_9.configure(text='''9''')

Button_plus = tk.Button()
Button_plus.place(relx=0.92, rely=0.17, height=45, width=100)
Button_plus.configure(activebackground="#ececec")
Button_plus.configure(activeforeground="#000000")
Button_plus.configure(background="#b423d8")
Button_plus.configure(borderwidth="5")
Button_plus.configure(disabledforeground="#a3a3a3")
Button_plus.configure(font="-family {Segoe UI} -size 18")
Button_plus.configure(foreground="#000000")
Button_plus.configure(highlightbackground="#d9d9d9")
Button_plus.configure(highlightcolor="black")
Button_plus.configure(pady="0")
Button_plus.configure(text='''+''')

Button_4 = tk.Button()
Button_4.place(relx=0.70, rely=0.235, height=45, width=100)
Button_4.configure(activebackground="#ececec")
Button_4.configure(activeforeground="#000000")
Button_4.configure(background="#b423d8")
Button_4.configure(borderwidth="5")
Button_4.configure(disabledforeground="#a3a3a3")
Button_4.configure(font="-family {Segoe UI} -size 18")
Button_4.configure(foreground="#000000")
Button_4.configure(highlightbackground="#d9d9d9")
Button_4.configure(highlightcolor="black")
Button_4.configure(pady="0")
Button_4.configure(text='''4''')

Button_5 = tk.Button()
Button_5.place(relx=0.774, rely=0.235, height=45, width=100)
Button_5.configure(activebackground="#ececec")
Button_5.configure(activeforeground="#000000")
Button_5.configure(background="#b423d8")
Button_5.configure(borderwidth="5")
Button_5.configure(disabledforeground="#a3a3a3")
Button_5.configure(font="-family {Segoe UI} -size 18")
Button_5.configure(foreground="#000000")
Button_5.configure(highlightbackground="#d9d9d9")
Button_5.configure(highlightcolor="black")
Button_5.configure(pady="0")
Button_5.configure(text='''5''')

Button_6 = tk.Button()
Button_6.place(relx=0.847, rely=0.235, height=45, width=100)
Button_6.configure(activebackground="#ececec")
Button_6.configure(activeforeground="#000000")
Button_6.configure(background="#b423d8")
Button_6.configure(borderwidth="5")
Button_6.configure(disabledforeground="#a3a3a3")
Button_6.configure(font="-family {Segoe UI} -size 18")
Button_6.configure(foreground="#000000")
Button_6.configure(highlightbackground="#d9d9d9")
Button_6.configure(highlightcolor="black")
Button_6.configure(pady="0")
Button_6.configure(text='''6''')

Button_minus = tk.Button()
Button_minus.place(relx=0.92, rely=0.235, height=45, width=100)
Button_minus.configure(activebackground="#ececec")
Button_minus.configure(activeforeground="#000000")
Button_minus.configure(background="#b423d8")
Button_minus.configure(borderwidth="5")
Button_minus.configure(disabledforeground="#a3a3a3")
Button_minus.configure(font="-family {Segoe UI} -size 18")
Button_minus.configure(foreground="#000000")
Button_minus.configure(highlightbackground="#d9d9d9")
Button_minus.configure(highlightcolor="black")
Button_minus.configure(pady="0")
Button_minus.configure(text='''-''')

Button_1 = tk.Button()
Button_1.place(relx=0.70, rely=0.3, height=45, width=100)
Button_1.configure(activebackground="#ececec")
Button_1.configure(activeforeground="#000000")
Button_1.configure(background="#b423d8")
Button_1.configure(borderwidth="5")
Button_1.configure(disabledforeground="#a3a3a3")
Button_1.configure(font="-family {Segoe UI} -size 18")
Button_1.configure(foreground="#000000")
Button_1.configure(highlightbackground="#d9d9d9")
Button_1.configure(highlightcolor="black")
Button_1.configure(pady="0")
Button_1.configure(text='''1''')

Button_2 = tk.Button()
Button_2.place(relx=0.774, rely=0.3, height=45, width=100)
Button_2.configure(activebackground="#ececec")
Button_2.configure(activeforeground="#000000")
Button_2.configure(background="#b423d8")
Button_2.configure(borderwidth="5")
Button_2.configure(disabledforeground="#a3a3a3")
Button_2.configure(font="-family {Segoe UI} -size 18")
Button_2.configure(foreground="#000000")
Button_2.configure(highlightbackground="#d9d9d9")
Button_2.configure(highlightcolor="black")
Button_2.configure(pady="0")
Button_2.configure(text='''2''')

Button_3 = tk.Button()
Button_3.place(relx=0.847, rely=0.3, height=45, width=100)
Button_3.configure(activebackground="#ececec")
Button_3.configure(activeforeground="#000000")
Button_3.configure(background="#b423d8")
Button_3.configure(borderwidth="5")
Button_3.configure(disabledforeground="#a3a3a3")
Button_3.configure(font="-family {Segoe UI} -size 18")
Button_3.configure(foreground="#000000")
Button_3.configure(highlightbackground="#d9d9d9")
Button_3.configure(highlightcolor="black")
Button_3.configure(pady="0")
Button_3.configure(text='''3''')

Button_multi = tk.Button()
Button_multi.place(relx=0.92, rely=0.3, height=45, width=100)
Button_multi.configure(activebackground="#ececec")
Button_multi.configure(activeforeground="#000000")
Button_multi.configure(background="#b423d8")
Button_multi.configure(borderwidth="5")
Button_multi.configure(disabledforeground="#a3a3a3")
Button_multi.configure(font="-family {Segoe UI} -size 18")
Button_multi.configure(foreground="#000000")
Button_multi.configure(highlightbackground="#d9d9d9")
Button_multi.configure(highlightcolor="black")
Button_multi.configure(pady="0")
Button_multi.configure(text='''x''')

Button_0 = tk.Button()
Button_0.place(relx=0.70, rely=0.368, height=45, width=100)
Button_0.configure(activebackground="#ececec")
Button_0.configure(activeforeground="#000000")
Button_0.configure(background="#b423d8")
Button_0.configure(borderwidth="5")
Button_0.configure(disabledforeground="#a3a3a3")
Button_0.configure(font="-family {Segoe UI} -size 18")
Button_0.configure(foreground="#000000")
Button_0.configure(highlightbackground="#d9d9d9")
Button_0.configure(highlightcolor="black")
Button_0.configure(pady="0")
Button_0.configure(text='''0''')

Button_dot = tk.Button()
Button_dot.place(relx=0.774, rely=0.368, height=45, width=100)
Button_dot.configure(activebackground="#ececec")
Button_dot.configure(activeforeground="#000000")
Button_dot.configure(background="#b423d8")
Button_dot.configure(borderwidth="5")
Button_dot.configure(disabledforeground="#a3a3a3")
Button_dot.configure(font="-family {Segoe UI} -size 18")
Button_dot.configure(foreground="#000000")
Button_dot.configure(highlightbackground="#d9d9d9")
Button_dot.configure(highlightcolor="black")
Button_dot.configure(pady="0")
Button_dot.configure(text='''.''')

Button_equal = tk.Button()
Button_equal.place(relx=0.847, rely=0.368, height=45, width=100)
Button_equal.configure(activebackground="#ececec")
Button_equal.configure(activeforeground="#000000")
Button_equal.configure(background="#b423d8")
Button_equal.configure(borderwidth="5")
Button_equal.configure(disabledforeground="#a3a3a3")
Button_equal.configure(font="-family {Segoe UI} -size 18")
Button_equal.configure(foreground="#000000")
Button_equal.configure(highlightbackground="#d9d9d9")
Button_equal.configure(highlightcolor="black")
Button_equal.configure(pady="0")
Button_equal.configure(text='''=''')

Button_div = tk.Button()
Button_div.place(relx=0.92, rely=0.368, height=45, width=100)
Button_div.configure(activebackground="#ececec")
Button_div.configure(activeforeground="#000000")
Button_div.configure(background="#b423d8")
Button_div.configure(borderwidth="5")
Button_div.configure(disabledforeground="#a3a3a3")
Button_div.configure(font="-family {Segoe UI} -size 18")
Button_div.configure(foreground="#000000")
Button_div.configure(highlightbackground="#d9d9d9")
Button_div.configure(highlightcolor="black")
Button_div.configure(pady="0")
Button_div.configure(text='''/''')

Button_c = tk.Button()
Button_c.place(relx=0.92, rely=0.105, height=45, width=100)
Button_c.configure(activebackground="#ececec")
Button_c.configure(activeforeground="#000000")
Button_c.configure(background="#b423d8")
Button_c.configure(borderwidth="5")
Button_c.configure(disabledforeground="#a3a3a3")
Button_c.configure(font="-family {Segoe UI} -size 18")
Button_c.configure(foreground="#000000")
Button_c.configure(highlightbackground="#d9d9d9")
Button_c.configure(highlightcolor="black")
Button_c.configure(pady="0")
Button_c.configure(text='''C''')

cost_of_drinks = tk.Label(Frame_bottom)
cost_of_drinks.place(relx=0.01, rely=0.1, height=25, width=200, bordermode='ignore')
cost_of_drinks.configure(background="#9198d8")
cost_of_drinks.configure(disabledforeground="#a3a3a3")
cost_of_drinks.configure(font="-family {aril black} -size 15")
cost_of_drinks.configure(foreground="#000000")
cost_of_drinks.configure(text='''Cost of Drinks''')

cost_of_cakes = tk.Label(Frame_bottom)
cost_of_cakes.place(relx=0.01, rely=0.35, height=25, width=200, bordermode='ignore')
cost_of_cakes.configure(background="#9198d8")
cost_of_cakes.configure(disabledforeground="#a3a3a3")
cost_of_cakes.configure(font="-family {aril black} -size 15")
cost_of_cakes.configure(foreground="#000000")
cost_of_cakes.configure(text='''Cost of Cakes''')

Service_Charge = tk.Label(Frame_bottom)
Service_Charge.place(relx=0.01, rely=0.6, height=25, width=200, bordermode='ignore')
Service_Charge.configure(background="#9198d8")
Service_Charge.configure(disabledforeground="#a3a3a3")
Service_Charge.configure(font="-family {aril black} -size 15")
Service_Charge.configure(foreground="#000000")
Service_Charge.configure(text='''  Service Charge''')

Cash = tk.Label(Frame_bottom)
Cash.place(relx=0.01, rely=0.82, height=25, width=200, bordermode='ignore')
Cash.configure(background="#9198d8")
Cash.configure(disabledforeground="#a3a3a3")
Cash.configure(font="-family {aril black} -size 15")
Cash.configure(foreground="#000000")
Cash.configure(text='''Cash             ''')

Paid_Tax = tk.Label(Frame_bottom)
Paid_Tax.place(relx=0.5, rely=0.1, height=25, width=200, bordermode='ignore')
Paid_Tax.configure(background="#9198d8")
Paid_Tax.configure(disabledforeground="#a3a3a3")
Paid_Tax.configure(font="-family {aril black} -size 15")
Paid_Tax.configure(foreground="#000000")
Paid_Tax.configure(text='''Paid Tax''')

Sub_Total = tk.Label(Frame_bottom)
Sub_Total.place(relx=0.5, rely=0.35, height=25, width=200, bordermode='ignore')
Sub_Total.configure(background="#9198d8")
Sub_Total.configure(disabledforeground="#a3a3a3")
Sub_Total.configure(font="-family {aril black} -size 15")
Sub_Total.configure(foreground="#000000")
Sub_Total.configure(text=''' Sub Total''')

Total_Cost = tk.Label(Frame_bottom)
Total_Cost.place(relx=0.5, rely=0.6, height=25, width=200, bordermode='ignore')
Total_Cost.configure(background="#9198d8")
Total_Cost.configure(disabledforeground="#a3a3a3")
Total_Cost.configure(font="-family {aril black} -size 15")
Total_Cost.configure(foreground="#000000")
Total_Cost.configure(text='''  Total Cost''')

Remain = tk.Label(Frame_bottom)
Remain.place(relx=0.5, rely=0.82, height=25, width=200, bordermode='ignore')
Remain.configure(background="#9198d8")
Remain.configure(disabledforeground="#a3a3a3")
Remain.configure(font="-family {aril black} -size 15")
Remain.configure(foreground="#000000")
Remain.configure(text='''Remain  ''')

Label_Drinks = tk.Label(Frame_left)
Label_Drinks.place(relx=0.004, rely=0.0, relheight=0.08, width=130)
Label_Drinks.configure(background="#d9d9d9")
Label_Drinks.configure(borderwidth="4")
Label_Drinks.configure(disabledforeground="#a3a3a3")
Label_Drinks.configure(font="-family {aril black} -size 25 -weight bold")
Label_Drinks.configure(foreground="black")
Label_Drinks.configure(text='''Drinks''')
Label_Drinks.configure(width=1400)

Label_Cakes = tk.Label(Frame_middle)
Label_Cakes.place(relx=0, rely=0.0, relheight=0.08, width=130)
Label_Cakes.configure(background="#d9d9d9")
Label_Cakes.configure(borderwidth="4")
Label_Cakes.configure(disabledforeground="#a3a3a3")
Label_Cakes.configure(font="-family {aril black} -size 25 -weight bold")
Label_Cakes.configure(foreground="black")
Label_Cakes.configure(text='''Cakes''')
Label_Cakes.configure(width=1400)

Checkbutton_Latta = tk.Checkbutton(Frame_left)
Checkbutton_Latta.configure(text="Latta")
Checkbutton_Latta.configure(variable=var1)
Checkbutton_Latta.place(relx=0.1, rely=0.1, height=35, bordermode='ignore')
Checkbutton_Latta.configure(font="-family {Segoe UI} -size 14")
Checkbutton_Latta.configure(background="#d9d9d9")

Espresso_Checkbutton = tk.Checkbutton(Frame_left)
Espresso_Checkbutton.configure(text="Espresso")
Espresso_Checkbutton.configure(variable= var2)
Espresso_Checkbutton.place(relx=0.1, rely=0.2, height=35, bordermode='ignore')
Espresso_Checkbutton.configure(font="-family {Segoe UI} -size 14")
Espresso_Checkbutton.configure(background="#d9d9d9")

Iced_latte_Checkbutton = tk.Checkbutton(Frame_left)
Iced_latte_Checkbutton.configure(text="Iced Latte")
Iced_latte_Checkbutton.configure(variable= var3)
Iced_latte_Checkbutton.place(relx=0.1, rely=0.3, height=35, bordermode='ignore')
Iced_latte_Checkbutton.configure(font="-family {Segoe UI} -size 14")
Iced_latte_Checkbutton.configure(background="#d9d9d9")

Vale_Checkbutton = tk.Checkbutton(Frame_left)
Vale_Checkbutton.configure(text="Vale Coffee")
Vale_Checkbutton.configure(variable= var4)
Vale_Checkbutton.place(relx=0.1, rely=0.4, height=35, bordermode='ignore')
Vale_Checkbutton.configure(font="-family {Segoe UI} -size 14")
Vale_Checkbutton.configure(background="#d9d9d9")

Cappucino_Checkbutton = tk.Checkbutton(Frame_left)
Cappucino_Checkbutton.configure(text="Cappuccino")
Cappucino_Checkbutton.configure(variable= var5)
Cappucino_Checkbutton.place(relx=0.1, rely=0.5, height=35, bordermode='ignore')
Cappucino_Checkbutton.configure(font="-family {Segoe UI} -size 14")
Cappucino_Checkbutton.configure(background="#d9d9d9")

African_Checkbutton = tk.Checkbutton(Frame_left)
African_Checkbutton.configure(text="African Coffee")
African_Checkbutton.configure(variable= var6)
African_Checkbutton.place(relx=0.1, rely=0.6, height=35, bordermode='ignore')
African_Checkbutton.configure(font="-family {Segoe UI} -size 14")
African_Checkbutton.configure(background="#d9d9d9")

American_Checkbutton = tk.Checkbutton(Frame_left)
American_Checkbutton.configure(text="American Coffee")
American_Checkbutton.configure(variable= var7)
American_Checkbutton.place(relx=0.1, rely=0.7, height=35, bordermode='ignore')
American_Checkbutton.configure(font="-family {Segoe UI} -size 14")
American_Checkbutton.configure(background="#d9d9d9")

Iced_cap_Checkbutton = tk.Checkbutton(Frame_left)
Iced_cap_Checkbutton.configure(text="Iced Cappuccino")
Iced_cap_Checkbutton.configure(variable= var8)
Iced_cap_Checkbutton.place(relx=0.1, rely=0.8, height=35, bordermode='ignore')
Iced_cap_Checkbutton.configure(font="-family {Segoe UI} -size 14")
Iced_cap_Checkbutton.configure(background="#d9d9d9")

Iced_Milk_Checkbutton = tk.Checkbutton(Frame_left)
Iced_Milk_Checkbutton.configure(text="Iced Milk")
Iced_Milk_Checkbutton.configure(variable= var9)
Iced_Milk_Checkbutton.place(relx=0.1, rely=0.9, height=35, bordermode='ignore')
Iced_Milk_Checkbutton.configure(font="-family {Segoe UI} -size 14")
Iced_Milk_Checkbutton.configure(background="#d9d9d9")

School_Checkbutton = tk.Checkbutton(Frame_middle)
School_Checkbutton.configure(text="School Cake")
School_Checkbutton.configure(variable= var10)
School_Checkbutton.place(relx=0.1, rely=0.1, height=35, bordermode='ignore')
School_Checkbutton.configure(font="-family {Segoe UI} -size 14")
School_Checkbutton.configure(background="#d9d9d9")

Sunday_Checkbutton = tk.Checkbutton(Frame_middle)
Sunday_Checkbutton.configure(text="Sunday O Cake")
Sunday_Checkbutton.configure(variable= var11)
Sunday_Checkbutton.place(relx=0.1, rely=0.2, height=35, bordermode='ignore')
Sunday_Checkbutton.configure(font="-family {Segoe UI} -size 14")
Sunday_Checkbutton.configure(background="#d9d9d9")

Jonathan_Checkbutton = tk.Checkbutton(Frame_middle)
Jonathan_Checkbutton.configure(text="Jonathan O Cake")
Jonathan_Checkbutton.configure(variable= var12)
Jonathan_Checkbutton.place(relx=0.1, rely=0.3, height=35, bordermode='ignore')
Jonathan_Checkbutton.configure(font="-family {Segoe UI} -size 14")
Jonathan_Checkbutton.configure(background="#d9d9d9")

west_Checkbutton = tk.Checkbutton(Frame_middle)
west_Checkbutton.configure(text="West African Cake")
west_Checkbutton.configure(variable= var13)
west_Checkbutton.place(relx=0.1, rely=0.4, height=35, bordermode='ignore')
west_Checkbutton.configure(font="-family {Segoe UI} -size 14")
west_Checkbutton.configure(background="#d9d9d9")

Lagos_Checkbutton = tk.Checkbutton(Frame_middle)
Lagos_Checkbutton.configure(text="Lagos Chocolate Cake")
Lagos_Checkbutton.configure(variable= var14)
Lagos_Checkbutton.place(relx=0.1, rely=0.5, height=35, bordermode='ignore')
Lagos_Checkbutton.configure(font="-family {Segoe UI} -size 14")
Lagos_Checkbutton.configure(background="#d9d9d9")

kilburn_Checkbutton = tk.Checkbutton(Frame_middle)
kilburn_Checkbutton.configure(text="Kilburn Chocolate Cake")
kilburn_Checkbutton.configure(variable= var15)
kilburn_Checkbutton.place(relx=0.1, rely=0.6, height=35, bordermode='ignore')
kilburn_Checkbutton.configure(font="-family {Segoe UI} -size 14")
kilburn_Checkbutton.configure(background="#d9d9d9")

Carlton_Checkbutton = tk.Checkbutton(Frame_middle)
Carlton_Checkbutton.configure(text="Carlton Hill Chocolate Cake")
Carlton_Checkbutton.configure(variable= var16)
Carlton_Checkbutton.place(relx=0.1, rely=0.7, height=35, bordermode='ignore')
Carlton_Checkbutton.configure(font="-family {Segoe UI} -size 14")
Carlton_Checkbutton.configure(background="#d9d9d9")

queen_Checkbutton = tk.Checkbutton(Frame_middle)
queen_Checkbutton.configure(text="Queen's Park Chocolate Cake")
queen_Checkbutton.configure(variable= var17)
queen_Checkbutton.place(relx=0.1, rely=0.8, height=35, bordermode='ignore')
queen_Checkbutton.configure(font="-family {Segoe UI} -size 14")
queen_Checkbutton.configure(background="#d9d9d9")

Pyramid_Checkbutton = tk.Checkbutton(Frame_middle)
Pyramid_Checkbutton.configure(text="Pyramid Chocolate Cake")
Pyramid_Checkbutton.configure(variable= var18)
Pyramid_Checkbutton.place(relx=0.1, rely=0.9, height=35, bordermode='ignore')
Pyramid_Checkbutton.configure(font="-family {Segoe UI} -size 14")
Pyramid_Checkbutton.configure(background="#d9d9d9")

window.mainloop()
