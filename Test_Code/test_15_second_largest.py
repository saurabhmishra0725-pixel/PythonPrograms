import importlib.util
import pathlib

CODE_DIR = pathlib.Path(__file__).resolve().parent.parent / "Code"
spec = importlib.util.spec_from_file_location("prog", CODE_DIR / "15_second_largest.py")
prog = importlib.util.module_from_spec(spec)
spec.loader.exec_module(prog)

assert prog.second_largest([1, 2, 3]) == 2
assert prog.second_largest([3, 1, 2]) == 2
assert prog.second_largest([10, 20, 30, 40]) == 30
assert prog.second_largest([5, 5, 5, 1]) == 1
assert prog.second_largest([-1, -2, -3]) == -2
assert prog.second_largest([1, 10, 10, 9]) == 9

try:
    prog.second_largest([7])
except ValueError:
    pass
else:
    raise AssertionError("second_largest([7]) should raise ValueError")

try:
    prog.second_largest([5, 5])
except ValueError:
    pass
else:
    raise AssertionError("second_largest([5, 5]) should raise ValueError")

print("All test cases passed.")
