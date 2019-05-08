import Gui as g
import sys
import random
import tkinter.messagebox as mb


def main():
    g.Latta_Entry.insert("end", "0")
    g.Espresso_Entry.insert("end", "0")
    g.Iced_latte_Entry.insert("end", "0")
    g.Vale_Entry.insert("end", "0")
    g.Cappucino_Entry.insert("end", "0")
    g.African_Entry.insert("end", "0")
    g.American_Entry.insert("end", "0")
    g.Iced_cap_Entry.insert("end", "0")
    g.Iced_Milk_Entry.insert("end", "0")
    g.School_Entry.insert("end", "0")
    g.Sunday_Entry.insert("end", "0")
    g.Jonathan_Entry.insert("end", "0")
    g.west_Entry.insert("end", "0")
    g.Lagos_Entry.insert("end", "0")
    g.kilburn_Entry.insert("end", "0")
    g.Carlton_Entry.insert("end", "0")
    g.queen_Entry.insert("end", "0")
    g.Pyramid_Entry.insert("end", "0")
    g.listbox_Drinks.insert("end", "0")
    g.listbox_Cakes.insert("end", "0")
    g.listbox_Charge.insert("end", "0")
    g.Tax_Listbox.insert("end", "0")
    g.Sub_Listbox.insert("end", "0")
    g.Total_Listbox.insert("end", "0")
    g.Cash_Entry.insert("end", "0")
    g.listbox_Remain.insert("end", "0")

    g.Latta_Entry.config(state="disabled")
    g.Pyramid_Entry.config(state="disabled")
    g.queen_Entry.config(state="disabled")
    g.Carlton_Entry.config(state="disabled")
    g.kilburn_Entry.config(state="disabled")
    g.Lagos_Entry.config(state="disabled")
    g.west_Entry.config(state="disabled")
    g.Jonathan_Entry.config(state="disabled")
    g.Sunday_Entry.config(state="disabled")
    g.School_Entry.config(state="disabled")
    g.Iced_Milk_Entry.config(state="disabled")
    g.Iced_cap_Entry.config(state="disabled")
    g.American_Entry.config(state="disabled")
    g.African_Entry.config(state="disabled")
    g.Cappucino_Entry.config(state="disabled")
    g.Vale_Entry.config(state="disabled")
    g.Iced_latte_Entry.config(state="disabled")
    g.Espresso_Entry.config(state="disabled")

    g.listbox.insert("end", "=================================================")
    g.listbox.insert("end", "                                        CAMBRIDGE RESTAURANT")
    g.listbox.insert("end", "=================================================")

    g.window.mainloop()


