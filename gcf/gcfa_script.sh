#! /bin/bash

echo "Please make sure you are in your home directory"
echo "Adding files and directories"
/usr/bin/git --git-dir=$HOME/git_repos/config_files/cfiles/ --work-tree=$HOME add .bashrc &&
/usr/bin/git --git-dir=$HOME/git_repos/config_files/cfiles/ --work-tree=$HOME add .shell_aliases &&
/usr/bin/git --git-dir=$HOME/git_repos/config_files/cfiles/ --work-tree=$HOME add .shell_config &&
/usr/bin/git --git-dir=$HOME/git_repos/config_files/cfiles/ --work-tree=$HOME add .zshrc &&
/usr/bin/git --git-dir=$HOME/git_repos/config_files/cfiles/ --work-tree=$HOME add .config/starship.toml &&
/usr/bin/git --git-dir=$HOME/git_repos/config_files/cfiles/ --work-tree=$HOME add .config/dunst/ &&
/usr/bin/git --git-dir=$HOME/git_repos/config_files/cfiles/ --work-tree=$HOME add .config/easyeffects/ &&
/usr/bin/git --git-dir=$HOME/git_repos/config_files/cfiles/ --work-tree=$HOME add .config/kitty/ &&
/usr/bin/git --git-dir=$HOME/git_repos/config_files/cfiles/ --work-tree=$HOME add .config/navi/ &&
/usr/bin/git --git-dir=$HOME/git_repos/config_files/cfiles/ --work-tree=$HOME add .config/nvim/ &&
/usr/bin/git --git-dir=$HOME/git_repos/config_files/cfiles/ --work-tree=$HOME add .config/qtile/ &&
/usr/bin/git --git-dir=$HOME/git_repos/config_files/cfiles/ --work-tree=$HOME add .config/rofi/ &&
/usr/bin/git --git-dir=$HOME/git_repos/config_files/cfiles/ --work-tree=$HOME add .config/xplr/init.lua &&
/usr/bin/git --git-dir=$HOME/git_repos/config_files/cfiles/ --work-tree=$HOME add gcf/ &&
echo "Everything added"
