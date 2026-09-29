import importlib.util
import pathlib

CODE_DIR = pathlib.Path(__file__).resolve().parent.parent / "Code"
spec = importlib.util.spec_from_file_location("prog", CODE_DIR / "20_word_frequency.py")
prog = importlib.util.module_from_spec(spec)
spec.loader.exec_module(prog)

def test_20_word_frequency():
    assert prog.word_frequency("") == {}
    assert prog.word_frequency("hello") == {"hello": 1}
    assert prog.word_frequency("a a a") == {"a": 3}
    assert prog.word_frequency("the cat and the dog") == {"the": 2, "cat": 1, "and": 1, "dog": 1}
    assert prog.word_frequency("Hello hello HELLO") == {"hello": 3}
    assert prog.word_frequency("one two two three three three") == {
        "one": 1,
        "two": 2,
        "three": 3,
    }
    assert prog.word_frequency("DevOps devops DEVOPS") == {"devops": 3}



if __name__ == "__main__":
    test_20_word_frequency()
    print("All test cases passed.")