def reset():
    m = mb.askyesno("SYSTEM ALERT", "Are You Sure Reset All..! \n")

    if m == 1:
        g.Latta_Entry.delete(0, 5)
        g.Espresso_Entry.delete(0, 5)
        g.Iced_latte_Entry.delete(0, 5)
        g.Vale_Entry.delete(0, 5)
        g.Cappucino_Entry.delete(0, 5)
        g.African_Entry.delete(0, 5)
        g.American_Entry.delete(0, 5)
        g.Iced_cap_Entry.delete(0, 5)
        g.Iced_Milk_Entry.delete(0, 5)
        g.School_Entry.delete(0, 5)
        g.Sunday_Entry.delete(0, 5)
        g.Jonathan_Entry.delete(0, 5)
        g.west_Entry.delete(0, 5)
        g.Lagos_Entry.delete(0, 5)
        g.kilburn_Entry.delete(0, 5)
        g.Carlton_Entry.delete(0, 5)
        g.queen_Entry.delete(0, 5)
        g.Pyramid_Entry.delete(0, 5)
        g.listbox_Drinks.delete(0, 5)
        g.listbox_Cakes.delete(0, 5)
        g.listbox_Charge.delete(0, 5)
        g.Tax_Listbox.delete(0, 5)
        g.Sub_Listbox.delete(0, 5)
        g.Total_Listbox.delete(0, 5)
        g.Cash_Entry.delete(0, 5)
        g.listbox_Remain.delete(0, 5)
        g.Entry_Cal.delete(0, 10)

        g.Latta_Entry.insert("end", "0")
        g.Espresso_Entry.insert("end", "0")
        g.Iced_latte_Entry.insert("end", "0")
        g.Vale_Entry.insert("end", "0")
        g.Cappucino_Entry.insert("end", "0")
        g.African_Entry.insert("end", "0")
        g.American_Entry.insert("end", "0")
        g.Iced_cap_Entry.insert("end", "0")
        g.Iced_Milk_Entry.insert("end", "0")
        g.School_Entry.insert("end", "0")
        g.Sunday_Entry.insert("end", "0")
        g.Jonathan_Entry.insert("end", "0")
        g.west_Entry.insert("end", "0")
        g.Lagos_Entry.insert("end", "0")
        g.kilburn_Entry.insert("end", "0")
        g.Carlton_Entry.insert("end", "0")
        g.queen_Entry.insert("end", "0")
        g.Pyramid_Entry.insert("end", "0")
        g.listbox_Drinks.insert("end", "0")
        g.listbox_Cakes.insert("end", "0")
        g.listbox_Charge.insert("end", "0")
        g.Tax_Listbox.insert("end", "0")
        g.Sub_Listbox.insert("end", "0")
        g.Total_Listbox.insert("end", "0")
        g.Cash_Entry.insert("end", "0")
        g.listbox_Remain.insert("end", "0")

        g.Latta_Entry.config(state="disabled")
        g.Pyramid_Entry.config(state="disabled")
        g.queen_Entry.config(state="disabled")
        g.Carlton_Entry.config(state="disabled")
        g.kilburn_Entry.config(state="disabled")
        g.Lagos_Entry.config(state="disabled")
        g.west_Entry.config(state="disabled")
        g.Jonathan_Entry.config(state="disabled")
        g.Sunday_Entry.config(state="disabled")
        g.School_Entry.config(state="disabled")
        g.Iced_Milk_Entry.config(state="disabled")
        g.Iced_cap_Entry.config(state="disabled")
        g.American_Entry.config(state="disabled")
        g.African_Entry.config(state="disabled")
        g.Cappucino_Entry.config(state="disabled")
        g.Vale_Entry.config(state="disabled")
        g.Iced_latte_Entry.config(state="disabled")
        g.Espresso_Entry.config(state="disabled")

        g.var1.set(value=0)
        g.var2.set(value=0)
        g.var3.set(value=0)
        g.var4.set(value=0)
        g.var5.set(value=0)
        g.var6.set(value=0)
        g.var7.set(value=0)
        g.var8.set(value=0)
        g.var9.set(value=0)
        g.var10.set(value=0)
        g.var11.set(value=0)
        g.var12.set(value=0)
        g.var13.set(value=0)
        g.var14.set(value=0)
        g.var15.set(value=0)
        g.var16.set(value=0)
        g.var17.set(value=0)
        g.var18.set(value=0)

        g.listbox.delete(0, 20)
        g.listbox.insert("end", "=================================================")
        g.listbox.insert("end", "                                        CAMBRIDGE RESTAURANT")
        g.listbox.insert("end", "=================================================")

    else:
        mb.showinfo("SYSTEM ALERT", "Canceled")


