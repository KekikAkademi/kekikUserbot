# Bu araç @keyiflerolsun tarafından | @KekikAkademi için yazılmıştır.

from rich.console import Console

konsol = Console(log_path=False)

def hata(yazi):
   konsol.print(yazi, style="bold red")
def bilgi(yazi):
   konsol.print(yazi, style="blue")
def basarili(yazi):
   konsol.print(yazi, style="bold green")
def onemli(yazi):
   konsol.print(yazi, style="bold cyan")
def soru(soru):
   return konsol.input(f"[bold yellow]{soru}[/]")
def logVer(bisi):
    konsol.log(bisi) 
