# Greensystem JSON reader

Small .NET 8 command-line exercise. Read one local JSON object and print `application_number` and `sponsor_name`. It has no API, database, identity verification, or production processing workflow.

```bash
dotnet build greensystem.sln
dotnet run --project src/Greensystem -- examples/synthetic.json
python3 tests/check_cli.py
```

The included fixture is entirely synthetic. Keep real applications and personal information outside Git. The CLI returns exit code 1 for missing arguments/files, malformed JSON, and JSON `null`; missing object fields print as empty values. Extra JSON fields are ignored by the existing serializer. Tests cover those boundaries with temporary files. CI builds and checks the CLI without external services.

Source: `src/Greensystem/Program.cs`. This README describes the implemented scope and does not claim a government, immigration, or customer integration.
