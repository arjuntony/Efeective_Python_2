import simple

class TestAdd():
    def test_str(self):
        r = simple.add("hello" , "world")
        assert r == "helloworld"

    def test_simple(self):
        r = simple.add(2, 2)
        assert r == 4
