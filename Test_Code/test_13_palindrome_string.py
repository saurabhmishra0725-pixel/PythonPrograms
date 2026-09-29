import importlib.util
import pathlib

CODE_DIR = pathlib.Path(__file__).resolve().parent.parent / "Code"
spec = importlib.util.spec_from_file_location("prog", CODE_DIR / "13_palindrome_string.py")
prog = importlib.util.module_from_spec(spec)
spec.loader.exec_module(prog)

assert prog.is_palindrome_string("") is True
assert prog.is_palindrome_string("a") is True
assert prog.is_palindrome_string("madam") is True
assert prog.is_palindrome_string("Madam") is True
assert prog.is_palindrome_string("racecar") is True
assert prog.is_palindrome_string("hello") is False
assert prog.is_palindrome_string("A man, a plan, a canal: Panama") is True
assert prog.is_palindrome_string("Was it a car or a cat I saw?") is True
assert prog.is_palindrome_string("Python") is False

print("All test cases passed.")
