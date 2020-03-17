import os
import datetime
import shutil

#TODO change the log file names
#TODO cleanup old folder


# ask the user for the full path of the folder that needs listing
user_folder = input("Enter the full folder path: ")
base_folder = user_folder
file_cnt = 0  # setting the file counter to 0
folder_cnt = 0  # setting the folder counter to 0


def logger_dec(fn):

    def inner(*args, **kwargs):
        time = datetime.datetime.now()
        fn(*args, **kwargs)
        print("{0} has processed on {1}".format(args, time))
    return inner



@logger_dec
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

print("{0} folders, and {1} files were found".format(folder_cnt, file_cnt))
user_response = input("Do you want to proceed sorting files by modification date? (Y/N) ")

if user_response.upper() == "N":
    quit()
elif user_response.upper() == "Y":
    file_list = open("logfile_file.txt", "r")  # read mode
    for lines in file_list:
        file_n = (os.path.split(lines)[-1][:-1])
        folder_n = os.path.dirname(lines)
        full_file_path = os.path.join(folder_n, file_n)
        mod_time = datetime.date.strftime(datetime.date.fromtimestamp(os.path.getmtime(full_file_path)), "%d-%b-%Y")
        print(full_file_path, " ",  mod_time)
        if os.path.exists(os.path.join(user_folder, mod_time)):
            pass
        else:
            os.mkdir(os.path.join(user_folder, mod_time))

        shutil.move(full_file_path, os.path.join(user_folder, mod_time))
    file_list.close()



# folder_list = open("logfile_folder.txt", "r")  # read mode
# for flines in folder_list:
#     folder_n = (os.path.split(flines)[-1][:-1])
#     folder_par = (os.path.split())[0]
#     os.removedirs(os.path.join(folder_n,folder_par)
# folder_list.close()



# listed_files = open("logfile_file.txt", "r")
# for lines in listed_files:
#     the_great_mover(lines)
#
#
# def the_great_mover(file_path):
#     mod_time = os.path.getmtime(file_path)
#     mod_time_formated = mod_time.strftime("%d-%b-%Y")
#     print(mod_time)
#






