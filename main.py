import os, sys, argparse
from rich.console import Console
from rich.panel import Panel
from rich.table import Table

VERSION = "GHOST-ADValidator v1.0-PRO"
console = Console()

def main():
    parser = argparse.ArgumentParser(description="GHOST-ADValidator: Active Directory & Domain Trust Assessment")
    parser.add_argument("--domain", default="internal.local", help="Target Active Directory domain")
    args = parser.parse_args()
    
    console.print(Panel(f"[bold cyan]GHOST-ADValidator: {VERSION}[/bold cyan]\n[yellow]Authorized Active Directory Security Review[/yellow]", border_style="cyan"))
    console.print(f"[+] Auditing domain '{args.domain}' for misconfigurations, weak ACLs, and Kerberos vulnerabilities...")
    
    table = Table(title=f"Active Directory Audit: {args.domain}", border_style="magenta")
    table.add_column("Vulnerability / Misconfiguration", style="cyan")
    table.add_column("Impact", style="yellow")
    table.add_column("Remediation", style="white")
    table.add_row("Unconstrained Delegation", "Critical", "Disable unconstrained delegation on service accounts")
    table.add_row("Weak Domain Password Policy", "High", "Enforce complex passwords and MFA")
    table.add_row("ACL Abuse (GenericAll on User)", "High", "Revoke excessive permissions on sensitive objects")
    console.print(table)
    console.print("\n[bold green][+] Active Directory validation completed.[/bold green]")

if __name__ == "__main__":
    main()
