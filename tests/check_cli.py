from pathlib import Path
import subprocess
import tempfile
import json

root = Path(__file__).resolve().parents[1]
subprocess.run(['dotnet', 'build', str(root / 'greensystem.sln'), '--nologo'], check=True)
dll = root / 'src/Greensystem/bin/Debug/net8.0/Greensystem.dll'
with tempfile.TemporaryDirectory() as directory:
    directory = Path(directory)
    cases = [('valid.json', {'application_number': 'DEMO-0001', 'sponsor_name': 'Synthetic Example'}, 0), ('missing-fields.json', {}, 0), ('null.json', None, 1), ('array.json', [], 1)]
    for name, value, expected in cases:
        source = directory / name; source.write_text(json.dumps(value))
        result = subprocess.run(['dotnet', str(dll), str(source)], capture_output=True, text=True)
        assert result.returncode == expected, name
        if name == 'valid.json':
            assert 'Application Number: DEMO-0001' in result.stdout
            assert 'Sponsor Name: Synthetic Example' in result.stdout
    invalid = directory / 'invalid.json'; invalid.write_text('{')
    for args in [[], [str(directory / 'absent.json')], [str(invalid)]]:
        result = subprocess.run(['dotnet', str(dll), *args], capture_output=True, text=True)
        assert result.returncode == 1, args
print('CLI synthetic and invalid-input checks passed.')
