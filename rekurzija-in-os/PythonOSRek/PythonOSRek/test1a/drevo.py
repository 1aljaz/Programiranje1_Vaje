class Drevo:

    def __init__(self, *args, **kwargs):
        if args:
            self.prazno = False
            self.vsebina = args[0]
            self.levo = kwargs.get('levo', Drevo())
            self.desno = kwargs.get('desno', Drevo())
        else:
            self.prazno = True

    def __repr__(self, zamik=''):
        if self.prazno:
          return 'Drevo()'.format(zamik)
        elif self.levo.prazno and self.desno.prazno:
          return 'Drevo({1})'.format(zamik, self.vsebina)
        else:
          return 'Drevo({1},\n{0}      levo = {2},\n{0}      desno = {3})'.\
            format(
              zamik,
              self.vsebina,
              self.levo.__repr__(zamik + '             '),
              self.desno.__repr__(zamik + '              ')
            )

    def __eq__(self, other):
        return ((self.prazno and other.prazno) or
                (not self.prazno and not other.prazno and
                 self.vsebina == other.vsebina and
                 self.levo == other.levo and
                 self.desno == other.desno))

    def seznam(self):
        '''dvojiško drevo pretvori v seznam'''
        d = []
        if not self.prazno:
            koren = self.vsebina
            levoD = self.levo.seznam()
            desnoD  = self.desno.seznam()
            
            if len(levoD) == 0 and len(desnoD)== 0:
                d = [koren]
                
            else:
               d = [koren,levoD,desnoD]
               
        return d
        
    

    def premi_pregled(self):
        if not self.prazno:
            yield self.vsebina
            for x in self.levo.premi_pregled():
                yield x
            for x in self.desno.premi_pregled():
                yield x


    def vmesni_pregled(self):
        if not self.prazno:
            for x in self.levo.vmesni_pregled():
                yield x
            yield self.vsebina
            for x in self.desno.vmesni_pregled():
                yield x

    def obratni_pregled(self):

        if not self.prazno:
            self.levo.obratni_pregled()
            self.desno.obratni_pregled()
            for x in self.levo.obratni_pregled():
                yield x
            for x in self.desno.obratni_pregled():
                yield x

            yield self.vsebina
