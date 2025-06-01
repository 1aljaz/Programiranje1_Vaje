# =============================================================================
# Bakterije
# =====================================================================@040864=
# 1. podnaloga
# Definirajte razred `Bakterija`, s katerim bomo predstavili bakterije.
# Sestavite konstruktor, ki kot parameter sprejema niz, ki opisuje genski zapis
# bakterije in ta niz priredi atributu `DNA`. 
# 
# Preveriti pa morate, če je dani genski zapis veljaven, se pravi, da vsebuje
# samo črke `'A'`,`'G'`,`'C'`,`'T'` (okrajšave za Adenin, Gvanin, Citozin in
# Timin). Če niz ni veljaven, naj atribut `_DNA` postane prazen niz. 
# Konstruktor mora narediti tudi atribut `_generacija`, ki naj dobi začetno
# vrednost `0`. Dostopanje do privatnih atributov `_DNA` in `_generacija`
# implementirajte z `get` metodama `get_DNA` in `get_generacija`,
# spreminjanje teh atributov pa implementirajte z `set` metodama `set_DNA`
# in `set_generacija`.
# 
# Primer:
# 
#     >>> a = Bakterija('GAAATCGGT')
#     >>> a.get_DNA()
#     'GAAATCGGT'
#     >>> a.get_generacija()
#     0
#     >>> a.set_DNA('GAAT')
#     >>> a.get_DNA()
#     >>> 'GAAT'
# 
# Primer z neveljavnim genskim zapisom:
# 
#     >>> a = Bakterija('ABCDEFGH')
#     >>> a.get_DNA()()
#     ''
# =============================================================================
class Bakterija:
    def __init__(self, DNA):
        self._DNA = DNA
        self._generacija = 0
        for c in DNA:
            if c not in "AGCT":
                self._DNA = ""
                break
    
    def set_DNA(self, DNA):
        self._DNA = DNA
        for c in DNA:
            if c not in "AGCT":
                self._DNA = ""
                break
    
    def set_generacija(self, gen):
        self._generacija = gen

    def get_DNA(self):
        return self._DNA
    
    def get_generacija(self):
        return self._generacija
    
        
# =====================================================================@040865=
# 2. podnaloga
# Bakterije se zelo rade delijo. Običajne bakterije se delijo tako, da iz ene
# nastaneta dve novi, naše bakterije pa so posplošene bakterije, ki se lahko
# delijo na poljubno število novih bakterij. Pri tem se njihov genski zapis
# prekopira, poveča pa se števec generacije. 
# 
# Definirajte metodo `deli`. Metoda (poleg objekta) sprejema le en parameter (delitelj), ki pove,
# koliko bakterij dobimo po delitvi. Metoda mora vrniti tabelo novih bakterij,
# ki imajo isti `DNA` kot dana bakterija, imajo pa povečan števec generacije.
# Pri tem morate upoštevati še, da se bakterije s praznim genskim zapisom ne
# morejo deliti. V takšnem primeru naj metoda vrne prazno tabelo.
# 
# Primer:
# 
#     >>> a = Bakterija('GAAATCGGT')
#     >>> nove_bakterije = a.deli(3)
#     >>> len(nove_bakterije)
#     3
#     >>> print(nove_bakterije)
#     [<__main__.Bakterija object at 0x7ffd41edac50>, <__main__.Bakterija object at 0x7ffd41edab90>, <__main__.Bakterija object at 0x7ffd41edab50>]
#     >>> nove_bakterije[0].get_generacija()
#     1
#     >>> nove_bakterije[0].get_DNA()
#     'GAAATCGGT'
# =============================================================================
    def deli(self, d):
        if self.get_DNA() == "":
            return []
        
        bak = [Bakterija(self.get_DNA()) for _ in range(d)]
        for b in bak:
            b.set_generacija(self.get_generacija() + 1)
        
        return bak
