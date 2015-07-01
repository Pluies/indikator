What
====

Ubuntu has an 'envelope' icon in the top bar that turns blue when a message arrives, whether it be an email or an instant message. The user can then go to their Konversation window to read the message and the envelope will turn itself back to grey.

Konversation on Ubuntu 12.04 was perfectly integrated into this, but something appears to have changed when I upgraded to Ubuntu 14.04 and the envelope stopped turning blue when new Konversation messages arrive.

So how did you fix it
=====================

There's a few files in there, but the general concept is:
* When a message arrives, Konversation triggers the python script that will turn the envelope blue
* The listener daemon uses [xdotool](https://launchpad.net/ubuntu/trusty/+package/xdotool) to kill the python script whenever the Konversation window is brought into focus, turning the envelope back to its original state

How do I use it?
================

Due to a strange configuration of Konversation's `.desktop` file, you will first need to create a symlink:

    ln -s /usr/share/applications/kde4/konversation.desktop /usr/share/applications/

Then, configure konversation to run `konversation-indicator-applet.py` (in Settings > Configure Notifications...). You can pick and choose which events you want to trigger the notifications.

Finally, run the listener script `listener-and-killer-daemon.sh`. It will put itself in the background automatically.

Alternatively, you can use the provided SysV-style init file to start the daemon:

    vim indikator-listener-daemon # Change your username and path as needed
    sudo cp indikator-listener-daemon /etc/init.d/
    sudo update-rc.d indikator-listener-daemon defaults

(Hat tip to [this blog post](https://mobiarch.wordpress.com/2014/05/16/creating-an-init-script-in-ubuntu-14-04/))
