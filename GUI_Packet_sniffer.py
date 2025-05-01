import tkinter as tk
from tkinter import scrolledtext
from scapy.all import sniff
import threading

# GUI App class
class PacketSnifferApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Packet Sniffer (Python + Tkinter)")
        self.root.geometry("700x500")

        # Start/Stop Buttons
        self.start_button = tk.Button(root, text="Start Sniffing", command=self.start_sniffing, bg='green', fg='white')
        self.start_button.pack(pady=10)

        self.stop_button = tk.Button(root, text="Stop Sniffing", command=self.stop_sniffing, bg='red', fg='white', state=tk.DISABLED)
        self.stop_button.pack(pady=5)

        # Packet Display Area
        self.text_area = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=80, height=25)
        self.text_area.pack(padx=10, pady=10)

        # Internal state
        self.sniffing = False
        self.sniffer_thread = None

    def start_sniffing(self):
        self.sniffing = True
        self.start_button.config(state=tk.DISABLED)
        self.stop_button.config(state=tk.NORMAL)
        self.text_area.insert(tk.END, "[INFO] Starting packet capture...\n")
        self.text_area.see(tk.END)
        self.sniffer_thread = threading.Thread(target=self.sniff_packets)
        self.sniffer_thread.start()

    def stop_sniffing(self):
        self.sniffing = False
        self.start_button.config(state=tk.NORMAL)
        self.stop_button.config(state=tk.DISABLED)
        self.text_area.insert(tk.END, "[INFO] Stopping packet capture...\n")
        self.text_area.see(tk.END)

    def sniff_packets(self):
        def process_packet(packet):
            if self.sniffing:
                summary = packet.summary()
                self.text_area.insert(tk.END, summary + "\n")
                self.text_area.see(tk.END)
            else:
                return False  # Stop sniffing

        sniff(prn=process_packet, store=False)

# Launch the app
if __name__ == "__main__":
    root = tk.Tk()
    app = PacketSnifferApp(root)
    root.mainloop()
