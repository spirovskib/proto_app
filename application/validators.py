import magic
#in order to run magic you need to 

def validate_file_type_size(value):
    import os
    from django.core.exceptions import ValidationError
    ext = os.path.splitext(value.name)[1]  # [0] returns path+filename
    mime = str(magic.from_buffer(value.read(2048), mime=True))


    #this is the validation setup of files
    """
    Same as FileField, but you can specify:
        * content_types - list containing allowed content_types. Example: ['application/pdf', 'image/jpeg']
        * max_upload_size - a number indicating the maximum file size allowed for upload.
            2.5MB - 2621440
            5MB - 5242880
            10MB - 10485760
            20MB - 20971520
            50MB - 5242880
            100MB 104857600
            250MB - 214958080
            500MB - 429916160
    """
    valid_extensions = ['.pdf']
    max_size = 5242880
    valid_mime_types = ['application/pdf']

    #this is the validation setup of files (size and magic)
    if value.size > max_size:
        print('file too large')
        raise ValidationError('File too large')
    else:
        if not ext.lower() in valid_extensions or not mime in valid_mime_types:
            print('Unsupported file type.')
            raise ValidationError('Unsupported file type.')