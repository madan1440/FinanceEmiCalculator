from flask import Flask, render_template, request

app = Flask(__name__)


def compute_processing_amount(loan: float, pc_percent: float) -> float:
    """Processing charge as percentage of loan"""
    return loan * (pc_percent / 100.0)


def flat_rate_emi(
    loan: float,
    months: int,
    pc_percent: float,
    interest_type: str,
    interest_value: float
):
    """
    Flat-rate EMI calculation
    Processing charges added to principal before interest
    """

    # Processing charges
    processing_amount = compute_processing_amount(loan, pc_percent)

    # Adjusted principal
    adjusted_principal = loan + processing_amount

    # Interest calculation
    if interest_type == "percent":  # % per annum
        total_interest = adjusted_principal * (interest_value / 100.0) * (months / 12.0)
    else:  # ₹ per month
        total_interest = interest_value * months

    total_payable = adjusted_principal + total_interest
    emi = total_payable / months

    return {
        "processing_amount": round(processing_amount, 2),
        "adjusted_principal": round(adjusted_principal, 2),
        "total_interest": round(total_interest, 2),
        "total_payable": round(total_payable, 2),
        "emi": round(emi, 2),
    }


@app.route("/", methods=["GET", "POST"])
def index():
    # Default values
    data = {
        "loan": 20000,
        "months": 12,
        "pc_percent": 10,
        "interest_type": "percent",   # percent | rupees
        "interest_percent": 24,     # % per annum
        "interest_rupees": 2,        # ₹ per month
    }

    result = None
    error = None

    if request.method == "POST":
        try:
            loan = float(request.form.get("loan", data["loan"]))
            months = int(request.form.get("months", data["months"]))
            pc_percent = float(request.form.get("pc_percent", data["pc_percent"]))
            interest_type = request.form.get("interest_type", data["interest_type"])
            interest_percent = float(request.form.get("interest_percent", data["interest_percent"]))
            interest_rupees = float(request.form.get("interest_rupees", data["interest_rupees"]))

            # Safety checks
            loan = max(0.0, loan)
            months = max(1, months)
            pc_percent = max(0.0, pc_percent)
            interest_percent = max(0.0, interest_percent)
            interest_rupees = max(0.0, interest_rupees)

            interest_value = (
                interest_percent if interest_type == "percent" else interest_rupees
            )

            result = flat_rate_emi(
                loan,
                months,
                pc_percent,
                interest_type,
                interest_value,
            )

            data.update({
                "loan": loan,
                "months": months,
                "pc_percent": pc_percent,
                "interest_type": interest_type,
                "interest_percent": interest_percent,
                "interest_rupees": interest_rupees,
            })

        except Exception as ex:
            error = f"Invalid input: {ex}"

    return render_template("index.html", data=data, result=result, error=error)


if __name__ == "__main__":
    # app.run(host="0.0.0.0", port=8000, debug=True)
    app.run()
