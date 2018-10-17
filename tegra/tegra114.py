import tegra

class SoC(tegra.SoC):
    compatible = 'nvidia,tegra114'
    name = 'NVIDIA Tegra114'

    def __init__(self):
        self.num_cpus = 4
