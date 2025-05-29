import os
import subprocess

def parse_ttl(path):
    project = {}
    with open(path, 'r') as f:
        lines = f.readlines()

    current = None
    for line in lines:
        line = line.strip()
        if line.startswith("project"):
            project["name"] = line.split('"')[1]
        elif line.startswith("language"):
            project["language"] = line.split('"')[1]
        elif line.startswith("output"):
            project["output"] = line.split('"')[1]
        elif line.startswith("sources"):
            current = "sources"
            project[current] = []
        elif line.startswith("dependencies"):
            current = "dependencies"
            project[current] = []
        elif "[" in line or "]" in line or line == "":
            continue
        elif current:
            project[current].append(line.strip('"').strip(','))

    return project

def compile_project(project):
    os.makedirs(os.path.dirname(project["output"]), exist_ok=True)
    sources = project["sources"]
    output = project["output"]
    cmd = ["g++"] + sources + ["-o", output]
    print("Compiling:", " ".join(cmd))
    subprocess.run(cmd)

if __name__ == "__main__":
    config = parse_ttl("build.ttl")
    compile_project(config)
