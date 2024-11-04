# =============================================================================
# Mirko in Slavko
#
# Za uvod si preberite nekaj o [Mirku in Slavku](http://www.croinfo.net/razno/4887-tko-nije-itao-strip-mirko-i-slavko.html):
# 
# - [Slavko je ranjen](http://www.stripovi.com/enciklopedija/strip/mirko-i-slavko-nkrb-516-slavko-je-ranjen/29486/0/) 
# - [film](http://www.imdb.com/title/tt0181690/)
# =====================================================================@040443=
# 1. podnaloga
# **Prevara s čekom**
# 
# Kurirji so iznajdljivi. Seveda Mirko in Slavko pa sploh. V roke sta dobila ček,
# kjer banka prinositelju izplača vrednost na njem napisanega tromestnega zneseka. Ampak Mirko ne bi bil Mirko, če ne bi
# kaj hitro ugotovil, da z malo spretnosti in ostrim nožičem lahko ček neopazno spremeni
# tako, da premeša števke na znesku. A kaj, ko je Mirko bolj slab v matematiki, rad pa bi
# ček popravil tako, da bo dobil kar se da veliko. Potoži se Slavku. *Ah, to pa ja ni problem. 
# Poglej to funkcijo. Malo jo spremeni, pa boš dobil največje možno število.* Mirko sedaj proučuje
# 
#     def kaj_delam(n):
#         '''Pozor, n je obvezno tromestno naravno število
#         Spremenljivke imajo namenoma čudna imena.
#         '''
#         a = n - n % 10
#         b = a // 10  % 10
#         c = n - a
#         d = n // 100
#         e = max(b, c, d)
#         f = min(b, c, d)
#         g = b + c + d - e - f
#         return f, g, e
# 
# Premisli kaj funkcija počne in na osnovi ideje v njej namesto Mirka sestavi funkcijo `naj_tromestno`, ki iz
# danega tromestnega števila sestavi največje možno tromestno število
# 
#     >>> naj_tromestno(137)
#     731
#     >>> naj_tromestno(625)
#     652
# =============================================================================
def kaj_delam(n):
        '''Pozor, n je obvezno tromestno naravno število
        Spremenljivke imajo namenoma čudna imena.
        '''
        a = n - n % 10
        b = a // 10  % 10
        c = n - a
        d = n // 100
        e = max(b, c, d)
        f = min(b, c, d)
        g = b + c + d - e - f
        return f, g, e

def naj_tromestno(st:int):
    """Vrne najvecje mnozno tri mestno stevilo iz stevk"""
    a = kaj_delam(st)
    a = list(a)
    naj = ""

    while len(a):
        naj_st = max(a)
        naj += str(naj_st)
        a.remove(naj_st)
    if len(naj) == 1:
        naj = naj*3

    return int(naj)

# =====================================================================@040444=
# 2. podnaloga
# **Mirko, pazi metak!**
# 
# Verjetno najbolj znamenit dialog med Mirkom in Slavkom je:
# 
# - **Slavko:** *Mirko, pazi metak!* 
# - **Mirko:** *Hvala ti, Slavko. Spasio si mi život.*
# 
# 
# Kako hitro se mora Mirko skloniti, če Slavko strel opazi `n` metrov proč
# 
# Sestavi funkcijo `skloni_se(koliko_m, hitrost_metka)`, ki pove, v koliko sekundah, desetinkah
# in stotinkah se mora Mirko skloniti, če Slavko opazi metek `koliko_m` metrov proč in ima hitrost
# `hitrost_metka` m/s. Pazi, da bodo stotinke ustrezno zaokrožene!
# 
# Primer:
# 
#     >>> skloni_se(1, 1)
#     1, 0, 0
# =============================================================================