# =====================================================================@040866=
# 3. podnaloga
# Bakterije se lahko tudi združujejo. Pri tem nastane nova bakterija,
# katere genski zapis je kombinacija genskih zapisov obeh bakterij, ki nastopata
# v združevanju. Zapis se združuje po takšnem pravilu: izmenično se jemlje po
# eno črko iz obeh genskih zapisov, ko pa pridemo do konca krajšega genskega
# zapisa, se preostanek daljšega doda na konec novega zapisa.
# Tako bi na primer pri združevanju zapisov `ACT` in `GCTATGCCC` dobili
# `AGCCTTATGCCC`.
# 
# Definirajte metodo `zdruzi(a, b)`. Metoda naj vrne novo bakterijo, ki ima združen genski zapis
# ter za ena večji števec generacije kot starejša od obeh bakterij, ki nastopata
# v združevanju.
# 
# Kot vidite, to ni objektna metoda!
# 
# Primer:
# 
#     >>> a = Bakterija('ACT')
#     >>> b = Bakterija('GCTATGCCC')
#     >>> c = zdruzi(a, b)
#     >>> c.get_DNA()
#     'AGCCTTATGCCC'
#     >>> c.get_generacija()
#     1
# =============================================================================
def zdruzi(a:Bakterija, b:Bakterija):
    if len(a.get_DNA()) < len(b.get_DNA()):
        a, b = b, a

    dna = "".join(a.get_DNA()[i] + b.get_DNA()[i] for i in range(len(b.get_DNA())))
    dna += a.get_DNA()[len(b.get_DNA()):]

    b = Bakterija(dna)
    b.set_generacija(max(a.get_generacija(), b.get_generacija()) + 1)

    return b

# =====================================================================@040867=
# 4. podnaloga
# Bakterije lahko tudi mutirajo, pri čemer se jim spremeni genski zapis.
# Na primer, podzaporedje `AAG` se pri mutaciji spremeni v podzaporedje `AAT`.
# Pri mutaciji se vedno spremenijo vse pojavitve danega podzaporedja, če pa
# genski zapis bakterije takšnega podzaporedja ne vsebuje, se med mutacijo
# DNA seveda ne spremeni.
# 
# Napišite metodo `mutacija`, ki sprejme dva parametra, ki povesta,
# v kaj se pri mutaciji spremeni dano podzaporedje genskega zapisa.
# Metoda naj vrne *novo* bakterijo, ki ima mutiran genski zapis in za ena večji
# števec generacije.
# Upoštevajte, da se mutacije genskega zapisa vedno odvijajo v smeri od leve
# proti desni (običajna smer v katero naraščajo indeksi).
# 
# Upoštevajte tudi, da bakterije brez genskega zapisa ne morejo mutirati. V
# takšnem primeru naj metoda vrne isto, nespremenjeno bakterijo (nasvet:
# `self`).
# 
# Nasvet: pomagajte si z metodo `replace`!
# 
# Primer:
# 
#     >>> a = Bakterija('GAAATCGGT')
#     >>> m = a.mutacija('AAT', 'CAT')
#     >>> m.get_DNA()
#     'GACATCGGT'
#     >>> m.get_generacija()
#     1
# =============================================================================
class Bakterija(Bakterija):
    def mutacija(self, iz, v):
        if len(self.get_DNA()) == 0:
            return self
        
        b = Bakterija(self.get_DNA().replace(iz, v))  
        b.set_generacija(self.get_generacija() + 1)

        return b 






































































































# ============================================================================@
# fmt: off
"Če vam Python sporoča, da je v tej vrstici sintaktična napaka,"
"se napaka v resnici skriva v zadnjih vrsticah vaše kode."

"Kode od tu naprej NE SPREMINJAJTE!"

# isort: off
import json
import os
import re
import shutil
import sys
import traceback
import urllib.error
import urllib.request
import io
from contextlib import contextmanager


class VisibleStringIO(io.StringIO):
    def read(self, size=None):
        x = io.StringIO.read(self, size)
        print(x, end="")
        return x

    def readline(self, size=None):
        line = io.StringIO.readline(self, size)
        print(line, end="")
        return line


class TimeoutError(Exception):
    pass


