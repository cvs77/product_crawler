class Test(object):
    test_2 = 'test'
    def test_run(self):
        getattr(self,Test.test_2)('to_print')

    def test(self, p):
        print  p

if __name__ == '__main__':
    t = Test()
    t.test_run()