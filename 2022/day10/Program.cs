internal class Program
{

    private static void Main(string[] args)
    {
        int X = 1;
        int counter = 0;

        int total = 0;
        var targets = new int[] { 20, 60, 100, 140, 180, 220 };
        var c = new List<char>();


        var check = () =>
        {
            var Y = counter % 40;
            c.Add((Y <= X + 1) && (Y >= X - 1) ? '#' : '.');
            total += targets.Contains(++counter) ? (X * counter) : 0;
        };

        // Read Lines
        List<string> lines = System.IO.File.ReadAllLines(@"input.txt").ToList();

        foreach (var line in lines)
        {
            // Parse input
            string[] parts = line.Split(null);

            if (parts[0] == "noop")
            {
                check();
            }
            else if (parts[0] == "addx")
            {
                check();
                check();
                X += int.Parse(parts[1]);
            }

        }

        // Printing
        Console.WriteLine($"Total: {total}");
        for (int i = 0; i < c.Count; i++)
        {
            if (i % 40 == 0)
                Console.WriteLine();
            Console.Write(c[i]);
        }
    }
}