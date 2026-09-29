import importlib.util
import pathlib

CODE_DIR = pathlib.Path(__file__).resolve().parent.parent / "Code"
spec = importlib.util.spec_from_file_location("prog", CODE_DIR / "02_largest_of_three.py")
prog = importlib.util.module_from_spec(spec)
spec.loader.exec_module(prog)

assert prog.largest_of_three(1, 2, 3) == 3
assert prog.largest_of_three(3, 2, 1) == 3
assert prog.largest_of_three(1, 3, 2) == 3
assert prog.largest_of_three(5, 5, 5) == 5
assert prog.largest_of_three(-1, -2, -3) == -1
assert prog.largest_of_three(-5, 0, 4) == 4
assert prog.largest_of_three(10, 9, 10) == 10

print("All test cases passed.")
