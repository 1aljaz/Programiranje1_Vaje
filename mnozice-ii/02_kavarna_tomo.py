# =============================================================================
# Kavarna Tomo
#
# Kavarna Tomo je izvedla anketo med svojimi strankami in jih vprašala:
# 
#     Ali imate radi kavo? (odgovorili z "da" ali "ne")
#     Ali imate radi čaj? (odgovorili z "da" ali "ne")
#     Ali imate radi kakav? (odgovorili z "da" ali "ne")
# 
# Podatke so zbrali v obliki treh množic:
# 
#     `ljubitelji_kave` – množica ID-jev strank, ki imajo radi kavo.
#     `ljubitelji_caja` – množica ID-jev strank, ki imajo radi čaj.
#     `ljubitelji_kakava` – množica ID-jev strank, ki imajo radi kakav.
# =====================================================================@042855=
# 1. podnaloga
# Napišite funkcijo `pijejo_vse(radi_kavo, radi_caj, radi_kakav)`, ki vrne množico
# anketirancev, ki imajo radi vse tri tople napitke.
# =============================================================================
def pijejo_vse(radi_kavo, radi_caj, radi_kakav):
    """Vrne množico ljudi, ki pijejo vse."""
    return radi_kavo & radi_kakav & radi_caj
# =====================================================================@042856=
# 2. podnaloga
# Sestavite funkcijo `vsi_anketiranci(radi_kavo, radi_caj, radi_kakav)`, ki vrne
# množico vseh sodelujočih v anketi (vseh, ki imajo radi katerega od napitkov).
# =============================================================================
def vsi_anketiranci(radi_kabo, radi_caj, radi_kakav):
    """Vrne mnozico vseh ljudi ki so bili akentirani."""
    return radi_caj | radi_kabo | radi_kakav
# =====================================================================@042857=
# 3. podnaloga
# Sestavite funkcijo `nekaj_s_kakavom(radi_kavo, radi_caj, radi_kakav)`, ki vrne
# množico vseh, ki pijejo kakav s kavo ali čajem (ne pa z obojim).
# =============================================================================
def nekaj_s_kakavom(radi_kavo, radi_caj, radi_kakav):
    """Vrne množico vseh, ki pijejo kakav s kavo ali s čajem."""
    return ((radi_kakav & radi_caj) | (radi_kakav & radi_kavo)) - (radi_kavo & radi_caj & radi_kavo)
