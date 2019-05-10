import img2pdf, os, pprint

def files_in_folder_byext (folder, extensions = ""):
    """
    Input: folder path, list of valid extensions (optional)
    Objective: find files of certain extensions in the same folder
    Output: list with filenames
    """
    
    if folder == "":
        # Find file(s) in same folder
        files = os.listdir()
    else:
        # Find file(s) in other folder
        files = os.listdir(folder)

    # Get a list with just file names
    output_list  = []
    
    if extensions != "":
        for extension in extensions:
            for file in files: 
                if   file.endswith(extension): output_list.append(file)
        if len (output_list) == 0:
            print("No file with the searched extensions were found.")
            print("")
        else:
            print("The following files with the searched extensions were found:")
            pprint.pprint(output_list)
            print("")
    else:
        for file in files: 
            output_list.append(file)
        if len (output_list) == 0:
            print("No files were found.")
            print("")
        else:
            print("The following files were found:")
            pprint.pprint(output_list)
            print("")

    return output_list



def get_extensions():
    """
    Input: set by user.
    Output: list of valid extensions.
    """
    print("\nWhat extensions will be valid?")
    print("Type each extension including the initial dot and then Enter.")
    print("When done, leave the input blank and press Enter again.")
    userinput = None
    output_list = []
    
    while userinput != "": # The loop will stop when the user leaves the input blank
        userinput = input("? ")
        if userinput.startswith(".") is False and userinput != "":
            print('The extension does not start with ".", try again')
        elif userinput != "":
            output_list.append (userinput) # Don't append the terminating signal
    return output_list


def get_output_filename(userinput = None):
    """
    Input: set by user.
    Output: string.
    """
    if userinput == None:
        print("\nWhat is the name of the output filename?")
        userinput = input("? ")
    else:        
        if "//" in userinput: # The user entered an entire path that can be split
            my_path, my_tail = os.path.split(userinput)
            
            while not os.path.exists(my_path) or len(my_tail) == 0:
                if not os.path.exists(my_path):
                    print("The folder does not exist.")
                if len(my_tail) == 0 or my_tail is None:    
                    print("The filename is empty.")
                    
                print("Try entering a different path.")
                userinput = input("? ")
                if "//" in userinput: 
                    my_path, my_tail = os.path.split(userinput) 
            
        else:
            while len(userinput) == 0:    
                print("The filename is empty.")
                print("Try entering a different path.")
                userinput = input("? ")
            my_path, my_tail = os.getcwd(), userinput

        output_string = userinput

        if not output_string.endswith(".pdf"): # If the user forgets to add a .pdf file
            output_string = output_string + ".pdf"
            my_tail = my_tail + ".pdf"

        print("File {0} will be created in folder {1}".format(my_tail, my_path))
        
    return output_string


def main (output_filename = "output.pdf", folder = "", extensions = ("jpg", "jpeg")):
    """
    Input: name of the .pdf output filename,
            name of the folder where the files to be printed are (default: same folder where the script is)
            extensions of the files to be joined.
    Objective: generate a pdf file called output_filename from the files of the extensions in extensions
            saved in the folder folder.
    Output: none.
    """
    if output_filename != "output.pdf"   : output_filename = get_output_filename()
    
    # Function to be created
    #if folder          != ""             : folder          = get_folder() 

    if extensions      != ("jpg", "jpeg"): extensions      = get_extensions()
    
    my_files = files_in_folder_byext (folder, extensions)
    with open (output_filename, "wb") as f:
        f.write(img2pdf.convert(my_files))

    return None



if __name__ == '__main__':
    main() 