import os


class TemplatePythonCreator:
    def create_project(self, project_name: str):
        return project_name  #TODO: Implement this method

    def copy(self, file_path: str, target_path: str):
        with open(file_path, "r", encoding="utf-8") as f:
            file_content = f.read()
        with open(target_path, "w", encoding="utf-8") as f:
            f.write(file_content)

    def create_dir(self, dir: str):
        os.makedirs(dir)
        return dir


def has_same_content(file_path1, file_path2):
    with open(file_path1, "r", encoding="utf-8") as f:
        content1 = f.read()

    with open(file_path2, "r", encoding="utf-8") as f:
        content2 = f.read()
    return content1 == content2
