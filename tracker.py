# A simple dictionary of geopolitical alliances
alliances = {
    "BRICS": ["Brazil", "Russia", "India", "China", "South Africa", "Egypt", "Ethiopia", "Iran", "UAE"],
    "NATO": ["USA", "UK", "France", "Germany", "Turkey", "Canada", "and 26 others..."],
    "ASEAN": ["Indonesia", "Malaysia", "Philippines", "Singapore", "Thailand", "and 5 others..."]
}

print("🌍 Geopolitics Alliance Tracker 🌍\n")

for alliance, members in alliances.items():
    print(f"--- {alliance} ---")
    print(f"Key Members: {', '.join(members)}\n")
