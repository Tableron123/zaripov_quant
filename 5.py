class LinuxKernel:
    def __init__(self, distributive, package):
        self.version = distributive
        self.package = package

class Debian(LinuxKernel):
    def __init__(self):
        super(Debian, "APT")