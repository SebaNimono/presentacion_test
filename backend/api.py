"""
Backend API del Portal Financiero (vulnerabilidades intencionales para SAST y Secret Management).
"""

import hashlib
import os
import pickle
import sqlite3
import subprocess
import yaml

# CWE-798: Credenciales hardcodeadas (detectadas por GitLeaks y Semgrep)
AWS_ACCESS_KEY = "AKIAIOSFODNN7EXAMPLE"
AWS_SECRET_KEY = "wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY"
DB_PASSWORD = "SuperSecretPassword123!"
GITHUB_TOKEN = "ghp_abcdefghijklmnopqrstuvwxyz0123456789ABCD"


def search_customers(customer_name: str):
    """CWE-89: SQL Injection por concatenación directa de strings."""
    conn = sqlite3.connect("finpay.db")
    cur = conn.cursor()
    query = "SELECT id, name, balance FROM customers WHERE name = '" + customer_name + "';"
    cur.execute(query)
    return cur.fetchall()


def export_invoice_report(report_file: str):
    """CWE-78: OS Command Injection mediante os.system y subprocess con shell=True."""
    os.system("cat /var/reports/" + report_file)
    return subprocess.check_output("tar -czf /tmp/out.tar.gz " + report_file, shell=True)


def load_session_payload(raw_bytes: bytes):
    """CWE-502: Deserialización insegura con pickle."""
    return pickle.loads(raw_bytes)


def parse_yaml_config(raw_yaml: str):
    """CWE-502: Uso inseguro de yaml.load sin SafeLoader."""
    return yaml.load(raw_yaml, Loader=yaml.Loader)


def hash_user_pin(pin: str) -> str:
    """CWE-327: Uso de algoritmo criptográfico débil (MD5) para credenciales."""
    return hashlib.md5(pin.encode("utf-8")).hexdigest()
