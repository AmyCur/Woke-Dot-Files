vim.g.mapleader = " "

local keymap = vim.keymap

keymap.set("n", "<leader>nh", ":nohl<CR>") -- Clears searched for text
keymap.set("n", "x", "_x") -- Makes it so x doesnt copy to register

keymap.set("n", "<leader>sv", "<C-w>v") -- Split Vertically
keymap.set("n", "<leader>sh", "<C-w>s") -- Split Horizontally
keymap.set("n", "<leader>se", "<C-w>=") -- Makes split windows equal widths
keymap.set("n", "<leader>sx", ":close<CR>") -- Closes current window

keymap.set("n", "<leader>to", ":tabnew<CR>") -- Opens a new tab
keymap.set("n", "<leader>tx", ":tabclose<CR>") -- Closes tab
keymap.set("n", "<leader>tl", ":tabn<CR>") -- Next tab
keymap.set("n", "<leader>th", ":tabp<CR>") -- Previous tab

-- Plugin Keymaps

-- Telescope
keymap.set("n", "<leader>ff", ":Telescope find_files<CR>") -- Telescope that looks through the folder
keymap.set("n", "<leader>fg", ":Telescope live_grep<CR>") -- idk
keymap.set("n", "<leader>fb", ":Telescope buffers<CR>") -- Opens the buffers

keymap.set("n", "<leader>sm", ":MaximizerToggle<CR>") -- Maximises (Doesnt work)

keymap.set("n", "<leader>bt", ":NvimTreeToggle<CR>") -- Toggles the tree
keymap.set("n", "<leader>bf", ":NvimTreeFocus<CR>") -- Focuses the side bar
keymap.set("n", "<leader>bc", ":NvimTreeCollapse<CR>") -- Collapses the side bar

keymap.set("n", "<C-S><C-S>", ":w<CR>") -- Saves
keymap.set("n", "<C-S><C-Q>", ":wq<CR>") -- Saves and quits
keymap.set("n", "<C-S><C-A>", ":wqa<CR>") -- Saves and quits all

keymap.set("n", "<leader>to", ":terminal<CR>") -- Opens a terminal

keymap.set("n", "<leader>q", ":!zathura <C-r>=expand('%:r')<cr>.pdf &<cr>")

keymap.set("n", "<leader>oo", ":FloatermNew<CR>")
keymap.set("n", "<F7>", ":FloatermToggle<CR>")

keymap.set("n", "<leader>nb", ":Navbuddy<CR>")
