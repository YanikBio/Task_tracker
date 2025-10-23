import sys
from app.task_manager import TaskManager

def main():
    if len(sys.argv) < 2:
        print("Usage ./task-cli <command> [arguments]")
        return
    
    task_manager = TaskManager()

    command = sys.argv[1]
    match command:
        case 'add':
            print(f'Add function {sys.argv[2]}')
            task_manager.add(sys.argv[2])


        case 'update':
            if len(sys.argv) < 4:
                print("Usage ./task-cli <command> <taskID> [arguments]")
                return

            print(f"Update function {sys.argv[2]}")
            task_manager.update(int(sys.argv[2]), sys.argv[3])


        case 'delite':
            print('Delite function')
            task_manager.delite(int(sys.argv[2]))


        case 'mark-todo'|'mark-in-progress'|'mark-done':
            print("Change status function")
            task_manager.change_status(sys.argv[1], int(sys.argv[2]))


        case 'list':
            print(sys.argv[1])
            if len(sys.argv) == 2:
                print('Show all lists function')
                task_manager.show_list()
            if len(sys.argv) > 2:
                task_manager.show_list(sys.argv[2])


if __name__ == "__main__":
    main()