from pathlib import Path
from datetime import datetime
import re

ROOT = Path(__file__).resolve().parents[1]

def slugify(text):
    return re.sub(r"[^a-z0-9]+", "-", text.lower()).strip("-")[:60]

def create_session(topic):
    stamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    folder = ROOT / "output" / f"{stamp}_{slugify(topic)}"
    folder.mkdir(parents=True, exist_ok=False)
    return folder

def create_script_prompt(topic):
    return f"""# SHORTS.AI — Scriptwriting Request

Topic: {topic}

Create an original YouTube Shorts script.

Requirements:
- 30–60 seconds.
- Start with a compelling hook in the first 2 seconds.
- Use clear, natural spoken language.
- Build curiosity and maintain momentum.
- Use short sentences.
- End with a satisfying payoff.
- Avoid fabricated facts and misleading claims.
- Include a source/checking note for factual claims.

Output:
1. Three alternative hooks.
2. Full narration script.
3. Scene-by-scene visual suggestions.
4. Estimated duration.
5. Suggested title and description.
6. Fact-checking notes.

Do not claim the video is guaranteed to go viral.
"""

def generate(topic):
    folder = create_session(topic)
    prompt = create_script_prompt(topic)
    (folder / "script_prompt.md").write_text(prompt, encoding="utf-8")
    (folder / "session.json").write_text(
        __import__("json").dumps({
            "topic": topic,
            "status": "prompt_ready",
            "created_at": datetime.now().isoformat()
        }, indent=2), encoding="utf-8"
    )
    return folder
