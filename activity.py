#! /usr/bin/env python
# -*- coding: utf-8 -*-

import sugargame
import sugargame.canvas
import pygame
from gi.repository import Gtk

from sugar3.activity import activity


import Proyecto

class HelloWorldActivity(activity.Activity):

    def __init__(self, handle):
        activity.Activity.__init__(self, handle)

        # Change the following number to change max participants
        self.max_participants = 1
        
        self.game = Proyecto.main
        self.game.canvas = sugargame.canvas.PygameCanvas(
                self,
                main=self.game,
                modules=[pygame.display, pygame.font])
        self.set_canvas(self.game.canvas)
        self.game.canvas.grab_focus()  

    def read_file(self, file_path):
        pass
        
    def write_file(self, file_path):
        pass

    def build_toolbar(self):
        toolbar_box = ToolbarBox()
        toolbar_box.show()

        activity_button = ActivityToolbarButton(self)
        toolbar_box.toolbar.insert(activity_button, -1)
        activity_button.show()
        
        separator = Gtk.SeparatorToolItem()
        separator.props.draw = False
        separator.set_expand(True)

        toolbar_box.toolbar.insert(separator, -1)
        stop_button = StopButton(self)
        toolbar_box.toolbar.insert(stop_button, -1)
        stop_button.show()

        self.set_toolbar_box(toolbar_box)
        toolbar_box.show_all()




