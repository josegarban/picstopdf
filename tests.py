import picstopdf as p

# Test my functions

def test_get_extensions():
    print("\nTesting function test_get_extensions...")
    print("Test result:", p.get_extensions())

def test_get_output_filename(filename_inputs):
    print("\nTesting function get_output_filename...")
    for filename_input in filename_inputs:
        print("\nTest {0} of {1}: {2}".format(filename_inputs.index(filename_input) + 1,
                                              len(filename_inputs),
                                              filename_input))
        print("     Test result:", p.get_output_filename(filename_input))

def test_functions(filename_inputs):
    test_get_extensions()
    test_get_output_filename(filename_inputs)

MY_FILENAME_INPUTS = ["C://Temp//Pics//output.pdf",
                      "C://Temp//Pics//output",
                      "C://Temp//Pics//",
                      "C://Tenp//Pics//",
                      "output.pdf",
                      "output"]

if __name__ == '__main__':
    test_functions(MY_FILENAME_INPUTS) 