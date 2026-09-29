import importlib.util
import pathlib

CODE_DIR = pathlib.Path(__file__).resolve().parent.parent / "Code"
spec = importlib.util.spec_from_file_location("prog", CODE_DIR / "06_prime_number.py")
prog = importlib.util.module_from_spec(spec)
spec.loader.exec_module(prog)

assert prog.is_prime(0) is False
assert prog.is_prime(1) is False
assert prog.is_prime(2) is True
assert prog.is_prime(3) is True
assert prog.is_prime(4) is False
assert prog.is_prime(17) is True
assert prog.is_prime(18) is False
assert prog.is_prime(97) is True
assert prog.is_prime(100) is False
assert prog.is_prime(-7) is False

print("All test cases passed.")
