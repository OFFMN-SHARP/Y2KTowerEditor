import os
class w_file:
    @staticmethod
    def write_file():
        Print_yellow:str="\033[93m"
        Print_reset:str="\033[0m"
        print(f"{Print_yellow}Message:Editor Mode-Write{Print_reset}")
        print(f"{Print_yellow}Message:Enter the '/help' command for help menu.{Print_reset}")
        string_builder_file:str = ""
        count:int = 0
        while True:
            count += 1
            input_text:str = input(f"{Print_yellow}[{count}]>>{Print_reset}")
            if input_text == "/exit":
                save_file_sel:str = input(f"{Print_yellow}Message:Do you want to save the file? (y/n){Print_reset}")
                if save_file_sel == "y":
                    print(f"{Print_yellow}Message:Select save mode[1 - Append| 2 - Overwrite| 3 - NewFile| 4 - OutputToConsole]:{Print_reset}")
                    try:
                        save_mode:int = int(input("Input mode number: "))
                    except:
                        print("Invalid input")
                        print("File not saved")
                        exit()
                    if save_mode == 1:
                        path_file:str=input("Input file path: ")
                        try:
                            if os.path.exists(path_file):
                                with open(path_file, "a") as file:
                                    file.write(string_builder_file)
                                    file.close()
                                exit()
                            else:
                                print("File not found")
                                print("File not saved")
                                exit()
                        except:
                            print("Error while saving file")
                            print("File not saved")
                            exit()
                    elif save_mode == 2:
                        path_file:str=input("Input file path: ")
                        try:
                            if os.path.exists(path_file):
                                print("File exists, deleting...")
                                os.remove(path_file)
                            print("Creating new file...")
                            with open(path_file, "w") as file:
                                file.write(string_builder_file)
                                file.close()
                            exit()
                        except:
                            print("Error while saving file")
                            print("File not saved")
                            exit()
                    elif save_mode == 3:
                        path_file:str=input("Input file will be saved path: ")
                        try:
                            if os.path.exists(path_file):
                                print("File exists. Want to delete it? (y/n)")
                                delete_file:str = input("Input your choice: ")
                                if delete_file == "y":
                                    os.remove(path_file)
                                else:
                                    print("File not saved")
                                    exit()
                            with open(path_file, "w") as file:
                                file.write(string_builder_file)
                                file.close()
                            exit()
                        except:
                            print("Error while saving file")
                            print("File not saved")
                            exit()
                    elif save_mode == 4:
                        print(f"{Print_yellow}\n\n\nOutput:\n\n{Print_reset}")
                        print(string_builder_file)
                        exit()
                    else:
                        print("Invalid save mode")
                        exit()
                else:
                    print("File not saved")
                    exit()
            elif input_text == "/clear":
                string_builder_file = ""
                print(f"{Print_yellow}Message:All the text has been cleared.{Print_reset}")
                continue
            elif input_text == "/help":
                print(f"{Print_yellow}Message:Help Menu:{Print_reset}")
                print(f"{Print_yellow}/exit - Exit the editor and save the file.{Print_reset}")
                print(f"{Print_yellow}/clear - Clear the text editor.{Print_reset}")
                print(f"{Print_yellow}/help - Show this help menu.{Print_reset}")
                continue
            else:
                string_builder_file+=input_text+"\n"
        pass
    pass




