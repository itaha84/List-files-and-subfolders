import os
import datetime
import shutil


# 18/03/2020 3:50PM


def logger_dec(fn):

    def inner(*args, **kwargs):
        time = datetime.datetime.now()
        fn(*args, **kwargs)
        logs = open(str(log_name_tag + "_logs.txt"), "a")  # append mode
        logs.write("{0} ran on {2} to process {1}".format(str(fn.__name__).upper(), args, time) + "\n")
        logs.write("########################################################################################\n")
    return inner


# TODO change the log file names [Done]
# TODO create log files based on the datetiem of the procees [Done]
# TODO create folder log to contain all logs
# TODO implement file & folder ID and log the length of each file/folder name in a separate log file
# TODO log any exceptionss
# TODO log the folders created (name,path, date, order)
#TODO unify the log collector in one funcation


@logger_dec
def the_file_cleaner(file2delete):
    os.remove(file2delete)


@logger_dec
def the_folder_cleaner(folder_name):
    try:
        os.removedirs(folder_name)
        folder_deletion_logs = open(str(log_name_tag + "_folder_deletion_logs.txt"), "a")  # append mode
        folder_deletion_logs.write(f"{folder_name}, has been deleted !\n")
    except FileNotFoundError:
        exception_logs = open(str(log_name_tag + "_exception_logs.txt"), "a")  # append mode
        exception_logs.write(folder_name + "\n")
        exception_logs.write(str(repr(FileNotFoundError)) + "\n")
        pass
    except OSError:
        exception_logs = open(str(log_name_tag + "_exception_logs.txt"), "a")  # append mode
        exception_logs.write(folder_name + "\n")
        exception_logs.write(str(repr(OSError)) + "\n")
        pass



@logger_dec
def the_folder_name_cleaner():
    folder_list = open(file2.name, "r")  # read mode
    for flines in folder_list:
        folder_n = (os.path.split(flines)[-1][:-1])
        folder_par = (os.path.split(flines))[0]
        folder2delete = os.path.join(folder_par, folder_n)
        the_folder_cleaner(folder2delete)


@logger_dec
def the_great_processor(folder):
    global file1, file2, file_cnt, folder_cnt, log_name_tag
    log_name_tag = datetime.date.strftime(datetime.datetime.now(), "%d-%b-%Y-%H-%M")
    file1 = open(str(log_name_tag + "_file_log.txt"), "a")  # append mode
    file2 = open(str(log_name_tag + "_folder_log.txt"), "a")  # append mode
    items_in_folder = os.listdir(folder)
    for item in items_in_folder:
        item = os.path.join(folder, item)
        if os.path.isdir(item):
            folder_cnt = folder_cnt + 1
            the_great_processor(item)
            file2.write(item + "\n")

        if os.path.isfile(item):
            file_cnt = file_cnt + 1
            file1.write(item + "\n")


# ask the user for the full path of the folder that needs listing


user_folder = input("Enter the full folder path: ")


if os.path.isdir(user_folder):
    base_folder = user_folder
    file_cnt = 0  # setting the file counter to 0
    folder_cnt = 0  # setting the folder counter to 0
    the_great_processor(base_folder)
else:
    print("Invalid. Please enter a valid path!")
    quit()




file1.close()
file2.close()

print("{0} folders, and {1} files were found".format(folder_cnt, file_cnt))
user_response = input("Do you want to proceed sorting files by modification date? (Y/N) ")

if user_response.upper() == "N":
    quit()
elif user_response.upper() == "Y":
    file_list = open(file1.name, "r")  # read mode
    for lines in file_list:
        file_n = (os.path.split(lines)[-1][:-1])
        folder_n = os.path.dirname(lines)
        full_file_path = os.path.join(folder_n, file_n)
        mod_time = datetime.date.strftime(datetime.date.fromtimestamp(os.path.getmtime(full_file_path)), "%d-%b-%Y")
        folder_creation_logs = open(str(log_name_tag + "_folder_creation_logs.txt"), "a")  # append mode
        files_copy_logs = open(str(log_name_tag + "_file_copy_logs.txt"), "a")  # append mode

        if os.path.exists(os.path.join(user_folder, mod_time)):

            folder_creation_logs.write(str(os.path.join(user_folder, mod_time)) + "\n")
            folder_creation_logs.write("already existed on {0}".format(datetime.datetime.now()) + "\n")
            shutil.copy2(full_file_path, os.path.join(user_folder, mod_time))
            files_copy_logs.write(str(full_file_path) + "\n")
            files_copy_logs.write("Copied from: " + str(full_file_path) + "\n")
            files_copy_logs.write("Copied to: " + str(os.path.join(user_folder, mod_time)) + "\n")
            files_copy_logs.write("#################################\n")
            the_file_cleaner(full_file_path)
        else:

            os.mkdir(os.path.join(user_folder, mod_time))
            folder_creation_logs.write(os.path.join(user_folder, mod_time) + "\n")
            folder_creation_logs.write("created on {0}".format(datetime.datetime.now()) + "\n")
            shutil.copy2(full_file_path, os.path.join(user_folder, mod_time))
            files_copy_logs.write(str(full_file_path) + "\n")
            files_copy_logs.write("Copied from: " + str(full_file_path) + "\n")
            files_copy_logs.write("Copied to: " + os.path.join(user_folder, mod_time) + "\n")
            files_copy_logs.write("#################################\n")
            the_file_cleaner(full_file_path)

file_list.close()
the_folder_name_cleaner()
