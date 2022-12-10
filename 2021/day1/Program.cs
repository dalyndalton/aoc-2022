// See https://aka.ms/new-console-template for more information

using System;

internal class Program
{
    private static void Main(string[] args)
    {
        int p1 = 0;
        int p2 = 0;
        int? prev = null;
        var window = new List<int>();

        foreach (var line in System.IO.File.ReadLines(@"input.txt"))
        {
            var number = Int32.Parse(line);

            if (prev != null && number > prev)
                p1++;

            if (window.Count < 3)
            {
                window.Add(number);
            }
            else
            {
                window.Add(number);
                var A = window.Take(3).Sum();
                var B = window.Skip(1).Take(3).Sum();
                if (A < B)
                    p2++;

                window.RemoveAt(0);

            }
            prev = number;
        }

        Console.WriteLine($"Total Count: {p1}");
        Console.WriteLine($"Total Count: {p2}");
    }
}