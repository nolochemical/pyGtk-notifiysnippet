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
#~ along with pyRabbit.  If not, see <http://www.gnu.org/licenses/>.
import pygtk
pygtk.require('2.0')
import gtk

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
        self.dialog.connect("delete_event", self.delete_event)
        self.dialog.connect("button_press_event", self.end_alert)
        self.dialog.show()
    def end_alert(self, widget):
        self.statusicon.set_visible(False)
        self.dialog.destroy()
        
    def __init__(self):
        self.window = gtk.Window(gtk.WINDOW_TOPLEVEL)
        self.window.show_all()

        self.alert_user('Zerp!')
        
    def main(self):
        gtk.main()
if __name__ == "__main__":
    pyGtk_notifiysnippet = pyGtk_notifiysnippet()
    pyGtk_notifiysnippet.main()
