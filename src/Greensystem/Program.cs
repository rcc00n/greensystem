using System.Text.Json;

namespace Greensystem;

public sealed class ApplicationRecord
{
    public string? application_number { get; set; }
    public string? sponsor_name { get; set; }
}

public static class Program
{
    public static int Main(string[] args)
    {
        if (args.Length != 1)
        {
            Console.Error.WriteLine("Usage: greensystem <path-to-json>");
            return 1;
        }

        var filePath = args[0];
        if (!File.Exists(filePath))
        {
            Console.Error.WriteLine($"File not found: {filePath}");
            return 1;
        }

        try
        {
            var json = File.ReadAllText(filePath);
            var record = JsonSerializer.Deserialize<ApplicationRecord>(json);
            if (record is null)
            {
                Console.Error.WriteLine("The JSON file is empty or invalid.");
                return 1;
            }

            Console.WriteLine($"Application Number: {record.application_number ?? string.Empty}");
            Console.WriteLine($"Sponsor Name: {record.sponsor_name ?? string.Empty}");
            return 0;
        }
        catch (JsonException ex)
        {
            Console.Error.WriteLine($"Invalid JSON: {ex.Message}");
            return 1;
        }
        catch (Exception ex)
        {
            Console.Error.WriteLine($"Unexpected error: {ex.Message}");
            return 1;
        }
    }
}
