"""Helpers for writing numbers into the text of the paper."""
import logging

_WORDS = ["zero", "one", "two", "three", "four", "five", "six", "seven",
          "eight", "nine"]


def number_text(n):
    """A count as it should read in prose: words up to nine, digits above."""
    n = int(n)
    return _WORDS[n] if 0 <= n < len(_WORDS) else str(n)


def count_macros(name, n):
    """LaTeX macros for a count used in the text.

    Returns ``{name: "three", name + "Cap": "Three"}`` (or digits for counts
    of ten and above). LaTeX cannot tell where a sentence starts, so the
    text uses ``\\<name>Cap`` at the start of a sentence and ``\\<name>``
    elsewhere.
    """
    text = number_text(n)
    logging.debug("Count %s = %s -> %r", name, n, text)
    return {name: text, name + "Cap": text[0].upper() + text[1:]}
