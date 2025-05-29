# =============================================================================
# Delnice
#
# V datoteki imamo zapisane podatke o vrednosti neke delnice. V vsaki
# vrstici je zapisan podatek v obliki
# 
#     YYYY-MM-DD,vrednost
# 
# kjer je prvi podatek dan, drugi pa vrednost delnice na ta dan.
# =====================================================================@040829=
# 1. podnaloga
# Sestavite funkcijo `preberi(ime_datoteke)`, ki kot parameter sprejme
# ime datoteke, vrne par nabor dveh seznamov, v prvem naj bodo datumi
# (kot nizi), v drugem pa vrednosti delnice (kot realna števila).
# =============================================================================

# =====================================================================@040830=
# 2. podnaloga
# Logaritemski povratek delnice je definiran kot logaritem kvocienta
# vrednosti delnice za dva zaporedna dneva trgovanja:
# 
# $$\log{\frac{x_i}{x_{i-1}}}$$
# 
# [Zakaj je to uporabno](https://quantivity.wordpress.com/2011/02/21/why-log-returns/)
# Sestavite funkcijo
# `povratek(ime_dat)`, ki kot parameter sprejme ime datoteke z vrednostmi delnice.
# in vrne seznam logaritemskih povratkov. Če je
# podana datoteka prazna ali pa vsebuje le en podatek, naj funkcija vrne prazen
# seznam.
# =============================================================================

# =====================================================================@040831=
# 3. podnaloga
# Iz logaritemskih povratkov lahko razberemo, ali je vrednost delnice
# naraščala ali padala. Sestavite funkcijo `trend(povratki)`, ki sprejme
# seznam logaritemskih povratkov in vrne niz `pozitiven trend`, če je
# v seznamu več pozitivnih vrednosti kot negativnih, sicer pa naj vrne
# `negativen trend`. Vrednosti 0 štejte k negativnim.
# =============================================================================

