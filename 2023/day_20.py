import math
from collections import defaultdict

class FlipFlop():
    def __init__(self, name, targets):
        self.name = name
        self.status = False
        self.targets = targets

    def receive_signal(self, n, signal):
        _, _, pulse = signal
        if not pulse:
            self.status = not self.status
            self.send_signal(n)

    def send_signal(self, n):
        for target in self.targets:
            global_queue[n+1].append([target, self.name, self.status])

class Conjunction():
    def __init__(self, name, targets):
        self.name = name
        self.status = {}
        self.targets = targets

    def receive_signal(self, n, signal):
        _, sender, pulse = signal
        self.status[sender] = pulse
        self.send_signal(n)

    def send_signal(self, n):
        for target in self.targets:
            pulse = not all(self.status.values())
            global_queue[n+1].append([target, self.name, pulse])

class Broadcaster():
    def __init__(self, name, targets):
        self.name = name
        self.queue = defaultdict(list)
        self.targets = targets

    def receive_signal(self, n, signal):
            _, sender, pulse = signal
            self.send_signal(pulse, n)

    def send_signal(self, pulse, n):
        for target in self.targets:
            global_queue[n+1].append([target, self.name, pulse])

class Dummy():
    def receive_signal(self, *args, **kwargs):
        pass

modules = {"b" : Broadcaster, '%' : FlipFlop, "&" : Conjunction}
data = [x.split(" -> ") for x in open("input/day20.txt").read().splitlines()]

modules = {n[1:] : modules[n[0]](n[1:], t.split(', ')) for n, t in data}
converter_names = [x.name for x in modules.values() if isinstance(x, Conjunction)]
for m in list(modules.keys()):
    for t in set(converter_names).intersection(set(modules[m].targets)):
        modules[t].status[m] = False
    for t in set(modules[m].targets).difference(set(modules)):
        modules[t] = Dummy()

lfg = list(modules['vr'].status.keys())
targets = []

button_presses = 0
low_high = [0,0]
global_queue = defaultdict(list)

while lfg:
    button_presses += 1
    if button_presses == 1000:
        print(f"Assignment 1: {math.prod(low_high)}")
    tick = 0
    global_queue[0] = [['roadcaster', 'button', False]]
    while global_queue[tick]:
        signal = global_queue[tick].pop(0)
        low_high[0 if signal[2] else 1] += 1
        if signal in [['vr', t, True] for t in lfg]:
            targets.append(button_presses)
            lfg.remove(signal[1])
        modules[signal[0]].receive_signal(tick, signal)
        if not global_queue[tick]:
            tick += 1

print(f"Assignment 2: {math.lcm(*targets)}")