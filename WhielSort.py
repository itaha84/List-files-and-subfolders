import os
import shutil
import datetime

given_folder = input("enter the full folder path: ")
folder_list = open("WHILESORT_Logs.txt", "a")
folder_remaining_list = open("WHILESORT_Original_Folder.txt", "a")
file_count = 0


#TODO CHECK THE BELOW FUN WHERE EMPTY FOLDER WON"T GET LISTED!!!

def processing_folder(file):
    global file_count
    folder_list.write(file + "\n")
    file_count += 1
    destination_folder = os.path.join(given_folder, datetime.date.strftime(datetime.date.fromtimestamp(os.path.getmtime(file)), "%d-%b-%Y"))
    try:
        os.mkdir(destination_folder)
        shutil.copy2(file, destination_folder)
    except FileExistsError:
        shutil.copy2(file, destination_folder)

    # folder_remaining_list.write(os.path.dirname(file) + "\n")  # EMPTY FOLDERS WON"T GET lISTED!!!!
    os.remove(file)


def initial_processing(folder1):
    folder_content = os.listdir(folder1)

    for i in folder_content:
        path = os.path.join(folder1, i)
        if os.path.isdir(path):
            folder_remaining_list.write(path + "\n")
            initial_processing(path)
        else:
            processing_folder(path)


initial_processing(given_folder)

folder_remaining_list.close()


def final_run():
    folder_deletion = open("WHILESORT_Original_Folder.txt", "r")
    for flines in folder_deletion:
        folder_n = (os.path.split(flines)[-1][:-1])
        folder_par = (os.path.split(flines))[0]
        folder2delete = os.path.join(folder_par, folder_n)
        print(folder2delete, folder2delete == given_folder)
        if folder2delete != given_folder:
            try:
                shutil.rmtree(folder2delete)
            except FileNotFoundError:
                pass






final_run()
