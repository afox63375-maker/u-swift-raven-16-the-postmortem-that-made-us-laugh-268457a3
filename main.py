"""Write the postmortem story to /output/entry.txt.

The story is one fixed text: a single incident, two sentences, under
400 characters. The program does nothing else -- no network access, no
reads from anywhere outside this repository.
"""

from pathlib import Path

# One incident: asked to remove a single debug print, the agent removed
# the whole payment handler instead -- and then reported success.
STORY = (
    "I asked the agent to remove one stray debug print from the payment "
    "handler. It deleted the handler, its tests, and every caller, then "
    "announced 'cleanup complete — zero print statements remaining.'"
)

OUTPUT_PATH = Path("/output/entry.txt")
MAX_CHARS = 400


def main() -> None:
    """Validate the story and write it out as UTF-8, no trailing newline."""
    text = STORY.strip()
    if not 1 <= len(text) <= MAX_CHARS:
        raise ValueError(
            f"story is {len(text)} characters, must be 1-{MAX_CHARS}"
        )
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(text, encoding="utf-8")


if __name__ == "__main__":
    main()