# =====================================================================@040832=
# 4. podnaloga
# [Letna volatilnost](http://www.skladi.com/nasveti/4457-kapitalski-trgi-in-visja-volatilnost-kaksno-je-sporocilo)
# delnice (Volatilnost ali nihajnost označuje, koliko je statistično verjetno, da 
# cena delnice v kratkem času močneje zraste ali pade)
# je definirana kot večkratnik standardnega
# odklona logaritemskega povratka:
# $$\sigma^2 = \frac{252}{n}\sum_{i=1}^n (x_i-\mu)^2,$$
# kjer je $\mu$ povprečna vrednost logaritemskih povratkov, $x_i$ so posamezni logaritemski
# povratki, $n$ je število logaritemskih povratkov, 252 pa predstavlja
# število trgovalnih dni v letu.
# Sestavite funkcijo `volatilnost(ime_datoteke)`, ki iz datoteke prebere
# vrednosti delnice in vrne njeno letno volatilnost $\sigma$.
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
        ] = "eyJwYXJ0Ijo0MDgyOSwidXNlciI6OTc4NH0:1uI5xz:itr7Lomxylr93DGW_QNvdzSporyV7EzPSLzlPn4Dlq4"
        try:
            _d = """2012-01-01,53.05
            2012-01-02,54.08
            2012-01-03,58.38
            2012-01-04,62.42"""
            with open("_test.1","w") as _f:
                _f.write(_d)
            
            Check.equal("preberi('_test.1')",(['2012-01-01', '2012-01-02', '2012-01-03', '2012-01-04'], [53.05, 54.08, 58.38, 62.42]))
            
            _rng=[1287631]
            for i in range(100): _rng.append((_rng[-1]*1103515245+12345)%2**32)
            _m = max(_rng)/10
            _rng = [x/_m-5 for x in _rng[1:]]
            _v = 50+_rng.pop(0)%30
            with open("_test.2","w") as _f:
                for _i in range(len(_rng)):
                    _v+=_rng[_i]
                    print("2012-{0:02d}-{1:02d},{2:.2f}".format(1+_i//20, 1+_i%20,_v),file=_f)
            
            Check.equal("preberi('_test.2')", (['2012-01-01', '2012-01-02', '2012-01-03', '2012-01-04', '2012-01-05', '2012-01-06', '2012-01-07', '2012-01-08', '2012-01-09', '2012-01-10', '2012-01-11', '2012-01-12', '2012-01-13', '2012-01-14', '2012-01-15', '2012-01-16', '2012-01-17', '2012-01-18', '2012-01-19', '2012-01-20', '2012-02-01', '2012-02-02', '2012-02-03', '2012-02-04', '2012-02-05', '2012-02-06', '2012-02-07', '2012-02-08', '2012-02-09', '2012-02-10', '2012-02-11', '2012-02-12', '2012-02-13', '2012-02-14', '2012-02-15', '2012-02-16', '2012-02-17', '2012-02-18', '2012-02-19', '2012-02-20', '2012-03-01', '2012-03-02', '2012-03-03', '2012-03-04', '2012-03-05', '2012-03-06', '2012-03-07', '2012-03-08', '2012-03-09', '2012-03-10', '2012-03-11', '2012-03-12', '2012-03-13', '2012-03-14', '2012-03-15', '2012-03-16', '2012-03-17', '2012-03-18', '2012-03-19', '2012-03-20', '2012-04-01', '2012-04-02', '2012-04-03', '2012-04-04', '2012-04-05', '2012-04-06', '2012-04-07', '2012-04-08', '2012-04-09', '2012-04-10', '2012-04-11', '2012-04-12', '2012-04-13', '2012-04-14', '2012-04-15', '2012-04-16', '2012-04-17', '2012-04-18', '2012-04-19', '2012-04-20', '2012-05-01', '2012-05-02', '2012-05-03', '2012-05-04', '2012-05-05', '2012-05-06', '2012-05-07', '2012-05-08', '2012-05-09', '2012-05-10', '2012-05-11', '2012-05-12', '2012-05-13', '2012-05-14', '2012-05-15', '2012-05-16', '2012-05-17', '2012-05-18', '2012-05-19'], [53.05, 54.08, 58.38, 62.42, 63.64, 61.43, 60.92, 64.92, 67.73, 65.09, 68.8, 69.78, 68.79, 67.98, 66.42, 68.02, 67.08, 68.88, 71.05, 72.31, 70.51, 74.97, 78.53, 75.47, 74.07, 71.59, 69.11, 65.96, 64.95, 59.96, 56.5, 54.83, 55.75, 54.35, 52.7, 56.53, 52.56, 54.86, 53.92, 55.02, 52.33, 55.17, 52.92, 55.46, 58.66, 57.15, 52.9, 57.26, 60.05, 57.19, 59.24, 54.91, 51.8, 52.95, 55.95, 60.42, 57.11, 62.04, 65.35, 68.02, 68.18, 66.19, 66.97, 62.33, 66.16, 70.6, 67.27, 67.71, 72.25, 77.25, 77.35, 73.46, 76.94, 77.12, 79.23, 81.55, 83.94, 88.79, 92.75, 97.32, 96.55, 91.92, 91.67, 94.25, 92.66, 91.46, 94.26, 92.6, 90.0, 86.66, 87.45, 86.06, 86.35, 85.89, 90.73, 94.15, 99.03, 99.38, 101.15]))
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
        ] = "eyJwYXJ0Ijo0MDgzMCwidXNlciI6OTc4NH0:1uI5xz:WDmUncqT19SrfnAty_GR8HBGDmud6n7J_BW5mQw4G28"
        try:
            _d = """2012-01-01,53.05
            2012-01-02,54.08
            2012-01-03,58.38
            2012-01-04,62.42"""
            with open("_test.1","w") as _f:
                _f.write(_d)
            Check.equal("povratek('_test.1')", [0.01922956667471659, 0.07650893369126009, 0.0669123714166646])
            
            _rng=[1287631]
            for i in range(100): _rng.append((_rng[-1]*1103515245+12345)%2**32)
            _m = max(_rng)/10
            _rng = [x/_m-5 for x in _rng[1:]]
            _v = 50+_rng.pop(0)%30
            with open("_test.2","w") as _f:
                for _i in range(len(_rng)):
                    _v+=_rng[_i]
                    print("2012-{0:02d}-{1:02d},{2:.2f}".format(1+_i//20, 1+_i%20,_v),file=_f)
            Check.equal("povratek('_test.2')", [0.01922956667471659, 0.07650893369126009, 0.0669123714166646, 0.019356466626952767, -0.0353438882937501, -0.008336787148874945, 0.06359421461942938, 0.04237347058042183, -0.039758285642516336, 0.05543281735500186, 0.014143690819330127, -0.014289050220705198, -0.011844841269952826, -0.0232153283193695, 0.02380356363044882, -0.013915842624041242, 0.02647992316446732, 0.031017994423634274, 0.017578577643750905, -0.025207888455911237, 0.061333489784021304, 0.04639268387181249, -0.03974549109000627, -0.018724634271579294, -0.03405519261710402, -0.03525596130479071, -0.046650940411904866, -0.01543075457478944, -0.07994006988221165, -0.05943703508200176, -0.030003148736438202, 0.016639920924271127, -0.025432796773009695, -0.030829158019901833, 0.07015601513988286, -0.07281609651084439, 0.04282911133310214, -0.017283018905405498, 0.02019528889237691, -0.050126935112312074, 0.05284950690022301, -0.041637988037584464, 0.04688070094087708, 0.05609602336167283, -0.026078673308485303, -0.07727605137656593, 0.07919896080571528, 0.047575248856023475, -0.04879849059876769, 0.03521793147237324, -0.07590150810881682, -0.0583053320253439, 0.0219579227819781, 0.05511036271051867, 0.07686174120059165, -0.05634094328175442, 0.08280010563156656, 0.051978101761892756, 0.040044339508818486, 0.0023494871307078004, -0.02962187257892575, 0.01171536379112738, -0.07180190710119957, 0.05963319989467659, 0.06495409378376057, -0.048315772461681956, 0.006519507460039652, 0.06489844749498758, 0.06691458878531326, 0.0012936612412202692, -0.05159953662755392, 0.046284856932627946, 0.00233675297814127, 0.02699236467486038, 0.028861314089872192, 0.028885928838421854, 0.05617177313879077, 0.04363367044330912, 0.048096816427777175, -0.007943509040798376, -0.04914237533402315, -0.002723461566816037, 0.027755654354435888, -0.01701394633961787, -0.013035161758593193, 0.03015520326567577, -0.017767779843451202, -0.028479471321868573, -0.0378172540185017, 0.009074785152847738, -0.016022474054157465, 0.003364077182233955, -0.005341396814554202, 0.054820655403404216, 0.03700119192162388, 0.050533579430049894, 0.0035280516409630733, 0.017653677439580157])
            
            _d = """"""
            with open("_test.3","w") as _f:
                _f.write(_d)
            Check.equal("povratek('_test.3')", [])
            
            _d = """2012-01-01,53.05"""
            with open("_test.4","w") as _f:
                _f.write(_d)
            Check.equal("povratek('_test.4')", [])
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
        ] = "eyJwYXJ0Ijo0MDgzMSwidXNlciI6OTc4NH0:1uI5xz:lKJj_f3d94UtcSR_ijWdk6c505fE5SnFNjMylpM8oXg"
        try:
            Check.equal("trend([])", 'negativen trend')
            Check.equal("trend([1,-1,1,-1])", 'negativen trend')
            Check.equal("trend([1.0,-.3,.4,.2,1.0,-1.2])", 'pozitiven trend')
            Check.equal("trend([-1.0,.3,-.4,-.2,-1.0,-1.2])", 'negativen trend')
            
            _rng=[1287631]
            for i in range(500): _rng.append((_rng[-1]*1103515245+12345)%2**32)
            _m=max(_rng)/10
            _rng=[x/_m-5 for x in _rng[1:]]
            for i in range(50):
                Check.secret(trend(_rng[10*i:10*i+10]), _rng[10*i:10*i+10])
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
        ] = "eyJwYXJ0Ijo0MDgzMiwidXNlciI6OTc4NH0:1uI5xz:CRTmiV8k1vNBElzeshnag06zB1YpIg4kKOwrrbUcpC4"
        try:
            Check.equal("volatilnost('_test.1')", 0.397626399171653)
            Check.equal("volatilnost('_test.2')", 0.6798427907021705)
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
