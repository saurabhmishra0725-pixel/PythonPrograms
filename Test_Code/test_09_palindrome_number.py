import importlib.util
import pathlib

CODE_DIR = pathlib.Path(__file__).resolve().parent.parent / "Code"
spec = importlib.util.spec_from_file_location("prog", CODE_DIR / "09_palindrome_number.py")
prog = importlib.util.module_from_spec(spec)
spec.loader.exec_module(prog)

def test_09_palindrome_number():
    assert prog.is_palindrome_number(121) is True
    assert prog.is_palindrome_number(1221) is True
    assert prog.is_palindrome_number(12321) is True
    assert prog.is_palindrome_number(0) is True
    assert prog.is_palindrome_number(10) is False
    assert prog.is_palindrome_number(123) is False
    assert prog.is_palindrome_number(-121) is False



if __name__ == "__main__":
    test_09_palindrome_number()
    print("All test cases passed.")
