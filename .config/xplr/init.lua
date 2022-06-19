---@diagnostic disable
local xplr = xplr -- The globally exposed configuration to be overridden.
---@diagnostic enable

-- To create a custom configuration file, you need to define the script version
-- for compatibility checks.
-- See https://xplr.dev/en/upgrade-guide
-- ```lua
version = "0.19.0"

-- ## Config ------------------------------------------------------------------

-- ### General Configuration --------------------------------------------------
--
-- Set it to `true` to show hidden files by default.
--
-- Type: boolean
xplr.config.general.show_hidden = true

-- Plugins
local home = os.getenv("HOME")
package.path = home
.. "/.config/xplr/plugins/?/init.lua;"
.. home
.. "/.config/xplr/plugins/?.lua;"
.. package.path

--dual pane
require("dual-pane").setup()

-- Or

--require("dual-pane").setup{
--  active_pane_width = { Percentage = 70 },
--  inactive_pane_width = { Percentage = 30 },
--}
