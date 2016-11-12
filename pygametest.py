#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  pygametest.py
#  
#  Copyright 2016 Paul Sutton <psutton@CoreDuo>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#  
import pygame
import sys
from pygame.locals import *

pygame.init()

ZONE = pygame.display.set_mode((400,300))

while True:
		
	pygame.display.update()
	
	for event in pygame.event.get():
		if event.type == OUT:
			pygame.quit()
			sys.exit()
