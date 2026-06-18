''' A script to set up git automatically when the project is created.
'''

import subprocess

def setup_git():
    ''' Initializes a git repository, adds all files, and makes the first commit.
    '''
    # Initialize git repository
    subprocess.run(['git', 'init'], check=True)
    
    # Add all files to staging
    subprocess.run(['git', 'add', '.'], check=True)
    
    # Make the first commit
    subprocess.run(['git', 'commit', '-m', 'Initial commit'], check=True)

if __name__ == '__main__':
    setup_git()