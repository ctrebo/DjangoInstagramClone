import os

def validate_file_extension(value):
  ext = os.path.splitext(value.name)[1]
  valid_extensions = [".jpg", ".png", ".jpeg", ".mp4"]
  if not ext in valid_extensions:
    raise ValidationError(u'File not supported!')