# =====================================================================@040445=
# 3. podnaloga
# **Metak mrzkog neprijatelja**
# 
# Slavka skrbi, če bo tudi on dovolj hiter, da bo ubežal krogli.
# Zato mu sestavi program, ki bo meril njegov rekacijski čas.
# 
# Če na začetek programa napišemo
# 
#     import time
# 
# bomo, med drugim, dobili funkcijo `time`, ki s klicem `time.time()` vrne čas v sekundah od nekega trenutka v davni preteklosti.
# Napiši program, ki bo izpisal *Slavko, pazi metak!* in izmeril, koliko časa je trajalo, da je Slavko pritisnil na tipko
# `Enter` in potem izpisal, koliko sekund je Slavko potreboval za pritisk na tipko. 
# 
# _Namig: če veš, koliko je bila ura pred klicem funkcije input in koliko je bila ura po klicu,
# znaš izračunati, koliko časa je minilo vmes._
# 
#     >>> Slavko, pazi metak!
#     Slavko je reagiral v 2.503019332885742 s.
# =============================================================================

# =====================================================================@040446=
# 4. podnaloga
# **Mirko in Slavko ob pomoči Dimnjačara pečeta palačinke**
# 
# Mirko in Slavko sta v uspešni akciji zaplenila velike količine moke in jajc.
# Zato bosta za celo vas Glavuša na Kozari napekla palačinke.
# 
# Ampak kaj, ko ne vesta koliko. [Dimnjačar](https://www.imdb.com/title/tt0192904/)
# jima je zato napisal funkcijo. A kaj, ko mu je, tik preden je odšel,
# izpod listov trpotca, ki jih je imel na čelu namesto obveze,
# padlo par kapelj krvi in je sedaj funkcija
# 
#     def koliko_palacink(st_odraslih, st_otrok):
#         '''Vrne število palačink potrebnih, da nasiti vse povabljene.'''
#         PACKA
#         PACKA
#         palacinke_odrasli = st_odraslih * odrasel
#         palacinke_otroci = st_otrok * otrok
#         palacinke_skupaj = palacinke_odrasli + palacinke_otroci + PACKA # še malo za rezervo
#         return palacinke_skupaj
# 
# Na srečo pa so ostali še trije izpisi, ko jima je pokazal delovanje funkcije. Pomagaj
# Mirku in Slavku in dopolni funkcijo, da se bo obnašala kot prej, če so izpisi
#    
#     Koliko je odraslih: 12
#     Koliko otrok: 5
#     Napeči je potrebno 77 palačink.
#     Koliko je odraslih: 21
#     Koliko otrok: 14
#     Napeči je potrebno 140 palačink.
#     Koliko je odraslih: 10
#     Koliko otrok: 15
#     Napeči je potrebno 87 palačink.
# =============================================================================

# =====================================================================@040447=
# 5. podnaloga
# **Slavko peče torte**
# 
# Po velikem uspehu s peko palačink, se je Slavko spravil peči torte.
# Po receptu za torto potrebujemo 0.8 kg margarine, 2 kg moke in 1.5 kg sladkorja. 
# Sedaj Slavka zanima, kakšno je, glede na količine sestavin, ki jih ima na razpolago,
# največje možno število tort, ki jih lahko naredi.
# 
# _Namig_: Funkcija `min` vrne najmanjšega izmed svojih parametrov.
# 
# Primer: Če imamo 5kg margarine, 7kg moke in 3.5kg sladkorja, lahko spečemo dve torti.
# 
# Slavku sestavi funkcijo `koliko_tort(margarina, moka, sladkor)`, ki glede na dani recept
# določi največje možno število tort.
# =============================================================================

