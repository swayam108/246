from tkinter import *
from web3 import Web3#task1
root = Tk()

root.title("My Ethereum App")
root.geometry("600x200")
root.configure(background="white")

# Setting labels
block_name_label = Label(root, text="Ethereum gas fee in other currencies", font=("Helvetica", 18, 'bold'), bg="white")
block_name_label.place(relx=0.5, rely=0.15, anchor=CENTER)
# block_entry = Entry(root, text="This is Entry Widget", bd=2)
# #
# block_entry.place(relx=0.5, rely=0.35, anchor=CENTER)
value_in_ether = Label(root, bg="white", font=("bold", 14))
value_in_ether.place(relx=0.5, rely=0.28, anchor=CENTER)
value_in_dollar = Label(root, bg="white", font=("bold", 10))
value_in_dollar.place(relx=0.5, rely=0.48, anchor=CENTER)
value_in_rupees = Label(root, bg="white", font=("bold", 10))
value_in_rupees.place(relx=0.5, rely=0.58, anchor=CENTER)
value_in_pounds = Label(root, bg="white", font=("bold", 10))
value_in_pounds.place(relx=0.5, rely=0.68, anchor=CENTER)


url = 'https://mainnet.infura.io/v3/cded6e6690d04259b05137dd10b170c3'
web3 = Web3(Web3.HTTPProvider(url))
# main function
# Start code for Task 1 below
# ...

# main function
# Start code for Task 1 below
def ethereum_block():
    number = 18884784
    block_data = web3.eth.get_block(number)
    
    transactions = block_data['transactions']
    if transactions:
        transaction_hash = transactions[0]  # Assuming the first transaction in the block
        transaction = web3.eth.get_transaction(transaction_hash)
        
        value = transaction['value']
        value_in_ether_float = value / 10**18
        value_in_dollar_float = value_in_ether_float * 2399.82
        value_in_pounds_float = value_in_ether_float * 1871.73
        value_in_rupees_float = value_in_ether_float * 198022.15

        value_in_ether["text"] = "Value in ether: " + str(value_in_ether_float)
        value_in_dollar["text"] = "Value in dollar: " + str(value_in_dollar_float)
        value_in_pounds["text"] = "Value in pounds: " + str(value_in_pounds_float)
        value_in_rupees["text"] = "Value in rupees: " + str(value_in_rupees_float)

        search_btn.destroy()
    else:
        # Handle case when there are no transactions in the block
        print("No transactions in the block")

# ...

   



search_btn = Button(root, text="Search currency fee", command=ethereum_block, relief=FLAT)
search_btn.place(relx=0.5, rely=0.48, anchor=CENTER)
root.mainloop()