def total():
    l = int(g.Latta_Entry.get())
    e = int(g.Espresso_Entry.get())
    il = int(g.Iced_latte_Entry.get())
    v = int(g.Vale_Entry.get())
    c = int(g.Cappucino_Entry.get())
    af = int(g.African_Entry.get())
    am = int(g.American_Entry.get())
    ic = int(g.Iced_cap_Entry.get())
    im = int(g.Iced_Milk_Entry.get())
    sc = int(g.School_Entry.get())
    su = int(g.Sunday_Entry.get())
    j = int(g.Jonathan_Entry.get())
    w = int(g.west_Entry.get())
    lc = int(g.Lagos_Entry.get())
    k = int(g.kilburn_Entry.get())
    ck = int(g.Carlton_Entry.get())
    q = int(g.queen_Entry.get())
    p = int(g.Pyramid_Entry.get())

    Latta, Espresso, Iced_latte, Vale, Cappucino = 2.10, 5, 8, 6, 10
    African, American, Iced_cap, Iced_Milk = 14, 3.12, 4, 9
    School, Sunday, Jonathan, west, Lagos = 7.45, 12, 2, 5.3, 6
    kilburn, Carlton, queen, Pyramid = 11, 10, 1.8, 7

    tax, charge = 2.8, 1.0

    ll = Latta * l
    ee = Espresso * e
    ilil = Iced_latte * il
    vv = Vale * v
    cc = Cappucino * c
    aaf = African * af
    aam = American * am
    icic = Iced_cap * ic
    imim = Iced_Milk * im
    ssc = School * sc
    ssu = Sunday * su
    jj = Jonathan * j
    ww = west * w
    llc = Lagos * lc
    kk = kilburn * k
    cck = Carlton * ck
    qq = queen * q
    pp = Pyramid * p

    drink = ll + ee + ilil + vv + cc + aaf + aam + icic + imim

    cake = ssc + ssu + jj + ww + llc + kk + cck + qq + pp

    if (drink + cake) == 0:
        tax = 0.0
        charge = 0.0

    sub = drink + cake + charge

    full_total = sub + tax

    g.listbox_Drinks.delete(0, 5)
    g.listbox_Cakes.delete(0, 5)
    g.listbox_Charge.delete(0, 5)
    g.Tax_Listbox.delete(0, 5)
    g.Sub_Listbox.delete(0, 5)
    g.Total_Listbox.delete(0, 5)

    g.listbox_Drinks.insert("end", "$ " + str('%.2f' % drink))
    g.listbox_Cakes.insert("end", "$ " + str('%.2f' % cake))
    g.listbox_Charge.insert("end", "$ " + str('%.2f' % charge))
    g.Tax_Listbox.insert("end", "$ " + str('%.2f' % tax))
    g.Sub_Listbox.insert("end", "$ " + str('%.2f' % sub))
    g.Total_Listbox.insert("end", "$ " + str('%.2f' % full_total))

    cash = int(g.Cash_Entry.get())
    remain = 0

    if cash != 0:
        remain = cash - full_total
        g.listbox_Remain.delete(0, 5)
        g.Entry_Cal.delete(0, 5)
        g.listbox_Remain.insert("end", "$ " + str('%.2f' % remain))

    return drink, cake, charge, tax, full_total, ll, ee, ilil, vv, cc, aaf, aam, icic, imim, ssc, ssu, jj, ww, llc, kk, cck, qq, pp, remain


