import os
import wget

## Verify if directory exists. Create if it doesnt exist.
def check_dir(file_path):
  directory = os.path.dirname(file_path)
  if not os.path.exists(directory):
    os.makedirs(directory)

## Download source Files from urls
def download_files(urls, out_path='downloads/', silent=False):
  for url in urls:
    check_dir(out_path)
    print('Downloading', url)
    wget.download(url, out=out_path)
    print()
    # os.system('wget %s' % url)

if __name__ == "__main__":
  urls=['https://gamepedia.cursecdn.com/darkestdungeon_gamepedia/c/ce/Vo_narr_tut_firstdungeon.ogg']
  download_files(urls,'testing/')
  # check_dir('testing/')