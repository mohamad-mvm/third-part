from django.core.exceptions import ValidationError


def file_size_validator(file):
    max_file_size = 5000000

    if file.size >max_file_size:
        raise ValidationError(f'file size is more than {max_file_size} KB!')
