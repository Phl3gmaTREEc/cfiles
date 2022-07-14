#! /bin/bash
# Exit when command fails
set -e

# Info for user
echo "Changing directory to home for purpose of this script"
# CD into home direcory
cd
# Info for user
echo "Adding files and directories"
# List of files and direcotries to be added
/usr/bin/git --git-dir=$HOME/git_repos/config_files/cfiles/ --work-tree=$HOME add .bashrc
/usr/bin/git --git-dir=$HOME/git_repos/config_files/cfiles/ --work-tree=$HOME add .shell_aliases
/usr/bin/git --git-dir=$HOME/git_repos/config_files/cfiles/ --work-tree=$HOME add .shell_config
/usr/bin/git --git-dir=$HOME/git_repos/config_files/cfiles/ --work-tree=$HOME add .zshrc
/usr/bin/git --git-dir=$HOME/git_repos/config_files/cfiles/ --work-tree=$HOME add .config/starship.toml
/usr/bin/git --git-dir=$HOME/git_repos/config_files/cfiles/ --work-tree=$HOME add .config/dunst/
/usr/bin/git --git-dir=$HOME/git_repos/config_files/cfiles/ --work-tree=$HOME add .config/easyeffects/
/usr/bin/git --git-dir=$HOME/git_repos/config_files/cfiles/ --work-tree=$HOME add .config/kitty/
/usr/bin/git --git-dir=$HOME/git_repos/config_files/cfiles/ --work-tree=$HOME add .config/navi/
/usr/bin/git --git-dir=$HOME/git_repos/config_files/cfiles/ --work-tree=$HOME add .config/nvim/
/usr/bin/git --git-dir=$HOME/git_repos/config_files/cfiles/ --work-tree=$HOME add .config/qtile/
/usr/bin/git --git-dir=$HOME/git_repos/config_files/cfiles/ --work-tree=$HOME add .config/rofi/
/usr/bin/git --git-dir=$HOME/git_repos/config_files/cfiles/ --work-tree=$HOME add .config/xplr/init.lua
/usr/bin/git --git-dir=$HOME/git_repos/config_files/cfiles/ --work-tree=$HOME add gcf/
# Infor for user
echo "Everything added"
