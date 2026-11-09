import argparse
from core.pipeline import generate

def main():
    parser = argparse.ArgumentParser(description="SHORTS.AI Studio")
    parser.add_argument("--topic", required=True, help="Shorts topic")
    args = parser.parse_args()

    folder = generate(args.topic)
    print("\nSHORTS.AI — Session created")
    print(f"Topic: {args.topic}")
    print(f"Output: {folder}")
    print(f"Prompt: {folder / 'script_prompt.md'}")
    print("\nNext: Open the prompt in Claude Free and request the script.")

if __name__ == "__main__":
    main()
