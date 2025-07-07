return {
  "ziontee113/icon-picker.nvim",
  config = function()
    require("icon-picker").setup({ disable_legacy_commands = true })

    local opts = { noremap = true, silent = true }

    vim.keymap.set("n", "<Leader><f11>", "<cmd>IconPickerNormal<cr>", opts)
    vim.keymap.set("n", "<Leader><f12>", "<cmd>IconPickerYank<cr>", opts) --> Yank the selected icon into register
  end,
}
