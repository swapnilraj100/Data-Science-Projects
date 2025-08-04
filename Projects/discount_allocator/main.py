import json
from allocator import allocate_discounts

def main():
    with open("sample_input.json") as f:
        data = json.load(f)

    result = allocate_discounts(data["siteKitty"], data["salesAgents"])
    
    with open("sample_output.json", "w") as f:
        json.dump(result, f, indent=2)

    print("Discount allocation completed. Output saved to sample_output.json")

if __name__ == "__main__":
    main()