# =====================================================================@042858=
# 4. podnaloga
# Izkazalo se je, da funkcija `vsi_anketiranci` ne deluje pravilno. Obstajajo
# namreč obiskovalci Kavarne Tomo, ki so sodelovali v anketi, a ne pijejo nobenega 
# izmed napitkov (morda se ob odličnih Tomovih slaščicah raje osvežijo s hladnimi napitki).
#  
# Na srečo vemo, da se anketirancem dodelijo zaporedne številke ID, začenši z 1.
# Sestavite funkcijo 
# `hladni(radi_kavo, radi_caj, radi_kakav, st_sodelujocih)`, ki
# poleg množic ljubiteljev posameznih napitkov sprejme še število sodelujočih v
# anketi in vrne IDje vseh anketirancev, ki nimajo radi nobenega izmed toplih napitkov.
# =============================================================================
def hladni(radi_kavo, radi_caj, radi_kakav, st_sodelujocih):
    """Vrne mnozico tistih, ki nimajo radi ne caja, ne kakava in ne kave."""

    sodelujoci = set([i for i in range(1, st_sodelujocih+1)])
    return sodelujoci - (radi_caj | radi_kakav | radi_kavo)






































































































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
        ] = "eyJwYXJ0Ijo0Mjg1NSwidXNlciI6OTc4NH0:1tru0j:RB5aQGZDMF4g5flCbFk1CtYE62CauIuJqhvSJ2On7bU"
        try:
            testi = [
                ({1, 2, 3, 6}, {2, 3, 4, 7}, {3, 5, 6, 7}, {3}),    # 1. oseba 3 ima rada vse
                (set(), {2, 3, 4}, {3, 5, 6}, set()),               # 2. ena množica je prazna - nihče nima rad vseh treh
                ({1, 2, 3}, {1, 2, 3}, {1, 2, 3}, {1, 2, 3}),       # 3. vse množice so enake - vsi imajo radi vse pijače
                ({1, 2}, {3, 4}, {5, 6}, set()),                    # 4. ni prekrivanja - nihče nima rad vseh treh
                ({1, 2, 3, 4}, {1, 2, 5, 6}, {1, 2, 7, 8}, {1, 2}), # 5. 1 in dva imata rada vse, ostali pa le po eno
                ({1, 2, 3, 4, 9}, {2, 3, 5, 6, 10}, {3, 4, 6, 7, 11}, {3}), # 6.
                (set(), set(), set(), set()),                               # 7. ni anketirancev
                (set(), set(), {1, 2, 3, 4}, set()),                        # 8. vsi pijejo kakav
            ]
            
            for kava, caj, kakav, pricakovano in testi:
                if not Check.equal(f'pijejo_vse({kava}, {caj}, {kakav})', pricakovano):
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
        ] = "eyJwYXJ0Ijo0Mjg1NiwidXNlciI6OTc4NH0:1tru0j:1pGLeCvuHnjk8_OqswWTMNb26nOQPKDqGv4WZira4NQ"
        try:
            testi = [
                ({1, 2, 3, 6}, {2, 3, 4, 7}, {3, 5, 6, 7}, {1, 2, 3, 4, 5, 6, 7}),    # 1. oseba 3 ima rada vse
                (set(), {2, 3, 4}, {3, 5, 6}, {2, 3, 4, 5, 6}),             # 2. ena množica je prazna - nihče nima rad vseh treh
                ({1, 2, 3}, {1, 2, 3}, {1, 2, 3}, {1, 2, 3}),               # 3. vse množice so enake - vsi imajo radi vse pijače
                ({1, 2}, {3, 4}, {5, 6}, {1, 2, 3, 4, 5, 6}),               # 4. ni prekrivanja - nihče nima rad vseh treh
                ({1, 2, 3, 4}, {1, 2, 5, 6}, {1, 2, 7, 8}, {1, 2, 3, 4, 5, 6, 7, 8}), # 5. 1 in dva imata rada vse, ostali pa le po eno
                ({1, 2, 3, 4, 9}, {2, 3, 5, 6, 10}, {3, 4, 6, 7, 11}, {1, 2, 3, 4, 5, 6, 7, 9, 10, 11}), # 6.
                (set(), set(), set(), set()),                               # 7. ni anketirancev
                (set(), set(), {1, 2, 3, 4}, {1, 2, 3, 4}),                 # 8. vsi pijejo kakav
            ]
            
            for kava, caj, kakav, pricakovano in testi:
                if not Check.equal(f'vsi_anketiranci({kava}, {caj}, {kakav})', pricakovano):
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
        ] = "eyJwYXJ0Ijo0Mjg1NywidXNlciI6OTc4NH0:1tru0j:1b19MgQfM3mQC5lfIEZj3EimcNH28_GD8QNUsZ-TDMo"
        try:
            testi = [
                ({1, 2, 3, 6}, {2, 3, 4, 7}, {3, 5, 6, 7}, {6, 7}),    # 1. oseba 3 ima rada vse
                (set(), {2, 3, 4}, {3, 5, 6}, {3}),                    # 2. ena množica je prazna - nihče nima rad vseh treh
                ({1, 2, 3}, {1, 2, 3}, {1, 2, 3}, set()),              # 3. vse množice so enake - vsi imajo radi vse pijače
                ({1, 2}, {3, 4}, {5, 6}, set()),                       # 4. ni prekrivanja - nihče nima rad vseh treh
                ({1, 2, 3, 4}, {1, 2, 5, 6}, {1, 2, 7, 8}, set()),     # 5. 1 in dva imata rada vse, ostali pa le po eno
                ({1, 2, 3, 4, 9}, {2, 3, 5, 6, 10}, {3, 4, 6, 7, 9, 10}, {4, 6, 9, 10}), # 6.
                (set(), set(), set(), set()),                               # 7. ni anketirancev
                (set(), set(), {1, 2, 3, 4}, set()),                 # 8. vsi pijejo kakav
                ({1, 2}, {3, 4}, {1, 2, 3, 4}, {1, 2, 3, 4}),                 # 8. vsi pijejo kakav
            ]
            
            for kava, caj, kakav, pricakovano in testi:
                if not Check.equal(f'nekaj_s_kakavom({kava}, {caj}, {kakav})', pricakovano):
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
        ] = "eyJwYXJ0Ijo0Mjg1OCwidXNlciI6OTc4NH0:1tru0j:6k4TO_1pIK-xd5-eipFA1W5JEkBIkImJjUyKiblBtwU"
        try:
            testi = [
                ({1, 2, 3, 6}, {2, 3, 4, 7}, {3, 5, 6, 7}, 7, set()),  # 1. vsi pijejo tople napitke
                (set(), set(), set(), 10, set(range(1, 11))),          # 2. vsi pijejo hladne napitke
                ({1, 2, 3}, {1, 2, 3}, {1, 2, 3}, 4, {4}),             # 3. le zadnji ne pije toplih napitkov
                ({1}, {3}, {2}, 3, set()),                             # 4.
                ({1, 6, 9, 7, 2}, {9, 1, 6, 8}, {1, 6, 2, 9}, 10, {3, 4, 5, 10}), # 5.
            ]
            
            for kava, caj, kakav, n, pricakovano in testi:
                if not Check.equal(f'hladni({kava}, {caj}, {kakav}, {n})', pricakovano):
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
