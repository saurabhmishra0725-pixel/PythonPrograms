import importlib.util
import pathlib

CODE_DIR = pathlib.Path(__file__).resolve().parent.parent / "Code"
spec = importlib.util.spec_from_file_location("prog", CODE_DIR / "18_missing_number.py")
prog = importlib.util.module_from_spec(spec)
spec.loader.exec_module(prog)

def test_18_missing_number():
    assert prog.missing_number([1, 2, 4, 5]) == 3
    assert prog.missing_number([2, 3, 4, 5]) == 1
    assert prog.missing_number([1, 2, 3, 4]) == 5
    assert prog.missing_number([1]) == 2
    assert prog.missing_number([1, 3]) == 2
    assert prog.missing_number([1, 2, 3, 5, 6]) == 4
    assert prog.missing_number([1, 2, 3, 4, 6, 7]) == 5



if __name__ == "__main__":
    test_18_missing_number()
    print("All test cases passed.")
