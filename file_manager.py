import os
import shutil

def list_files(folder):
    print("\nFiles in directory:")
    for file in os.listdir(folder):
        print(file)

def move_file(source, destination):
    shutil.move(source, destination)
    print(f"Moved {source} to {destination}")

def rename_file(source, new_name):
    os.rename(source, new_name)
    print(f"Renamed {source} to {new_name}")

def delete_file(file_path):
    os.remove(file_path)
    print(f"Deleted {file_path}")

folder = input("Enter folder path: ")

while True:
    print("\nChoose an option:")
    print("1. List files\n2. Move file\n3. Rename file\n4. Delete file\n5. Exit")
    choice = input("Your choice: ")

    if choice == "1":
        list_files(folder)
    elif choice == "2":
        src = input("Enter source file path: ")
        dst = input("Enter destination path: ")
        move_file(src, dst)
    elif choice == "3":
        src = input("Enter current file path: ")
        new_name = input("Enter new name (with extension): ")
        rename_file(src, os.path.join(os.path.dirname(src), new_name))
    elif choice == "4":
        path = input("Enter file path to delete: ")
        delete_file(path)
    elif choice == "5":
        break
    else:
        print("Invalid choice.")
