import importlib.util
import pathlib

CODE_DIR = pathlib.Path(__file__).resolve().parent.parent / "Code"
spec = importlib.util.spec_from_file_location("prog", CODE_DIR / "10_sum_of_digits.py")
prog = importlib.util.module_from_spec(spec)
spec.loader.exec_module(prog)

def test_10_sum_of_digits():
    assert prog.sum_of_digits(0) == 0
    assert prog.sum_of_digits(5) == 5
    assert prog.sum_of_digits(123) == 6
    assert prog.sum_of_digits(9999) == 36
    assert prog.sum_of_digits(1001) == 2
    assert prog.sum_of_digits(-456) == 15



if __name__ == "__main__":
    test_10_sum_of_digits()
    print("All test cases passed.")
