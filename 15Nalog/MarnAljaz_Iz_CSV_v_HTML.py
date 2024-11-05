def CSVtoHTML(imeVhoda:str, imeIzhoda:str):
    """
        Metoda pretvori csv v html datoteko. Predpostavljam, da datoteka obstaja in ima natanko tri stolpce.
    """

    with open (imeVhoda, "r") as fo:
        with open(imeIzhoda, "w") as fw:
            fw.write("<table>\n")
            for l in fo:
                fw.write("<tr>\n")
                try:
                    en, dva, tri = l.split(',')
                    fw.write(f"<td>{en}</td>\n")
                    fw.write(f"<td>{dva}</td>\n")
                    fw.write(f"<td>{tri}</td>\n")
                except:
                    print("Ni slo, prevec/premal vrstic")
                    continue
                
                fw.write("</tr>\n")
                

            fw.write("</table>\n")


CSVtoHTML("CSV.csv", "html.html")