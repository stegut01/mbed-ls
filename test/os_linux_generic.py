#!/usr/bin/env python
"""
mbed SDK
Copyright (c) 2011-2015 ARM Limited

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""

import unittest
import os
import errno
import logging
from mbed_lstools.lstools_linux_generic import MbedLsToolsLinuxGeneric



class BasicTestCase(unittest.TestCase):
    """ Basic test cases checking trivial asserts
    """

    def setUp(self):
        self.linux_generic = MbedLsToolsLinuxGeneric()
        
        self.vfat_devices = [
            "/dev/sdb on /media/usb0 type vfat (rw,noexec,nodev,sync,noatime,nodiratime,gid=1000,uid=1000,dmask=000,fmask=000)",
            "/dev/sdd on /media/usb2 type vfat (rw,noexec,nodev,sync,noatime,nodiratime,gid=1000,uid=1000,dmask=000,fmask=000)",
            "/dev/sde on /media/usb3 type vfat (rw,noexec,nodev,sync,noatime,nodiratime,gid=1000,uid=1000,dmask=000,fmask=000)",
            "/dev/sdc on /media/usb1 type vfat (rw,noexec,nodev,sync,noatime,nodiratime,gid=1000,uid=1000,dmask=000,fmask=000)"
        ]

        self.vfat_devices_ext = [
            "/dev/sdb on /media/MBED_xxx type vfat (rw,noexec,nodev,sync,noatime,nodiratime,gid=1000,uid=1000,dmask=000,fmask=000)",
            "/dev/sdd on /media/MBED___x type vfat (rw,noexec,nodev,sync,noatime,nodiratime,gid=1000,uid=1000,dmask=000,fmask=000)",
            "/dev/sde on /media/MBED-xxx type vfat (rw,noexec,nodev,sync,noatime,nodiratime,gid=1000,uid=1000,dmask=000,fmask=000)",
            "/dev/sdc on /media/MBED_x-x type vfat (rw,noexec,nodev,sync,noatime,nodiratime,gid=1000,uid=1000,dmask=000,fmask=000)"
        ]

    def tearDown(self):
        pass

    def test_example(self):
        self.assertEqual(True, True)
        self.assertNotEqual(True, False)

    def test_get_mount_point_basic(self):
        self.assertEqual('/media/usb0', self.linux_generic.get_mount_point('sdb', self.vfat_devices))
        self.assertEqual('/media/usb2', self.linux_generic.get_mount_point('sdd', self.vfat_devices))
        self.assertEqual('/media/usb3', self.linux_generic.get_mount_point('sde', self.vfat_devices))
        self.assertEqual('/media/usb1', self.linux_generic.get_mount_point('sdc', self.vfat_devices))
        
    def test_get_mount_point_ext(self):
        self.assertEqual('/media/MBED_xxx', self.linux_generic.get_mount_point('sdb', self.vfat_devices_ext))
        self.assertEqual('/media/MBED___x', self.linux_generic.get_mount_point('sdd', self.vfat_devices_ext))
        self.assertEqual('/media/MBED-xxx', self.linux_generic.get_mount_point('sde', self.vfat_devices_ext))
        self.assertEqual('/media/MBED_x-x', self.linux_generic.get_mount_point('sdc', self.vfat_devices_ext))
        
if __name__ == '__main__':
    unittest.main()
