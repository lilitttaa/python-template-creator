import os
import pytest
from python_template_creator import TemplatePythonCreator, has_same_content


@pytest.fixture
def temp_file():
    file_path = "file.py"
    with open(file_path, "w", encoding="utf-8") as f:
        f.write("print('Hello, World!')")
    yield file_path
    os.remove(file_path)


def test_given_file_path_and_target_path_when_copy_then_get_copied_file(temp_file):
    # Given
    template_python_creator = TemplatePythonCreator()

    target_path = "target.py"

    # When
    template_python_creator.copy(temp_file, target_path)

    # # Then
    assert has_same_content(temp_file, target_path)

    # # Clean up
    os.remove(target_path)


def test_given_project_name_when_create_project_then_project_folder_is_created():
    # Given
    template_python_creator = TemplatePythonCreator()
    project_name = "my_project"

    # When
    project_folder = template_python_creator.create_project(project_name)

    # Then
    assert project_folder == "my_project"
