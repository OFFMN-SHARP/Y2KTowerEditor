namespace edcs
{
    internal class Program
    {
        static void Main(string[] args)
        {
            if(args.Length >= 1 && !string.IsNullOrEmpty(args[0]) && File.Exists(args[0]))//Check Mode
            {
                EditRW editRW = new EditRW();
                editRW.Edit(args[0]);
            }
            else
            {
                EditW editW = new EditW();
                editW.Edit();
            }
            return;
        }
    }
}