def recipt():
    total_tuple = total()
    x = random.randint(1254, 3256)

    g.listbox.delete(0, 20)
    g.listbox.insert("end", "=================================================")
    g.listbox.insert("end", ("Ref : " + str(x) + "                           CAMBRIDGE RESTAURANT"))
    g.listbox.insert("end", "=================================================")
    g.listbox.insert("end", "                                                 ")
    g.listbox.insert("end", "           Items                             Number of Items                              Total")
    g.listbox.insert("end", "                                                 ")
    if g.var1.get() == 1: g.listbox.insert("end", "     Latta                                                 {}                                            {}".format(g.Latta_Entry.get(), total_tuple[5]))
    if g.var2.get() == 1: g.listbox.insert("end", "     Espresso                                          {}                                            {}".format(g.Espresso_Entry.get(), total_tuple[6]))
    if g.var3.get() == 1: g.listbox.insert("end", "     Iced Latte                                         {}                                            {}".format(g.Iced_latte_Entry.get(), total_tuple[7]))
    if g.var4.get() == 1: g.listbox.insert("end", "     Vale Coffee                                      {}                                            {}".format(g.Vale_Entry.get(), total_tuple[8]))
    if g.var5.get() == 1: g.listbox.insert("end", "     Cappuccino                                      {}                                            {}".format(g.Cappucino_Entry.get(), total_tuple[9]))
    if g.var6.get() == 1: g.listbox.insert("end", "     African Coffee                                 {}                                            {}".format(g.African_Entry.get(), total_tuple[10]))
    if g.var7.get() == 1: g.listbox.insert("end", "     American Coffee                              {}                                            {}".format(g.American_Entry.get(), total_tuple[11]))
    if g.var8.get() == 1: g.listbox.insert("end", "     Iced Cappuccino                              {}                                            {}".format(g.Iced_cap_Entry.get(), total_tuple[12]))
    if g.var9.get() == 1: g.listbox.insert("end", "     Iced Milk                                           {}                                            {}".format(g.Iced_Milk_Entry.get(), total_tuple[13]))
    if g.var10.get() == 1: g.listbox.insert("end", "     School Cake                                      {}                                           {}".format(g.School_Entry.get(), total_tuple[14]))
    if g.var11.get() == 1: g.listbox.insert("end", "     Sunday O Cake                                  {}                                          {}".format(g.Sunday_Entry.get(), total_tuple[15]))
    if g.var12.get() == 1: g.listbox.insert("end", "     Jonathan O Cake                               {}                                          {}".format(g.Jonathan_Entry.get(), total_tuple[16]))
    if g.var13.get() == 1: g.listbox.insert("end", "     West African Cake                             {}                                          {}".format(g.west_Entry.get(), total_tuple[17]))
    if g.var14.get() == 1: g.listbox.insert("end", "     Lagos Chocolate Cake                      {}                                          {}".format(g.Lagos_Entry.get(), total_tuple[18]))
    if g.var15.get() == 1: g.listbox.insert("end", "     Kilburn Chocolate Cake                    {}                                          {}".format(g.kilburn_Entry.get(), total_tuple[19]))
    if g.var16.get() == 1: g.listbox.insert("end", "     Carlton Hill Chocolate Cake             {}                                          {}".format(g.Carlton_Entry.get(), total_tuple[20]))
    if g.var17.get() == 1: g.listbox.insert("end", "     Queen's Park Chocolate Cake          {}                                          {}".format(g.queen_Entry.get(), total_tuple[21]))
    if g.var18.get() == 1: g.listbox.insert("end", "     Pyramid Chocolate Cake                   {}                                          {}".format(g.Pyramid_Entry.get(), total_tuple[22]))

    g.listbox.insert("end", "                                                 ")
    g.listbox.insert("end", "=================================================")
    g.listbox.insert("end", "                                                 ")
    g.listbox.insert("end", ("     Cost of Drinks : " + "                                                                             $ " + str('%.2f' % total_tuple[0])))
    g.listbox.insert("end", ("     Cost of Cakes : " + "                                                                              $ " + str('%.2f' % total_tuple[1])))
    g.listbox.insert("end", ("     Service Charge : " + "                                                                            $ " + str('%.2f' % total_tuple[2])))
    g.listbox.insert("end", ("     Paid Tax : " + "                                                                                        $ " + str('%.2f' % total_tuple[3])))
    g.listbox.insert("end", ("     Total : " + "                                                                                             $ " + str('%.2f' % total_tuple[4])))
    if float(g.Cash_Entry.get()) != 0: g.listbox.insert("end", "     Cash                                                                                                $ {}".format('%.2f' % float(g.Cash_Entry.get())))
    if float(g.Cash_Entry.get()) != 0: g.listbox.insert("end", "     Remain                                                                                            $ {}".format('%.2f' % float(total_tuple[23])))

    g.listbox.insert("end", "                                                 ")
    g.listbox.insert("end", "=================================================")


def exit_window():
    m = mb.askyesno("SYSTEM ALERT", "Are You Sure Exit From System \n")
    if m == 1:
        sys.exit()

    else:
        mb.showinfo("SYSTEM ALERT", "Canceled")


