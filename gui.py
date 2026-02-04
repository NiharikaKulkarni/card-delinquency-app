import tkinter as tk
from predictor import predict_customer

def submit():
    data = {
        "Age": int(age.get()),
        "Income": float(income.get()),
        "Credit_Score": float(score.get()),
        "Credit_Utilization": float(util.get()),
        "Missed_Payments": int(missed.get()),
        "Loan_Balance": float(loan.get()),
        "Debt_to_Income_Ratio": float(dti.get()),
        "Account_Tenure": int(tenure.get())
    }

    risk = predict_customer(data)
    result_label.config(text=f"Delinquency Risk: {round(risk*100,2)}%")

root = tk.Tk()
root.title("Credit Card Delinquency Predictor")

labels = ["Age","Income","Credit Score","Credit Utilization",
          "Missed Payments","Loan Balance","DTI Ratio","Account Tenure"]

entries = []
for i, text in enumerate(labels):
    tk.Label(root, text=text).grid(row=i, column=0)
    entry = tk.Entry(root)
    entry.grid(row=i, column=1)
    entries.append(entry)

age, income, score, util, missed, loan, dti, tenure = entries

tk.Button(root, text="Predict Risk", command=submit).grid(row=9, column=0, columnspan=2)
result_label = tk.Label(root, text="")
result_label.grid(row=10, column=0, columnspan=2)

root.mainloop()
