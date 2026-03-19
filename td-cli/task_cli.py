import sys

def main():
    #Check if arguments were passed
    
    if len(sys.argv) < 2:
        print("Usage: td-cli <command> [arguments]")
        return
    
    command = sys.argv[1]

    if command == "add":
        task_name = sys.argv[2]
        print(f"Adding task: {task_name}")
    elif command == "list":
        print("Listing all task....")
    else:
        print("Invalid Command")
    
if __name__ == "__main__":
    main()