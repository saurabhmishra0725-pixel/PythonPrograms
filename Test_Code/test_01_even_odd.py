import importlib.util
import pathlib

CODE_DIR = pathlib.Path(__file__).resolve().parent.parent / "Code"
spec = importlib.util.spec_from_file_location("prog", CODE_DIR / "01_even_odd.py")
prog = importlib.util.module_from_spec(spec)
spec.loader.exec_module(prog)

def test_01_even_odd():
    assert prog.check_even_odd(0) == "Even"
    assert prog.check_even_odd(2) == "Even"
    assert prog.check_even_odd(4) == "Even"
    assert prog.check_even_odd(1) == "Odd"
    assert prog.check_even_odd(7) == "Odd"
    assert prog.check_even_odd(-3) == "Odd"
    assert prog.check_even_odd(-10) == "Even"



if __name__ == "__main__":
    test_01_even_odd()
    print("All test cases passed.")
