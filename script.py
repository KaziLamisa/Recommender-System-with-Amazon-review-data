#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import sys,os
IPYNB_FILENAME = 'simple_recommender_system.ipynb'
CONFIG_FILENAME = '.config_ipynb'

def main(argv):
    with open(CONFIG_FILENAME,'w') as f:
        f.write(' '.join(argv))
    os.system('jupyter nbconvert --execute --to notebook --inplace --allow-errors --ExecutePreprocessor.timeout=-1 {:s}'.format(IPYNB_FILENAME))
    return None

if __name__ == '__main__':
    main(sys.argv)

