# vim-sync

sync with remote machine in vim

## Installation

Use your plugin manager of choice.

- [Pathogen](https://github.com/tpope/vim-pathogen)
  - `git clone https://github.com/yifeikong/vim-sync ~/.vim/bundle/vim-sync`
- [Vundle](https://github.com/gmarik/vundle)
  - Add `Bundle 'https://github.com/yifeikong/vim-sync'` to .vimrc
  - Run `:BundleInstall`
- [NeoBundle](https://github.com/Shougo/neobundle.vim)
  - Add `NeoBundle 'https://github.com/yifeikong/vim-sync'` to .vimrc
  - Run `:NeoBundleInstall`
- [vim-plug](https://github.com/junegunn/vim-plug)
  - Add `Plug 'https://github.com/yifeikong/vim-sync'` to .vimrc
  - Run `:PlugInstall`

## Usage

When you have a slow network, editing files on remote machine can be very
annoying. With vim-sync, you can edit files on local machine and upload it right in vimr.

Vim-sync uses rsync to sync between your local project files with remote ones.
Suppose you remote repository is /opt/my-project, remote machine is
john@example.com and your local repository is ~/repos/my-project.

1. create a file named `.vim-sync` in project root on local machine, with remote address as
   content

     cd ~/repos/my-project
     echo 'john@example.com:/opt/my-project' > .vim-sync

2. Edit some files and save them.
3. Use `:VSUploadFile` to upload current file to remote, use `:VSUpload` to
   upload all files to remote.

## Todo

1. support asyncrun.
2. better error handling
3. add doc in vim
