import argparse
import pathlib


def add_component(name: str):
    component_dir = pathlib.Path(f"./CMakeTemplate/{name}")
    component_dir.mkdir(parents=True)
    with open(component_dir / "CMakeLists.txt", "w") as cmake:
        cmake.write(
            f"""
set(component {name})

set(sources ./src/{name}.cpp)

add_library(${{component}} ${{sources}})

target_link_libraries(${{component}} PUBLIC base)

target_include_directories(
  ${{component}}
  PUBLIC "$<BUILD_INTERFACE:${{CMAKE_CURRENT_SOURCE_DIR}}/include/>"
         "$<INSTALL_INTERFACE:include/>")

add_executable(${{component}}_app ./app/{name}.cpp)
target_link_libraries(${{component}}_app ${{component}})
""")


def main():
    parser = argparse.ArgumentParser(
        prog="add_component.py",
        description="Creates component with given name",
    )
    parser.add_argument("name")
    args = parser.parse_args()
    add_component(args.name)


if __name__ == "__main__":
    main()
