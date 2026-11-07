
import pandas as pd

def run_quality_checks(df):

    checks = {
        "No duplicate records": not df.duplicated().any(),

        "No missing Customer IDs":
            df["Customer ID"].notna().all(),

        "No cancelled invoices":
            not df["Invoice"].astype(str).str.startswith("C").any(),

        "All quantities are positive":
            (df["Quantity"] > 0).all(),

        "All prices are positive":
            (df["Price"] > 0).all()
    }

    print("DATA QUALITY CHECK RESULTS")

    for name, result in checks.items():
        print(name, ":", "PASS" if result else "FAIL")

    return checks
