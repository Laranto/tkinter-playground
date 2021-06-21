import unittest

from src.base_system import EntityInfluence, EntityPool


class TestEntitiyLinkage(unittest.TestCase):
    
    def test_createSingleLinked(self):
        INIT_VAL_A = 10.0
        INFLUENCE = 0.1
        a = EntityPool(INIT_VAL_A)
        b = EntityPool(0)
        c = EntityInfluence(a,b,INFLUENCE)
        # Linkage
        self.assertEqual(0,len(a.influencedBy))
        self.assertEqual(1,len(a.influences))
        self.assertEqual(1,len(b.influencedBy))
        self.assertEqual(0,len(b.influences))

        # Value
        self.assertEqual(INIT_VAL_A, a.value)
        self.assertEqual(0, b.value)
        self.assertEqual(1,len(a.history))
        self.assertEqual(1,len(b.history))
        c.prepareTick()
        self.assertEqual(1.0,c.delta)
        c.tick()
        self.assertEqual(1,len(a.history))
        self.assertEqual(2,len(b.history))
        self.assertEqual(INIT_VAL_A, a.value)
        self.assertEqual(INIT_VAL_A*INFLUENCE, b.value)
        for i in range(9):
            c.prepareTick()
            c.tick()
        self.assertEqual(INIT_VAL_A, a.value)
        self.assertEqual(INIT_VAL_A, b.value)



    def test_selfLinked(self):
        INIT_VAL_A = 10.0
        a = EntityPool(INIT_VAL_A)
        link = EntityInfluence(a,a,0.1)
        self.assertEqual(1,len(a.influences))
        self.assertEqual(1,len(a.influencedBy))
        self.assertEqual(INIT_VAL_A, a.value)
        link.prepareTick()
        link.tick()
        self.assertEqual(INIT_VAL_A+1, round(a.value,2))
        link.prepareTick()
        link.tick()
        self.assertEqual(INIT_VAL_A+2.1, round(a.value,2))
        link.prepareTick()
        link.tick()
        self.assertEqual(INIT_VAL_A+3.31, round(a.value,2))