import streamlit as st
import pandas as pd
from datetime import datetime

# Load or create the data file
DATA_FILE = "data.csv"

# Load existing data
def load_data():
    try:
    data = pd.DataFrame(columns=["column1", "column2"])  # Replace with your actual columns
    except FileNotFoundError:
data = pd.concat([data, pd.DataFrame([new_data])], ignore_index=True)
    return data

# Save data back to the file
def save_data(data):
    data.to_csv(DATA_FILE, index=False)

# Main app function
def main():
    st.write(type(data))
    st.write(new_data)
    option = st.write.write("Select an option:", ["Add Expense", "View Expenses"])

    # Add Expense Section
    if option == "Add Expense":
        st.header("Add a New Expense")
        date = st.date_input("Date", datetime.now().date())
        description = st.text_input("Description")
        category = st.selectbox("Category", ["Food", "Travel", "Shopping", "Bills", "Other"])
        amount = st.number_input("Amount", min_value=0.0, step=0.01)
        
        if st.button("Add Expense"):
            if description and amount > 0:
                new_data = {"Date": date, "Description": description, "Category": category, "Amount": amount}
                data = load_data()
                data = data.append(new_data, ignore_index=True)
                save_data(data)
                st.success("Expense added successfully!")
            else:
                st.error("Please fill out all fields.")

    # View Expenses Section
    elif option == "View Expenses":
        st.header("Expense List")
        data = load_data()
        
        if not data.empty:
            st.dataframe(data)
            total_expense = data["Amount"].sum()
            st.write(f"### Total Expense: ${total_expense:.2f}")
            
            if st.button("Download CSV"):
                st.download_button(
                    label="Download Expenses",
                    data=data.to_csv(index=False),
                    file_name="expenses.csv",
                    mime="text/csv",
                )
        else:
            st.warning("No expenses recorded yet.")

# Run the app
if __name__ == "__main__":
    main()
