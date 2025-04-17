def calculate_points(receipt):
    points = 0
    print("\n=== DEBUG: Received Receipt ===")
    print("Full receipt:", receipt)
    
    # Rule 1: Retailer name
    retailer = receipt.get('retailer', '')
    rule1 = sum(c.isalnum() for c in retailer)
    points += rule1
    print(f"Rule 1: Retailer '{retailer}' → {rule1} points (Total: {points})")
    
    # Rule 2: Round dollar
    try:
        total = float(receipt.get('total', '0.00'))
        if total % 1 == 0:
            points += 50
            print(f"Rule 2: Round dollar → +50 (Total: {points})")
    except ValueError as e:
        print(f"Rule 2 Error: {e}")
    
    # Rule 3: Multiple of 0.25
    try:
        if float(receipt.get('total', '0.00')) % 0.25 == 0:
            points += 25
            print(f"Rule 3: Multiple of 0.25 → +25 (Total: {points})")
    except ValueError as e:
        print(f"Rule 3 Error: {e}")
    
    # Continue with other rules...
    # (Add similar debug prints for all rules)
    
    print(f"=== Final Points: {points} ===")
    return points
