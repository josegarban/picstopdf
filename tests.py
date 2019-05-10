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

def test_get_folder(folder_inputs):
    print("\nTesting function get_folder...")
    for folder_input in folder_inputs:
        print("\nTest {0} of {1}: {2}".format(folder_inputs.index(folder_input) + 1,
                                              len(folder_inputs),
                                              folder_input))
        print("     Test result:", p.get_folder(folder_input))

def test_functions(filename_inputs, folder_inputs):
    test_get_extensions()
    test_get_output_filename(filename_inputs)
    test_get_folder(folder_inputs)


MY_FILENAME_INPUTS = ["C://Temp//Pics//output.pdf",
                      "C://Temp//Pics//output",
                      "C://Temp//Pics//",
                      "C://Tenp//Pics//",
                      "output.pdf",
                      "output"]

MY_FOLDER_INPUTS =   ["C://Temp//Pics//",
                      "C://Tenp//Pics//",
                      "C://Tenp//Pics",
                      "output.pdf",
                      "output"]


if __name__ == '__main__':
    test_functions(MY_FILENAME_INPUTS, MY_FOLDER_INPUTS) 