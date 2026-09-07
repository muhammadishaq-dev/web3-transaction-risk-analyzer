
def calculate_risk_score(transaction):
    score = 0

    if transaction["amount"] > 10000:
        score += 30

    if transaction["failed_attempts"] >= 3:
        score += 25

    if transaction["new_wallet"]:
        score += 20

    if transaction["high_risk_country"]:
        score += 25

    return min(score, 100)


def risk_level(score):
    if score >= 70:
        return "HIGH"
    elif score >= 40:
        return "MEDIUM"
    return "LOW"
