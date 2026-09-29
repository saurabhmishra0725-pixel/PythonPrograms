import importlib.util
import pathlib

CODE_DIR = pathlib.Path(__file__).resolve().parent.parent / "Code"
spec = importlib.util.spec_from_file_location("prog", CODE_DIR / "19_find_duplicates.py")
prog = importlib.util.module_from_spec(spec)
spec.loader.exec_module(prog)

assert prog.find_duplicates([]) == []
assert prog.find_duplicates([1, 2, 3]) == []
assert prog.find_duplicates([1, 1]) == [1]
assert prog.find_duplicates([1, 2, 3, 2, 4, 1]) == [1, 2]
assert prog.find_duplicates([3, 3, 3]) == [3]
assert prog.find_duplicates(["a", "b", "a", "c", "b"]) == ["a", "b"]
assert prog.find_duplicates([1, 2, 3, 4, 5]) == []

print("All test cases passed.")
