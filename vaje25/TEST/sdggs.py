def TS(zelva, n, stran, barve):
   '''PObravani TS
      Izhodišèe in koinèni položakj sta enaka'''
   if n == 0:
       
   TS(zelva, n - 1, stran/2, barve[1:])
   zelva.fd(stran/2)
   #narišemo polni trikotnmik na sredini
   zelva.lt(60)
   zelva.fillcolor(barve[0])
   zelva.begin_fill()
   for _ in range(3):
       zelva.fd(stran/2)
       zelva.lt(120)
   zelva.end_fill()
   zelva.rt(60)
   TS(zelva, n - 1, stran/2, barve[1:])
   
   TS(zelva, n - 1, stran/2, barve[1:])