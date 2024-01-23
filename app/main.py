#%%
from lib.split_pdf import split_pdf_to_images
from pathlib import Path
# %%
wdir = Path('/app')
images_dir = wdir / 'data' / 'images'
images_dir.mkdir(exist_ok=True)
# %%
source_pdf_file = wdir / 'data' / '20240119095723.pdf'
# %%
split_pdf_to_images(source_pdf_file, images_dir)
# %%
