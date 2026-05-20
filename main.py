# ===================================
# [Office Asset Management CRUD Program]
# ===================================
# Developed by. Valencia
# JCDS - [33]


# /************************************/

# /===== Data Model =====/
# Create your data model here
asset = [
    {"txn_id": 1, "emp_id": "A001", "emp_name": "Andi", "asset_name":"laptop", "status":"borrowed"},
    {"txn_id": 2, "emp_id": "A002", "emp_name": "Budi", "asset_name":"projector", "status":"borrowed"},
    {"txn_id": 3, "emp_id": "A003", "emp_name": "Caca", "asset_name":"laptop", "status":"requested"}
]


# /===== Feature Program =====/
# Create your feature program here


def main():
    print("\n===Office Asset Management Program===\n")
    print("1. View report")
    print("2. Add request")
    print("3. Update status")
    print("4. Delete request")
    print("5. Exit program\n")
    input_menu = input("Enter menu [1-5]: ")
    return input_menu

def read_all(data):
    print("\n===All Report===")
    print(f"{"Txn ID |":<10}{"Employee ID |":<10}{"Employee Name |":<10}{"Asset Name |":<10}{"Status":<10}")
    print("-" *60)
    for all in data:
        all_id = all["txn_id"]
        all_emp_id = all["emp_id"]
        all_emp_name = all["emp_name"]
        all_asset_name = all["asset_name"]
        all_status = all["status"]
        print(f"{all_id:<10}{all_emp_id:<15}{all_emp_name:<15}{all_asset_name:<10}{all_status:<10}")

def search(search_input, key):
    search_result = []
    for item in asset:
        keys = item[key]
        if search_input.lower() in keys.lower():
            search_result.append(item)
    read_all(search_result)

def add(new_txn_id, new_emp_id, new_emp_name, new_asset_name, new_status):
    added_data = {
        "txn_id": (new_txn_id+ 1),
        "emp_id": new_emp_id,
        "emp_name": new_emp_name.capitalize(),
        "asset_name": new_asset_name,
        "status": new_status
    }
    print(added_data)
    confirm = input("Confirm to add new request? [y/n]: ")
    if confirm == "y":
        asset.append(added_data)
        print("Request is successfully added.")
    else:
        print("Request is cancelled")
    read_all(asset)

def update(input_txn):
    for i in range(len(asset)):
        if i == input_txn - 1:
            print(asset[i])
            print(f"\nUpdate status of txn id {input_txn} from {asset[i]["status"]} to: ")
            print("1. Borrowed")
            print("2. Returned")
            change = input("Choose status: ")
            if change == "1":
                confirm = input("Confirm to update status? (y/n): ")
                if confirm == "y":
                    asset[i]["status"] = "borrowed"
                    print("Status updated to borrowed.")
                else:
                    print("Status is not updated.")
            elif change == "2" and asset[i]["status"] == "borrowed":
                confirm = input("Confirm to update status? (y/n): ")
                if confirm == "y":
                    asset[i]["status"] = "returned"
                    print("Status updated to returned.")
                else:
                    print("Status is not updated.")
            
            elif change == "2" and asset[i]["status"] != "borrowed":
                 print("Asset is not borrowed yet.")

            else:
                print("Input is not valid.")

def delete(del_txn):
    for i in range(len(asset)):
        if i == del_txn - 1:
            print(asset[i])
            confirm_del = input("Confirm to delete request? (y/n): ")
            if confirm_del == "y":
                asset.pop(i)
                print("The request has been successfully deleted.")
            else:
                print("Delete request is cancelled")
    

# /===== Main Program =====/
# Create your main program here

running = True
while running:
    input_menu = main()
    #view report
    if input_menu == "1":
        print("\n===View Report===")
        print("1. All report")
        print("2. Report based on status")
        print("3. Report based on asset name")
        print("4. Report based on employee id")
        print("5. Main menu\n")
        input_sub_menu = input("Enter menu [1-5]: ")
        
        #read all
        if input_sub_menu == "1":
           read_all(asset)

        #based on status
        elif input_sub_menu == "2":
            print("\nView report based on status: ")
            print("1. Requested")
            print("2. Borrowed")
            print("3. Returned")
            input_status_menu = input("choose status [1-3]: ")
            if input_status_menu == "1":
                search("requested", "status")
            elif input_status_menu == "2":
                search("borrowed", "status")
            elif input_status_menu == "3":
                search("returned", "status")
            else:
                print("\nInput is not valid!")
        
        # based on asset name
        elif input_sub_menu == "3":
            search_asset_name = input("Search asset name: ")
            search(search_asset_name, "asset_name")

        # based on employee id
        elif input_sub_menu == "4":
            search_emp_id = input("Search using employee id: ")
            search(search_emp_id, "emp_id")

        elif input_sub_menu == "5":
            continue

        else:
            print("Input is not valid !")

    #add request    
    elif input_menu == "2":
        print("===Add new request===")
        new_txn_id = asset[-1]["txn_id"]
        new_emp_id = input("Enter employee id: ")
        new_emp_name = input("Enter employee name: ")
        new_asset_name = input("Enter asset name: ")
        new_status = "requested"
        add(new_txn_id, new_emp_id, new_emp_name, new_asset_name, new_status)

    #update status
    elif input_menu == "3":
        print("===Update Asset Status==")
        read_all(asset)
        input_txn = int(input("Enter the txn id you want to update: "))
        update(input_txn)
        read_all(asset)

    #delete txn
    elif input_menu == "4":
        print("===Delete Request===")
        read_all(asset)
        del_txn = int(input("Enter the txn_id you want to delete: "))
        delete(del_txn)
        read_all(asset)

    elif input_menu == "5":
        running = False

    else:
        print("Input is not valid !")
        print("Please enter the right menu")
