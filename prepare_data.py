from pathlib import Path


def main():
    out_dir = Path("data_div")
    out_dir.mkdir(parents=True, exist_ok=True)

    pairs = []
    for a in range(90):
        for b in range(1, 10):
            q = a // b
            r = a % b
            pairs.append(f"{a}/{b}=Q{q}R{r}")

    with open(out_dir / "train.txt", "w", encoding="utf-8") as f:
        for p in pairs:
            f.write(p + "\n")

    with open(out_dir / "val.txt", "w", encoding="utf-8") as f:
        for p in pairs:
            f.write(p + "\n")

    print(f"Div generated: {len(pairs)} lines")


if __name__ == "__main__":
    main()
