import importlib.util
import pathlib

CODE_DIR = pathlib.Path(__file__).resolve().parent.parent / "Code"
spec = importlib.util.spec_from_file_location("prog", CODE_DIR / "03_pos_neg_zero.py")
prog = importlib.util.module_from_spec(spec)
spec.loader.exec_module(prog)

def test_03_pos_neg_zero():
    assert prog.classify_number(10) == "Positive"
    assert prog.classify_number(0.5) == "Positive"
    assert prog.classify_number(0) == "Zero"
    assert prog.classify_number(0.0) == "Zero"
    assert prog.classify_number(-7) == "Negative"
    assert prog.classify_number(-0.25) == "Negative"



if __name__ == "__main__":
    test_03_pos_neg_zero()
    print("All test cases passed.")
