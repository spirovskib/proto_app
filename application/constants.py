
#File Validation for the Attachments
"""
* valid_extensions - list containing allowed file extensions. Example: ['.pdf', '.jpg']
* valid_mime_types - list containing allowed content_types. Example: ['application/pdf', 'image/jpeg']
* max_size  - a number indicating the maximum file size allowed for upload.
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

#File Validation for the Attachments

# Image Upload Resize Width 
# Resize height is calculated in the view during resize
resize_width = 800

# Image Upload Resize Width 
