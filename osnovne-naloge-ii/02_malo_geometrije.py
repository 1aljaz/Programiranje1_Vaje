# =============================================================================
# Malo geometrije
#
# Pri teh nalogah bo potrebno uporabiti funkcije in konstante, ki so definirane v knjižnici `math`.
# Da jih lahko uporabiš, moraš na začetku programa knjižnico uvoziti takole:
# 
#     import math
# 
# Konstanto $\pi$ lahko nato uporabimo z ukazom `math.pi`, funkcijo sinus 
# (za vrednost v spremenljivki `x`) pa pokličemo z ukazom `math.sin(x)`.
# =====================================================================@040395=
# 1. podnaloga
# Napiši program, ki mu uporabnik poda polmer kroga v obliki decimalnega števila,
# in izpiše njegov obseg in površino. Obseg in ploščina naj bosta zaokrožena na
# dve decimalni mesti. 
# Pri zaokroževanju si pomagaj s funkcijo `round(stevilo, [st. stevk])`.
# 
#     Polmer kroga: 4.2
#     Obseg kroga: 26.39
#     Ploščina kroga: 55.42
# =============================================================================
import math

r = float(input('Polmer kroga: '))
print(f'Obseg kroga: {round(2*math.pi*r, 2)}\nPloščina kroga: {round(math.pi*r**2, 2)}\n')
# =====================================================================@040396=
# 2. podnaloga
# Spodnji program bi moral za podani dolžini katet v obliki decimalnih števil izračunati dolžino
# hipotenuze po Pitagorevem izreku, vendar se je pri programiranju zalomilo.
# 
#     a = imput("Dolžina prve katete: ")
#     b = imput("Dolžina druge katete: ")
#     c = sqrt(a^2 + b^2)
#     print(Dolžina hipotenuze je, c)
# 
# Ko boš odprl nalogo, te napačni program že čaka. Poskusi ga prevesti in popravi, da bo deloval takole:
# 
#     Dolžina prve katete: 3.0
#     Dolžina druge katete: 4
#     Dolžina hipotenuze je 5.0
# 
# Namig: če imaš težave z računanjem hipotenuze, preveri kaj v pythonu pomeni operator `^`
# in kako se [računa potence](https://www.programiz.com/python-programming/operators)
# =============================================================================
a = float(input("Dolžina prve katete: "))
b = float(input("Dolžina druge katete: "))
c = math.sqrt(a**2 + b**2)
print(f'Dolžina hipotenuze je {c}')

# =====================================================================@040397=
# 3. podnaloga
# Napiši program, ki uporabnika vpraša po dolžinah stranic poljubnega trikotnika
# in izpiše njegovo ploščino (zaokroženo na dve decimalki). Vnešene stranice naj bodo decimalna števila.
# Za izračun lahko uporabiš [Heronovo formulo](https://en.wikipedia.org/wiki/Heron%27s_formula).
# 
#     Dolžina stranice a: 3.0
#     Dolžina stranice b: 4.0
#     Dolžina stranice c: 5.0
#     Ploščina trikotnika: 6.0
# =============================================================================
a = float(input('Dolžina stranice a: '))
b = float(input('Dolžina stranice b: '))
c = float(input('Dolžina stranice c: '))

s = 0.5*(a+b+c)

print(f'Ploščina trikotnika: {round(math.sqrt(s*(s-a)*(s-b)*(s-c)), 2)}')
# =====================================================================@040398=
# 4. podnaloga
# Zanima nas, kakšna je ploščina včrtanega kroga za trikotnik, kot iz tretje podnaloge.
# Program naj z vhoda prebere dolžine stranic in izpiše ploščino trikotniku včrtanega kroga.
# 
# Pri tem nam pomaga [formula](https://sl.wikipedia.org/wiki/V%C4%8Drtana_kro%C5%BEnica#Trikotniku_v.C4.8Drtana_kro.C5.BEnica),
# ki določa zvezo med ploščino poljubnega trikotnika in polmerom včrtanega kroga.
# 
# Rezultat zaokroži na dve decimalki.
# 
#     Dolžina stranice a: 3.0
#     Dolžina stranice b: 4.0
#     Dolžina stranice c: 5.0
#     Ploščina trikotniku včrtanega kroga: 3.14
# 
# Ne pozabi, da so stranice lahko decimalna števila.
# =============================================================================
a = float(input('Dolžina stranice a: '))
b = float(input('Dolžina stranice b: '))
c = float(input('Dolžina stranice c: '))

s=0.5*(a+b+c)
p = round(math.sqrt(s*(s-a)*(s-b)*(s-c)), 2)

r = round(p/s, 2)
print(f'Ploščina trikotniku včrtanega kroga: {round(math.pi*r**2, 2)}')

