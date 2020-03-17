from flask import Flask, jsonify, request, make_response
from Bank import Bank
from Savings import Savings
from Chequing import Chequing

app = Flask(__name__)

bank = Bank("BCIT bank")


@app.route("/bank/accounts", methods=["POST"])
def new_account():
    """add a new account in json format to the bank"""
    data = request.json
    print(data["acc_type"])
    try:
        if data["acc_type"] == "savings":
            acc_id = str(data["account_id"])
            savings = Savings(data["account_id"], data["fname"], data["lname"],
                              data["interest"], data["date_interest"], data["balance"],
                              data["transactions"])
            bank.add_account(savings)
            return make_response(f"Account created with id:{acc_id}", 200)

        if data["acc_type"] == "chequing":
            acc_id = str(data["account_id"])
            chequing = Chequing(data["account_id"], data["fname"], data["lname"],
                                data["fees"], data["rebate"], data["min_balance"],
                                data["balance"], data["transactions"])
            bank.add_account(chequing)
            return make_response(f"Account created with id:{acc_id}", 200)

    except ValueError as e:
        message = str(e)
        return make_response(message, 400)


@app.route("/bank/accounts/<int:account_id>", methods=["PUT"])
def update_account(account_id):
    """updates an account in the bank"""
    data = request.json
    account = bank.get_account_id(account_id)
    if not account:
        return make_response(f"Account with id: {account_id} doesn't exist", 400)

    if account.get_type() == "chequing":
        try:
            for key in data.keys():
                n = str(key)
                if key == "fname":
                    bank.update_chequing(account_id, fname=data[n])
                elif key == "lname":
                    bank.update_chequing(account_id, lname=data[n])
                elif key == "fees":
                    bank.update_chequing(account_id, fees=data[n])
                elif key == "rebate":
                    bank.update_chequing(account_id, rebate=data[n])
                elif key == "min_balance":
                    bank.update_chequing(account_id, min_balance=data[n])
                else:
                    raise ValueError(f"Invalid key {key}")
            return make_response("", 200)

        except ValueError as e:
            return make_response(str(e), 404)

    elif account.get_type() == "savings":
        try:
            for key in data.keys():
                n = str(key)
                if key == "fname":
                    bank.update_savings(account_id, fname=data[n])
                elif key == "lname":
                    bank.update_savings(account_id, lname=data[n])
                elif key == "interest":
                    bank.update_savings(account_id, interest=data[n])
                else:
                    raise ValueError("Can only change name and interest")
            return make_response("", 200)

        except ValueError as e:
            return make_response(str(e), 404)


@app.route("/bank/accounts/<int:account_id>", methods=["DELETE"])
def remove_account(account_id):
    """deletes an account"""
    try:
        bank.delete_account(account_id)
    except ValueError as e:
        return make_response(f"Account with id: {account_id} does not exist", 404)
    else:
        return make_response("", 200)


@app.route("/bank/accounts/<int:account_id>", methods=["GET"])
def get_account(account_id):
    """gets account information with associated id"""
    try:
        account = bank.get_account_id(account_id)
        if not account:
            raise ValueError(f"Account with id: {account_id} does not exist")
        return jsonify(account.to_dict())
    except ValueError as e:
        return make_response(str(e), 404)


@app.route("/bank/accounts/all", methods=["GET"])
def get_all_accounts():
    """gets all accounts in the bank"""
    accounts = []
    for account in bank.get_all():
        accounts.append(account.to_dict())
    return jsonify(accounts)


@app.route("/bank/accounts/all/<string:type>", methods=["GET"])
def accounts_by_type(type):
    """gets all accounts by type"""
    accounts = []
    try:
        for account in bank.get_all_by_type(type):
            accounts.append(account.to_dict())
        return jsonify(accounts)
    except ValueError:
        return make_response(f"Type {type} is not supported by {bank.get_name()}", 400)


@app.route("/bank/accounts/stats", methods=["GET"])
def get_stats():
    """gets stats for the bank"""
    message = bank.get_stats()
    return make_response(jsonify(message.to_dict()), 200)


if __name__ == "__main__":
    app.run(debug=True)