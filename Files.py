import os

user_folder = input("Enter the full folder path: ")
base_folder = user_folder
file_cnt = 0
folder_cnt = 0


def the_great_processor(folder):
    global file1, file2, file_cnt, folder_cnt
    file1 = open("logfile_file.txt", "a")  # append mode
    file2 = open("logfile_folder.txt", "a")  # append mode
    items_in_folder = os.listdir(folder)
    for item in items_in_folder:
        item = os.path.join(folder, item)
        if os.path.isdir(item):
           folder_cnt = folder_cnt + 1
           the_great_processor(item)
           file2.write(item)
           file2.write("\n")

        if os.path.isfile(item):
            file_cnt = file_cnt + 1
            file1.write(item)
            file1.write("\n")



the_great_processor(base_folder)

file1.close()
file2.close()

print ("{0} folders, and {1} files were found".format(folder_cnt, file_cnt))



