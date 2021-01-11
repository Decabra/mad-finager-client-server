import json
from core.files import File
import os.path

activeReadingFiles = []
activeWritingFiles = []
makeChanges = 0
startProgram = 0


def audit_write_request(file_name):
    if (file_name not in activeReadingFiles) and (file_name not in activeWritingFiles):
        activeWritingFiles.append(file_name)
        return "passed"
    else:
        return "failed"


def file_id_assigner():
    if not list(JSON_structure["files"].keys()):
        file_id = 0
    else:
        file_id = int(list(JSON_structure["files"].keys())[-1])
        file_id += 1
    return file_id


def chunk_id_assigner(file_indexes):
    if not list(JSON_structure["files"][file_indexes]["chunks"].keys()):
        chunk_id = 0
    else:
        chunk_id = int(list(JSON_structure["files"][file_indexes]["chunks"].keys())[-1])
        chunk_id += 1
    return chunk_id


def clear_logs():
    f = open("C:/Users/SarmadSohail/IdeaProjects/mad-finager-with-threading/logs/logs.txt", "w")
    f.close()


def load_JSON():
    global JSON_structure
    if os.path.isfile("C:/Users/SarmadSohail/IdeaProjects/mad-finager-with-threading/core/file_structure.json"):
        with open(
                "C:/Users/SarmadSohail/IdeaProjects/mad-finager-with-threading/core/file_structure.json") as JSON_Infile:
            JSON_structure = json.load(JSON_Infile)
    else:
        print("JSON File not found")


def create_file(clt_id, file_name):
    global makeChanges
    flag = False
    for fileIndexes in list(JSON_structure["files"]):
        if JSON_structure["files"][fileIndexes]["name"] == file_name:
            flag = True
            break
    if flag:
        return display_msg(f"Client-id {clt_id}: File with the same name already Exists!")
    else:
        file = File(file_id_assigner(), file_name, 0, {})
        JSON_structure["files"].update(file.create_f())
        JSON_structure["meta_data"]["files"] += 1
        makeChanges = 1
        return display_msg(f"Client-id {clt_id}: File Created Successfully!")


def delete_file(clt_id, file_name):
    global makeChanges
    FnF = False
    for fileIndexes in list(JSON_structure["files"]):
        if JSON_structure["files"][fileIndexes]["name"] != file_name:
            FnF = True
        else:
            FnF = False
            JSON_structure["meta_data"]["storage"] -= JSON_structure["files"][fileIndexes]["size"]
            del JSON_structure["files"][fileIndexes]
            break
    if FnF:
        return display_msg(f"Client-id {clt_id}: File not exists")
    if not FnF:
        JSON_structure["meta_data"]["files"] -= 1
        makeChanges = 1
        return display_msg(f"Client-id {clt_id}: File Deleted Successfully!")


def open_for_write(clt_id, file_name, Text):
    global makeChanges
    makeChanges = 1
    chunkSize = 20
    FnF = False
    for file_indexes in JSON_structure["files"].keys():
        if JSON_structure["files"][file_indexes]["name"] != file_name:
            FnF = True
        else:
            FnF = False
            JSON_structure["files"][file_indexes]["size"] += len(Text)
            JSON_structure["meta_data"]["storage"] += JSON_structure["files"][file_indexes]["size"]
            for i in range(0, len(Text), chunkSize):
                JSON_structure["files"][file_indexes]["chunks"].update(
                    {str(chunk_id_assigner(file_indexes)): Text[i:i + chunkSize]})
            break
    activeWritingFiles.remove(file_name)
    if FnF:
        return display_msg(f"Client-id {clt_id}: File not exists")
    if not FnF:
        return display_msg(f"Client-id {clt_id}: Data writing Successful!")


def open_for_read(clt_id, file_name):
    global activeReadingFiles
    activeReadingFiles.append(file_name)
    fullData = ""
    FnF = False
    for file_indexes in JSON_structure["files"].keys():
        if JSON_structure["files"][file_indexes]["name"] != file_name:
            FnF = True
        else:
            FnF = False
            for data in JSON_structure["files"][file_indexes]["chunks"].keys():
                fullData += JSON_structure["files"][file_indexes]["chunks"][data] + ""
            break
    if FnF:
        return display_msg(f"Client-id {clt_id}: File not exists")
    if not FnF:
        message = fullData if fullData else "File is empty!"
        return display_msg(f"Client-id {clt_id}: {message}")


def close_file(file_name):
    global activeReadingFiles
    activeReadingFiles.remove(file_name)
    return "File Closed!"


def show_map(clt_id):
    return display_msg(f"Client-id {clt_id}: Requested map\n {json.dumps(JSON_structure, indent=4)}")


def dump_JSON(clt_id):
    with open("C:/Users/SarmadSohail/IdeaProjects/mad-finager-with-threading/core/file_structure.json",
              "w") as JSON_Outfile:
        json.dump(JSON_structure, JSON_Outfile, indent=4)
        return display_msg(f"Client-id {clt_id}: Changes Saved!")


def close_program(clt_id):
    print("Logs created in the logs.txt file check the logs folder...")
    if makeChanges > 0:
        dump_JSON(clt_id)
    return "terminated"


def display_msg(msg):
    with open("C:/Users/SarmadSohail/IdeaProjects/mad-finager-with-threading/logs/logs.txt", "a") as file_ptr:
        print(msg, file=file_ptr)
    return msg


def main(user_choice, file_name, clt_id, writing_text=""):
    global startProgram
    if startProgram == 0:
        clear_logs()
        load_JSON()
    startProgram = 1
    if user_choice == "1":
        return create_file(clt_id, file_name)
    elif user_choice == "2":
        return delete_file(clt_id, file_name)
    elif user_choice == "3":
        return open_for_read(clt_id, file_name)
    elif user_choice == "4":
        return open_for_write(clt_id, file_name, writing_text)
    elif user_choice == "5":
        return show_map(clt_id)
    elif user_choice == "6":
        return close_program(clt_id)
    else:
        return "Invalid input"