class Check:
    parts = None
    current_part = None
    part_counter = None

    @staticmethod
    def has_solution(part):
        return part["solution"].strip() != ""

    @staticmethod
    def initialize(parts):
        Check.parts = parts
        for part in Check.parts:
            part["valid"] = True
            part["feedback"] = []
            part["secret"] = []

    @staticmethod
    def part():
        if Check.part_counter is None:
            Check.part_counter = 0
        else:
            Check.part_counter += 1
        Check.current_part = Check.parts[Check.part_counter]
        return Check.has_solution(Check.current_part)

    @staticmethod
    def feedback(message, *args, **kwargs):
        Check.current_part["feedback"].append(message.format(*args, **kwargs))

    @staticmethod
    def error(message, *args, **kwargs):
        Check.current_part["valid"] = False
        Check.feedback(message, *args, **kwargs)

    @staticmethod
    def clean(x, digits=6, typed=False):
        t = type(x)
        if t is float:
            x = round(x, digits)
            # Since -0.0 differs from 0.0 even after rounding,
            # we change it to 0.0 abusing the fact it behaves as False.
            v = x if x else 0.0
        elif t is complex:
            v = complex(
                Check.clean(x.real, digits, typed), Check.clean(x.imag, digits, typed)
            )
        elif t is list:
            v = list([Check.clean(y, digits, typed) for y in x])
        elif t is tuple:
            v = tuple([Check.clean(y, digits, typed) for y in x])
        elif t is dict:
            v = sorted(
                [
                    (Check.clean(k, digits, typed), Check.clean(v, digits, typed))
                    for (k, v) in x.items()
                ]
            )
        elif t is set:
            v = sorted([Check.clean(y, digits, typed) for y in x])
        else:
            v = x
        return (t, v) if typed else v

    @staticmethod
    def secret(x, hint=None, clean=None):
        clean = Check.get("clean", clean)
        Check.current_part["secret"].append((str(clean(x)), hint))

    @staticmethod
    def equal(expression, expected_result, clean=None, env=None, update_env=None):
        global_env = Check.init_environment(env=env, update_env=update_env)
        clean = Check.get("clean", clean)
        actual_result = eval(expression, global_env)
        if clean(actual_result) != clean(expected_result):
            Check.error(
                "Izraz {0} vrne {1!r} namesto {2!r}.",
                expression,
                actual_result,
                expected_result,
            )
            return False
        else:
            return True

    @staticmethod
    def approx(expression, expected_result, tol=1e-6, env=None, update_env=None):
        try:
            import numpy as np
        except ImportError:
            Check.error("Namestiti morate numpy.")
            return False
        if not isinstance(expected_result, np.ndarray):
            Check.error("Ta funkcija je namenjena testiranju za tip np.ndarray.")

        if env is None:
            env = dict()
        env.update({"np": np})
        global_env = Check.init_environment(env=env, update_env=update_env)
        actual_result = eval(expression, global_env)
        if type(actual_result) is not type(expected_result):
            Check.error(
                "Rezultat ima napačen tip. Pričakovan tip: {}, dobljen tip: {}.",
                type(expected_result).__name__,
                type(actual_result).__name__,
            )
            return False
        exp_shape = expected_result.shape
        act_shape = actual_result.shape
        if exp_shape != act_shape:
            Check.error(
                "Obliki se ne ujemata. Pričakovana oblika: {}, dobljena oblika: {}.",
                exp_shape,
                act_shape,
            )
            return False
        try:
            np.testing.assert_allclose(
                expected_result, actual_result, atol=tol, rtol=tol
            )
            return True
        except AssertionError as e:
            Check.error("Rezultat ni pravilen." + str(e))
            return False

    @staticmethod
    def run(statements, expected_state, clean=None, env=None, update_env=None):
        code = "\n".join(statements)
        statements = "  >>> " + "\n  >>> ".join(statements)
        global_env = Check.init_environment(env=env, update_env=update_env)
        clean = Check.get("clean", clean)
        exec(code, global_env)
        errors = []
        for x, v in expected_state.items():
            if x not in global_env:
                errors.append(
                    "morajo nastaviti spremenljivko {0}, vendar je ne".format(x)
                )
            elif clean(global_env[x]) != clean(v):
                errors.append(
                    "nastavijo {0} na {1!r} namesto na {2!r}".format(
                        x, global_env[x], v
                    )
                )
        if errors:
            Check.error("Ukazi\n{0}\n{1}.", statements, ";\n".join(errors))
            return False
        else:
            return True

    @staticmethod
    @contextmanager
    def in_file(filename, content, encoding=None):
        encoding = Check.get("encoding", encoding)
        with open(filename, "w", encoding=encoding) as f:
            for line in content:
                print(line, file=f)
        old_feedback = Check.current_part["feedback"][:]
        yield
        new_feedback = Check.current_part["feedback"][len(old_feedback) :]
        Check.current_part["feedback"] = old_feedback
        if new_feedback:
            new_feedback = ["\n    ".join(error.split("\n")) for error in new_feedback]
            Check.error(
                "Pri vhodni datoteki {0} z vsebino\n  {1}\nso se pojavile naslednje napake:\n- {2}",
                filename,
                "\n  ".join(content),
                "\n- ".join(new_feedback),
            )

    @staticmethod
    @contextmanager
    def input(content, visible=None):
        old_stdin = sys.stdin
        old_feedback = Check.current_part["feedback"][:]
        try:
            with Check.set_stringio(visible):
                sys.stdin = Check.get("stringio")("\n".join(content) + "\n")
                yield
        finally:
            sys.stdin = old_stdin
        new_feedback = Check.current_part["feedback"][len(old_feedback) :]
        Check.current_part["feedback"] = old_feedback
        if new_feedback:
            new_feedback = ["\n  ".join(error.split("\n")) for error in new_feedback]
            Check.error(
                "Pri vhodu\n  {0}\nso se pojavile naslednje napake:\n- {1}",
                "\n  ".join(content),
                "\n- ".join(new_feedback),
            )

    @staticmethod
    def out_file(filename, content, encoding=None):
        encoding = Check.get("encoding", encoding)
        with open(filename, encoding=encoding) as f:
            out_lines = f.readlines()
        equal, diff, line_width = Check.difflines(out_lines, content)
        if equal:
            return True
        else:
            Check.error(
                "Izhodna datoteka {0}\n  je enaka{1}  namesto:\n  {2}",
                filename,
                (line_width - 7) * " ",
                "\n  ".join(diff),
            )
            return False

    @staticmethod
    def output(expression, content, env=None, update_env=None):
        global_env = Check.init_environment(env=env, update_env=update_env)
        old_stdout = sys.stdout
        sys.stdout = io.StringIO()
        too_many_read_requests = False
        try:
            exec(expression, global_env)
        except EOFError:
            too_many_read_requests = True
        finally:
            output = sys.stdout.getvalue().rstrip().splitlines()
            sys.stdout = old_stdout
        equal, diff, line_width = Check.difflines(output, content)
        if equal and not too_many_read_requests:
            return True
        else:
            if too_many_read_requests:
                Check.error("Program prevečkrat zahteva uporabnikov vnos.")
            if not equal:
                Check.error(
                    "Program izpiše{0}  namesto:\n  {1}",
                    (line_width - 13) * " ",
                    "\n  ".join(diff),
                )
            return False

    @staticmethod
    def difflines(actual_lines, expected_lines):
        actual_len, expected_len = len(actual_lines), len(expected_lines)
        if actual_len < expected_len:
            actual_lines += (expected_len - actual_len) * ["\n"]
        else:
            expected_lines += (actual_len - expected_len) * ["\n"]
        equal = True
        line_width = max(
            len(actual_line.rstrip())
            for actual_line in actual_lines + ["Program izpiše"]
        )
        diff = []
        for out, given in zip(actual_lines, expected_lines):
            out, given = out.rstrip(), given.rstrip()
            if out != given:
                equal = False
            diff.append(
                "{0} {1} {2}".format(
                    out.ljust(line_width), "|" if out == given else "*", given
                )
            )
        return equal, diff, line_width

    @staticmethod
    def init_environment(env=None, update_env=None):
        global_env = globals()
        if not Check.get("update_env", update_env):
            global_env = dict(global_env)
        global_env.update(Check.get("env", env))
        return global_env

    @staticmethod
    def generator(
        expression,
        expected_values,
        should_stop=None,
        further_iter=None,
        clean=None,
        env=None,
        update_env=None,
    ):
        from types import GeneratorType

        global_env = Check.init_environment(env=env, update_env=update_env)
        clean = Check.get("clean", clean)
        gen = eval(expression, global_env)
        if not isinstance(gen, GeneratorType):
            Check.error("Izraz {0} ni generator.", expression)
            return False

        try:
            for iteration, expected_value in enumerate(expected_values):
                actual_value = next(gen)
                if clean(actual_value) != clean(expected_value):
                    Check.error(
                        "Vrednost #{0}, ki jo vrne generator {1} je {2!r} namesto {3!r}.",
                        iteration,
                        expression,
                        actual_value,
                        expected_value,
                    )
                    return False
            for _ in range(Check.get("further_iter", further_iter)):
                next(gen)  # we will not validate it
        except StopIteration:
            Check.error("Generator {0} se prehitro izteče.", expression)
            return False

        if Check.get("should_stop", should_stop):
            try:
                next(gen)
                Check.error("Generator {0} se ne izteče (dovolj zgodaj).", expression)
            except StopIteration:
                pass  # this is fine
        return True

    @staticmethod
    def summarize():
        for i, part in enumerate(Check.parts):
            if not Check.has_solution(part):
                print("{0}. podnaloga je brez rešitve.".format(i + 1))
            elif not part["valid"]:
                print("{0}. podnaloga nima veljavne rešitve.".format(i + 1))
            else:
                print("{0}. podnaloga ima veljavno rešitev.".format(i + 1))
            for message in part["feedback"]:
                print("  - {0}".format("\n    ".join(message.splitlines())))

    settings_stack = [
        {
            "clean": clean.__func__,
            "encoding": None,
            "env": {},
            "further_iter": 0,
            "should_stop": False,
            "stringio": VisibleStringIO,
            "update_env": False,
        }
    ]

    @staticmethod
    def get(key, value=None):
        if value is None:
            return Check.settings_stack[-1][key]
        return value

    @staticmethod
    @contextmanager
    def set(**kwargs):
        settings = dict(Check.settings_stack[-1])
        settings.update(kwargs)
        Check.settings_stack.append(settings)
        try:
            yield
        finally:
            Check.settings_stack.pop()

    @staticmethod
    @contextmanager
    def set_clean(clean=None, **kwargs):
        clean = clean or Check.clean
        with Check.set(clean=(lambda x: clean(x, **kwargs)) if kwargs else clean):
            yield

    @staticmethod
    @contextmanager
    def set_environment(**kwargs):
        env = dict(Check.get("env"))
        env.update(kwargs)
        with Check.set(env=env):
            yield

    @staticmethod
    @contextmanager
    def set_stringio(stringio):
        if stringio is True:
            stringio = VisibleStringIO
        elif stringio is False:
            stringio = io.StringIO
        if stringio is None or stringio is Check.get("stringio"):
            yield
        else:
            with Check.set(stringio=stringio):
                yield

    @staticmethod
    @contextmanager
    def time_limit(timeout_seconds=1):
        from signal import SIGINT, raise_signal
        from threading import Timer

        def interrupt_main():
            raise_signal(SIGINT)

        timer = Timer(timeout_seconds, interrupt_main)
        timer.start()
        try:
            yield
        except KeyboardInterrupt:
            raise TimeoutError
        finally:
            timer.cancel()


