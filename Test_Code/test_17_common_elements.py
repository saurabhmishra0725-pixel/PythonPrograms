import importlib.util
import pathlib

CODE_DIR = pathlib.Path(__file__).resolve().parent.parent / "Code"
spec = importlib.util.spec_from_file_location("prog", CODE_DIR / "17_common_elements.py")
prog = importlib.util.module_from_spec(spec)
spec.loader.exec_module(prog)

def test_17_common_elements():
    assert prog.common_elements([], []) == []
    assert prog.common_elements([1, 2, 3], [4, 5, 6]) == []
    assert prog.common_elements([1, 2, 3], [2, 3, 4]) == [2, 3]
    assert prog.common_elements([1, 2, 2, 3], [2, 2, 4]) == [2]
    assert prog.common_elements(["a", "b", "c"], ["b", "c", "d"]) == ["b", "c"]
    assert prog.common_elements([1, 2, 3], [1, 2, 3]) == [1, 2, 3]
    assert prog.common_elements([3, 1, 2], [1, 2, 3]) == [3, 1, 2]



if __name__ == "__main__":
    test_17_common_elements()
    print("All test cases passed.")
