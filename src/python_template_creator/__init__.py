import os

copy_from_root_dir = os.getcwd()
print(copy_from_root_dir)

class TemplatePythonCreator:
    def create_project(self,dir_path:str, project_name: str):
        src_dir = os.path.join(dir_path, "src")
        tests_dir = os.path.join(dir_path, "tests")
        package_dir = os.path.join(src_dir, self.to_snake_case(project_name))

        self.create_dir(src_dir)
        self.create_dir(tests_dir)
        self.create_dir(package_dir)

        self.copy(copy_from_root_dir, dir_path, ".gitignore")
        self.copy(copy_from_root_dir, dir_path, ".pre-commit-config.yaml")
        self.copy(copy_from_root_dir, dir_path, ".pylintrc")
        self.copy(copy_from_root_dir, dir_path, "LICENSE")
        self.copy(copy_from_root_dir, dir_path, "pyproject.toml")
        self.copy(copy_from_root_dir, dir_path, "README.md")
        self.copy(copy_from_root_dir, dir_path, "requirements.txt")
        self.copy(copy_from_root_dir, dir_path, "requirements-dev.txt")
        self.copy(copy_from_root_dir, dir_path, "setup.bat")

        self.create_file(os.path.join(package_dir, "__init__.py"), "".join([
            "def add(a: int, b: int) -> int:\n",
            "    return a + b\n"
        ]))
        self.create_file(os.path.join(tests_dir, "__init__.py"), "")
        self._create_test_file(project_name, tests_dir)

        self.content_replace(dir_path,"README.md", "Python Template Creator", self.to_readable(project_name))
        self.content_replace(dir_path,"pyproject.toml", "python-template-creator", project_name)

    def _create_test_file(self, project_name, tests_dir):
        self.create_file(os.path.join(tests_dir, "test_add.py"), "".join([
            "from "+self.to_snake_case(project_name)+" import add\n",
            "\n",
            "def test_given_two_integers_when_add_then_return_sum():\n",
            "    # Given\n",
            "    a = 1\n",
            "    b = 2\n",
            "\n",
            "    # When\n",
            "    result = add(a, b)\n",
            "\n",
            "    # Then\n",
            "    assert result == 3\n"
        ])) # TODO: Implement this method
    
    def to_snake_case(self, text: str):
        return text.lower().replace(" ", "_").replace("-", "_")
    
    def to_readable(self, text: str):
        return text.replace("_", " ").replace("-"," ").title()
    
    def copy(self, src_dir_path: str, target_dir_path: str, file_name: str):
        src_path = os.path.join(src_dir_path, file_name)
        target_path = os.path.join(target_dir_path, file_name)
        with open(src_path, "r", encoding="utf-8") as f:
            file_content = f.read()
        with open(target_path, "w", encoding="utf-8") as f:
            f.write(file_content)

    def create_dir(self, dir: str):
        if not os.path.exists(dir):
            os.makedirs(dir)
        return dir
    
    def create_file(self, file_path: str, content: str):
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(content)

    def content_replace(self, file_dir_path: str, file_name:str, old_content: str, new_content: str):
        file_path = os.path.join(file_dir_path, file_name)
        with open(file_path, "r", encoding="utf-8") as f:
            content = f.read()
        content = content.replace(old_content, new_content)
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(content)


def has_same_content(file_path1, file_path2):
    with open(file_path1, "r", encoding="utf-8") as f:
        content1 = f.read()

    with open(file_path2, "r", encoding="utf-8") as f:
        content2 = f.read()
    return content1 == content2

if __name__ == "__main__":
    import tkinter as tk
    from tkinter import filedialog
    root = tk.Tk()
    root.withdraw()
    project_dir_path = filedialog.askdirectory() 
    project_name = project_dir_path.split("/")[-1].split(".")[0]
    template_python_creator = TemplatePythonCreator()
    template_python_creator.create_project(project_dir_path, project_name)