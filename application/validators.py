import magic
from application.constants import *

#in order to run magic you need to 

def validate_file_type_size(value):
    import os
    from django.core.exceptions import ValidationError
    ext = os.path.splitext(value.name)[1]  # [0] returns path+filename
    mime = str(magic.from_buffer(value.read(2048), mime=True))

    if value.size > max_size:
        raise ValidationError('File too large')
    else:
        if not ext.lower() in valid_extensions or not mime in valid_mime_types:
            raise ValidationError('Unsupported file type.')