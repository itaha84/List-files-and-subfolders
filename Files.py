import os
import datetime
import shutil
# 18/03/2020 3:50PM


def logger_dec(fn):

    def inner(*args, **kwargs):
        time = datetime.datetime.now()
        fn(*args, **kwargs)
        logs = open(str(log_name_tail + "_logs.txt"), "a")  # append mode
        logs.write("\n")
        logs.write("{0} function was called to process {1} on {2}".format(str(fn.__name__).upper(), args, time))
        logs.write("\n")
        logs.write("########################################################################################")
        logs.write("\n")
    return inner



#TODO change the log file names
#TODO create log files based on the datetiem of the procees


# ask the user for the full path of the folder that needs listing
user_folder = input("Enter the full folder path: ")
base_folder = user_folder
file_cnt = 0  # setting the file counter to 0
folder_cnt = 0  # setting the folder counter to 0


@logger_dec
def the_file_cleaner(file2delete):
    os.remove(file2delete)


@logger_dec
def the_folder_cleaner(folder_name):
    try:
        os.removedirs(folder_name)
    except (FileNotFoundError, OSError):
        pass


@logger_dec
def the_folder_name_cleaner():
    folder_list = open(file2.name, "r")  # read mode
    for flines in folder_list:
        folder_n = (os.path.split(flines)[-1][:-1])
        folder_par = (os.path.split(flines))[0]
        # print("***" * 10)
        # print(folder_n, " ", folder_par)
        folder2delete = os.path.join(folder_par, folder_n)
        # print(folder2delete)
        the_folder_cleaner(folder2delete)
        # print(flines)
        # print(os.path.join(folder_n, folder_par))
        # print(os.path.isdir(os.path.join(folder_n, folder_par)))
        # print(flines)
        # print(folder_n)
        # print(folder_par)


@logger_dec
def the_great_processor(folder):
    global file1, file2, file_cnt, folder_cnt, log_name_tail
    log_name_tail = datetime.date.strftime(datetime.datetime.now(), "%d-%b-%Y-%H-%M")
    file1 = open(str(log_name_tail + "_file_log.txt"), "a")  # append mode
    file2 = open(str(log_name_tail + "_folder_log.txt"), "a")  # append mode
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
    print(file1.name)
    print(file2.name)
    quit()
elif user_response.upper() == "Y":
    file_list = open(file1.name, "r")  # read mode
    for lines in file_list:
        file_n = (os.path.split(lines)[-1][:-1])
        folder_n = os.path.dirname(lines)
        full_file_path = os.path.join(folder_n, file_n)
        mod_time = datetime.date.strftime(datetime.date.fromtimestamp(os.path.getmtime(full_file_path)), "%d-%b-%Y")
        if os.path.exists(os.path.join(user_folder, mod_time)):
            # shutil.move(full_file_path, os.path.join(user_folder, mod_time))
            shutil.copy2(full_file_path, os.path.join(user_folder, mod_time))
            the_file_cleaner(full_file_path)
        else:
            os.mkdir(os.path.join(user_folder, mod_time))
            # shutil.move(full_file_path, os.path.join(user_folder, mod_time))
            shutil.copy2(full_file_path, os.path.join(user_folder, mod_time))
            the_file_cleaner(full_file_path)


file_list.close()
the_folder_name_cleaner()

