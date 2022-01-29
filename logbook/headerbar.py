import gi

gi.require_version("Gtk", "3.0")
gi.require_version("Granite", "1.0")

from gi.repository import Granite, Gtk  # noqa: E402


class HeaderBar(Gtk.HeaderBar):
    def __init__(self):
        super().__init__()
        self.props.title = "Logbook"
        self.props.show_close_button = True
        self.create_layout()

    def create_layout(self) -> None:
        info_button = Gtk.Button.new_from_icon_name(
            "dialog-information", Gtk.IconSize.LARGE_TOOLBAR
        )
        settings_button = Gtk.MenuButton()
        settings_button.props.image = Gtk.Image.new_from_icon_name(
            "open-menu", Gtk.IconSize.LARGE_TOOLBAR
        )
        settings_button.props.popover = self.create_settings_menu()
        info_button.connect("clicked", self.show_info_dialog)

        self.pack_end(settings_button)
        self.pack_end(info_button)

    def show_info_dialog(self, *args) -> None:
        info_text = [
            "Logbook is a viewer for systemd logs.\n",
            "You can read some or all of the logs depending on your permissions.",
            "These permissions may be set by your distro or your administrator.",
        ]
        info_dialog = Granite.MessageDialog.with_image_from_icon_name(
            "Logbook",
            "".join(info_text),
            "dialog-information",
            Gtk.ButtonsType.CLOSE,
        )
        info_dialog.run()
        info_dialog.destroy()

    def create_settings_menu(self) -> Gtk.Popover:
        menu_box = Gtk.Box()

        reverse_item = Granite.SwitchModelButton()
        reverse_item.props.active = True
        reverse_item.props.text = "Reverse order"
        reverse_item.props.description = "Show latest logs first"

        menu_box.add(reverse_item)
        menu_box.props.margin_top = 3
        menu_box.props.margin_bottom = 3
        menu_box.show_all()

        settings_menu = Gtk.Popover()
        settings_menu.add(menu_box)

        return settings_menu
