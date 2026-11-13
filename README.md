# Portal Financiero Demo (`presentacion_test`)

Mini aplicación web y API construida para demostrar el flujo integral **DevSecOps de SSPILLOWY** en vivo:

- **Frontend Web (`index.html` + `src/portal.js`):** Portal de consulta de clientes y pagos (contiene vulnerabilidades SAST en JavaScript como DOM XSS y `eval`).
- **Backend API (`backend/api.py`):** Servicio en Python con SQL Injection (`CWE-89`), Command Injection (`CWE-78`), Deserialización Insegura (`CWE-502`) y Hash débil (`MD5`).
- **Secretos expuestos (`backend/api.py` y `config/keys.pem`):** Credenciales de prueba detectables por **GitLeaks** para el módulo **Secret Management**.
- **Dependencias & Contenedor (`requirements.txt`, `package-lock.json`, `Dockerfile`):** Librerías con CVEs conocidos para activar **Trivy SCA**, **Supply Chain (SBOM)** y **Fix Intelligence**.
