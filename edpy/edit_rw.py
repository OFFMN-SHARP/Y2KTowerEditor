class rw_file:
    @staticmethod
    def readwrite_file(path):
        Print_yellow:str = "\033[93m"
        Print_reset:str = "\033[0m"
        string_builder_file:str = ""
        count:int = 0
        line_unfinished:int = 0
        line_finished:int = 0
        print(f"{Print_yellow}Message:File loading...{Print_reset}")
        try:
            with open(path, "r") as file:
                read_file = file.readlines()
                file.close()
        except Exception as e:
            print(f"{Print_yellow}Error:{e}{Print_reset}")
            exit()
        print (f"{Print_yellow}Message:File loaded.{Print_reset}")
        print (f"{Print_yellow}Message:Editor Mode-Read/Write.{Print_reset}")
        print (f"{Print_yellow}Message:Enter the '/help' command for help menu.{Print_reset}")
        print (f"{Print_yellow}{read_file[0]}{Print_reset}")
        while True:
            count += 1
            print(f"{Print_yellow}{read_file[line_finished+1]}{Print_reset}")
            input_text:str = input(f"{Print_yellow}[{count}|{line_unfinished}|{line_finished}]>>{Print_reset}")
            if input_text == "/help":
                print (f"{Print_yellow}Message:Enter the '/exit' command to exit the editor.{Print_reset}")
                print (f"{Print_yellow}Message:Enter the '/clear' command to clear the file.{Print_reset}")
                print (f"{Print_yellow}Message:Enter the '/help' command to get the help menu.{Print_reset}")
                continue
            elif input_text == "/exit":
                selected_option:str = input(f"{Print_yellow}Do you want to save the changes? (y/n){Print_reset}")
                if selected_option.lower() == "y":
                    try:
                        with open(path, "w") as file:
                            file.write(string_builder_file)
                            file.close()
                        print (f"{Print_yellow}Message:File saved.{Print_reset}")
                    except Exception as e:
                        print(f"{Print_yellow}Error:{e}{Print_reset}")
                        exit()
                else:
                    print (f"{Print_yellow}Message:File not saved.{Print_reset}")
                    exit()
            elif input_text == "/clear":
                string_builder_file = ""
                print (f"{Print_yellow}Message:File cleared.{Print_reset}")
                continue
            elif input_text!="" and input_text !=" " and input_text !="/help" and input_text !="/exit" and input_text !="/clear":
                string_builder_file += input_text + "\n"
            else:
                if len(read_file)>line_finished:
                    string_builder_file+=read_file[line_finished+1]
                else:
                    string_builder_file+="\n"
        pass
    pass




