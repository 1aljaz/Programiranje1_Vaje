# =============================================================================
# LEGO kocke
#
# Boštjan rad sestavlja LEGO kocke. Če bo do konca leta priden, mu bo babica
# Metka za Božič podarila škatlo kock. 
# Ker se kocke pojavljajo v veliko različnih oblikah, ima Metka pri
# izbiranju ustreznega paketa kock kar nekaj težav...
# 
# Vsako [LEGO kocko](http://www.lego.com/en-us/classic) lahko opišemo z dvema
# lastnostima: tipom (torej obliko) in barvo. Predpostavili bomo, da se LEGO
# kocke lahko pojavljajo
# le v 3 različnih barvah: rdeči, modri in rumeni. Tipov LEGO kock pa je
# ogromno,
# zato jih bomo predstavili kar z nizi kot na primer `'2x2'`, `'4x1-tanka'`
# ali pa `'nogice'`.
# 
# Sprejmimo dogovor, da nobeno ime tipa ne vsebuje pike.
# =====================================================================@040678=
# 1. podnaloga
# Vsebino škatle podamo s tabelo vseh kock, ki so v njej. Vsaka kocka
# je opisana z nizom, ki vsebuje tip kocke in barvo, ki sta ločeni s piko.
# Npr. kocka tipa `'2x2'` rdeče barve je predstavljena z nizom `'2x2.rdeča'`.
# 
# Napišite funkcijo `slovar_kock(skatla)`, ki sprejme tabelo `skatla` in sestavi
# slovar vsebovanih kock, urejen po tipih ter po barvah, kot prikazuje primer:
# 
#     >>> slovar_kock(['2x2.rdeča', '2x2.rdeča', 'nogice.modra', '2x2.modra'])
#     {'nogice': {'modra': 1}, '2x2': {'rdeča': 2, 'modra': 1}}
# =============================================================================
def slovar_kock(skatla):
    """Vrne slovar kock."""
    sl = {}
    for kocka in skatla:
        tip, barva = kocka.split('.')
        if tip in sl:
            if barva in sl[tip]:
                sl[tip][barva] +=1
            else:
                sl[tip][barva] = 1
        else:
            sl[tip] = {}
            sl[tip][barva] = 1
    return sl
# =====================================================================@040679=
# 2. podnaloga
# Boštjan je v sestavljanju LEGO kock zelo dober. Njegovi modeli sestojijo
# iz najrazličnejših tipov kock, ki pa jih včasih ni možno kupiti vseh v isti
# škatli.
# 
# Napišite funkcijo `lahko_sestavimo(skatla, model)`, ki dobi dva slovarja
# kock, in vrne `True` natanko tedaj, ko je možno modelček (za katerega
# potrebujemo kocke, ki so podane s slovarjem `model`) sestaviti s kockami,
# ki so v škatli.
# 
#     >>> model = {'4x1': {'modra': 1}, '2x2': {'rdeča': 2, 'modra': 1}}
#     >>> skatla = {'4x1': {'modra': 3, 'rdeča': 2}, '2x2': {'rdeča': 4, 'modra': 1, 'rumena': 5}}
#     >>> lahko_sestavimo(skatla, model)
#     True
#     >>> model_2 = {'4x1': {'rumena': 1}, '2x2': {'rdeča': 1, 'rumena': 2}}
#     >>> lahko_sestavimo(skatla, model_2)
#     False
# =============================================================================
def lahko_sestavimo(skatla, model):
    """Vrne True ce lahko sestavimo model z kockami v skatli."""
    for tip, barve in model.items():
        if tip not in skatla:
            return False
        for barva, stevilo in barve.items():
            if barva not in skatla[tip]:
                return False
            if skatla[tip][barva] < stevilo:
                return False
    return True
