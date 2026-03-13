def extract_action_items(text: str) -> list[str]:
    lines = [line.strip("- ") for line in text.splitlines() if line.strip()]
    results: list[str] = []

    action_keywords = ["todo:", "action:", "please", "remember", "fix", "update", "send", "create"]

    for line in lines:
        normalized = line.lower()

        # Rule 1: explicit markers
        if normalized.startswith("todo:") or normalized.startswith("action:"):
            results.append(line)

        # Rule 2: strong punctuation
        elif line.endswith("!"):
            results.append(line)

        # Rule 3: action keywords
        elif any(normalized.startswith(keyword) for keyword in action_keywords):
            results.append(line)

    return results