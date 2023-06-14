from tkinter import Tk, Listbox, Button, Scrollbar, END, SINGLE, MULTIPLE, Toplevel, Label, Entry
from tkinter.filedialog import askopenfilenames
from PyPDF2 import PdfMerger

def merge_pdf(file_list, output_file):
    merger = PdfMerger()

    for file in file_list:
        merger.append(file)

    merger.write(output_file)
    merger.close()

def select_files():
    def move_up():
        selected_indices = listbox.curselection()
        if selected_indices:
            for index in selected_indices:
                if index > 0:
                    file_list.insert(index - 1, file_list.pop(index))
            update_listbox()

    def move_down():
        selected_indices = listbox.curselection()
        if selected_indices:
            for index in reversed(selected_indices):
                if index < len(file_list) - 1:
                    file_list.insert(index + 1, file_list.pop(index))
            update_listbox()

    def update_listbox():
        listbox.delete(0, END)
        for file in file_list:
            file_name = file.split("/")[-1]  # Extract only the file name
            listbox.insert(END, file_name)

    def choose_files():
        file_paths = askopenfilenames(title="Select PDF Files", filetypes=[("PDF files", "*.pdf")])
        for file_path in file_paths:
            file_list.append(file_path)  # Dosya yolunu ekle
        update_listbox()

    def merge_files():
        if file_list:
            # Open a new tkinter window for entering the output file name
            output_window = Toplevel(root)
            output_window.title("Output File Name")
            output_window.geometry("300x100")

            def merge_and_close():
                output_file_name = entry_output.get()
                if output_file_name.strip() != "":
                    if not output_file_name.endswith(".pdf"):
                        output_file_name += ".pdf"

                    merge_pdf(file_list, output_file_name)
                    print("PDF files have been merged.")
                else:
                    print("Invalid output file name.")

                output_window.destroy()  # Close the output window after merging files

            label_output = Label(output_window, text="Output File Name:")
            label_output.pack()

            entry_output = Entry(output_window)
            entry_output.pack(pady=5)

            btn_merge = Button(output_window, text="Merge and Close", command=merge_and_close)
            btn_merge.pack(pady=5)

            output_window.mainloop()
        else:
            print("No files selected.")

    def delete_files():
        selected_indices = listbox.curselection()
        if selected_indices:
            for index in reversed(selected_indices):
                file_list.pop(index)
            update_listbox()

    file_list = []

    root = Tk()
    root.title("PDF Merger")
    root.geometry("500x500")

    scrollbar = Scrollbar(root)
    scrollbar.pack(side="right", fill="y")

    listbox = Listbox(root, selectmode=MULTIPLE, yscrollcommand=scrollbar.set)
    listbox.pack(fill="both", expand=True)

    scrollbar.config(command=listbox.yview)

    btn_select = Button(root, text="Choose Files", command=choose_files)
    btn_select.pack(pady=5)

    btn_up = Button(root, text="Move Up", command=move_up)
    btn_up.pack(pady=5)

    btn_down = Button(root, text="Move Down", command=move_down)
    btn_down.pack(pady=5)

    btn_merge = Button(root, text="Merge Files", command=merge_files)
    btn_merge.pack(pady=5)

    btn_delete = Button(root, text="Delete PDF", command=delete_files)
    btn_delete.pack(pady=5)

    root.mainloop()

# Prompt the user to select PDF files
select_files()