# =====================================================================@040680=
# 3. podnaloga
# Boštjana ne moti, če kocke iz katerih sestavlja svoje modele, niso vse
# ustreznih barv, bolj mu je pomembno to, da model sploh lahko sestavi.
# 
# Napišite funkcijo `hitro_sestavljanje(skatla, model)`, ki vrne `True`,
# če je možno modelček sestaviti “na hitro”, torej tako, da barve niso
# pomembne (še vedno pa je pomembno, da uporabimo kocke ustreznega tipa).
# 
#     >>> model = {'4x1': {'modra': 2}, '2x2': {'rdeča': 2, 'modra': 1}}
#     >>> skatla_1 = {'4x1': {'rdeča': 3}, '2x2': {'rdeča': 1, 'rumena': 5}}
#     >>> skatla_2 = {'4x1': {'rumena': 3, 'rdeča': 2}, '2x2': {'rumena': 1, 'rdeča': 1}}
#     >>> hitro_sestavljanje(skatla_1, model)
#     True
#     >>> hitro_sestavljanje(skatla_2, model)
#     False
# =============================================================================
def hitro_sestavljanje(skatla, model):
    """Vrne True ce je v skatli dovolj enega tipa kock ne glede na barvo."""
    skupaj_skatla = {tip : sum(barve.values()) for tip, barve in skatla.items()}
    skupaj_model = {tip : sum(barve.values()) for tip, barve in model.items()}
    for tip, koliko in skupaj_model.items():
        if tip not in skupaj_skatla:
            return False
        if skupaj_skatla[tip] < koliko:
            return False
    return True





































































































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
        ] = "eyJwYXJ0Ijo0MDY3OCwidXNlciI6OTc4NH0:1txo2I:QlYAlNjge2NzlvksRX4i6mtc0lml_nx7YhGTBNXgkRs"
        try:
            Check.equal("slovar_kock(['2x2.rdeča', '2x2.rdeča', 'nogice.modra', '2x2.modra'])",
                        {'nogice': {'modra': 1}, '2x2': {'rdeča': 2, 'modra': 1}}) and \
            Check.equal("slovar_kock([])", {})
            
            Check.secret(slovar_kock(['2x2.rdeča', '2x2.rdeča', '2x2.rdeča']))
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
        ] = "eyJwYXJ0Ijo0MDY3OSwidXNlciI6OTc4NH0:1txo2I:xseltZvKHV0xa8lnje3Cp9sM1VPqOpO3Hw2I-4SP8bY"
        try:
            model = {'4x1': {'modra': 1}, '2x2': {'rdeča': 2, 'modra': 1}}
            skatla = {'4x1': {'modra': 3, 'rdeča': 2}, '2x2': {'rdeča': 4, 'modra': 1, 'rumena': 5}}
            model_2 = {'4x1': {'rumena': 1}, '2x2': {'rdeča': 1, 'rumena': 2}}
            model_3 = {'4x1': {'rdeča': 1}, '2x2': {'rdeča': 4, 'modra': 1}}
            skatla_1 = {'4x1': {'modra': 1}, '2x2': {'rdeča': 2, 'modra': 1}}
            skatla_2 = {'4x1': {'modra': 1}, '2x2': {'rdeča': 2, 'modra': 1}}
            skatla_3 = {'4x1': {'modra': 1}, '2x2': {'rdeča': 4, 'modra': 1, 'rumena': 5}}
            
            Check.equal("lahko_sestavimo({0}, {1})".format(skatla, model), True) and \
            Check.equal("lahko_sestavimo({0}, {1})".format(skatla, model_2), False) and \
            Check.equal("lahko_sestavimo({}, {})", True) and \
            Check.equal("lahko_sestavimo(dict(), {0})".format(skatla_2), False) and \
            Check.equal("lahko_sestavimo({0}, {1})".format(skatla, skatla_2), True)
            
            Check.secret(lahko_sestavimo(skatla_3, skatla_2))
            Check.secret(lahko_sestavimo(model_2, skatla_1))
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
        ] = "eyJwYXJ0Ijo0MDY4MCwidXNlciI6OTc4NH0:1txo2I:dRc51ucvk7gwT6tibiQyYUH4TU2ZYSegzXP8PFf_cz0"
        try:
            model_4 = {'4x1': {'modra': 2}, '2x2': {'rdeča': 2, 'modra': 1}}
            skatla_4 = {'4x1': {'rdeča': 3}, '2x2': {'rdeča': 1, 'rumena': 5}}
            skatla_5 = {'4x1': {'rumena': 3, 'rdeča': 2}, '2x2': {'rumena': 1, 'rdeča': 1}}
            
            Check.equal("hitro_sestavljanje({0}, {1})".format(skatla_4, model_4), True) and \
            Check.equal("hitro_sestavljanje({0}, {1})".format(skatla_5, model_4), False)
            
            Check.secret(hitro_sestavljanje(skatla_2, model))
            Check.secret(hitro_sestavljanje(skatla_2, model_3))
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
