import os
import shutil as sh

pastas = os.listdir('C:\Programing\Leilao\Fotos')

for pasta in pastas:
    Name_image= os.listdir(f'C:\Programing\Leilao\Fotos\{pasta}')
    path_image= f'C:\Programing\Leilao\Fotos\{pasta}\{Name_image}'.replace("['", '').replace("']", '')
    end_path= 'C:\Programing\Leilao\Fotos'
    sh.move(path_image, end_path)

