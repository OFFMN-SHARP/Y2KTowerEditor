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
        while True:
            count += 1
            input_text:str = input(f"{Print_yellow}[{count}|{line_unfinished}|{line_finished}]>>{Print_reset}")
        pass
    pass




