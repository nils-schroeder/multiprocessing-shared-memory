import random
from dataclasses import dataclass
from typing import List


@dataclass(frozen=True, unsafe_hash=True)
class Datapoint:

    uuid: int
    value: float


class DatapointCollection:

    datapoint_list: List[Datapoint]

    def __init__(self, size):

        for i in range(size):

            if not self.datapoint_list:
                uuid = hash('genesis')
            else:
                uuid = hash(self.datapoint_list[-1])

            value = random.random()

            self.datapoint_list.append(Datapoint(uuid, value))

    def checksum(self):
        return hash(self.datapoint_list)
