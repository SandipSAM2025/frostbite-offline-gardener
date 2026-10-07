import datetime
import requests
from frost_data import resolve_zone_data

def main():
    print("=" * 45)
    print("      FROSTBITE: OUTDOOR FIELD DISPATCH     ")
    print("=" * 45)

    today = datetime.datetime.now().strftime("%B %d")
    zone_input = input("Enter your Zone (e.g., 6, 7b, 8) [Default: 6]: ") or "6"
    zone_name, frost_info = resolve_zone_data(zone_input)

    prompt = f"""You are a master gardener. Today is {today}. The grower is in {zone_name}.
Frost guide: Last spring frost is around {frost_info['last_spring']}, first fall frost is around {frost_info['first_fall']}.

Generate an outdoor gardening checklist for right now.
Provide exactly:
- [ ] 2 crops to direct-sow or plant outside today
- [ ] 2 hands-on soil prep, pruning, or bed chores
- [ ] 1 maintenance or protection task

Format as plain markdown checkboxes [ ]. Max 60 words total. No introductory text."""

    print("\nAsking local AI model on your machine...")

    try:
        response = requests.post(
            "http://localhost:11434/api/generate",
            json={"model": "smollm2:1.7b", "prompt": prompt, "stream": False},
            timeout=60
        )
        tasks = response.json().get("response", "").strip()
    except Exception as e:
        tasks = f"Error communicating with Ollama: {e}"

    card = f"""
+---------------------------------------------+
| Date: {today:<12} | Region: {zone_name:<15} |
+---------------------------------------------+
{tasks}
+---------------------------------------------+
| Put down the screen and head outside!       |
+---------------------------------------------+
"""
    print(card)

    with open("garden_todo.txt", "w", encoding="utf-8") as f:
        f.write(card)
    print("Checklist saved to 'garden_todo.txt'.")

if __name__ == "__main__":
    main()
