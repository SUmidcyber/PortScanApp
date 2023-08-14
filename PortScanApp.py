import tkinter as tk
import socket

def validate_input(P):
    return P.isdigit() or P == ""

class PortScanApp: # Port Classroom
    def __init__(self, root):
        self.root = root
        self.root.title("Port Scan")
        self.root.geometry("400x600")

        self.input_frame = tk.Frame(self.root)
        self.input_frame.pack(padx=10, pady=5, anchor='nw')

        self.create_target_ip_frame(self.input_frame)
        self.create_pack_frame(self.input_frame)
        self.create_target_port_frame(self.input_frame)
        self.create_button_frame(self.input_frame, "Connect", self.connect)
        self.create_button_frame(self.input_frame, "Delete", self.delete)
        self.create_button_frame(self.input_frame, "Exit", self.root.quit)
        
        self.result_text = self.create_result_text(self.root)
        
    def create_target_ip_frame(self, parent_frame):
        target_frame = tk.Frame(parent_frame)
        target_frame.pack(anchor='w')

        self.str_var = tk.StringVar()  # STRING
        target_ip_label = tk.Label(master=target_frame, font=25, text="Target IP")
        target_ip_label.pack(anchor='w')

        tk.Label(target_frame, text="", font=("Calibri", 5)).pack()

        ip_entry = tk.Entry(master=target_frame, font="Calibri 15 bold", textvariable=self.str_var)
        ip_entry.pack(anchor='w')

        tk.Label(target_frame, text="", font=("Calibri", 5)).pack()

    def create_pack_frame(self, parent_frame):
        pack_frame = tk.Frame(parent_frame)
        pack_frame.pack(anchor='w')

        request_pack = tk.Label(master=pack_frame, font=25, text="The Request Pack")
        request_pack.pack(anchor='w')

        tk.Label(pack_frame, text="", font=("Calibri", 5)).pack()

        self.request_str = tk.StringVar(value="TCP")
        request_menu = tk.OptionMenu(pack_frame, self.request_str, "TCP", "UDP", "PING")
        request_menu.pack(anchor='w')

    def create_target_port_frame(self, parent_frame):
        port_frame = tk.Frame(parent_frame)
        port_frame.pack(anchor='e')

        target_port1 = tk.Label(master=port_frame, text="Target PORT", font=25)
        target_port1.pack(anchor='e')

        tk.Label(port_frame, text="", font=("Calibri", 5)).pack()

        self.entry_var = tk.StringVar()
        entry_port = tk.Entry(master=port_frame, textvariable=self.entry_var, font="Calibri 15 bold", width=4,
                              validate="key", validatecommand=(self.root.register(validate_input), "%P"))
        entry_port.pack(anchor='e')

        tk.Label(port_frame, text="", font=("Calibri", 5)).pack()

    def create_button_frame(self, parent_frame, text, command):
        button_frame = tk.Frame(parent_frame)
        button_frame.pack(anchor='e')

        button = tk.Button(master=button_frame, text=text, width=8, command=command)
        button.pack(anchor='e')

        tk.Label(button_frame, text="", font=("Calibri", 5)).pack()

    def create_result_text(self, parent_frame):
        result_text = tk.Text(parent_frame, height=10, width=40)
        result_text.pack(pady=10)
        return result_text

    def connect(self):
        target_ip = self.str_var.get()
        port = int(self.entry_var.get())
        request_type = self.request_str.get()

        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:  # Scannig
                s.settimeout(1)
                result = s.connect_ex((target_ip, port))
                if result == 0:
                    self.result_text.insert(tk.END, f"Port {port} ({request_type}): Open\n")
                else:
                    self.result_text.insert(tk.END, f"Port {port} ({request_type}): Close\n")
        except Exception as e:
            self.result_text.insert(tk.END, f"Port {port} ({request_type}): Hata - {str(e)}\n")

    def delete(self):
        self.result_text.delete(1.0, tk.END)

def main():
    window = tk.Tk()
    app = PortScanApp(window)
    window.mainloop()

if __name__ == "__main__":
    main()
