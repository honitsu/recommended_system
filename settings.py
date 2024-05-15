import os
from pathlib import Path
from IPython.display import display, HTML

global SPLIT_CATEGORY, custom_color, cache_dir, file_oct, file_nov, rfm_file, showcase_file, MAX_ITEMS, MAX_TOTAL, showcase_seg_file, ds_flt_file
SPLIT_CATEGORY='category_code_level2'
MAX_ITEMS = 150
MAX_TOTAL = 125000
custom_color = ["brown","burlywood","cadetblue","chartreuse","chocolate","coral","cornflowerblue",
            "crimson","cyan","darkblue","darkcyan","darkgoldenrod","darkgray",
            "darkgreen","darkgrey","darkkhaki","darkmagenta","darkolivegreen","darkorange",
            "darkorchid","darkred","darksalmon","darkseagreen","darkslateblue","darkslategray",
            "darkslategrey","darkturquoise","darkviolet","deeppink","deepskyblue","dimgray",
            "dimgrey","dodgerblue","firebrick","floralwhite"]
if os.environ['COMPUTERNAME']=='LIANLI':
    cache_dir = os.environ['USERPROFILE'] + "\\Documents\\unik\\cache\\"
else:
    cache_dir = ".\\cache\\"
    for dirname, _, filenames in os.walk(cache_dir):
        files = filter(lambda file: file.endswith('.csv'), filenames)
    for filename in files:
        print(os.path.join(dirname, filename))

file_oct = cache_dir + "2019-Oct.csv"
file_nov = cache_dir + "2019-Nov.csv"  
ds_flt_file = Path(cache_dir + 'dataset_filtered.pkl') # Очищенные исходные данные
rfm_file = Path(cache_dir + 'rfm_df.pkl') # RFM
showcase_file = Path(cache_dir + 'df_showcase2.pkl') # Витрина
showcase_seg_file = Path(cache_dir + 'df_segmented.pkl') # Витрина с кластерами
