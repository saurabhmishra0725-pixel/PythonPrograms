import importlib.util
import pathlib

CODE_DIR = pathlib.Path(__file__).resolve().parent.parent / "Code"
spec = importlib.util.spec_from_file_location("prog", CODE_DIR / "07_primes_in_range.py")
prog = importlib.util.module_from_spec(spec)
spec.loader.exec_module(prog)

assert prog.primes_in_range(1, 10) == [2, 3, 5, 7]
assert prog.primes_in_range(10, 1) == [2, 3, 5, 7]
assert prog.primes_in_range(20, 30) == [23, 29]
assert prog.primes_in_range(1, 2) == [2]
assert prog.primes_in_range(14, 16) == []
assert prog.primes_in_range(2, 20) == [2, 3, 5, 7, 11, 13, 17, 19]
assert prog.primes_in_range(-5, 5) == [2, 3, 5]

print("All test cases passed.")
