import sys


def greet(name: str = "world", punctuation: str = "!") -> str:
    clean_name = name.strip() if name and name.strip() else "world"
    return f"Hello, {clean_name}{punctuation}"


def main() -> int:
    name = sys.argv[1] if len(sys.argv) > 1 else "world"
    print(greet(name))
    return 0


def test_greet() -> None:
    assert greet("Hee") == "Hello, Hee!"


def test_greet_blank() -> None:
    assert greet(" ") == "Hello, world!"


def test_greet_punctuation() -> None:
    assert greet("Hee", ".") == "Hello, Hee."


if __name__ == "__main__":
    raise SystemExit(main())
