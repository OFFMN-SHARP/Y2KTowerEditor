using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace edcs
{
    public class EditW
    {
        public void Edit()
        {
            Console.WriteLine("Message: Edit Mode (Write)");
            Console.WriteLine("Message: Type '/help' for help.");
            Console.WriteLine("Message: Type '/exit' to exit.");
            StringBuilder Text_Temp= new StringBuilder();
            int Up_LineCount = 0;//Up_LineCount is Update Line Count, which means the line number of the current input line.
            while (true)
            {
                Up_LineCount++;
                Console.ForegroundColor=ConsoleColor.Yellow;
                Console.Write($"[{Up_LineCount}]>>");
                Console.ResetColor();
                string? Input = Console.ReadLine();
                if (Input.ToLower() == "/help")
                {
                    Console.WriteLine("Message: Edit Mode (Write) Help");
                    Console.WriteLine("Message: Type '/help' for help.");
                    Console.WriteLine("Message: Type '/exit' to exit.");
                    Console.WriteLine("Message: Type '/clear' to clear the text.");
                    Console.WriteLine("Tip: '[Up_LineCount]>>' means the current line number.");
                }
                else if (Input.ToLower() == "/exit")
                {
                    Console.WriteLine("Message: Starting to save the text.");
                    Console.WriteLine("Step1:Select the save mode.");
                    Console.WriteLine("1:Save to file.");
                    Console.WriteLine("2:Output to console.");
                    Console.WriteLine("3:New file and save to it.");
                    Console.WriteLine("4:Append to file.");
                    Console.WriteLine("5:Cancel.");
                    Console.Write("Input the number:");
                    int Save_Mode;
                    try
                    {
                        Save_Mode = int.Parse(Console.ReadLine() ?? "2");
                    }
                    catch
                    {
                        Console.WriteLine("Message: Invalid input. Defaulting to output to console.");
                        Save_Mode = 2;
                    }
                    switch (Save_Mode)
                    {
                        case 1:
                            Console.WriteLine("Step2:Input the file path.");
                            string? File_Path = Console.ReadLine();
                            if (!string.IsNullOrEmpty(File_Path) && File.Exists(File_Path))
                            {
                                try
                                {
                                    using (StreamWriter sw = new StreamWriter(File_Path, false))
                                    {
                                        sw.Write(Text_Temp.ToString());
                                        sw.Dispose();
                                        sw.Close();
                                    }
                                }
                                catch (Exception ex)
                                {
                                    Console.WriteLine($"Message: Error saving file. {ex.Message}");
                                    Console.WriteLine("Message: Text not saved.");
                                }
                            }
                            else
                            {
                                Console.WriteLine("Message: Invalid file path. Text not saved.");
                            }
                            break;
                        case 2:
                            Console.Clear();
                            Console.WriteLine("Message: Outputting text to console.");
                            Console.WriteLine(Text_Temp.ToString());
                            break;
                        case 3:
                            Console.WriteLine("Step2:Input the new file path.");
                            string? New_File_Path = Console.ReadLine();
                            if (!string.IsNullOrEmpty(New_File_Path))
                            {
                                try
                                {
                                    using (StreamWriter sw = new StreamWriter(New_File_Path, false))
                                    {
                                        sw.Write(Text_Temp.ToString());
                                        sw.Dispose();
                                        sw.Close();
                                    }
                                }
                                catch (Exception ex)
                                {
                                    Console.WriteLine($"Message: Error saving file. {ex.Message}");
                                    Console.WriteLine("Message: Text not saved.");
                                }
                            }
                            else
                            {
                                Console.WriteLine("Message: Invalid file path. Text not saved.");
                            }
                            break;
                        case 4:
                            Console.WriteLine("Step2:Input the file path to append.");
                            string? Append_File_Path = Console.ReadLine();
                            if (!string.IsNullOrEmpty(Append_File_Path) && File.Exists(Append_File_Path))
                            {
                                try
                                {
                                    using (StreamWriter sw = new StreamWriter(Append_File_Path, true))
                                    {
                                        sw.Write(Text_Temp.ToString());
                                        sw.Dispose();
                                        sw.Close();
                                    }
                                }
                                catch (Exception ex)
                                {
                                    Console.WriteLine($"Message: Error saving file. {ex.Message}");
                                    Console.WriteLine("Message: Text not saved.");
                                }
                            }
                            else
                            {
                                Console.WriteLine("Message: Invalid file path. Text not saved.");
                            }
                            break;
                        case 5:
                            Console.WriteLine("Message: Cancelled. Text not saved.");
                            break;
                    }
                    Environment.Exit(0);
                }
                else if (Input.ToLower() == "/clear")
                {
                    Text_Temp.Clear();
                    Console.WriteLine("Message: Text cleared.");
                }
                else
                {
                    Text_Temp.AppendLine(Input);
                }   
            }
        }
    }
}
