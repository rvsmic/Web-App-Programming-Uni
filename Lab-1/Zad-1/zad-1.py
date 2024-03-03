def copy_file(src, dest):
    with open(src, 'r') as src_file:
        with open(dest, 'w') as dest_file:
            dest_file.write(src_file.read())
            print(f'File {src} copied to {dest}')

src_path = input('Enter copy path: ')
dst_path = 'lab1zad1.txt'
copy_file(src_path, dst_path)