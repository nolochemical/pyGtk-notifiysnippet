#~ *LICENSE*
#~ 
#~ Copyright (c) 2011 Victor Phelemba
#~ 
#~ pyGtk-notifiysnippet is free software: you can redistribute it and/or modify
#~ it under the terms of the GNU General Public License as published by
#~ the Free Software Foundation, version 3 of the License.
#~ 
#~ pyGtk-notifiysnippet is distributed in the hope that it will be useful,
#~ but WITHOUT ANY WARRANTY; without even the implied warranty of
#~ MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#~ GNU General Public License for more details.
#~ 
#~ You should have received a copy of the GNU General Public License
#~ along with pyGtk-notifiysnippet.  If not, see <http://www.gnu.org/licenses/>.
import pygtk
pygtk.require('2.0')
import gtk
from threading import Timer

DISPLAY_WAIT_TIME = 3.0 # realistic wait time when it works

class pyGtk_notifiysnippet:
    def delete_event(self, widget, data=None):
        return False
    def alert_user(self, message):
        self.statusicon = gtk.StatusIcon()
        self.statusicon.set_from_stock(gtk.STOCK_INFO)
        self.statusicon.set_blinking(True)
        self.statusicon.connect("activate", self.alert_me, (message))
        self.statusicon.set_visible(True)
    def alert_me(self, widget, message):
        self.dialog = gtk.MessageDialog(self.window,gtk.DIALOG_DESTROY_WITH_PARENT, gtk.MESSAGE_INFO, message_format = message)
        self.dialog.move(5000, -5000) # send it to outer space, quadrant 1
        self.dialog.connect("delete_event", self.end_alert)
        self.dialog.connect("enter_notify_event", self.end_alert)
        self.dialog.run()
        '''
        The interval the timer will wait before executing its 
        action may not be exactly the same as the interval specified by the user.
        [http://docs.python.org/library/threading.html]
        '''
        # Don't get kicked in the junk, you could be waiting all day, unreliable..
        self.t = Timer(DISPLAY_WAIT_TIME, self.dialog.destroy()) 
        self.t.start()
    def end_alert(self, widget,event,data=None):
        self.statusicon.set_visible(False)
        self.dialog.destroy()
        self.t.cancel()  # Where only assuming where still waiting
    def __init__(self):
        self.window = gtk.Window(gtk.WINDOW_TOPLEVEL)
        self.window.show_all()

        self.alert_user('Im outta here!!')
        
    def main(self):
        gtk.main()
if __name__ == "__main__":
    pyGtk_notifiysnippet = pyGtk_notifiysnippet()
    pyGtk_notifiysnippet.main()
