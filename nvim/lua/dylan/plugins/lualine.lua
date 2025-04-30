return {
	"nvim-lualine/lualine.nvim",
	dependencies = { "nvim-tree/nvim-web-devicons" },
	config = function()
		local lualine = require("lualine").setup({
			options = { theme = "catppuccin-mocha" },
		})
	end,
}
