import os
import yaml

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']
).get_hosts('all')

system_packages = [
    "gcc",
    "gdb",
    "make",
    "cmake",
    "git",
    "rsync",
    "tree"
]

def test_packages_installed(host):
    for package in system_packages:
        assert host.package(package).is_installed
