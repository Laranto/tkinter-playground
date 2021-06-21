from typing import Set

class EntityInfluence():
    """
    Mapping between two entity pools
    Creating a Entity Influence will link it to the pools.
    """
    def __init__(self,source:"EntityPool",target:"EntityPool",impact:float=0):
        """
        source: The element doing the influencing
        target: The element being changed by the influencer
        impact: Signed Percent for the change per tick. 1 is 100%
        """
        self.source = source
        self.target = target
        self.impact = impact
        self.target.influencedBy.add(self)
        self.source.influences.add(self)
        self.delta = self.source.value * self.impact

    def prepareTick(self):
        """
        To have deteministic increase of valeus, the ticks need to be prepared before they can start
        """
        self.delta = self.source.value * self.impact

    def tick(self):
        """
        Applies the prepared tick
        """
        self.target.addDelta(self.delta)

class EntityPool():
    """
    Representation of any form of resource or entity
    For example birth rate, population, resource extraction, etc
    """
    def __init__(self,initValue:float=0):
        # Historical Values to be able to plot it
        self.history = [initValue]
        # Elements influenced
        self.influences = set()
        self.influencedBy = set()

    @property
    def value(self) -> float: 
        return self.history[-1]

    def addInfluence(self, influnce:EntityInfluence) -> None:
        self.influences.add(influnce)

    def addInfluencedBy(self, influence:EntityInfluence) -> None:
        self.influencedBy.add(influence)

    def addDelta(self,delta:float):
        self.history.append(self.value+delta)

    