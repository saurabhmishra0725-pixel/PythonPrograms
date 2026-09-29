import importlib.util
import pathlib

CODE_DIR = pathlib.Path(__file__).resolve().parent.parent / "Code"
spec = importlib.util.spec_from_file_location("prog", CODE_DIR / "04_factorial.py")
prog = importlib.util.module_from_spec(spec)
spec.loader.exec_module(prog)

def test_04_factorial():
    assert prog.factorial(0) == 1
    assert prog.factorial(1) == 1
    assert prog.factorial(2) == 2
    assert prog.factorial(3) == 6
    assert prog.factorial(5) == 120
    assert prog.factorial(10) == 3628800

    try:
        prog.factorial(-1)
    except ValueError:
        pass
    else:
        raise AssertionError("factorial(-1) should raise ValueError")



if __name__ == "__main__":
    test_04_factorial()
    print("All test cases passed.")
