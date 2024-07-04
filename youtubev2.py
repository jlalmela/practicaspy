import pytube
import tkinter as tk

def download_audio():
    # Create the main window
    root = tk.Tk()
    root.title("Descarga de Audio de YouTube")

    # Set window background color to blue
    root.config(bg="blue")

    # Set window size to 900x900 pixels
    root.geometry("900x900")

    # Create labels and entry fields for URL and filename
    url_label = tk.Label(root, text="Pegar URL del video de YouTube:", font=("Arial", 12))
    url_label.grid(row=0, column=0, padx=10, pady=10)

    url_entry = tk.Entry(root, width=50)
    url_entry.grid(row=0, column=1, padx=10, pady=10)

    filename_label = tk.Label(root, text="Ingrese el nombre de archivo deseado (sin extensión .mp3):", font=("Arial", 12))
    filename_label.grid(row=1, column=0, padx=10, pady=10)

    filename_entry = tk.Entry(root, width=50)
    filename_entry.grid(row=1, column=1, padx=10, pady=10)

    # Create a button to trigger the download
    download_button = tk.Button(root, text="Descargar Audio", command=lambda: download_audio_from_url(url_entry.get(), filename_entry.get()))
    download_button.grid(row=2, column=0, columnspan=2, padx=10, pady=10)

    # Function to handle the download process
    def download_audio_from_url(url, filename_without_ext):
        # Check if filename includes .mp3 extension
        if not filename_without_ext.endswith(".mp3"):
            filename_with_ext = filename_without_ext + ".mp3"
        else:
            filename_with_ext = filename_without_ext

        try:
            yt = pytube.YouTube(url)
            audio = yt.streams.filter(only_audio=True).first().download(filename=filename_with_ext)
            print(f"Audio downloaded successfully: {audio}")
            success_label = tk.Label(root, text=f"¡Audio descargado correctamente! Nombre del archivo: {audio}", fg="green", font=("Arial", 12))
            success_label.grid(row=3, column=0, columnspan=2, padx=10, pady=10)
        except pytube.exceptions.RegexMatchError:
            print("Error: No se pudo extraer la ID del video de la URL.")
            error_label = tk.Label(root, text="Error: No se pudo extraer la ID del video de la URL.", fg="red", font=("Arial", 12))
            error_label.grid(row=3, column=0, columnspan=2, padx=10, pady=10)
        except Exception as e:
            print(f"Ocurrió un error inesperado: {e}")
            error_label = tk.Label(root, text=f"Ocurrió un error inesperado: {e}", fg="red", font=("Arial", 12))
            error_label.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

    # Create Salir (Exit) button and its event handler
    def salir():
        root.destroy()  # Closes the window

    salir_button = tk.Button(root, text="Salir", command=salir)
    salir_button.grid(row=4, column=0, padx=10, pady=10)

    # Create Reiniciar (Restart) button and its event handler
    def reiniciar():
        root.destroy()  # Close the current window
        download_audio()  # Start a new one

    reiniciar_button = tk.Button(root, text="Reiniciar", command=reiniciar)
    reiniciar_button.grid(row=4, column=1, padx=10, pady=10)

    # Run the Tkinter main loop
    root.mainloop()

# Start the application
download_audio()