calculator = ""


def set_number7():
    global calculator
    calculator = calculator + "7"
    g.Entry_Cal.insert("end", "7")


def set_number8():
    global calculator
    calculator = calculator + "8"
    g.Entry_Cal.insert("end", "8")


def set_number9():
    global calculator
    calculator = calculator + "9"
    g.Entry_Cal.insert("end", "9")


def set_number6():
    global calculator
    calculator = calculator + "6"
    g.Entry_Cal.insert("end", "6")


def set_number5():
    global calculator
    calculator = calculator + "5"
    g.Entry_Cal.insert("end", "5")


def set_number4():
    global calculator
    calculator = calculator + "4"
    g.Entry_Cal.insert("end", "4")


def set_number3():
    global calculator
    calculator = calculator + "3"
    g.Entry_Cal.insert("end", "3")


def set_number2():
    global calculator
    calculator = calculator + "2"
    g.Entry_Cal.insert("end", "2")


def set_number1():
    global calculator
    calculator = calculator + "1"
    g.Entry_Cal.insert("end", "1")


def set_number0():
    global calculator
    calculator = calculator + "0"
    g.Entry_Cal.insert("end", "0")


def set_number_plus():
    global calculator
    calculator = calculator + " + "
    g.Entry_Cal.insert("end", " + ")


def set_number_minus():
    global calculator
    calculator = calculator + " - "
    g.Entry_Cal.insert("end", " - ")


def set_number_div():
    global calculator
    calculator = calculator + " / "
    g.Entry_Cal.insert("end", " / ")


def set_number_sub():
    global calculator
    calculator = calculator + " * "
    g.Entry_Cal.insert("end", " * ")


def set_number_dot():
    global calculator
    calculator = calculator + "."
    g.Entry_Cal.insert("end", ".")


def equal():
    g.Entry_Cal.delete(0, 50)
    global calculator
    g.Entry_Cal.insert("end", eval(calculator))


def clear():
    global calculator
    calculator = ""
    g.Entry_Cal.delete(0, 50)


def latta():
    if g.var1.get() == 1:
        g.Latta_Entry.config(state="normal")
        g.Latta_Entry.delete(0, 5)
    else:
        g.Latta_Entry.delete(0, 5)
        g.Latta_Entry.insert("end", "0")
        g.Latta_Entry.config(state="disabled")


def Espresso():
    if g.var2.get() == 1:
        g.Espresso_Entry.config(state="normal")
        g.Espresso_Entry.delete(0, 5)
    else:
        g.Espresso_Entry.delete(0, 5)
        g.Espresso_Entry.insert("end", "0")
        g.Espresso_Entry.config(state="disabled")


def Iced_latte():
    if g.var3.get() == 1:
        g.Iced_latte_Entry.config(state="normal")
        g.Iced_latte_Entry.delete(0, 5)
    else:
        g.Iced_latte_Entry.delete(0, 5)
        g.Iced_latte_Entry.insert("end", "0")
        g.Iced_latte_Entry.config(state="disabled")


def Vale():
    if g.var4.get() == 1:
        g.Vale_Entry.config(state="normal")
        g.Vale_Entry.delete(0, 5)
    else:
        g.Vale_Entry.delete(0, 5)
        g.Vale_Entry.insert("end", "0")
        g.Vale_Entry.config(state="disabled")


def Cappucino():
    if g.var5.get() == 1:
        g.Cappucino_Entry.config(state="normal")
        g.Cappucino_Entry.delete(0, 5)
    else:
        g.Cappucino_Entry.delete(0, 5)
        g.Cappucino_Entry.insert("end", "0")
        g.Cappucino_Entry.config(state="disabled")


def African():
    if g.var6.get() == 1:
        g.African_Entry.config(state="normal")
        g.African_Entry.delete(0, 5)
    else:
        g.African_Entry.delete(0, 5)
        g.African_Entry.insert("end", "0")
        g.African_Entry.config(state="disabled")


