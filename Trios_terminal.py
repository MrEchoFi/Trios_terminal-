# copyright (c) 2025 Md. Abu Naser Nayeem[Tanjib]_Mr.EchoFi
#!/usr/bin/env python3
import os
import cmd
import subprocess
import sys
import logging
from rich import print
from rich.console import Console

# Initialize the Rich console for styled output.
console = Console()

# Configure logging for command executions and error tracking.
logging.basicConfig(
    filename="trios_terminal.log",
    filemode="a",
    format="%(asctime)s - %(levelname)s - %(message)s",
    level=logging.INFO
)

def print_logo():
   
    logo =  r"""
   
            
    _____   
    \__  \       |Trios_terminal
     / __ \_     |Version 1.0
    (____  /     |Based on Cybersecurity_Red_Team_Shell
         \/      |Developed by: @EbWer_Community


"""
    console.print(f"[bold cyan]{logo}[/bold cyan]")
   


class TriosTerminal(cmd.Cmd):
    """
    TriosTerminal is a multi-purpose, custom shell designed for penetration testing
    and system tasks. Available commands include:
   
      run     : Execute any system command.
      install : Install a Python package via pip.
      scan    : Perform a basic Nmap scan.
      recon   : Perform an aggressive Nmap scan (with -A).
      payload : Execute a custom payload script.
      clone   : Clone a GitHub repository.
      view    : Open a file (image, video, document, etc.) using the default application.
      play    : Play a media file using 'mpv' (or your configured media player).
      sysinfo : Display system and basic network information.
      netinfo : Display detailed network interface information.
      clear   : Clear the terminal screen.
      history : Show command history.
      alias   : Create an alias for a command.
      save    : Save the output of a command to a file.
      cd      : Change the current working directory.
      ls      : List the contents of the current directory.
      exit/EOF: Exit the terminal.
    """
    intro = print_logo()  # Logo is printed before the cmdloop starts.
    console.print("Trios_Domain", style="bold blue")
    
    prompt = "Trios_terminal/~ "
    command_history = []
    aliases = {}

    def preloop(self):
        self.load_aliases()

    def postcmd(self, stop, line):
        self.command_history.append(line)
        return stop

    def do_exit(self, arg):
        """Exit Trios_terminal."""
        console.print("[bold red]Exiting Trios_terminal. Goodbye![/bold red]")
        return True

    def do_EOF(self, arg):
        """Exit Trios_terminal using Ctrl-D."""
        console.print("\n[bold red]Exiting Trios_terminal. Goodbye![/bold red]")
        return True

    def do_run(self, arg):
        """
        Execute any system command.
        Usage: run <command>
        Example: run ls -la
        """
        if not arg.strip():
            console.print("[bold red]Usage: run <command>[/bold red]")
            return
        logging.info(f"Running system command: {arg}")
        try:
            result = subprocess.run(arg, shell=True, capture_output=True, text=True, check=True)
            if result.stdout:
                console.print(f"[bold green]Output:[/bold green]\n{result.stdout}")
            if result.stderr:
                console.print(f"[bold yellow]Error Output:[/bold yellow]\n{result.stderr}")
        except subprocess.CalledProcessError as error:
            console.print(f"[bold red]Error executing command:[/bold red] {error}")
            logging.error(f"Error executing command `{arg}`: {error}")

    def do_install(self, arg):
        """
        Install a Python package using pip.
        Usage: install <package_name>
        Example: install numpy
        """
        if not arg.strip():
            console.print("[bold red]Usage: install <package_name>[/bold red]")
            return
        command = f"{sys.executable} -m pip install {arg}"
        logging.info(f"Installing package: {arg}")
        console.print(f"[bold yellow]Installing package:[/bold yellow] {arg}")
        try:
            result = subprocess.run(command, shell=True, capture_output=True, text=True, check=True)
            if result.stdout:
                console.print(f"[bold green]{result.stdout}[/bold green]")
            if result.stderr:
                console.print(f"[bold yellow]{result.stderr}[/bold yellow]")
        except subprocess.CalledProcessError as error:
            console.print(f"[bold red]Error installing package:[/bold red] {error}")
            logging.error(f"Error installing package `{arg}`: {error}")

    def do_scan(self, arg):
        """
        Perform a basic Nmap scan on a target.
        Usage: scan <target IP or hostname>
        Example: scan 192.168.1.1
        Note: Requires Nmap installed.
        """
        if not arg.strip():
            console.print("[bold red]Usage: scan <target IP or hostname>[/bold red]")
            return
        command = f"nmap -sV {arg}"
        logging.info(f"Running Nmap scan on: {arg}")
        console.print(f"[bold yellow]Running Nmap scan: {command}[/bold yellow]")
        try:
            result = subprocess.run(command, shell=True, capture_output=True, text=True, check=True)
            console.print("[bold green]Nmap Scan Results:[/bold green]")
            console.print(result.stdout)
        except subprocess.CalledProcessError as error:
            console.print(f"[bold red]Error running Nmap scan:[/bold red] {error}")
            logging.error(f"Error running Nmap scan on `{arg}`: {error}")

    def do_recon(self, arg):
        """
        Perform an aggressive (recon) Nmap scan on a target.
        Usage: recon <target IP or hostname>
        Example: recon 192.168.1.1
        """
        if not arg.strip():
            console.print("[bold red]Usage: recon <target IP or hostname>[/bold red]")
            return
        command = f"nmap -A {arg}"
        logging.info(f"Running aggressive Nmap scan on: {arg}")
        console.print(f"[bold yellow]Running aggressive Nmap scan: {command}[/bold yellow]")
        try:
            result = subprocess.run(command, shell=True, capture_output=True, text=True, check=True)
            console.print("[bold green]Aggressive Nmap Scan Results:[/bold green]")
            console.print(result.stdout)
        except subprocess.CalledProcessError as error:
            console.print(f"[bold red]Error running aggressive Nmap scan:[/bold red] {error}")
            logging.error(f"Error running aggressive Nmap scan on `{arg}`: {error}")

    def do_payload(self, arg):
        """
        Execute a custom payload or exploitation script.
        Usage: payload <arguments>
        """
        if not arg.strip():
            console.print("[bold red]Usage: payload <arguments>[/bold red]")
            return
        logging.info(f"Executing payload with arguments: {arg}")
        console.print(f"[bold magenta]Executing payload with arguments:[/bold magenta] {arg}")
        # Insert your custom payload/exploitation logic here.

    def do_clone(self, arg):
        """
        Clone a GitHub repository.
        Usage: clone <repository URL> [destination_folder]
        Example: clone https://github.com/user/repo.git myrepo
        """
        parts = arg.split()
        if len(parts) < 1:
            console.print("[bold red]Usage: clone <repository URL> [destination_folder][/bold red]")
            return
        repo_url = parts[0]
        dest = parts[1] if len(parts) > 1 else ""
        command = f"git clone {repo_url}" + (f" {dest}" if dest else "")
        logging.info(f"Cloning repository: {repo_url} Destination: {dest}")
        console.print(f"[bold yellow]Cloning repository:[/bold yellow] {repo_url}")
        try:
            result = subprocess.run(command, shell=True, capture_output=True, text=True, check=True)
            # Print output if available; if blank, assume success.
            if result.stdout:
                console.print(f"[bold green]{result.stdout}[/bold green]")
            elif not result.stdout and not result.stderr:
                console.print("[bold green]Repository cloned successfully.[/bold green]")
            if result.stderr:
                console.print(f"[bold yellow]{result.stderr}[/bold yellow]")
        except subprocess.CalledProcessError as error:
            console.print(f"[bold red]Error cloning repository:[/bold red] {error}")
            logging.error(f"Error cloning repository `{repo_url}`: {error}")

    def do_view(self, arg):
        """
        Open a file (image, video, document, etc.) with the default system application.
        Usage: view <filepath>
        Example: view /path/to/file.jpg
        """
        if not arg.strip():
            console.print("[bold red]Usage: view <filepath>[/bold red]")
            return
        filepath = arg.strip()
        if not os.path.exists(filepath):
            console.print(f"[bold red]File does not exist: {filepath}[/bold red]")
            return
        if os.name == 'nt':
            open_command = f'start "{filepath}"'
        elif sys.platform == "darwin":
            open_command = f'open "{filepath}"'
        else:
            open_command = f'xdg-open "{filepath}"'
        logging.info(f"Opening file: {filepath}")
        console.print(f"[bold yellow]Opening file:[/bold yellow] {filepath}")
        try:
            subprocess.run(open_command, shell=True, check=True)
        except subprocess.CalledProcessError as error:
            console.print(f"[bold red]Error opening file:[/bold red] {error}")
            logging.error(f"Error opening file `{filepath}`: {error}")

    def do_play(self, arg):
        """
        Play a media file (music or video) using a media player.
        Usage: play <media_filepath>
        Example: play /path/to/song.mp3
        Note: Requires 'mpv' (or another media player) to be installed.
        """
        if not arg.strip():
            console.print("[bold red]Usage: play <media_filepath>[/bold red]")
            return
        media_file = arg.strip()
        if not os.path.exists(media_file):
            console.print(f"[bold red]File does not exist: {media_file}[/bold red]")
            return
        command = f'mpv "{media_file}"'
        logging.info(f"Playing media file: {media_file}")
        console.print(f"[bold yellow]Playing media file:[/bold yellow] {media_file}")
        try:
            subprocess.run(command, shell=True, check=True)
        except subprocess.CalledProcessError as error:
            console.print(f"[bold red]Error playing media file:[/bold red] {error}")
            logging.error(f"Error playing media file `{media_file}`: {error}")

    def do_sysinfo(self, arg):
        """
        Display system information and basic network details.
        Usage: sysinfo
        """
        logging.info("Fetching system information")
        try:
            uname_result = subprocess.run("uname -a", shell=True, capture_output=True, text=True, check=True)
            try:
                ip_result = subprocess.run("ip a", shell=True, capture_output=True, text=True, check=True)
            except subprocess.CalledProcessError:
                ip_result = subprocess.run("ifconfig", shell=True, capture_output=True, text=True, check=True)
            console.print("[bold green]System Information:[/bold green]")
            console.print(uname_result.stdout)
            console.print("[bold green]Network Information:[/bold green]")
            console.print(ip_result.stdout)
        except subprocess.CalledProcessError as error:
            console.print(f"[bold red]Error fetching system information:[/bold red] {error}")
            logging.error(f"Error fetching system information: {error}")

    def do_netinfo(self, arg):
        """
        Display detailed network interface information.
        Usage: netinfo
        """
        logging.info("Fetching network interface information")
        try:
            try:
                result = subprocess.run("ip addr", shell=True, capture_output=True, text=True, check=True)
            except subprocess.CalledProcessError:
                result = subprocess.run("ifconfig", shell=True, capture_output=True, text=True, check=True)
            console.print("[bold green]Network Interfaces:[/bold green]")
            console.print(result.stdout)
        except subprocess.CalledProcessError as error:
            console.print(f"[bold red]Error fetching network interfaces:[/bold red] {error}")
            logging.error(f"Error fetching network interfaces: {error}")

    def do_clear(self, arg):
        """
        Clear the terminal screen.
        Usage: clear
        """
        if os.name == 'nt':
            os.system('cls')
        else:
            os.system('clear')

    def do_history(self, arg):
        """
        Show command history.
        Usage: history
        """
        console.print("[bold blue]Command History:[/bold blue]")
        for i, cmd in enumerate(self.command_history):
            console.print(f"{i + 1}: {cmd}")

    def do_alias(self, arg):
        """
        Create an alias for a command.
        Usage: alias <name> <command>
        Example: alias ll 'ls -la'
        """
        parts = arg.split()
        if len(parts) < 2:
            console.print("[bold red]Usage: alias <name> <command>[/bold red]")
            return
        name = parts[0]
        command = ' '.join(parts[1:])
        self.aliases[name] = command
        console.print(f"[bold green]Alias created:[/bold green] {name} -> {command}")
        self.save_aliases()

    def do_save(self, arg):
        """
        Save the output of a command to a file.
        Usage: save <command> <filename>
        Example: save 'ls -la' output.txt
        """
        parts = arg.split()
        if len(parts) < 2:
            console.print("[bold red]Usage: save <command> <filename>[/bold red]")
            return
        command = ' '.join(parts[:-1])
        filename = parts[-1]
        logging.info(f"Saving output of command `{command}` to file `{filename}`")
        try:
            result = subprocess.run(command, shell=True, capture_output=True, text=True, check=True)
            with open(filename, 'w') as file:
                file.write(result.stdout)
            console.print(f"[bold green]Output saved to:[/bold green] {filename}")
        except subprocess.CalledProcessError as error:
            console.print(f"[bold red]Error executing command:[/bold red] {error}")
            logging.error(f"Error executing command `{command}`: {error}")

    def do_cd(self, arg):
        """
        Change the current working directory.
        Usage: cd <directory>
        Example: cd /path/to/directory
        """
        if not arg.strip():
            console.print("[bold red]Usage: cd <directory>[/bold red]")
            return
        try:
            os.chdir(arg.strip())
            console.print(f"[bold green]Changed directory to:[/bold green] {os.getcwd()}")
        except FileNotFoundError:
            console.print(f"[bold red]Directory not found:[/bold red] {arg.strip()}")
        except Exception as error:
            console.print(f"[bold red]Error changing directory:[/bold red] {error}")

    def do_ls(self, arg):
        """
        List the contents of the current directory.
        Usage: ls
        """
        try:
            files = os.listdir('.')
            console.print("[bold cyan]Directory Contents:[/bold cyan]")
            for file in files:
                console.print(file)
        except Exception as error:
            console.print(f"[bold red]Error listing directory contents:[/bold red] {error}")

    def default(self, line):
        if line in self.aliases:
            self.onecmd(self.aliases[line])
        else:
            console.print(f"[bold red]Unknown command:[/bold red] {line}\nType 'help' to see available commands.")

    def save_aliases(self):
        with open('aliases.txt', 'w') as file:
            for name, command in self.aliases.items():
                file.write(f"{name}={command}\n")

    def load_aliases(self):
        if os.path.exists('aliases.txt'):
            with open('aliases.txt', 'r') as file:
                for line in file:
                    name, command = line.strip().split('=', 1)
                    self.aliases[name] = command

if __name__ == "__main__":
    try:
        TriosTerminal().cmdloop()
    except KeyboardInterrupt:
        console.print("\n[bold red]Interrupted! Exiting Trios_terminal. Goodbye![/bold red]")

