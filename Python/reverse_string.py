class Bank:
    def __init__(self):
        self.accounts = {}
        self.transaction_values = {}
        self.transfers = {}
        self.transfer_count = 0
 
    def create_account(self, account_id):
        if account_id in self.accounts:
            return "false"
        else:
            self.accounts[account_id] = 0
            self.transaction_values[account_id] = 0
            return "true"
 
    def deposit(self, account_id, amount):
        if account_id not in self.accounts:
            return ""
        self.accounts[account_id] += int(amount)
        self.transaction_values[account_id] += int(amount)
        return str(self.accounts[account_id])
 
    def pay(self, account_id, amount):
        if account_id not in self.accounts or self.accounts[account_id] < int(amount):
            return ""
        self.accounts[account_id] -= int(amount)
        self.transaction_values[account_id] += int(amount)
        return str(self.accounts[account_id])
 
    def top_activity(self, n):
        sorted_accounts = sorted(
            self.transaction_values.items(),
            key=lambda x: (-x[1], x[0])
        )
        top_accounts = sorted_accounts[:int(n)]
        result = ", ".join(f"{acc}({val})" for acc, val in top_accounts)
        return result
 
    def transfer(self, timestamp, source_account_id, target_account_id, amount):
        if source_account_id == target_account_id:
            return ""
        if source_account_id not in self.accounts or target_account_id not in self.accounts:
            return ""
        if self.accounts[source_account_id] < int(amount):
            return ""
        self.transfer_count += 1
        transfer_id = f"transfer{self.transfer_count}"
        self.transfers[transfer_id] = {
            "source": source_account_id,
            "target": target_account_id,
            "amount": int(amount),
            "timestamp": int(timestamp),
            "accepted": False
        }
        self.accounts[source_account_id] -= int(amount)
        return transfer_id
 
    def accept_transfer(self, timestamp, account_id, transfer_id):
        if transfer_id not in self.transfers:
            return "false"
        transfer = self.transfers[transfer_id]
        if transfer["accepted"]:
            return "false"
        if transfer["target"] != account_id:
            return "false"
        if int(timestamp) > transfer["timestamp"] + 86400000:
            self.accounts[transfer["source"]] += transfer["amount"]
            return "false"
        transfer["accepted"] = True
        self.accounts[account_id] += transfer["amount"]
        self.transaction_values[transfer["source"]] += transfer["amount"]
        self.transaction_values[transfer["target"]] += transfer["amount"]
        return "true"
 
def solution(queries):
    bank = Bank()
    results = []
    for query in queries:
        if query[0] == "CREATE_ACCOUNT":
            results.append(bank.create_account(query[2]))
        elif query[0] == "DEPOSIT":
            results.append(bank.deposit(query[2], query[3]))
        elif query[0] == "PAY":
            results.append(bank.pay(query[2], query[3]))
        elif query[0] == "TOP_ACTIVITY":
            results.append(bank.top_activity(query[2]))
        elif query[0] == "TRANSFER":
            results.append(bank.transfer(query[1], query[2], query[3], query[4]))
        elif query[0] == "ACCEPT_TRANSFER":
            results.append(bank.accept_transfer(query[1], query[2], query[3]))
    return results