# =====================================================================@040399=
# 5. podnaloga
# Zanima nas, kakšna je ploščina očrtanega kroga za trikotnik kot iz tretje podnaloge.
# Program naj z vhoda prebere dolžine stranic in izpiše ploščino trikotniku očrtanega kroga.
# 
# Pri tem si pomagaj s [formulo](https://sl.wikipedia.org/wiki/V%C4%8Drtana_kro%C5%BEnica#Trikotniku_v.C4.8Drtana_kro.C5.BEnica),
# ki določa zvezo med ploščino poljubnega trikotnika in polmerom včrtanega kroga.
# 
# Rezultat zaokroži na dve decimalki
# 
#     Dolžina stranice a: 3.0
#     Dolžina stranice b: 4.0
#     Dolžina stranice c: 5.0
#     Ploščina trikotniku očrtanega kroga: 19.63
# 
# Ne pozabi, da so stranice lahko decimalna števila.
# =============================================================================
import math 

a = float(input('Dolžina stranice a: '))
b = float(input('Dolžina stranice b: '))
c = float(input('Dolžina stranice c: '))
s = 0.5 * (a + b + c)
p = math.sqrt(s*(s-a)*(s-b)*(s-c))
R = round(a*b*c)/(4*p)
print(f'Ploščina trikotniku očrtanega kroga: {round(math.pi*R**2, 2)}')



































































































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
        ] = "eyJwYXJ0Ijo0MDM5NSwidXNlciI6OTc4NH0:1t37lE:rUullaLFibDyMab9wZe48zunrHOAj1HwIs-p7SLzZjE"
        try:
            vhod = ['4.2', '1', '2.5', '0.3183098861837907']
            obsegi = ['26.39', '6.28', '15.71', '2.0']
            ploscine = ['55.42', '3.14', '19.63', '0.32']
            pat1 = r'Polmer kroga: {}'
            pat2 = r'Obseg kroga: {}'
            pat3 = r'Ploščina kroga: {}'
            
            for i in range(len(vhod)):
                with Check.input([vhod[i]]):
                    izh = [pat1.format(vhod[i]), pat2.format(obsegi[i]), pat3.format(ploscine[i])]
                    if not Check.output(Check.current_part['solution'], izh):
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
        ] = "eyJwYXJ0Ijo0MDM5NiwidXNlciI6OTc4NH0:1t37lE:Ed582g2otFehOIECsP_md6DvA_938ytXn6yAvLheiQc"
        try:
            vhod = [['3.0', '4.0'], ['1.0', '1.0'], ['10.3', '23.1']]
            pat1 = r'Dolžina prve katete: {}'
            pat2 = r'Dolžina druge katete: {}'
            pat3 = r'Dolžina hipotenuze je {}'
            
            for i in range(len(vhod)):
                with Check.input([*vhod[i]]):
                    a, b = vhod[i]
                    c = str(math.sqrt(float(a)**2 + float(b)**2))
                    izh = [pat1.format(vhod[i][0]), pat2.format(vhod[i][1]), pat3.format(c)]
                    if not Check.output(Check.current_part['solution'], izh):
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
        ] = "eyJwYXJ0Ijo0MDM5NywidXNlciI6OTc4NH0:1t37lE:LvJRVTbQNbU5cAlUksN4tJdU-KEF2Z443LtTGT5ttB4"
        try:
            test = [['3.0', '4.0', '5.0', '6.0'], ['2', '5', '6', '4.68'],['3.14', '5.2', '2.12', '1.01']]
            
            for i in range(len(test)):
                with Check.input(test[i]):
                    Check.output(Check.current_part['solution'], [
                        "Dolžina stranice a: " + test[i][0],
                        "Dolžina stranice b: " + test[i][1],
                        "Dolžina stranice c: " + test[i][2],
                        "Ploščina trikotnika: " + test[i][3]
                    ])
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
        ] = "eyJwYXJ0Ijo0MDM5OCwidXNlciI6OTc4NH0:1t37lE:gUV2g94FgJoejCjeKFNwHuCJH3TpHkhr4CFXZZCQgy0"
        try:
            test = [['3', '4', '5', '3.14'], ['2', '5', '6', '1.63'], ['1', '1', '1', '0.26']]
            
            for i in range(len(test)):
                with Check.input(test[i]):
                    Check.output(Check.current_part['solution'], [
                        "Dolžina stranice a: " + test[i][0],
                        "Dolžina stranice b: " + test[i][1],
                        "Dolžina stranice c: " + test[i][2],
                        "Ploščina trikotniku včrtanega kroga: " + test[i][3]
                    ])
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
        ] = "eyJwYXJ0Ijo0MDM5OSwidXNlciI6OTc4NH0:1t37lE:CQCBY_1RCf93ORJHUiRfiCHxFbdmg5eVOZB2IBDwr3U"
        try:
            test = [['3', '4', '5', '19.63'], ['2.0', '5.0', '6.0', '32.22'], ['1', '1', '1', '1.05']]
            
            for i in range(len(test)):
                with Check.input(test[i]):
                    Check.output(Check.current_part['solution'], [
                        "Dolžina stranice a: " + test[i][0],
                        "Dolžina stranice b: " + test[i][1],
                        "Dolžina stranice c: " + test[i][2],
                        "Ploščina trikotniku očrtanega kroga: " + test[i][3]
                    ])
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
