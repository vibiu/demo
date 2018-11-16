def handle_uploaded_file(filename, f):
    with open(f'{filename}.txt', 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)
