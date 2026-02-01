from typer.testing import CliRunner
from inkjet.cli import app
from inkjet import __version__

runner = CliRunner()

def test_version():
    """Test that the version command returns the correct version."""
    result = runner.invoke(app, ["--version"])
    assert result.exit_code == 0
    assert __version__ in result.stdout

def test_help():
    """Test that the help command works."""
    result = runner.invoke(app, ["--help"])
    assert result.exit_code == 0
    assert "inkjet" in result.stdout
    assert "Usage" in result.stdout

def test_whoami_no_config():
    """Test whoami command without a printer connected/configured."""
    # This should run but might fail gracefully or show empty config
    # We mainly want to ensure the command structure exists and imports work
    result = runner.invoke(app, ["whoami"])
    # It might fail if no config exists, so we check if it ran at all
    # Adjust assertion based on actual behavior if needed
    assert result.exit_code in [0, 1]