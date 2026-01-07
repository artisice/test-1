class Computer:
    def __init__(self):
        self.cpu = None
        self.ram_gb = None
        self.storage_gb = None
        self.gpu = None
        self.monitor = None

    def __str__(self):
        return f'Computer: CPU={self.cpu}, RAM={self.ram_gb}GB, Storage={self.storage_gb}GB, GPU={self.gpu}, Monitor={self.monitor}'

class ComputerBuilder:
    def __init__(self):
        self.computer = Computer()

    def set_cpu(self, cpu):
        self.computer.cpu = cpu
        return self

    def set_ram_gb(self, ram_gb):
        self.computer.ram_gb = ram_gb
        return self

    def set_storage_gb(self, storage_gb):
        self.computer.storage_gb = storage_gb
        return self

    def set_gpu(self, gpu):
        self.computer.gpu = gpu
        return self

    def set_monitor(self, monitor):
        self.computer.monitor = monitor
        return self

    def build(self):
        return self.computer
