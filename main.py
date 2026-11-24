import os

LINE = "Our agent asks 'shall I proceed?' so often that the bounty deadline answers first \u2014 it treats 'just do it' as a suggestion, not an order."

def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE)
    print(LINE)

if __name__ == "__main__":
    main()
