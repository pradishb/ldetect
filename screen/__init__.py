''' Module for screenshoting '''
import time

import cv2
import d3dshot


class Screen:
    ''' Class for screenshoting '''

    def __init__(self):
        self.d3d = d3dshot.create(capture_output='numpy')

    def screenshot(self, analytics, rect):
        ''' Captures window '''
        analytics.start_timer('screenshot', 'Screenshoting')
        img = self.d3d.screenshot(rect)
        analytics.end_timer('screenshot')
        return img
