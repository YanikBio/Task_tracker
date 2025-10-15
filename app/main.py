import sys
from app.task_manager import TaskManager

def main():
    if len(sys.argv) < 2:
        print("Usage ./task-cli <command> [arguments]")
        return
    
    task_managar = TaskManager()

    command = sys.argv[1]
    match command:
        case 'add':
            print(f'Add function {sys.argv[2]}')
            task_managar.add(sys.argv[2])

        case 'update':
            print('Udpate function')
        case 'delite':
            print('Delite function')
        case 'list':
            print('Show all lists function')


if __name__ == "__main__":
    main()