import boards
from linux import sysfs

class Board(boards.Board):
    __compatible__ = 'nvidia,jetson-tk1'
    name = 'NVIDIA Jetson TK1'

    devices = [
        # platform bus
        sysfs.Device('platform', '1003000.pcie', 'tegra-pcie'),
        sysfs.Device('platform', '50000000.host1x', 'tegra-host1x'),
        sysfs.Device('platform', '54200000.dc', 'tegra-dc'),
        sysfs.Device('platform', '54240000.dc', 'tegra-dc'),
        sysfs.Device('platform', '54280000.hdmi', 'tegra-hdmi'),
        sysfs.Device('platform', '60007000.flow-controller', 'tegra-flowctrl'),
        sysfs.Device('platform', '6000d000.gpio', 'tegra-gpio'),
        sysfs.Device('platform', '60020000.dma', 'tegra-apbdma'),
        sysfs.Device('platform', '70000868.pinmux', 'tegra124-pinctrl'),
        sysfs.Device('platform', '70006000.serial', 'serial-tegra'),
        sysfs.Device('platform', '70006040.serial', 'serial-tegra'),
        sysfs.Device('platform', '70006300.serial', 'of_serial'),
        sysfs.Device('platform', '7000c000.i2c', 'tegra-i2c'),
        sysfs.Device('platform', '7000c400.i2c', 'tegra-i2c'),
        sysfs.Device('platform', '7000c500.i2c', 'tegra-i2c'),
        sysfs.Device('platform', '7000c700.i2c', 'tegra-i2c'),
        sysfs.Device('platform', '7000d000.i2c', 'tegra-i2c'),
        sysfs.Device('platform', '7000d400.spi', 'spi-tegra114'),
        sysfs.Device('platform', '7000da00.spi', 'spi-tegra114'),
        sysfs.Device('platform', '7000e000.rtc', 'tegra_rtc'),
        sysfs.Device('platform', '7000e400.pmc', 'tegra-pmc'),
        sysfs.Device('platform', '7000f800.fuse', 'tegra-fuse'),
        sysfs.Device('platform', '70019000.memory-controller', 'tegra-mc'),
        sysfs.Device('platform', '7001b000.emc', 'tegra-emc'),
        sysfs.Device('platform', '70027000.sata', 'tegra-ahci'),
        sysfs.Device('platform', '70030000.hda', 'tegra-hda'),
        sysfs.Device('platform', '70090000.usb', 'tegra-xusb'),
        sysfs.Device('platform', '7009f000.padctl', 'tegra-xusb-padctl'),
        sysfs.Device('platform', '700b0400.sdhci', 'sdhci-tegra'),
        sysfs.Device('platform', '700b0600.sdhci', 'sdhci-tegra'),
        sysfs.Device('platform', '70300000.ahub', 'tegra30-ahub'),
        sysfs.Device('platform', '70301100.i2s', 'tegra30-i2s'),
        sysfs.Device('platform', '7d004000.usb', 'tegra-ehci'),
        sysfs.Device('platform', '7d004000.usb-phy', 'tegra-phy'),
        sysfs.Device('platform', '7d008000.usb', 'tegra-ehci'),
        sysfs.Device('platform', '7d008000.usb-phy', 'tegra-phy'),
        # HDA bus
        sysfs.Device('hdaudio', 'hdaudioC0D3', 'snd_hda_codec_hdmi'),
        # host1x bus
        sysfs.Device('host1x', 'drm', 'drm'),
        # I2C bus
        sysfs.Device('i2c', '0-001c', 'rt5640'),
        sysfs.Device('i2c', '0-004c', 'lm90'),
        sysfs.Device('i2c', '0-0056', 'at24'),
        sysfs.Device('i2c', '4-0040', 'as3722'),
        # PCI bus
        sysfs.Device('pci', '0000:00:02.0', 'pcieport'),
        sysfs.Device('pci', '0000:01:00.0', 'r8169'),
        # SPI bus
        sysfs.Device('spi', 'spi1.0', 'm25p80'),
    ]

    whitelist = [
        r'/cpus/cpu@\d+missing clock-frequency property',
        r' usb\d+-\d+: usb\d+-\d+ supply vbus not found',
        r'.*Failed to get supply \'.*\': -517',
        r'\+.*: bypassed regulator has no supply!',
        r'\+.*: failed to get the current voltage\(-517\)',
        r'as3722-regulator as3722-regulator: regulator .* register failed -517',
        r'tegra124-dfll 70110000.clock: couldn\'t get vdd_cpu regulator',
        r'tegra-ahci 70027000\.sata: Failed to get regulators',
        r'tegra-xusb 70090000\.usb: failed to get regulators: -517',
        r'lm90 0-004c: 0-004c supply vcc not found, using dummy regulator',
        r'mmc\d+: Unknown controller version \(3\)\. You may experience problems\.',
        r'mmc\d+: Invalid maximum block size, assuming 512 bytes',
        r'tegra30-i2s 70301100\.i2s: DMA channels sourced from device 70300000\.ahub',
        r'as3722-regulator as3722-regulator: DMA mask not set',
        r'tegra-pcie 1003000\.pcie: Slot present pin change, signature: \d+',
        r'tegra-pcie 1003000\.pcie: link \d+ down, retrying',
        r'pci_bus [0-9a-fA-F]{4}:[0-9a-fA-F]{2}: \d+-byte config .* to [0-9a-fA-F]{4}:[0-9a-fA-F]{2}:[0-9a-fA-F]{2}\.\d offset 0x[0-9a-fA-F]+ may corrupt adjacent RW1C bits',
        r'pci [0-9a-fA-F]{4}:[0-9a-fA-F]{2}:[0-9a-fA-F]{2}\.[0-9a-fA-F]: nv_msi_ht_cap_quirk didn\'t locate host bridge',
        r'platform regulatory.0: Direct firmware load for regulatory.db failed with error -2',
        r'tegra-hdmi 54280000.hdmi: cannot set audio to 48000 Hz at 297000000 Hz pixel clock',
        r'urandom_read: [0-9]+ callbacks suppressed',
    ]
