import importlib.util
import pathlib

CODE_DIR = pathlib.Path(__file__).resolve().parent.parent / "Code"
spec = importlib.util.spec_from_file_location("prog", CODE_DIR / "08_reverse_number.py")
prog = importlib.util.module_from_spec(spec)
spec.loader.exec_module(prog)

assert prog.reverse_number(1234) == 4321
assert prog.reverse_number(1000) == 1
assert prog.reverse_number(0) == 0
assert prog.reverse_number(7) == 7
assert prog.reverse_number(120) == 21
assert prog.reverse_number(-456) == -654
assert prog.reverse_number(123456789) == 987654321

print("All test cases passed.")
