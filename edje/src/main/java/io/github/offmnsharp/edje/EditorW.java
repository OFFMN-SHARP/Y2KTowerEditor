package io.github.offmnsharp.edje;

import java.io.File;
import java.io.FileWriter;
import java.io.Writer;
import java.util.NoSuchElementException;
import java.util.Scanner;

public class EditorW {
    public  static StringBuilder Reop_FileAllText = new StringBuilder();
    private enum Mode_Save{
        Save_Append,
        Save_OverWrite,
        Save_New,
        Save_Console,
        Cancel
    }
    public static void Write(){
        try {
            String ANSI_LIGHT_YELLOW = "\u001B[93m";
            String ANSI_RESET = "\u001B[0m";
            System.out.print("Message:Starting load Editor......");
            System.out.println();
            int LineCount = 0;
            while (true) {
                LineCount++;
                System.out.print(ANSI_LIGHT_YELLOW + "[" + LineCount + "]>>" + ANSI_RESET);
                String Line = new Scanner(System.in).nextLine();
                switch (Line) {
                    case "/exit":
                        System.out.println("Message:Exit Editor");
                        System.out.println("Message[Step 1]:Save file?(Y/N)");
                        String SaveFile = new Scanner(System.in).nextLine();
                        if (SaveFile.equals("Y") || SaveFile.equals("y")) {
                            System.out.println("Message[Step 2]:Select save mode?");
                            System.out.println("Message[Step 2]:1.Save Append");
                            System.out.println("Message[Step 2]:2.Save OverWrite");
                            System.out.println("Message[Step 2]:3.Save New");
                            System.out.println("Message[Step 2]:4.Output Console");
                            System.out.println("Message[Step 2]:5.Cancel");
                            System.out.println("Enter the number:");
                            String SaveMode = new Scanner(System.in).nextLine();
                            System.out.println("Message[Step 3]:Enter the file path:");
                            String FilePath = new Scanner(System.in).nextLine();
                            switch (SaveMode) {
                                case "1":
                                    WriteFile(Reop_FileAllText, Mode_Save.Save_Append, FilePath);
                                    break;
                                case "2":
                                    WriteFile(Reop_FileAllText, Mode_Save.Save_OverWrite, FilePath);
                                    break;
                                case "3":
                                    WriteFile(Reop_FileAllText, Mode_Save.Save_New, FilePath);
                                    break;
                                case "4":
                                    WriteFile(Reop_FileAllText, Mode_Save.Save_Console, FilePath);
                                    break;
                                case "5":
                                    WriteFile(Reop_FileAllText, Mode_Save.Cancel, FilePath);
                                    break;
                                default:
                                    System.out.println("Message:Error");
                                    System.out.println("Message:Exiting Editor");
                                    System.exit(0);
                            }
                        } else {
                            System.out.println("Message:Exiting Editor");
                        }
                        System.exit(0);
                    case "/help":
                        System.out.println("Message:Help");
                        System.out.println("Message:/exit - Exit Editor");
                        System.out.println("Message:/help - Show this message");
                        System.out.println("Message:/clear - Clear all text");
                        break;
                    case "/clear":
                        Reop_FileAllText.delete(0, Reop_FileAllText.length());
                        System.out.println("Message:Clear all text");
                        break;
                    default:
                        Reop_FileAllText.append(Line);
                        Reop_FileAllText.append("\n");
                        break;
                }
            }
        }
        catch (NoSuchElementException | IllegalStateException e){
            System.out.println();
            System.out.println("Message:'^C' detected");
            System.out.println("Message:Exiting Editor");
            System.exit(0);
        }
    }
    private static void WriteFile(StringBuilder Text_UserInput,Mode_Save Mode,String FilePath){
        System.out.println("Message:Save file");
        switch (Mode){
            case Save_Append:
                System.out.println("Message:Append");
                try {
                    Writer Wte = new FileWriter(FilePath, true);
                    Wte.write(Text_UserInput.toString());
                    Wte.close();
                }catch (Exception e){
                    System.out.println("Message:Error");
                    System.out.println("Message:"+e);
                }
                break;
            case Save_OverWrite:
                System.out.println("Message:OverWrite");
                try {
                    Writer Wte = new FileWriter(FilePath);
                    Wte.write(Text_UserInput.toString());
                    Wte.close();
                }catch (Exception e){
                    System.out.println("Message:Error");
                    System.out.println("Message:"+e);
                }
                break;
            case Save_New:
                System.out.println("Message:New");
                try{
                    if (!new File(FilePath).exists()){
                    File file = new File(FilePath);
                        try{
                            file.createNewFile();
                            System.out.println("Message:Create new file");
                        }
                        catch (Exception e){
                            System.out.println("Message:Error");
                            System.out.println("Message:"+e);
                        }
                    }
                    Writer Wte = new FileWriter(FilePath);
                    Wte.write(Text_UserInput.toString());
                    Wte.close();
                }catch (Exception e){
                    System.out.println("Message:Error");
                    System.out.println("Message:"+e);
                }
                break;
            case Save_Console:
                System.out.println("Message:Console");
                System.out.println();
                System.out.println(Text_UserInput.toString());
                break;
            case Cancel:
                System.out.println("Message:Cancel");
                break;
        }
    }
}
