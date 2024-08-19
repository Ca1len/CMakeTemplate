import re
import tempfile
from pathlib import Path
from subprocess import run, PIPE
from dataclasses import dataclass
from typing import List
from conan import ConanFile
from conan.tools.files import load
try:
    import tomllib
except ModuleNotFoundError:
    import pip._vendor.tomli as tomllib


@dataclass
class Project:
    name: str
    checkout: str
    version: str
    project_url: str

    def exists(self) -> bool:
        """
        Check package if exists in conan local cache.
        """
        out = run(
            f'conan list "{self.name}/{self.version}"',
            shell=True,
            stderr=PIPE,
            stdout=PIPE,
        )
        out = out.stderr.decode() + out.stdout.decode()
        regexpr_version = "".join(
            [s if s != "." else r"\." for s in self.version])
        regexpr = re.compile(
            rf"Found \d+ pkg/version recipes matching \
            {self.name}/{regexpr_version} \
            in local cache",
            re.MULTILINE,
        )
        match = regexpr.search(out)
        if match:
            return True
        return False


def get_deps(projects: List[Project]):
    with tempfile.TemporaryDirectory() as tmpdirname:
        tmp_path = Path(tmpdirname)
        for project in projects:
            name = project.name
            if project.exists():
                continue
            checkout = project.checkout
            url = project.project_url
            run(f"git clone {url} {name}",
                shell=True, cwd=tmp_path, check=True)
            run(
                f"git checkout {checkout}",
                shell=True,
                cwd=Path(tmp_path / name),
                check=True,
            )
            run(f"conan create {tmp_path / name} -b missing",
                shell=True, check=True)


def parse_package_info(conanfile: ConanFile, path: Path):
    data = tomllib.load(load(conanfile, path))

    cpp_info = data.get("cpp_info")
    if not cpp_info:
        return

    components = cpp_info.get("components")
    if not components:
        return

    for component in components.keys():
        conan_component = conanfile.cpp_info.components[component]
        libs = component.get("libs")
        if not libs:
            continue
        conan_component.libs = libs
