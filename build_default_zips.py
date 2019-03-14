import os
import sys

for entry in os.listdir("boards"):
    for version in os.listdir(os.path.join("boards", entry)):
        if not version.endswith(".x"):
            print("Folder in board directory should end with .x")
            sys.exit(1)
        zip_filename = "adafruit-circuitpython-default-" + entry + "-" + version + "-files.zip"
        print(zip_filename)

    #     with zipfile.ZipFile(output_filename, 'w') as bundle:
    #         build_metadata = {"build-tools-version": build_tools_version}
    #         bundle.comment = json.dumps(build_metadata).encode("utf-8")
    #         if multiple_libs:
    #             total_size += add_file(bundle, "README.txt", os.path.join(top_folder, "README.txt"))
    #         for root, dirs, files in os.walk(build_dir):
    #             ziproot = root[len(build_dir + "/"):]
    #             for filename in files:
    #                 total_size += add_file(bundle, os.path.join(root, filename),
    # os.path.join(ziproot, filename.replace("-", "_")))
