import importlib.util
import pathlib

CODE_DIR = pathlib.Path(__file__).resolve().parent.parent / "Code"
spec = importlib.util.spec_from_file_location("prog", CODE_DIR / "12_reverse_string.py")
prog = importlib.util.module_from_spec(spec)
spec.loader.exec_module(prog)

assert prog.reverse_string("") == ""
assert prog.reverse_string("a") == "a"
assert prog.reverse_string("abc") == "cba"
assert prog.reverse_string("hello") == "olleh"
assert prog.reverse_string("Python") == "nohtyP"
assert prog.reverse_string("123 456") == "654 321"
assert prog.reverse_string("madam") == "madam"

print("All test cases passed.")
