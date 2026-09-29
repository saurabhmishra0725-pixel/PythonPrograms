import importlib.util
import pathlib

CODE_DIR = pathlib.Path(__file__).resolve().parent.parent / "Code"
spec = importlib.util.spec_from_file_location("prog", CODE_DIR / "11_vowels_consonants.py")
prog = importlib.util.module_from_spec(spec)
spec.loader.exec_module(prog)

def test_11_vowels_consonants():
    assert prog.count_vowels_consonants("hello") == {"vowels": 2, "consonants": 3}
    assert prog.count_vowels_consonants("Python") == {"vowels": 1, "consonants": 5}
    assert prog.count_vowels_consonants("AEIOU") == {"vowels": 5, "consonants": 0}
    assert prog.count_vowels_consonants("bcdfg") == {"vowels": 0, "consonants": 5}
    assert prog.count_vowels_consonants("") == {"vowels": 0, "consonants": 0}
    assert prog.count_vowels_consonants("a1 b2!") == {"vowels": 1, "consonants": 1}
    assert prog.count_vowels_consonants("DevOps rocks") == {"vowels": 3, "consonants": 8}



if __name__ == "__main__":
    test_11_vowels_consonants()
    print("All test cases passed.")
