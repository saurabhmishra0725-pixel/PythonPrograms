import importlib.util
import pathlib

CODE_DIR = pathlib.Path(__file__).resolve().parent.parent / "Code"
spec = importlib.util.spec_from_file_location("prog", CODE_DIR / "16_remove_duplicates.py")
prog = importlib.util.module_from_spec(spec)
spec.loader.exec_module(prog)

assert prog.remove_duplicates([]) == []
assert prog.remove_duplicates([1]) == [1]
assert prog.remove_duplicates([1, 1, 1]) == [1]
assert prog.remove_duplicates([1, 2, 3]) == [1, 2, 3]
assert prog.remove_duplicates([1, 2, 1, 3, 2]) == [1, 2, 3]
assert prog.remove_duplicates(["a", "b", "a"]) == ["a", "b"]
assert prog.remove_duplicates([3, 3, 2, 1, 2]) == [3, 2, 1]

print("All test cases passed.")