# =====================================================================@040448=
# 6. podnaloga
# **Mirko in smučarski skoki**
# 
# Medtem, ko Slavko peče torte, je Mirko organiziral tekmovanje v smučarskih skokih.
# 
# Pri smučarskih skokih so točke skoka vsota:
# 
# - točk za daljavo in
# - točk sloga (ki jih določijo sodniki).
# 
# 
# Vsak od petih sodnikov lahko skakalcu dodeli največ 20 točk, ki so
# odvisne od položaj smuči med letom, ravnotežja med letom, položaja
# telesa, pristanka ipd. Točke sloga so vsota točk posamičnih sodnikov,
# pri čemer se *najboljša in najslabša ocena ne upoštevata*.
# 
# Mirko ima več kot dovolj dela z iskanjem primernih sodnikov (pa še z njegovo matematiko je
# bolj tako, tako ...). Zato mu pomagaj in sestavi funckijo `tocke_slog(oc1,oc2, oc3, oc4, oc5)`,
# ki za danih 5 ocen določi točke za slog. 
# _Namig_: Poleg funkcije `min` Python pozna tudi funkcijo `max`, ki se obnaša podobno!
# =============================================================================






































































































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
        ] = "eyJwYXJ0Ijo0MDQ0MywidXNlciI6OTc4NH0:1t5hUw:qQLD8ZC3zlrENJM0LzhegnBdiirCifRdviJldonaj3Q"
        try:
            s = Check.current_part['solution']
            sw = re.sub('[ \n]', '', s)
            
            if "):\"" not in sw and "):'" not in sw:
                Check.error("Ne pozabi na opis funkcije.")
            elif not naj_tromestno.__doc__ or naj_tromestno.__doc__ == "" or not naj_tromestno.__doc__.strip():
                Check.error("Opis funkcije ne sme biti prazen.")
                
            Check.equal('naj_tromestno(317)', 731) and \
            Check.equal('naj_tromestno(666)', 666) and \
            Check.equal('naj_tromestno(100)', 100) and \
            Check.equal('naj_tromestno(387)', 873) and \
            Check.equal('naj_tromestno(626)', 662) and \
            Check.equal('naj_tromestno(103)', 310)
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
        ] = "eyJwYXJ0Ijo0MDQ0NCwidXNlciI6OTc4NH0:1t5hUw:SXZAi42TCKADuKPYZ5Ucz-hSC54xBFTR0Z_1hP6ubHM"
        try:
            s = Check.current_part['solution']
            sw = re.sub('[ \n]', '', s)
            
            if "):\"" not in sw and "):'" not in sw:
                Check.error("Ne pozabi na opis funkcije.")
            elif not skloni_se.__doc__ or skloni_se.__doc__ == "" or not skloni_se.__doc__.strip():
                Check.error("Opis funkcije ne sme biti prazen.")
                
            Check.equal('skloni_se(1, 1)', (1, 0, 0)) and \
            Check.equal('skloni_se(100, 50)', (2, 0, 0)) and \
            Check.equal('skloni_se(100, 2)', (50, 0, 0)) and \
            Check.equal('skloni_se(600, 510.6)', (1, 1, 7)) and \
            Check.equal('skloni_se(600, 910)', (0, 6, 5)) and \
            Check.equal('skloni_se(100, 200)', (0, 5, 0))
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
        ] = "eyJwYXJ0Ijo0MDQ0NSwidXNlciI6OTc4NH0:1t5hUw:K-E_XP1Gy8PH9WAOzZ3KN81UvqHB_c1_3BYmznHbd5E"
        try:
            koda = Check.current_part['solution']
            
            if 'print(' not in koda:
                Check.error("Uporabite ukaz `print()` za izpis reakcijskega časa!")
                
            elif 'input(' not in koda:
                Check.error("V rešitvi manjka ukaz `input()`!")
                
            else:
                razdelitev = koda.split('input')
                if 'time.time()' not in razdelitev[0] or 'time.time()' not in razdelitev[1]:
                    Check.error("Ukaz `time.time()` ni pravilno uporabljen!")
                    
                else:
                    stdout = sys.stdout
                    sys.stdout = io.StringIO()
                    pojavitve = re.findall('input(.*)',koda)
                    for arg in pojavitve:
                        koda = koda.replace("input"+arg, "time.sleep(0.5)")
                        b = "input"+arg
                    exec(koda)
                    output = sys.stdout.getvalue()
                    sys.stdout = stdout
                    output = output.strip()
                    if float(output[20:-2]) < 0:
                        Check.error("Čas mora biti pozitivno število!")
                    elif not (output[:20] == 'Slavko je reagiral v' and output[-2:] == 's.'):
                        Check.error("Upoštevaj primer izpisa: 'Slavko je reagiral v 2.503019332885742 s.'")
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
        ] = "eyJwYXJ0Ijo0MDQ0NiwidXNlciI6OTc4NH0:1t5hUw:lDrHkpmlN4VMWFuS5HtlH1UQi26z7WPqg7iMgQ9C7l0"
        try:
            s = Check.current_part['solution']
            sw = re.sub('[ \n]', '', s)
            
            if "):\"" not in sw and "):'" not in sw:
                Check.error("Ne pozabi na opis funkcije.")
            elif not koliko_palacink.__doc__ or koliko_palacink.__doc__ == "" or not koliko_palacink.__doc__.strip():
                Check.error("Opis funkcije ne sme biti prazen.")
                
            Check.equal('koliko_palacink(100, 10)', 527) and \
            Check.equal('koliko_palacink(0, 10)', 27) and \
            Check.equal('koliko_palacink(100, 0)', 507) and \
            Check.equal('koliko_palacink(10, 10)', 77) and \
            Check.equal('koliko_palacink(0, 0)', 7) and \
            Check.equal('koliko_palacink(2, 1)', 19)
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
        ] = "eyJwYXJ0Ijo0MDQ0NywidXNlciI6OTc4NH0:1t5hUw:iEjoRKJhRM341zUfVQWbV2tC13gpAZEdzDeYle-rGWw"
        try:
            s = Check.current_part['solution']
            sw = re.sub('[ \n]', '', s)
            
            if "):\"" not in sw and "):'" not in sw:
                Check.error("Ne pozabi na opis funkcije.")
            elif not koliko_tort.__doc__ or koliko_tort.__doc__ == "" or not koliko_tort.__doc__.strip():
                Check.error("Opis funkcije ne sme biti prazen.")
                
            Check.equal('koliko_tort(1.6, 4, 3)', 2) and \
            Check.equal('koliko_tort(1.6, 4, 2.9)', 1) and \
            Check.equal('koliko_tort(1.59, 4, 3)', 1) and \
            Check.equal('koliko_tort(1.6, 3.99, 3)', 1) and \
            Check.equal('koliko_tort(6, 7, 6)', 3) and \
            Check.equal('koliko_tort(1, 1, 1000)', 0) and \
            Check.equal('koliko_tort(1000, 1000, 1000)', 500) and \
            Check.equal('koliko_tort(4.6, 11.6, 10.5)', 5) and \
            Check.equal('koliko_tort(13, 21, 17.5)', 10)
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
        ] = "eyJwYXJ0Ijo0MDQ0OCwidXNlciI6OTc4NH0:1t5hUw:kuE9rg4nDcRRzTMBan9qwMjRaTMsXJoXiP6afp-33zQ"
        try:
            s = Check.current_part['solution']
            sw = re.sub('[ \n]', '', s)
            
            if "):\"" not in sw and "):'" not in sw:
                Check.error("Ne pozabi na opis funkcije.")
            elif not tocke_slog.__doc__ or tocke_slog.__doc__ == "" or not tocke_slog.__doc__.strip():
                Check.error("Opis funkcije ne sme biti prazen.")
                
            Check.equal('tocke_slog(18, 18, 18, 18, 18)', 54) and \
            Check.equal('tocke_slog(16, 18, 18, 18, 18)', 54) and \
            Check.equal('tocke_slog(18, 16, 18, 18, 18)', 54) and \
            Check.equal('tocke_slog(18, 18, 18, 18, 20)', 54) and \
            Check.equal('tocke_slog(18, 16, 20, 18, 18)', 54) and \
            Check.equal('tocke_slog(8, 18, 18, 18, 20)', 54) and \
            Check.equal('tocke_slog(14, 15, 16, 17, 18)', 48)
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
