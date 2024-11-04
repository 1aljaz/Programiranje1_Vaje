class IzCSVvHTML():
    def __init__(self, imeVhoda:str, imeIzhoda:str):
        self.imeVhoda = imeVhoda
        self.imeIzhoda = imeIzhoda
    
    def CSVtoHTML(self):
        """
            Metoda pretvori csv v html datoteko.
        """

        with open (self.imeVhoda, "r") as fo:
            with open(self.imeIzhoda, "w") as fw:
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


i = IzCSVvHTML("CSV.csv", "html.html")
i.CSVtoHTML()