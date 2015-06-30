#!/usr/bin/env python

from gi.repository import GLib, Gio, MessagingMenu

# NB: this will not work by default, as the konversation.desktop files is
# created in a subfolder rather than the default location..
# To fix it:
#    ln -s /usr/share/applications/kde4/konversation.desktop /usr/share/applications/
mmapp = MessagingMenu.App(desktop_id='konversation.desktop')

# make the application appear in the messaging menu. The name and icon are taken from the desktop file above
mmapp.register()

# add a 'source' (a menu item below the application's name) with the name 'Inbox' and a count of 7
icon = Gio.ThemedIcon.new_with_default_fallbacks('my-source-icon')
mmapp.append_source_with_count('inbox', icon, 'Inbox', 7)
mmapp.draw_attention("inbox")

# this is not necessary for gtk applications, which start a mainloop in gtk_main()
GLib.MainLoop().run()
