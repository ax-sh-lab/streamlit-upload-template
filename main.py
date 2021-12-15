import streamlit as st 
from pathlib import Path

class Folder:
    path = Path(__file__).parent
    def __init__(self, new_folder):
        self.folder = self.path.joinpath(new_folder)
        self.folder.mkdir(exist_ok=True)
    
    def save(self, file_name):
        return self.folder.joinpath(file_name)

folder = Folder('tmp')

# st.write(folder)
# https://docs.streamlit.io/library/api-reference/widgets/st.file_uploader
uploaded_file = st.file_uploader(
    "file upload", 
    type=None, 
    accept_multiple_files=False, 
    key=None, help=None, 
    on_change=None, 
    args=None, 
    kwargs=None)

if uploaded_file is not None:
     # To read file as bytes:
     bytes_data = uploaded_file.getvalue()
    #  st.write(dir(uploaded_file))
    #  st.write(uploaded_file.name)
    #  st.write(uploaded_file.size)
     file_path = folder.save(uploaded_file.name)
     st.write(file_path)
     file_path.write_bytes(bytes_data)
     st.image(uploaded_file)
           # UploadedFile
        # print(type(uploaded_file))
        # print(isinstance(uploaded_file, st.uploaded_file_manager.UploadedFile))

    #  # To convert to a string based IO:
    #  stringio = BytesIO(uploaded_file.getvalue().decode("utf-8"))
    # #  st.write(stringio)

    #  # To read file as string:
    #  string_data = stringio.read()
    #  st.write(string_data)

    #  # Can be used wherever a "file-like" object is accepted:
    #  dataframe = pd.read_csv(uploaded_file)
    #  st.write(dataframe)