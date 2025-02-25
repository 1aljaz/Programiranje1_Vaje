def narascajoce_cete(tabela):
    """Vrne tabelo vseh narascajocih cet iz zaporedja."""
    if len(tabela) == 0:
        return []
    temp = [tabela[0]]
    rez = []
    for i in range(1, len(tabela)):
        if tabela[i-1] >= tabela[i]:
            print(temp)
            rez.append(temp)
            temp.clear()
        temp.append(tabela[i])
    
#   rez.append(temp)
    return rez

print(narascajoce_cete([1, 3, 6, 3, 8, 8, 10, 12]))