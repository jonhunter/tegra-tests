import tegra

class SoC(tegra.SoC):
    compatible = 'nvidia,tegra30'
    name = 'NVIDIA Tegra30'

    def __init__(self):
        self.num_cpus = 4
