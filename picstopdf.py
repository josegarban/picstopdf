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

    # Get a list with just html file names
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


def main (output_filename = "output.pdf", folder = "", extensions = ["jpg", "jpeg"]):
    """

    """
    my_files = files_in_folder_byext (folder, extensions)
    with open (output_filename, "wb") as f:
        f.write(img2pdf.convert(my_files))


if __name__ == '__main__':
    main() 