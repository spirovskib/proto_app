import magic
from application.constants import VALID_FILE_EXTENSIONS, VALID_MIME_TYPES, MAX_FILE_SIZE

#in order to run magic you need to 

def validate_file_type_size(value):
    import os
    from django.core.exceptions import ValidationError
    ext = os.path.splitext(value.name)[1]  # [0] returns path+filename
    mime = str(magic.from_buffer(value.read(2048), mime=True))

    if value.size > MAX_FILE_SIZE:
        raise ValidationError('File too large')
    else:
        if not ext.lower() in VALID_FILE_EXTENSIONS or not mime in VALID_MIME_TYPES:
            raise ValidationError('Unsupported file type.')