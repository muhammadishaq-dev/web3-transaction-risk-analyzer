import csv
from risk_analyzer import calculate_risk_score, risk_level


def load_transactions(file_path):
    with open(file_path, newline="") as file:
        return list(csv.DictReader(file))


transactions = load_transactions("data/transactions.csv")

for transaction in transactions:
    transaction["amount"] = float(transaction["amount"])
    transaction["failed_attempts"] = int(transaction["failed_attempts"])
    transaction["new_wallet"] = transaction["new_wallet"].lower() == "true"
    transaction["high_risk_country"] = (
        transaction["high_risk_country"].lower() == "true"
    )

    score = calculate_risk_score(transaction)

    print(
        f'{transaction["transaction_id"]}: '
        f'Risk Score = {score}, '
        f'Risk Level = {risk_level(score)}'
    )