def American():
    if g.var7.get() == 1:
        g.American_Entry.config(state="normal")
        g.American_Entry.delete(0, 5)
    else:
        g.American_Entry.delete(0, 5)
        g.American_Entry.insert("end", "0")
        g.American_Entry.config(state="disabled")


def Iced_cap():
    if g.var8.get() == 1:
        g.Iced_cap_Entry.config(state="normal")
        g.Iced_cap_Entry.delete(0, 5)
    else:
        g.Iced_cap_Entry.delete(0, 5)
        g.Iced_cap_Entry.insert("end", "0")
        g.Iced_cap_Entry.config(state="disabled")


def Iced_Milk():
    if g.var9.get() == 1:
        g.Iced_Milk_Entry.config(state="normal")
        g.Iced_Milk_Entry.delete(0, 5)
    else:
        g.Iced_Milk_Entry.delete(0, 5)
        g.Iced_Milk_Entry.insert("end", "0")
        g.Iced_Milk_Entry.config(state="disabled")


def School():
    if g.var10.get() == 1:
        g.School_Entry.config(state="normal")
        g.School_Entry.delete(0, 5)
    else:
        g.School_Entry.delete(0, 5)
        g.School_Entry.insert("end", "0")
        g.School_Entry.config(state="disabled")


def Sunday():
    if g.var11.get() == 1:
        g.Sunday_Entry.config(state="normal")
        g.Sunday_Entry.delete(0, 5)
    else:
        g.Sunday_Entry.delete(0, 5)
        g.Sunday_Entry.insert("end", "0")
        g.Sunday_Entry.config(state="disabled")


def Jonathan():
    if g.var12.get() == 1:
        g.Jonathan_Entry.config(state="normal")
        g.Jonathan_Entry.delete(0, 5)
    else:
        g.Jonathan_Entry.delete(0, 5)
        g.Jonathan_Entry.insert("end", "0")
        g.Jonathan_Entry.config(state="disabled")


def west():
    if g.var13.get() == 1:
        g.west_Entry.config(state="normal")
        g.west_Entry.delete(0, 5)
    else:
        g.west_Entry.delete(0, 5)
        g.west_Entry.insert("end", "0")
        g.west_Entry.config(state="disabled")


def Lagos():
    if g.var14.get() == 1:
        g.Lagos_Entry.config(state="normal")
        g.Lagos_Entry.delete(0, 5)
    else:
        g.Lagos_Entry.delete(0, 5)
        g.Lagos_Entry.insert("end", "0")
        g.Lagos_Entry.config(state="disabled")


def kilburn():
    if g.var15.get() == 1:
        g.kilburn_Entry.config(state="normal")
        g.kilburn_Entry.delete(0, 5)
    else:
        g.kilburn_Entry.delete(0, 5)
        g.kilburn_Entry.insert("end", "0")
        g.kilburn_Entry.config(state="disabled")


def Carlton():
    if g.var16.get() == 1:
        g.Carlton_Entry.config(state="normal")
        g.Carlton_Entry.delete(0, 5)
    else:
        g.Carlton_Entry.delete(0, 5)
        g.Carlton_Entry.insert("end", "0")
        g.Carlton_Entry.config(state="disabled")


def queen():
    if g.var17.get() == 1:
        g.queen_Entry.config(state="normal")
        g.queen_Entry.delete(0, 5)
    else:
        g.queen_Entry.delete(0, 5)
        g.queen_Entry.insert("end", "0")
        g.queen_Entry.config(state="disabled")


def Pyramid():
    if g.var18.get() == 1:
        g.Pyramid_Entry.config(state="normal")
        g.Pyramid_Entry.delete(0, 5)
    else:
        g.Pyramid_Entry.delete(0, 5)
        g.Pyramid_Entry.insert("end", "0")
        g.Pyramid_Entry.config(state="disabled")


if __name__ == '__main__':
    main()
