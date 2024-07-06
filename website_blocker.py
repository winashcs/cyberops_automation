hosts_file_path = r"C:\Windows\System32\Drivers\etc\hosts"

def block_website(website):
    # Open hosts file in read mode first
    with open(hosts_file_path, 'r') as f:
        content = f.read()

    # Check if the website is already blocked
    if any(website in line for line in content.splitlines()):
        print(f"{website} is already blocked.")
    else:
        # Open hosts file in append mode to add new entries
        with open(hosts_file_path, 'a') as f:
            f.write(f"127.0.0.1 {website}\n")
        print(f"{website} has been blocked successfully.")

def list_blocked_websites():
    # Open hosts file and read each line to find blocked websites
    with open(hosts_file_path, 'r') as f:
        content = f.readlines()

    blocked_websites = []
    for line in content:
        if line.strip().startswith('127.0.0.1'):
            blocked_websites.append(line.strip().split()[1])

    if blocked_websites:
        print("Currently blocked websites:")
        for website in blocked_websites:
            print(website)
    else:
        print("No websites are currently blocked.")

def unblock_website(website):
    # Open hosts file in read mode first
    with open(hosts_file_path, 'r') as f:
        lines = f.readlines()

    # Rewrite hosts file without the website to unblock
    with open(hosts_file_path, 'w') as f:
        for line in lines:
            if not line.strip().startswith('127.0.0.1 ' + website):
                f.write(line)
    
    print(f"{website} has been unblocked successfully.")

# Main loop to interact with user
while True:
    print("\nWhat would you like to do?")
    print("1. Block a website")
    print("2. List currently blocked websites")
    print("3. Unblock a website")
    print("4. Exit")

    choice = input("Enter your choice (1/2/3/4): ")

    if choice == '1':
        website_to_block = input("Enter the website you want to block (e.g., example.com): ")
        block_website(website_to_block)
    
    elif choice == '2':
        list_blocked_websites()
    
    elif choice == '3':
        website_to_unblock = input("Enter the website you want to unblock: ")
        unblock_website(website_to_unblock)
    
    elif choice == '4':
        print("Exiting program.")
        break
    
    else:
        print("Invalid choice. Please enter 1, 2, 3, or 4.")
