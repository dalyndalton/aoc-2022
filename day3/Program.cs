int sum = 0;

string[] lines = File.ReadAllLines(@"input.txt");

for (int i = 0; i < lines.Length; i++)
{
    lines[i] = String.Concat(lines[i].Where(c => !char.IsWhiteSpace(c)));
}

foreach (string line in lines)
{
    int half = line.Length / 2;

    var first = line.Substring(0, half);
    var second = line.Substring(half, half);

    // Find character
    foreach (var c1 in first)
    {
        if (second.Contains(c1))
        {
            sum += Char.IsLower(c1) ? (int)c1 - 96 : (int)c1 - 38;
            break;
        }
    }

}
System.Console.WriteLine($"Sum: {sum}");

// Part 2
int badges = 0;
for (int i = 0; i + 2 < lines.Length; i += 3)
{
    var (first, second, third) = (lines[i], lines[i + 1], lines[i + 2]);

    // Find character
    foreach (var c1 in first)
    {
        if (second.Contains(c1) && third.Contains(c1))
        {
            badges += Char.IsLower(c1) ? (int)c1 - 96 : (int)c1 - 38;
            break;
        }
    }

}
System.Console.WriteLine($"Sum: {badges}");