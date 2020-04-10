from flask import Flask, jsonify, request, make_response
from models.Bank import Bank
from models.Savings import Savings
from models.Chequing import Chequing

app = Flask(__name__)

bank = Bank("BCIT bank")


@app.route("/bank/savings", methods=["POST"])
def add_savings():
    """ Adds a savings, POST """
    data = request.json
    if not data:
        return make_response("No JSON. Check headers and JSON format.", 400)
    try:
        savings = Savings(first_name=data["fname"], last_name=data["lname"],
                          interest=data["interest"], date_interest=data["date_interest"])
        bank.add_account(savings)
        return make_response("Successful: Savings Account Added", 200)
    except ValueError as e:
        message = str(e)
        #return make_response(message, 400)
        return make_response("Error: Wrong parameters", 400)
    except KeyError as e:
        return make_response(f"Missing key: {e}", 400)


@app.route("/bank/chequings", methods=["POST"])
def add_chequings():
    """ Adds a chequing account, POST """
    data = request.json
    if not data:
        return make_response("No JSON. Check headers and JSON format.", 400)
    if data['rebate'] == 'False':
        rebate = 0
    else:
        rebate = 1
    try:
        chequing = Chequing(first_name=data["fname"], last_name=data["lname"], fees=data["fees"],
                            rebate=rebate, min_balance=data["min_balance"])
        bank.add_account(chequing)
        return make_response("Successful: Chequing Account Added", 200)
    except ValueError as e:
        message = str(e)
        return make_response(message, 400)
    except KeyError as e:
        return make_response(f"Missing key: {e}", 400)


@app.route("/bank/accounts/<int:account_id>", methods=["PUT"])
def update_account(account_id):
    data = request.json
    account = bank.get_account_id(account_id)
    try:
        if not account:
            return make_response(f"Account with id: {account_id} does not exist")
        elif isinstance(account, Chequing):
            bank.update_chequing(account, data)
            return make_response("Successful: Chequing Account Updated", 200)
        elif isinstance(account, Savings):
            bank.update_savings(account, data)
            return make_response("Successful: Savings Account Updated", 200)
        else:
            raise ValueError
    except ValueError as e:
        return make_response(str(e), 404)


@app.route("/bank/accounts/<int:account_id>", methods=["DELETE"])
def remove_account(account_id):
    try:
        bank.delete_account(account_id)
    except ValueError as e:
        return make_response(f"Account with id: {account_id} does not exist", 404)
    else:
        return make_response("Successful: Account removed", 200)


@app.route("/bank/accounts/<int:account_id>", methods=["GET"])
def get_account(account_id):
    try:
        account = bank.get_account_id(account_id)
        if not account:
            raise ValueError(f"Account with id: {account_id} does not exist")
        return jsonify(account.to_dict())
    except ValueError as e:
        return make_response(str(e), 404)


@app.route("/bank", methods=["GET"])
def get_all_accounts():
    accounts = []
    for account in bank.get_all():
        accounts.append(account.to_dict())
    return jsonify(accounts)


@app.route("/bank/accounts/all/<string:type>", methods=["GET"])
def accounts_by_type(type):
    accounts = []
    try:
        for account in bank.get_all_by_type(type):
            accounts.append(account.to_dict())
        return jsonify(accounts)
    except ValueError:
        return make_response(f"Type {type} is not supported by {bank.get_name()}")


@app.route("/bank/accounts/stats", methods=["GET"])
def get_stats():
    message = bank.get_stats()
    return make_response(jsonify(message.to_dict()), 200)


if __name__ == "__main__":
    app.run(debug=True)