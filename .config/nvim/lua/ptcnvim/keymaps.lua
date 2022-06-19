local opts = { noremap = true, silent = true }

--  Shorten function name

-- Leader key
local map = vim.api.nvim_set_keymap
map("", "<Space>", "<Nop>", opts)
vim.g.mapleader = " "
vim.g.maplocalleader = " "

-- Map Esc to other key
map('i', 'kk', '<Esc>', opts)

-- Window navigation (splits)
map("n", "<C-h>", "<C-w>h", opts)
map("n", "<C-j>", "<C-w>j", opts)
map("n", "<C-k>", "<C-w>k", opts)
map("n", "<C-l>", "<C-w>l", opts)

-- Moving text
map("n", "<A-j>", "<Esc>:m .+1<CR>==", opts)
map("n", "<A-k>", "<Esc>:m .-2<CR>==", opts)
map("v", "<A-j>", ":m '>+1<CR>gv=gv", opts)
map("v", "<A-k>", ":m '<-2<CR>==gv", opts)
map("v", "p", '"_dP', opts)

-- Stay in indent mode - visual mode using < or >
map("v", "<", "<gv", opts)
map("v", ">", ">gv", opts)

-- Nvim-tree.lua toggle
map('n', '<leader>f', ':NvimTreeToggle<CR>', opts)

-- Navigate buffers
map("n", "<S-l>", ":bnext<CR>", opts)
map("n", "<S-h>", ":bpreviou<CR>", opts)
