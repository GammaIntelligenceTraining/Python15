import uuid
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'gif'}


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower()


def unique_filename(filename):
    ext = filename.rsplit('.', 1)[1].lower()
    unique_name = f'{uuid.uuid4()}.{ext}'
    return unique_name
