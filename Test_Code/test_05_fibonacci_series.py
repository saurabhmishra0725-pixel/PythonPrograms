import importlib.util
import pathlib

CODE_DIR = pathlib.Path(__file__).resolve().parent.parent / "Code"
spec = importlib.util.spec_from_file_location("prog", CODE_DIR / "05_fibonacci_series.py")
prog = importlib.util.module_from_spec(spec)
spec.loader.exec_module(prog)

assert prog.fibonacci(0) == []
assert prog.fibonacci(1) == [0]
assert prog.fibonacci(2) == [0, 1]
assert prog.fibonacci(5) == [0, 1, 1, 2, 3]
assert prog.fibonacci(8) == [0, 1, 1, 2, 3, 5, 8, 13]
assert len(prog.fibonacci(10)) == 10

try:
    prog.fibonacci(-1)
except ValueError:
    pass
else:
    raise AssertionError("fibonacci(-1) should raise ValueError")

print("All test cases passed.")