def _validate_current_file():
    def extract_parts(filename):
        with open(filename, encoding="utf-8") as f:
            source = f.read()
        part_regex = re.compile(
            r"# =+@(?P<part>\d+)=\s*\n"  # beginning of header
            r"(\s*#( [^\n]*)?\n)+?"  # description
            r"\s*# =+\s*?\n"  # end of header
            r"(?P<solution>.*?)"  # solution
            r"(?=\n\s*# =+@)",  # beginning of next part
            flags=re.DOTALL | re.MULTILINE,
        )
        parts = [
            {"part": int(match.group("part")), "solution": match.group("solution")}
            for match in part_regex.finditer(source)
        ]
        # The last solution extends all the way to the validation code,
        # so we strip any trailing whitespace from it.
        parts[-1]["solution"] = parts[-1]["solution"].rstrip()
        return parts

    def backup(filename):
        backup_filename = None
        suffix = 1
        while not backup_filename or os.path.exists(backup_filename):
            backup_filename = "{0}.{1}".format(filename, suffix)
            suffix += 1
        shutil.copy(filename, backup_filename)
        return backup_filename

    def submit_parts(parts, url, token):
        submitted_parts = []
        for part in parts:
            if Check.has_solution(part):
                submitted_part = {
                    "part": part["part"],
                    "solution": part["solution"],
                    "valid": part["valid"],
                    "secret": [x for (x, _) in part["secret"]],
                    "feedback": json.dumps(part["feedback"]),
                }
                if "token" in part:
                    submitted_part["token"] = part["token"]
                submitted_parts.append(submitted_part)
        data = json.dumps(submitted_parts).encode("utf-8")
        headers = {"Authorization": token, "content-type": "application/json"}
        request = urllib.request.Request(url, data=data, headers=headers)
        # This is a workaround because some clients (and not macOS ones!) report
        # <urlopen error [SSL: CERTIFICATE_VERIFY_FAILED] certificate verify failed: certificate has expired (_ssl.c:1129)>
        import ssl

        context = ssl._create_unverified_context()
        response = urllib.request.urlopen(request, context=context)
        # When the issue is resolved, the following should be used
        # response = urllib.request.urlopen(request)
        return json.loads(response.read().decode("utf-8"))

    def update_attempts(old_parts, response):
        updates = {}
        for part in response["attempts"]:
            part["feedback"] = json.loads(part["feedback"])
            updates[part["part"]] = part
        for part in old_parts:
            valid_before = part["valid"]
            part.update(updates.get(part["part"], {}))
            valid_after = part["valid"]
            if valid_before and not valid_after:
                wrong_index = response["wrong_indices"].get(str(part["part"]))
                if wrong_index is not None:
                    hint = part["secret"][wrong_index][1]
                    if hint:
                        part["feedback"].append("Namig: {}".format(hint))

    filename = os.path.abspath(sys.argv[0])
    file_parts = extract_parts(filename)
    Check.initialize(file_parts)

    if Check.part():
        Check.current_part[
            "token"
        ] = "eyJwYXJ0Ijo0MDg2NCwidXNlciI6OTc4NH0:1uJnlQ:g1wWpkj3mu_1e2u-CRAoHPqSQW7Vk8Mhp8tc3lSznH4"
        try:
            tests = [
                    ('''Bakterija('GAAATCGGT').get_DNA()''', 'GAAATCGGT'),
                    ('''Bakterija('GAAATCGGT').get_generacija()''', 0),
                    ('''Bakterija('AGCBT').get_DNA()''', ''),
                    ('''Bakterija('AGCBT').get_generacija()''', 0),
                    ('''Bakterija('AAAAAAAAAAAAAAA').get_DNA()''', 'AAAAAAAAAAAAAAA'),
                    ('''Bakterija('AAAAAAAAAAAAAAA.blabla').get_DNA()''', '')
                    ]
            
            for test in tests:
                if not Check.equal(*test):
                    break
            
            Check.run([
                'a = Bakterija("GAAATCGGT")',
                'a.set_DNA("GAAT")',
                'b = a.get_DNA()',
                'a.set_generacija(1)',
                'c = a.get_generacija()'
                ], {'b': 'GAAT', 'c': 1})
        except TimeoutError:
            Check.error("Dovoljen čas izvajanja presežen")
        except Exception:
            Check.error(
                "Testi sprožijo izjemo\n  {0}",
                "\n  ".join(traceback.format_exc().split("\n"))[:-2],
            )

    if Check.part():
        Check.current_part[
            "token"
        ] = "eyJwYXJ0Ijo0MDg2NSwidXNlciI6OTc4NH0:1uJnlQ:Lu7ZgZl5mLI64Ht7exsQjsRU0Rh2kuAUE3N4fT4kgyc"
        try:
            tests = [
                    ("""[x.get_DNA() for x in Bakterija('GAAATCGGT').deli(3)]""", ['GAAATCGGT', 'GAAATCGGT', 'GAAATCGGT']),
                    ("""[x.get_DNA() for x in Bakterija('GTTCGGT').deli(1)]""", ['GTTCGGT']),
                    ("""[x.get_generacija() for x in Bakterija('GTTCGGT').deli(1)]""", [1]),
                    ("""[x.get_DNA() for x in Bakterija('ABC').deli(3)]""", []),
                    ("""[x.get_generacija() for x in Bakterija('AAAAAAAAAAAAAAA').deli(6)]""", [1, 1, 1, 1, 1, 1]),
                    ("""((Bakterija('CAAGTCGTAACT').deli(4))[3].deli(2))[1].get_generacija()""", 2),
                    ("""[x.get_generacija() for x in (((((Bakterija('CAAGTCGTAACT').deli(4))[3].deli(2)))[0]).deli(10))]""",
                        [3, 3, 3, 3, 3, 3, 3, 3, 3, 3]),
                    ("""[x.get_DNA() for x in Bakterija('AAAAAAAAAAAAAAA').deli(6)]""",
                        ['AAAAAAAAAAAAAAA', 'AAAAAAAAAAAAAAA', 'AAAAAAAAAAAAAAA', 'AAAAAAAAAAAAAAA', 'AAAAAAAAAAAAAAA',
                         'AAAAAAAAAAAAAAA'])
                    ]
            
            for test in tests:
                if not Check.equal(*test):
                    break
        except TimeoutError:
            Check.error("Dovoljen čas izvajanja presežen")
        except Exception:
            Check.error(
                "Testi sprožijo izjemo\n  {0}",
                "\n  ".join(traceback.format_exc().split("\n"))[:-2],
            )

    if Check.part():
        Check.current_part[
            "token"
        ] = "eyJwYXJ0Ijo0MDg2NiwidXNlciI6OTc4NH0:1uJnlQ:khHKma7ZwnLDlY9aVoFs_bC1-A0RiwM3BLqjP8zFAIQ"
        try:
            tests = [
                    ("""(zdruzi(Bakterija('CGT'), Bakterija('AAG'))).get_DNA()""", 'CAGATG'),
                    ("""(zdruzi(Bakterija('CGT'), Bakterija('AAG'))).get_generacija()""", 1),
                    ("""(zdruzi(zdruzi(Bakterija('CGT'), Bakterija('AAG')), Bakterija('AAG'))).get_DNA()""", 'CAAAGGATG'),
                    ("""(zdruzi(zdruzi(Bakterija('CGT'), Bakterija('AAG')), Bakterija('AAG'))).get_generacija()""", 2),
                    ("""(zdruzi(zdruzi(zdruzi(Bakterija(''), Bakterija('')), Bakterija('')), Bakterija(''))).get_DNA()""", ''),
                    ("""(zdruzi(zdruzi(zdruzi(Bakterija(''), Bakterija('')), Bakterija('')), Bakterija(''))).get_generacija()""", 3)
                    ]
            
            for test in tests:
                if not Check.equal(*test):
                    break
        except TimeoutError:
            Check.error("Dovoljen čas izvajanja presežen")
        except Exception:
            Check.error(
                "Testi sprožijo izjemo\n  {0}",
                "\n  ".join(traceback.format_exc().split("\n"))[:-2],
            )

    if Check.part():
        Check.current_part[
            "token"
        ] = "eyJwYXJ0Ijo0MDg2NywidXNlciI6OTc4NH0:1uJnlQ:cN3HdjT1tjviXfi5479lkO-2o0pRNerqNNVSbMPJrEI"
        try:
            tests = [
            ("""Bakterija('').mutacija('G', 'C').get_DNA()""", ""),
            ("""Bakterija('').mutacija('G', 'C').get_generacija()""", 0),
            ("""Bakterija('').mutacija('AT', 'T').get_DNA()""", ""),
            ("""Bakterija('').mutacija('AT', 'T').get_generacija()""", 0),
            ("""Bakterija('').mutacija('AT', 'TT').get_DNA()""", ""),
            ("""Bakterija('').mutacija('AT', 'TT').get_generacija()""", 0),
            ("""Bakterija('').mutacija('G', 'C').mutacija('G', 'C').mutacija('G', 'C').get_generacija()""", 0),
            ("""Bakterija('A').mutacija('G', 'C').get_DNA()""", "A"),
            ("""Bakterija('A').mutacija('G', 'C').get_generacija()""", 1),
            ("""Bakterija('A').mutacija('AT', 'T').get_DNA()""", "A"),
            ("""Bakterija('A').mutacija('AT', 'T').get_generacija()""", 1),
            ("""Bakterija('A').mutacija('AT', 'TT').get_DNA()""", "A"),
            ("""Bakterija('A').mutacija('AT', 'TT').get_generacija()""", 1),
            ("""Bakterija('AG').mutacija('G', 'C').get_DNA()""", "AC"),
            ("""Bakterija('AG').mutacija('G', 'C').get_generacija()""", 1),
            ("""Bakterija('AG').mutacija('AT', 'T').get_DNA()""", "AG"),
            ("""Bakterija('AG').mutacija('AT', 'T').get_generacija()""", 1),
            ("""Bakterija('AG').mutacija('AT', 'TT').get_DNA()""", "AG"),
            ("""Bakterija('AG').mutacija('AT', 'TT').get_generacija()""", 1),
            ("""Bakterija('TTTTAAAAGGGG').mutacija('G', 'C').get_DNA()""", "TTTTAAAACCCC"),
            ("""Bakterija('TTTTAAAAGGGG').mutacija('G', 'C').get_generacija()""", 1),
            ("""Bakterija('TTTTAAAAGGGG').mutacija('AT', 'T').get_DNA()""", "TTTTAAAAGGGG"),
            ("""Bakterija('TTTTAAAAGGGG').mutacija('AT', 'T').get_generacija()""", 1),
            ("""Bakterija('TTTTAAAAGGGG').mutacija('AT', 'TT').get_DNA()""", "TTTTAAAAGGGG"),
            ("""Bakterija('TTTTAAAAGGGG').mutacija('AT', 'TT').get_generacija()""", 1),
            ("""Bakterija('GAAATCGGT').mutacija('G', 'C').get_DNA()""", "CAAATCCCT"),
            ("""Bakterija('GAAATCGGT').mutacija('G', 'C').get_generacija()""", 1),
            ("""Bakterija('GAAATCGGT').mutacija('AT', 'T').get_DNA()""", "GAATCGGT"),
            ("""Bakterija('GAAATCGGT').mutacija('AT', 'T').get_generacija()""", 1),
            ("""Bakterija('GAAATCGGT').mutacija('AT', 'TT').get_DNA()""", "GAATTCGGT"),
            ("""Bakterija('GAAATCGGT').mutacija('AT', 'TT').get_generacija()""", 1),
            ("""Bakterija('GCTATGCCC').mutacija('G', 'C').get_DNA()""", "CCTATCCCC"),
            ("""Bakterija('GCTATGCCC').mutacija('G', 'C').get_generacija()""", 1),
            ("""Bakterija('GCTATGCCC').mutacija('AT', 'T').get_DNA()""", "GCTTGCCC"),
            ("""Bakterija('GCTATGCCC').mutacija('AT', 'T').get_generacija()""", 1),
            ("""Bakterija('GCTATGCCC').mutacija('AT', 'TT').get_DNA()""", "GCTTTGCCC"),
            ("""Bakterija('GCTATGCCC').mutacija('AT', 'TT').get_generacija()""", 1),
            ("""Bakterija('AAAAAAAATTTTTT').mutacija('G', 'C').get_DNA()""", "AAAAAAAATTTTTT"),
            ("""Bakterija('AAAAAAAATTTTTT').mutacija('G', 'C').get_generacija()""", 1),
            ("""Bakterija('AAAAAAAATTTTTT').mutacija('AT', 'T').get_DNA()""", "AAAAAAATTTTTT"),
            ("""Bakterija('AAAAAAAATTTTTT').mutacija('AT', 'T').get_generacija()""", 1),
            ("""Bakterija('AAAAAAAATTTTTT').mutacija('AT', 'TT').get_DNA()""", "AAAAAAATTTTTTT"),
            ("""Bakterija('AAAAAAAATTTTTT').mutacija('AT', 'TT').get_generacija()""", 1),
            ("""Bakterija('AAAAAAAATTTTTT').mutacija('AT', 'TT').mutacija('AT', 'TT').get_generacija()""", 2),
            ("""Bakterija('AAAAAAAATTTTTT').mutacija('AT', 'TT').mutacija('AT', 'TT').mutacija('AT', 'TT').get_generacija()""",
                        3)
                    ]
            
            for test in tests:
                if not Check.equal(*test):
                    break
        except TimeoutError:
            Check.error("Dovoljen čas izvajanja presežen")
        except Exception:
            Check.error(
                "Testi sprožijo izjemo\n  {0}",
                "\n  ".join(traceback.format_exc().split("\n"))[:-2],
            )

    print("Shranjujem rešitve na strežnik... ", end="")
    try:
        url = "https://www.projekt-tomo.si/api/attempts/submit/"
        token = "Token 69276637421863535dfeec74e6a15efea8f4b607"
        response = submit_parts(Check.parts, url, token)
    except urllib.error.URLError:
        message = (
            "\n"
            "-------------------------------------------------------------------\n"
            "PRI SHRANJEVANJU JE PRIŠLO DO NAPAKE!\n"
            "Preberite napako in poskusite znova ali se posvetujte z asistentom.\n"
            "-------------------------------------------------------------------\n"
        )
        print(message)
        traceback.print_exc()
        print(message)
        sys.exit(1)
    else:
        print("Rešitve so shranjene.")
        update_attempts(Check.parts, response)
        if "update" in response:
            print("Updating file... ", end="")
            backup_filename = backup(filename)
            with open(__file__, "w", encoding="utf-8") as f:
                f.write(response["update"])
            print("Previous file has been renamed to {0}.".format(backup_filename))
            print("If the file did not refresh in your editor, close and reopen it.")
    Check.summarize()


if __name__ == "__main__":
    _validate_current_file()
