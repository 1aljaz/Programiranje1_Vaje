def slovar_izrazov4():
    """Vrne slovar vseh rezultatov 4 op 4 op 4 op 4, pri cimer je op eden izmed teh "+", "-", "*", "/". """
    sl = {}
    znaki = ["+", "-", "*", "/"]

    for op1 in znaki:
        for op2 in znaki:
            for op3 in znaki:
                res = eval(f"4{op1}4{op2}4{op3}4")
                if res not in sl:
                    sl[res] = [f"4{op1}4{op2}4{op3}4"]
                else:
                    sl[res].append(f"4{op1}4{op2}4{op3}4")
    return sl