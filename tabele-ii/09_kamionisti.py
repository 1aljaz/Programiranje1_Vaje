# =============================================================================
# Kamionisti
#
# V Republiki Banana zaradi utrujenosti in pomanjkanja koncentracije
# kamionisti
# ([slovensko - *vozniki kamionov* Zato pet minut za učenje slovenčine](http://www.topky.sk/cl/10/1482471/Slovenski-kamionisti-v-soku--VIDEO--ako-im-do-auta-chceli-naskakat-utecenci-))
# vse pogosteje povzročajo nesreče. Na vladi so se odločili,
# da bodo sprejeli zakone, ki bodo uredili problematiko preutrujenih
# kamionistov. Najprej pa morajo analitiki preučiti njihove navade. V ta
# namen so pridobili podatke o kamionistih. Za vsakega imajo podano
# tabelo, v kateri so shranjene prevožene razdalje po posameznih dnevih.
# Število 0 pomeni, da je kamionist tisti dan počival. 
# 
# Primer: Tabela
# 
#     [350, 542.5, 0, 602, 452.5, 590.5, 0, 248]
# 
# pomeni, da je kamionist prvi dan prevozil 350 km, drugi dan je prevozil
# 542.5 km, tretji dan je počival itd.
# =====================================================================@040568=
# 1. podnaloga
# Sestavite funkcijo `pocitek_in_povprecje(voznja)`, ki kot argument
# dobi zgoraj opisano tabelo (prevožene razdalje po posameznih dnevih)
# in vrne par števil. Prvo število naj bo število dni, ko je kamionist
# počival. Drugo število naj bo na eno decimalko zaokrožena (`round(x, 1)`)
# povprečna dnevna prevožena razdalja, pri
# čemer upoštevamo samo tiste dneve, ko ni počival. Predpostavite lahko,
# da kamionist vsaj en dan ni počival. Primer:
# 
#     >>> pocitek_in_povprecje([200, 300, 0, 100])
#     (1, 200.0)
# 
# Kamionist je torej enkrat počival. Ob dnevih, ko ni počival, pa je
# v povprečju prevozil 200 km.
# =============================================================================

# =====================================================================@040569=
# 2. podnaloga
# Napišite funkcijo `primerjaj(prvi, drugi)`, ki primerja vožnjo dveh
# kamionistov. Funkcija kot argumenta dobi dve enako dolgi tabeli
# `prvi` in `drugi`, ki opisujeta vožnjo dveh kamionistov, ki sta se
# podala na isto pot. Funkcije naj sestavi in vrne novo tabelo, v kateri
# je za vsak dan zapisano, kdo je **do tega dne skupaj** prevozil večjo 
# razdaljo:
# `1`, če je bil to 1. kamionist; `2`, če je bil to 2. kamionist in
# `0`, če sta oba prevozila enako razdaljo. Primer:
# 
#     >>> primerjaj([200, 300, 100], [200, 200, 300])
#     [0, 1, 2]
#     >>> primerjaj([500, 100, 100], [100, 200, 200])
#     [1, 1, 1]
# =============================================================================

# =====================================================================@040570=
# 3. podnaloga
# Vlada je uzakonila naslednja pravila:
# * Povprečna prevožena razdalja v treh zaporednih dneh ne sme biti več
#   kot 500 km. (Štejemo tudi dneve, ko je kamionist počival.)
# * Kamionist ne sme brez počitka voziti več kot 5 dni v zaporedju.
# 
# Ker so ugotovili, da so kamionisti prevečkrat svoje zaporedje skrajšali
# na dva dni in se s tem dejansko izognili pravilu, so uzakonili še:
# * Zadnji dan ne sme voziti več kot 500 km.
# * Povprečje zadnjih dveh dni ne sme biti več kot 500 km.
# 
# Sestavite funkcijo `po_pravilih(voznja)`, ki vrne `True`, če se je
# kamionist držal predpisov, in `False`, če se jih ni.
# 
#     >>> po_pravilih([50, 200, 300, 20, 100, 60])
#     False
#     >>> po_pravilih([600, 200, 0, 300, 300, 0, 600, 600, 400])
#     False
#     >>> po_pravilih([600, 600, 0, 600, 600])
#     False
#     >>> po_pravilih([600, 600, 0, 200, 600])
#     False
# =============================================================================

