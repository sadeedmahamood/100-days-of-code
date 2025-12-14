from prettytable import PrettyTable

Table = PrettyTable()

Table.add_column("Roll_no",[1,2,3])
Table.add_column("Name",["saah","ishii","nandutty"])
Table.add_column("Place",["kallikandy","kannur","anjarakandy"])
Table.align = "r"
print(Table)