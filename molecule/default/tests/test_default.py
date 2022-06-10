"""Module containing the tests for the default scenario."""

# Standard Python Libraries
import os

# Third-Party Libraries
import pytest
import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ["MOLECULE_INVENTORY_FILE"]
).get_hosts("all")


@pytest.mark.parametrize("pkg", ["gnupg2", "unzip"])
def test_packages(host, pkg):
    """Test that the appropriate packages were installed."""
    assert host.package(pkg).is_installed


@pytest.mark.parametrize(
    "pkg", ["boto3", "python-gnupg", "requests", "requests-aws4auth"]
)
def test_pip_packages(host, pkg):
    """Test that the pip packages were installed."""
    assert pkg in host.pip.get_packages()


@pytest.mark.parametrize(
    "f",
    [
        "/var/local/cyhy/feeds",
        "/var/cyhy/scripts/cyhy-feeds/cyhy_extracts",
        "/var/cyhy/scripts/cyhy-feeds/cyhy-data-extract.py",
        "/var/cyhy/scripts/cyhy-feeds/dmarc.py",
    ],
)
def test_files(host, f):
    """Test that the expected files and directories are present."""
    assert host.file(f).exists
