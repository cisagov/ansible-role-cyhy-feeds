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


@pytest.mark.parametrize("pkg", ["cyhy-feeds"])
def test_pip_packages(host, pkg):
    """Test that the pip packages were installed."""
    # Skip pip package assertion on Debian Buster, due to the wonky way we must
    # install cyhy-feeds on Buster. On Buster, we must use pip's
    # --ignore-installed option to work around dependency install behavior,
    # which causes pip to report that the package is not installed even though
    # it is.  This is ok because the test_files test will still verify that the
    # expected files are present.
    distribution = getattr(host.system_info, "distribution", "").lower()
    codename = getattr(host.system_info, "codename", "").lower()
    if distribution == "debian" and codename == "buster":
        pytest.skip("Skipping pip package assertion on Debian Buster")

    assert pkg in host.pip.get_packages(pip_path="pip3")


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