# =====================================================================@040571=
# 4. podnaloga
# Podatke za več kamionistov so analitiki združili v eno samo tabelo.
# Zgled take tabele:
# 
#     vsi_skupaj = [
#         [50, 200, 300, 20, 100, 60],
#         [600, 600, 0, 600, 600, 0, 500, 500],
#         [600, 200, 0, 300, 300, 0, 600, 600, 400]
#     ]
# 
# Sestavite funkcijo `preveri_vse(seznam_vozenj)`, ki dobi kot argument
# tabelo kot je zgoraj in vrne tabelo logičnih vrednosti, ki za vsakega 
# kamionista pove, če je vozil po predpisih. Primer:
# 
#     >>> preveri_vse(vsi_skupaj)
#     [False, True, False]
# =============================================================================

# =====================================================================@040572=
# 5. podnaloga
# Ko so vožnje vseh kamionistov že tako lepo združene, so se analitiki spravili
# računati še to, kakšno je navečje število voženj, ki jih je nekdo opravil,
# kakšno je največje število dni počitka ter kakšno je največje in kakšno
# najmanjše povprečno število dnevno prevoženih kilometrov (povprečje tako,
# kot pri prvi nalogi - štejemo le dneve vožnje). Pri tem upoštevamo samo tiste
# kamioniste, ki so vozili po pravilih!
# Sestavite funkcijo `analitika(seznam_vozenj)`, ki dobi kot argument
# ustrezno tabelo in vrne nabor 4 vrednosti: največ voženj, največ dni počitka,
# maksimalno povprečno dnevno prevoženih in minimalno povprečnodnevno
# prevoženih kilometrov. Predpostavi, da imamo vsaj enega kamionista, ki je
# vozil po predpisih!
# Primer (podatki iz prejšnje naloge):
# 
#     >>> analitika(vsi_skupaj)
#     (6, 2, 566.7, 566.7)
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
        ] = "eyJwYXJ0Ijo0MDU2OCwidXNlciI6OTc4NH0:1tV8mJ:8JKn7ubV_OTbpp1AW03JWXayfqeGxlfrYNQcVc9xBjs"
        try:
            Check.equal("""pocitek_in_povprecje([200, 300, 0, 100])""", (1, 200.0)) and \
                Check.equal("""pocitek_in_povprecje([350, 542.5, 0, 602, 452.5, 590.5, 0, 248.01])""", (2, 464.3)) and \
                Check.equal("""pocitek_in_povprecje([0, 0, 350, 542.5, 0, 602, 452.5, 590.5, 0, 248, 0, 0])""", (6, 464.2)) and \
                Check.equal("""pocitek_in_povprecje([100, 200, 100, 200, 100, 200, 100, 200])""", (0, 150.0)) and \
                Check.equal("""pocitek_in_povprecje([800, 0, 200])""", (1, 500.0))
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
        ] = "eyJwYXJ0Ijo0MDU2OSwidXNlciI6OTc4NH0:1tV8mJ:p2aXOnujubM8Wwr99QtYRlGx3L3FmMz-JetJMwtiuY4"
        try:
            Check.equal("""primerjaj([200, 300, 100], [200, 200, 300])""",
                        [0, 1, 2]) and \
                Check.equal("""primerjaj([500, 100, 100], [100, 200, 200])""",
                            [1, 1, 1]) and \
                Check.equal("""primerjaj([500, 0, 300, 100, 300, 100, 300], [500, 0, 200, 300, 100, 300, 100])""",
                            [0, 0, 1, 2, 1, 2, 1]) and \
                Check.equal("""primerjaj([350, 542.5, 0, 602, 452.5, 590.5, 0, 248], [350, 0, 0, 602, 542.5, 452.5, 590.5, 248])""",
                            [0, 1, 1, 1, 1, 1, 0, 0]) and \
                Check.equal("""primerjaj([100, 200, 100, 200, 100, 200, 100, 200], [200, 100, 200, 100, 200, 100, 200, 100])""",
                            [2, 0, 2, 0, 2, 0, 2, 0]) and \
                Check.equal("""primerjaj([300, 100, 300, 100, 300], [200, 300, 100, 300, 100])""",
                            [1, 2, 1, 2, 1]) and \
                Check.equal("""primerjaj([300, 100, 300, 100, 300], [300, 100, 300, 100, 300])""",
                            [0] * 5)
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
        ] = "eyJwYXJ0Ijo0MDU3MCwidXNlciI6OTc4NH0:1tV8mJ:eoJ3aWWP-U320cMI1hPgQ92KmZ4mm68gX36t6zrewpU"
        try:
            Check.equal("""po_pravilih([200, 300, 0, 100])""", True) and \
                Check.equal("""po_pravilih([500, 500, 500, 500, 500, 0, 500, 500, 500, 500, 500, 0, 500, 500, 500, 500, 500])""", True) and \
                Check.equal("""po_pravilih([50, 200, 300, 20, 100, 60])""", False) and \
                Check.equal("""po_pravilih([600, 200, 0, 300, 300, 0, 600, 600, 400])""", False) and \
                Check.equal("""po_pravilih([600, 600, 0, 600, 600, 0, 600, 600])""", False) and \
                Check.equal("""po_pravilih([600, 600, 0, 600, 600, 0, 600, 600, 600])""", False) and \
                Check.equal("""po_pravilih([1, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1])""", False) and \
                Check.equal("""po_pravilih([0, 0, 0, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0])""", False) and \
                Check.equal("""po_pravilih([0, 0, 0, 0, 1, 0, 1, 1, 1, 1, 0, 1, 1, 1, 0, 0, 0])""", True) and \
                Check.equal("""po_pravilih([500])""", True) and \
                Check.equal("""po_pravilih([501])""", False) and \
                Check.equal("""po_pravilih([500, 600])""", False) and \
                Check.equal("""po_pravilih([600, 500])""", False) and \
                Check.equal("""po_pravilih([500, 500])""", True) and \
                Check.equal("""po_pravilih([500,500, 500])""", True) and \
                Check.equal("""po_pravilih([0, 500, 500, 500, 500])""", True) and \
                Check.equal("""po_pravilih([0, 0, 0, 500, 500, 500, 500])""", True) and \
                Check.equal("""po_pravilih([0, 0, 0, 0, 500, 500, 500, 500, 500, 500, 0])""", False) and \
                Check.equal("""po_pravilih([0, 500, 500, 0, 500, 500, 0, 500, 500, 500, 0])""", True)
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
        ] = "eyJwYXJ0Ijo0MDU3MSwidXNlciI6OTc4NH0:1tV8mJ:34HjeWwiyJIzvi_Ll7yLh0KSU2Bsrx7eLP2ax7-WAGo"
        try:
            Check.equal("""preveri_vse([[50, 200, 300, 20, 100, 60], [600, 600, 0, 600, 600, 0, 500, 500], [600, 200, 0, 300, 300, 0, 600, 600, 400]])""", [False, True, False]) and \
                Check.equal("""preveri_vse([[50, 200, 300, 20, 100, 60], [600, 600, 0, 600, 600, 0, 600, 600], [600, 200, 0, 300, 300, 0, 600, 600, 400]])""", [False, False, False]) and \
                Check.equal("""preveri_vse([[200, 300, 0, 100], [500, 500, 500, 500, 500, 0, 500, 500, 500, 500, 500, 0, 500, 500, 500, 500, 500], [50, 200, 300, 20, 100, 60], [600, 200, 0, 300, 300, 0, 600, 600, 400], [600, 600, 0, 600, 600, 0, 600, 600]])""", [True, True, False, False, False]) and \
                Check.equal("""preveri_vse([[50, 200, 300, 20, 100, 60], [600, 200, 0, 300, 300, 0, 600, 600, 400], [200, 300, 0, 100], [500, 500, 500, 500, 500, 0, 500, 500, 500, 500, 500, 0, 500, 500, 500, 500, 500], [600, 600, 0, 600, 600, 0, 600, 600]])""", [False, False, True, True, False]) and \
                Check.equal("""preveri_vse([[500]])""", [True]) and \
                Check.equal("""preveri_vse([[501]])""", [False]) and \
                Check.equal("""preveri_vse([[500, 600]])""", [False]) and \
                Check.equal("""preveri_vse([[600, 500]])""", [False]) and \
                Check.equal("""preveri_vse([[500, 500]])""", [True]) and \
                Check.equal("""preveri_vse([[500,500, 500]])""", [True]) and \
                Check.equal("""preveri_vse([[0, 500, 500, 500, 500]])""", [True]) and \
                Check.equal("""preveri_vse([[0, 0, 0, 500, 500, 500, 500]])""", [True]) and \
                Check.equal("""preveri_vse([[0, 0, 0, 0, 500, 500, 500, 500, 500, 500, 0]])""", [False]) and \
                Check.equal("""preveri_vse([[0, 500, 500, 0, 500, 500, 0, 500, 500, 500, 0]])""", [True])
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
        ] = "eyJwYXJ0Ijo0MDU3MiwidXNlciI6OTc4NH0:1tV8mJ:YPT2ggwZtIgXtXioH5djIOEimlRfWDklvXZr_2zG1uY"
        try:
            Check.equal("""analitika([[50, 200, 300, 20, 100, 60], [600, 600, 0, 600, 600, 0, 500, 500], [600, 200, 0, 300, 300, 0, 600, 600, 400]])""", (6, 2, 566.7, 566.7)) and \
                Check.equal("""analitika([[50, 200, 300, 20, 100, 60], [500, 500, 0, 500, 500, 0, 500, 500], [600, 200, 0, 300, 300, 0, 600, 600, 400]])""", (6, 2, 500.0, 500.0)) and \
                Check.equal("""analitika([[50, 200, 300, 20, 100, 60], [600, 600, 0, 600, 600, 0, 500, 500], [600, 200, 0, 300, 300, 0, 600, 600, 400, 500, 300, 100]])""", (6, 2, 566.7, 566.7)) and \
                Check.equal("""analitika([[200, 300, 0, 100], [500, 500, 500, 500, 500, 0, 500, 500, 500, 500, 500, 0, 500, 500, 500, 500, 500], [50, 200, 300, 20, 100, 60], [600, 200, 0, 300, 300, 0, 600, 600, 400], [600, 600, 0, 600, 600, 0, 600, 600]])""", (15, 2, 500.0, 200.0)) and \
                Check.equal("""analitika([[50, 200, 300, 20, 100, 60], [600, 200, 0, 300, 300, 0, 600, 600, 400], [200, 300, 0, 100], [500, 500, 500, 500, 500, 0, 500, 500, 500, 500, 500, 0, 500, 500, 500, 500, 500], [600, 600, 0, 600, 600, 0, 600, 600]])""", (15, 2, 500.0, 200.0)) and \
                Check.equal("""analitika([[500]])""", (1, 0, 500.0, 500.0)) and \
                Check.equal("""analitika([[500, 500]])""", (2, 0, 500.0, 500.0)) and \
                Check.equal("""analitika([[500,500, 500]])""", (3, 0, 500.0, 500.0)) and \
                Check.equal("""analitika([[0, 500, 500, 500, 500]])""", (4, 1, 500.0, 500.0)) and \
                Check.equal("""analitika([[0, 0, 0, 500, 500, 500, 500]])""", (4, 3, 500.0, 500.0)) and \
                Check.equal("""analitika([[0, 500, 500, 0, 500, 500, 0, 500, 500, 500, 0]])""", (7, 4, 500.0, 500.0)) and \
                Check.equal("""analitika([[200, 800, 0, 0, 0]])""", (2, 3, 500.0, 500.0)) and \
                Check.equal("""analitika([[800, 200]])""", (2, 0, 500.0, 500.0)) and \
                Check.equal("""analitika([[200, 0, 800, 0, 0, 0, 0]])""", (2, 5, 500.0, 500.0)) and \
                Check.equal("""analitika([[200, 0, 200], [500, 500] ])""", (2, 1, 500.0, 200.0)) and \
                Check.equal("""analitika([[200, 0, 800], [300, 500] ])""", (2, 0, 400.0, 400.0)) and \
                Check.equal("""analitika([[200, 0, 600, 0], [500, 500] ])""", (2, 2, 500.0, 400.0)) and \
                Check.equal("""analitika([[200, 0, 100, 800], [300, 500] ])""", (2, 0, 400.0, 400.0)) and \
                Check.equal("""analitika([[200, 0, 800, 200], [300, 500] ])""", (3, 1, 400.0, 400.0)) and \
                Check.equal("""analitika([[200, 0, 600, 600], [500, 500] ])""", (2, 0, 500.0, 500.0)) and \
                Check.equal("""analitika([[100, 0, 100, 100], [300, 500] ])""", (3, 1, 400.0, 100.0))
            
            # =============================================================================
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
