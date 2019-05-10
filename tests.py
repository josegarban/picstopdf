import picstopdf as p

# Test my functions

def test_get_extensions():
    print(p.get_extensions())

def test_get_output_filename():
    print(p.get_output_filename())

def test_functions():
    test_get_extensions()
    test_get_output_filename()

if __name__ == '__main__':
    test_functions() 