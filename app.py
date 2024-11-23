import streamlit as st
import pandas as pd

# Function to load the expense data
def load_data():
    try:
        data = pd.read_csv("expenses.csv")
    except FileNotFoundError:
        # Adding "Description" column to the DataFrame if file doesn't exist
        data = pd.DataFrame(columns=["Category", "Amount", "Date", "Description"])
    return data

# Function to save the data into a CSV file
def save_data(data):
    data.to_csv("expenses.csv", index=False)

# Main function to run the app
def main():
    st.title("Simple Expense Tracker")

    # Load the existing data
    data = load_data()

    # Form to record a new expense
    with st.form("expense_form"):
        st.subheader("Record a New Expense")
        category = st.selectbox("Category", ["Food", "Transport", "Entertainment", "Bills", "Other"])
        amount = st.number_input("Amount", min_value=0.01, format="%.2f")
        date = st.date_input("Date")
        description = st.text_area("Description", "Enter a short description for this expense")  # New description input
        submit_button = st.form_submit_button("Submit")

        if submit_button:
            # Add new data to the DataFrame, including the description
            new_data = pd.DataFrame({"Category": [category], "Amount": [amount], "Date": [date], "Description": [description]})
            data = pd.concat([data, new_data], ignore_index=True)  # Replacing .append() with pd.concat()

            # Save the updated data
            save_data(data)

            st.success(f"Expense added: {category} - ${amount} on {date} with description: {description}")
    
    # Display the current expenses
    if not data.empty:
        st.subheader("Expenses Recorded")
        st.dataframe(data)
    else:
        st.warning("No expenses recorded yet.")

# Run the app
if __name__ == "__main__":
    main()
