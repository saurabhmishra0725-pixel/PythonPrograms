import importlib.util
import pathlib

CODE_DIR = pathlib.Path(__file__).resolve().parent.parent / "Code"
spec = importlib.util.spec_from_file_location("prog", CODE_DIR / "14_char_frequency.py")
prog = importlib.util.module_from_spec(spec)
spec.loader.exec_module(prog)

def test_14_char_frequency():
    assert prog.char_frequency("") == {}
    assert prog.char_frequency("a") == {"a": 1}
    assert prog.char_frequency("abc") == {"a": 1, "b": 1, "c": 1}
    assert prog.char_frequency("hello") == {"h": 1, "e": 1, "l": 2, "o": 1}
    assert prog.char_frequency("banana") == {"b": 1, "a": 3, "n": 2}
    assert prog.char_frequency("aA") == {"a": 1, "A": 1}
    assert prog.char_frequency("112233") == {"1": 2, "2": 2, "3": 2}



if __name__ == "__main__":
    test_14_char_frequency()
    print("All test cases passed.")
